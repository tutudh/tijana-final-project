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
    "ImageNet": "HW4_副本/imagenet.csv",
    "ImageNetV2": "HW4_副本/imagenetv2.csv",
}


def load_dataset(path: Path):
    df = pd.read_csv(path)
    scores = 1.0 - df["confidence"].to_numpy(dtype=float)
    mistakes = (df["Y"].to_numpy() != df["Yhat"].to_numpy())
    return scores, mistakes


def evaluate_grid(scores, mistakes, thresholds):
    ai_mask = scores[:, None] <= thresholds[None, :]
    losses = np.mean(ai_mask & mistakes[:, None], axis=0)
    saved = np.mean(ai_mask, axis=0)
    return losses, saved


def select_fixed_price_monotone_ucb(
    scores,
    mistakes,
    thresholds,
    full_losses,
    full_saved,
    epsilon,
    alpha,
    sample_idx,
):
    n = len(scores)
    _ = n
    m = len(sample_idx)
    sample_scores = scores[sample_idx]
    sample_mistakes = mistakes[sample_idx]

    sample_ai = sample_scores[:, None] <= thresholds[None, :]
    empirical_loss = np.mean(sample_ai & sample_mistakes[:, None], axis=0)
    # In the single-source setting the fixed-price policies are nested
    # uncertainty-threshold rules, so the one-sided DKW/monotone-threshold
    # argument removes the union-bound factor over the threshold grid.
    radius = np.sqrt(np.log(1.0 / alpha) / (2.0 * m))
    ucb = empirical_loss + radius

    feasible = np.flatnonzero(ucb <= epsilon)
    if len(feasible) == 0:
        selected = 0
    else:
        selected = feasible[np.argmax(full_saved[feasible])]

    return {
        "method": "fixed_price_monotone_ucb",
        "m": m,
        "radius": radius,
        "selected_threshold": thresholds[selected],
        "empirical_loss": empirical_loss[selected],
        "ucb": ucb[selected],
        "realized_error": full_losses[selected],
        "budget_saved": full_saved[selected],
        "avg_cost": 1.0 - full_saved[selected],
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


def select_original_pac_hoeffding(scores, mistakes, epsilon, alpha, sample_idx):
    """Original monotone PAC-labeling threshold from HW4.

    This exploits that the AI-labeled set is nested as the uncertainty
    threshold grows. Therefore it uses a one-threshold Hoeffding radius rather
    than a union bound over all candidate prices.
    """
    m = len(sample_idx)
    radius = np.sqrt(np.log(1.0 / alpha) / (2.0 * m))
    q = first_exceeding_error_count(m, epsilon, alpha)

    sampled_mistake_scores = scores[sample_idx[mistakes[sample_idx]]]
    if q <= 0:
        threshold = -np.inf
    elif len(sampled_mistake_scores) < q:
        threshold = np.inf
    else:
        threshold = np.partition(sampled_mistake_scores, q - 1)[q - 1]

    ai_used = scores < threshold
    sample_ai = scores[sample_idx] < threshold
    sample_loss = np.mean(sample_ai & mistakes[sample_idx])
    realized_error = np.mean(ai_used & mistakes)
    budget_saved = np.mean(ai_used)

    return {
        "method": "original_pac_hoeffding",
        "m": m,
        "radius": radius,
        "selected_threshold": threshold,
        "empirical_loss": sample_loss,
        "ucb": sample_loss + radius if budget_saved > 0 else 0.0,
        "realized_error": realized_error,
        "budget_saved": budget_saved,
        "avg_cost": 1.0 - budget_saved,
        "violated": float(realized_error > epsilon + 1e-12),
    }


def summarize_trials(rows):
    df = pd.DataFrame(rows)
    group_cols = ["dataset", "method", "epsilon"]
    summary = (
        df.groupby(group_cols)
        .agg(
            n=("n", "first"),
            model_error=("model_error", "first"),
            m=("m", "first"),
            num_policies=("num_policies", "first"),
            radius=("radius", "first"),
            violation_rate=("violated", "mean"),
            mean_realized_error=("realized_error", "mean"),
            q95_realized_error=("realized_error", lambda x: np.quantile(x, 0.95)),
            mean_ucb=("ucb", "mean"),
            mean_budget_saved=("budget_saved", "mean"),
            mean_avg_cost=("avg_cost", "mean"),
            median_threshold=("selected_threshold", "median"),
            oracle_grid_budget_saved=("oracle_grid_budget_saved", "first"),
            oracle_grid_error=("oracle_grid_error", "first"),
        )
        .reset_index()
    )
    return summary


def make_plot(summary, out_path):
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), constrained_layout=True)
    colors = {
        "ImageNet": "tab:blue",
        "ImageNetV2": "tab:orange",
    }
    method_styles = {
        "fixed_price_monotone_ucb": ("o", "-"),
        "original_pac_hoeffding": ("s", "--"),
    }
    method_labels = {
        "fixed_price_monotone_ucb": "fixed-price monotone UCB",
        "original_pac_hoeffding": "original PAC",
    }

    for (dataset, method), sub in summary.groupby(["dataset", "method"]):
        sub = sub.sort_values("epsilon")
        color = colors.get(dataset)
        marker, linestyle = method_styles.get(method, ("o", "-"))
        label = f"{dataset}: {method_labels.get(method, method)}"
        axes[0].plot(
            sub["epsilon"],
            sub["mean_budget_saved"],
            marker=marker,
            linestyle=linestyle,
            color=color,
            label=label,
        )
        axes[1].plot(
            sub["epsilon"],
            sub["mean_realized_error"],
            marker=marker,
            linestyle=linestyle,
            color=color,
            label=label,
        )

    for dataset, sub in summary.groupby("dataset"):
        sub = (
            sub.sort_values("epsilon")
            .drop_duplicates(subset=["epsilon"], keep="first")
        )
        color = colors.get(dataset)
        axes[0].plot(
            sub["epsilon"],
            sub["oracle_grid_budget_saved"],
            marker="x",
            linestyle=":",
            color=color,
            alpha=0.75,
            label=f"{dataset}: oracle grid",
        )

    eps_values = np.sort(summary["epsilon"].unique())
    axes[1].plot(
        eps_values,
        eps_values,
        color="black",
        linewidth=1,
        alpha=0.35,
        label="target",
    )

    axes[0].set_xlabel("Target error epsilon")
    axes[0].set_ylabel("Average budget saved")
    axes[0].set_title("Cost savings")
    axes[0].set_ylim(0.0, 1.0)
    axes[0].grid(True, alpha=0.25)
    axes[0].legend(fontsize=8)

    axes[1].set_xlabel("Target error epsilon")
    axes[1].set_ylabel("Average realized error")
    axes[1].set_title("Certified policy error")
    axes[1].grid(True, alpha=0.25)
    axes[1].legend(fontsize=8)

    fig.savefig(out_path, dpi=200)
    plt.close(fig)


def run(args):
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    thresholds = np.concatenate(
        [[-np.inf], np.linspace(0.0, 1.0, args.num_thresholds)]
    )
    rng = np.random.default_rng(args.seed)

    trial_rows = []
    for dataset, rel_path in DEFAULT_DATASETS.items():
        scores, mistakes = load_dataset(Path(rel_path))
        n = len(scores)
        model_error = float(mistakes.mean())
        full_losses, full_saved = evaluate_grid(scores, mistakes, thresholds)

        for epsilon in args.epsilons:
            feasible_oracle = np.flatnonzero(full_losses <= epsilon)
            oracle_idx = feasible_oracle[np.argmax(full_saved[feasible_oracle])]
            oracle_saved = float(full_saved[oracle_idx])
            oracle_error = float(full_losses[oracle_idx])

            for trial in range(args.trials):
                m = max(1, int(round(args.cal_fraction * n)))
                sample_idx = rng.integers(0, n, size=m)
                selected_methods = [
                    select_fixed_price_monotone_ucb(
                        scores=scores,
                        mistakes=mistakes,
                        thresholds=thresholds,
                        full_losses=full_losses,
                        full_saved=full_saved,
                        epsilon=epsilon,
                        alpha=args.alpha,
                        sample_idx=sample_idx,
                    ),
                    select_original_pac_hoeffding(
                        scores=scores,
                        mistakes=mistakes,
                        epsilon=epsilon,
                        alpha=args.alpha,
                        sample_idx=sample_idx,
                    ),
                ]
                for selected in selected_methods:
                    trial_rows.append(
                        {
                            "dataset": dataset,
                            "trial": trial,
                            "epsilon": epsilon,
                            "alpha": args.alpha,
                            "n": n,
                            "model_error": model_error,
                            "num_policies": len(thresholds),
                            "oracle_grid_budget_saved": oracle_saved,
                            "oracle_grid_error": oracle_error,
                            **selected,
                        }
                    )

    trials_df = pd.DataFrame(trial_rows)
    summary = summarize_trials(trial_rows)

    trials_path = out_dir / "simple_offline_pac_trials.csv"
    summary_path = out_dir / "simple_offline_pac_summary.csv"
    plot_path = out_dir / "simple_offline_pac_summary.png"

    trials_df.to_csv(trials_path, index=False)
    summary.to_csv(summary_path, index=False)
    make_plot(summary, plot_path)

    print(f"Wrote {trials_path}")
    print(f"Wrote {summary_path}")
    print(f"Wrote {plot_path}")
    print()
    print(summary.to_string(index=False, float_format=lambda x: f"{x:.4f}"))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=500)
    parser.add_argument("--seed", type=int, default=357)
    parser.add_argument("--alpha", type=float, default=0.05)
    parser.add_argument("--cal-fraction", type=float, default=0.2)
    parser.add_argument("--num-thresholds", type=int, default=201)
    parser.add_argument(
        "--epsilons",
        type=float,
        nargs="+",
        default=[0.05, 0.10, 0.15],
    )
    parser.add_argument(
        "--output-dir",
        default="results/simple_offline_pac",
    )
    return parser.parse_args()


if __name__ == "__main__":
    run(parse_args())
