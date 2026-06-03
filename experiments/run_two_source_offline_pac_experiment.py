"""Two-source offline cost-aware PAC labeling experiment.

This script complements ``run_simple_offline_pac_experiment.py``. Where the
simple offline experiment has a single cheap source and falls back to the
monotone single-threshold PAC baseline of HW4, this experiment evaluates the
LP/dual-price method in the multi-source regime it is actually designed for.

Construction. From each base ImageNet table we synthesize a pair of
complementary cheap sources A and B with disjoint specialties. Items are
partitioned by the parity of the true class. Source A keeps the original
(Yhat, confidence) on even-class items (its specialty) and emits a uniform
random label with low confidence on odd-class items (out of specialty).
Source B mirrors A. This is the canonical mixture-of-experts setting that
motivates the LP formulation: each source is calibrated to its own competence
(low confidence outside its specialty), neither source dominates, and the
per-item argmin-proxy router approaches an oracle while any single source
must defer roughly the entire half of items outside its specialty.

Costs are c_A = c_B = 0 and c_E = 1, matching the simple offline experiment's
notion of "budget saved = 1 - deferral rate". Under homogeneous cheap costs
the LP dual rule reduces to: route each item to the source with the lower
proxy loss, defer to the expert if that minimum proxy loss exceeds a single
threshold tau = 1/lambda. Because the cheap-source costs are equal, changing
lambda cannot switch between sources; it only switches routed AI items to the
expert. The routed loss is therefore monotone in the scalar threshold and does
not need a union bound over the threshold grid.

Methods compared:
  - lp_two_source_monotone_ucb: the report's LP method, certified by the
    monotone-threshold Hoeffding UCB.
  - single_A_monotone_pac and single_B_monotone_pac: the report's monotone
    baseline applied to source A or B alone, ignoring the other source.
  - best_of_singles_bonferroni: run both single-source baselines at level
    alpha/2 each, then pick the source with larger empirical savings on the
    calibration sample. By Bonferroni this remains a valid alpha-PAC
    procedure.

The script is deliberately additive: it does not import from, modify, or
overwrite any existing file under this repository. Outputs go to a new
directory ``results/two_source_offline_pac/``.
"""

import argparse
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/private/tmp/matplotlib")

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt

DEFAULT_DATASETS = {
    "ImageNet": "data/imagenet.csv",
    "ImageNetV2": "data/imagenetv2.csv",
}


def load_dataset(path: Path):
    df = pd.read_csv(path)
    y = df["Y"].to_numpy()
    yhat = df["Yhat"].to_numpy()
    conf = df["confidence"].to_numpy(dtype=float)
    return y, yhat, conf


def synthesize_two_sources(y, yhat, conf, seed, low_conf_max):
    """Build two complementary cheap sources from a base predictor.

    Items with even true class belong to source A's specialty; items with odd
    true class belong to source B's specialty. Inside its specialty a source
    reuses the original predictor's label and confidence. Outside its
    specialty the source emits a uniform random label across the observed
    class set and draws a confidence value from Uniform[0, low_conf_max], so a
    router that prefers the lower-proxy-loss source will, item by item,
    correctly select the in-specialty source.
    """
    rng = np.random.default_rng(seed)
    num_classes = int(y.max()) + 1
    specialty_A = (y % 2 == 0)

    yhat_A = yhat.copy()
    conf_A = conf.copy().astype(float)
    out_A = ~specialty_A
    n_out_A = int(out_A.sum())
    yhat_A[out_A] = rng.integers(0, num_classes, size=n_out_A)
    conf_A[out_A] = rng.uniform(0.0, low_conf_max, size=n_out_A)

    yhat_B = yhat.copy()
    conf_B = conf.copy().astype(float)
    out_B = specialty_A
    n_out_B = int(out_B.sum())
    yhat_B[out_B] = rng.integers(0, num_classes, size=n_out_B)
    conf_B[out_B] = rng.uniform(0.0, low_conf_max, size=n_out_B)

    proxy_A = 1.0 - conf_A
    proxy_B = 1.0 - conf_B
    mistakes_A = (yhat_A != y)
    mistakes_B = (yhat_B != y)
    return proxy_A, proxy_B, mistakes_A, mistakes_B


def evaluate_lp_grid(proxy_A, proxy_B, mistakes_A, mistakes_B, thresholds):
    """Per-threshold loss and savings of the LP two-source router."""
    proxy_min = np.minimum(proxy_A, proxy_B)
    routed_mistake = np.where(proxy_A <= proxy_B, mistakes_A, mistakes_B)
    ai_mask = proxy_min[:, None] <= thresholds[None, :]
    losses = np.mean(ai_mask & routed_mistake[:, None], axis=0)
    saved = np.mean(ai_mask, axis=0)
    return losses, saved


def evaluate_single_grid(proxy, mistakes, thresholds):
    ai_mask = proxy[:, None] <= thresholds[None, :]
    losses = np.mean(ai_mask & mistakes[:, None], axis=0)
    saved = np.mean(ai_mask, axis=0)
    return losses, saved


def select_lp_two_source_ucb(
    proxy_A,
    proxy_B,
    mistakes_A,
    mistakes_B,
    thresholds,
    full_losses,
    full_saved,
    epsilon,
    alpha,
    sample_idx,
):
    m = len(sample_idx)
    sA = proxy_A[sample_idx]
    sB = proxy_B[sample_idx]
    mA = mistakes_A[sample_idx]
    mB = mistakes_B[sample_idx]
    proxy_min = np.minimum(sA, sB)
    routed_mistake = np.where(sA <= sB, mA, mB)
    ai_mask = proxy_min[:, None] <= thresholds[None, :]
    empirical_loss = np.mean(ai_mask & routed_mistake[:, None], axis=0)
    radius = np.sqrt(np.log(1.0 / alpha) / (2.0 * m))
    ucb = empirical_loss + radius

    feasible = np.flatnonzero(ucb <= epsilon)
    selected = feasible[np.argmax(full_saved[feasible])] if len(feasible) else 0
    return {
        "method": "lp_two_source_monotone_ucb",
        "m": m,
        "radius": float(radius),
        "alpha_used": float(alpha),
        "selected_threshold": float(thresholds[selected]),
        "empirical_loss": float(empirical_loss[selected]),
        "ucb": float(ucb[selected]),
        "realized_error": float(full_losses[selected]),
        "budget_saved": float(full_saved[selected]),
        "avg_cost": 1.0 - float(full_saved[selected]),
        "violated": float(full_losses[selected] > epsilon + 1e-12),
    }


def first_exceeding_error_count(m, epsilon, alpha):
    radius = np.sqrt(np.log(1.0 / alpha) / (2.0 * m))
    empirical_rates = np.arange(m + 1) / m
    ucb = empirical_rates + radius
    hits = np.flatnonzero(ucb > epsilon)
    if len(hits) == 0:
        return m + 1
    return int(hits[0])


def select_single_source_monotone(proxy, mistakes, epsilon, alpha, sample_idx):
    """Monotone PAC threshold on a single source (HW4 baseline)."""
    m = len(sample_idx)
    radius = np.sqrt(np.log(1.0 / alpha) / (2.0 * m))
    q = first_exceeding_error_count(m, epsilon, alpha)

    sampled_mistake_scores = proxy[sample_idx[mistakes[sample_idx]]]
    if q <= 0:
        threshold = -np.inf
    elif len(sampled_mistake_scores) < q:
        threshold = np.inf
    else:
        threshold = float(np.partition(sampled_mistake_scores, q - 1)[q - 1])

    ai_used = proxy < threshold
    sample_ai = proxy[sample_idx] < threshold
    sample_loss = float(np.mean(sample_ai & mistakes[sample_idx]))
    realized_error = float(np.mean(ai_used & mistakes))
    budget_saved = float(np.mean(ai_used))
    return {
        "m": m,
        "radius": float(radius),
        "alpha_used": float(alpha),
        "selected_threshold": threshold,
        "empirical_loss": sample_loss,
        "ucb": (sample_loss + radius) if budget_saved > 0 else 0.0,
        "realized_error": realized_error,
        "budget_saved": budget_saved,
        "avg_cost": 1.0 - budget_saved,
        "violated": float(realized_error > epsilon + 1e-12),
    }


def select_best_of_singles(
    proxy_A, mistakes_A, proxy_B, mistakes_B, epsilon, alpha, sample_idx
):
    """Bonferroni-corrected pick-the-better-single-source baseline."""
    outA = select_single_source_monotone(
        proxy_A, mistakes_A, epsilon, alpha / 2.0, sample_idx
    )
    outB = select_single_source_monotone(
        proxy_B, mistakes_B, epsilon, alpha / 2.0, sample_idx
    )
    if outA["budget_saved"] >= outB["budget_saved"]:
        chosen, out = "A", outA
    else:
        chosen, out = "B", outB
    return {
        "method": "best_of_singles_bonferroni",
        "chosen_source": chosen,
        **out,
    }


def summarize_trials(rows):
    df = pd.DataFrame(rows)
    return (
        df.groupby(["dataset", "method", "epsilon"])
        .agg(
            n=("n", "first"),
            m=("m", "first"),
            radius=("radius", "first"),
            alpha_used=("alpha_used", "first"),
            violation_rate=("violated", "mean"),
            mean_realized_error=("realized_error", "mean"),
            q95_realized_error=(
                "realized_error",
                lambda x: float(np.quantile(x, 0.95)),
            ),
            mean_budget_saved=("budget_saved", "mean"),
            mean_avg_cost=("avg_cost", "mean"),
            median_threshold=("selected_threshold", "median"),
            oracle_lp_saved=("oracle_lp_saved", "first"),
            oracle_lp_error=("oracle_lp_error", "first"),
        )
        .reset_index()
    )


METHOD_DISPLAY = {
    "lp_two_source_monotone_ucb": ("o", "-",  "tab:blue",   "LP two-source monotone UCB"),
    "single_A_monotone_pac":      ("s", "--", "tab:green",  "Source A monotone PAC"),
    "single_B_monotone_pac":      ("^", "--", "tab:olive",  "Source B monotone PAC"),
    "best_of_singles_bonferroni": ("D", "-.", "tab:red",    "Best-of-singles (Bonferroni)"),
}


def make_plot(summary, out_path):
    datasets = list(summary["dataset"].drop_duplicates())
    fig, axes = plt.subplots(
        len(datasets),
        2,
        figsize=(11, 4 * len(datasets)),
        squeeze=False,
        constrained_layout=True,
    )
    for row, dataset in enumerate(datasets):
        sub = summary[summary["dataset"] == dataset]
        for method, (marker, ls, color, label) in METHOD_DISPLAY.items():
            d = sub[sub["method"] == method].sort_values("epsilon")
            if len(d) == 0:
                continue
            axes[row, 0].plot(
                d["epsilon"], d["mean_budget_saved"],
                marker=marker, linestyle=ls, color=color, label=label,
            )
            axes[row, 1].plot(
                d["epsilon"], d["mean_realized_error"],
                marker=marker, linestyle=ls, color=color, label=label,
            )

        oracle = (
            sub[sub["method"] == "lp_two_source_monotone_ucb"]
            .sort_values("epsilon")
            .drop_duplicates(subset=["epsilon"])
        )
        if len(oracle):
            axes[row, 0].plot(
                oracle["epsilon"], oracle["oracle_lp_saved"],
                marker="x", linestyle=":", color="black", alpha=0.6,
                label="LP oracle (full data)",
            )

        eps_vals = np.sort(sub["epsilon"].unique())
        axes[row, 1].plot(
            eps_vals, eps_vals,
            color="black", linewidth=1, alpha=0.35, label="target",
        )

        axes[row, 0].set_title(f"{dataset}: cost savings")
        axes[row, 0].set_xlabel("Target error epsilon")
        axes[row, 0].set_ylabel("Mean budget saved")
        axes[row, 0].set_ylim(0.0, 1.0)
        axes[row, 0].grid(True, alpha=0.25)
        axes[row, 0].legend(fontsize=8, loc="lower right")

        axes[row, 1].set_title(f"{dataset}: realized error")
        axes[row, 1].set_xlabel("Target error epsilon")
        axes[row, 1].set_ylabel("Mean realized error")
        axes[row, 1].grid(True, alpha=0.25)
        axes[row, 1].legend(fontsize=8, loc="upper left")

    fig.savefig(out_path, dpi=200)
    plt.close(fig)


def run(args):
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    thresholds = np.concatenate(
        [[-np.inf], np.linspace(0.0, 1.0, args.num_thresholds)]
    )
    trial_rng = np.random.default_rng(args.seed)

    synth_records = []
    trial_rows = []
    for dataset, rel_path in DEFAULT_DATASETS.items():
        y, yhat, conf = load_dataset(Path(rel_path))
        proxy_A, proxy_B, mistakes_A, mistakes_B = synthesize_two_sources(
            y, yhat, conf, seed=args.synth_seed, low_conf_max=args.low_conf_max,
        )
        n = len(y)
        lp_losses, lp_saved = evaluate_lp_grid(
            proxy_A, proxy_B, mistakes_A, mistakes_B, thresholds,
        )

        router_mistake = np.where(proxy_A <= proxy_B, mistakes_A, mistakes_B)
        synth_records.append({
            "dataset": dataset,
            "n": n,
            "source_A_accuracy": float(1 - mistakes_A.mean()),
            "source_B_accuracy": float(1 - mistakes_B.mean()),
            "either_correct_oracle": float(((~mistakes_A) | (~mistakes_B)).mean()),
            "router_lower_proxy_accuracy": float(1 - router_mistake.mean()),
        })

        for epsilon in args.epsilons:
            feasible = np.flatnonzero(lp_losses <= epsilon)
            oracle_idx = (
                feasible[np.argmax(lp_saved[feasible])] if len(feasible) else 0
            )
            oracle_saved_v = float(lp_saved[oracle_idx])
            oracle_error_v = float(lp_losses[oracle_idx])

            for trial in range(args.trials):
                m = max(1, int(round(args.cal_fraction * n)))
                sample_idx = trial_rng.integers(0, n, size=m)

                results = [
                    select_lp_two_source_ucb(
                        proxy_A, proxy_B, mistakes_A, mistakes_B, thresholds,
                        lp_losses, lp_saved, epsilon, args.alpha, sample_idx,
                    ),
                    {
                        "method": "single_A_monotone_pac",
                        **select_single_source_monotone(
                            proxy_A, mistakes_A, epsilon, args.alpha, sample_idx,
                        ),
                    },
                    {
                        "method": "single_B_monotone_pac",
                        **select_single_source_monotone(
                            proxy_B, mistakes_B, epsilon, args.alpha, sample_idx,
                        ),
                    },
                    select_best_of_singles(
                        proxy_A, mistakes_A, proxy_B, mistakes_B,
                        epsilon, args.alpha, sample_idx,
                    ),
                ]
                for r in results:
                    trial_rows.append({
                        "dataset": dataset,
                        "trial": trial,
                        "epsilon": epsilon,
                        "alpha": args.alpha,
                        "n": n,
                        "num_policies": len(thresholds),
                        "oracle_lp_saved": oracle_saved_v,
                        "oracle_lp_error": oracle_error_v,
                        **r,
                    })

    trials_df = pd.DataFrame(trial_rows)
    summary = summarize_trials(trial_rows)
    synth_df = pd.DataFrame(synth_records)

    trials_path = out_dir / "two_source_offline_pac_trials.csv"
    summary_path = out_dir / "two_source_offline_pac_summary.csv"
    synth_path = out_dir / "two_source_offline_pac_construction.csv"
    plot_path = out_dir / "two_source_offline_pac_summary.png"

    trials_df.to_csv(trials_path, index=False)
    summary.to_csv(summary_path, index=False)
    synth_df.to_csv(synth_path, index=False)
    make_plot(summary, plot_path)

    print(f"Wrote {trials_path}")
    print(f"Wrote {summary_path}")
    print(f"Wrote {synth_path}")
    print(f"Wrote {plot_path}")
    print()
    print("Constructed two-source statistics:")
    print(synth_df.to_string(index=False, float_format=lambda x: f"{x:.4f}"))
    print()
    print(summary.to_string(index=False, float_format=lambda x: f"{x:.4f}"))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=500)
    parser.add_argument("--seed", type=int, default=357)
    parser.add_argument("--synth-seed", type=int, default=20260526)
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--cal-fraction", type=float, default=0.2)
    parser.add_argument("--num-thresholds", type=int, default=201)
    parser.add_argument("--low-conf-max", type=float, default=0.2)
    parser.add_argument(
        "--epsilons", type=float, nargs="+", default=[0.05, 0.10, 0.15],
    )
    parser.add_argument(
        "--output-dir", default="experiments/results/two_source_offline_pac",
    )
    return parser.parse_args()


if __name__ == "__main__":
    run(parse_args())
