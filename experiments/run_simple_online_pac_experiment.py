import argparse
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/private/tmp/matplotlib")

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt

EXPERIMENTS_DIR = Path(__file__).resolve().parent
DEFAULT_DATA_DIR = EXPERIMENTS_DIR / "data"
DEFAULT_OUTPUT_DIR = EXPERIMENTS_DIR / "results" / "simple_online_pac"
DATASET_FILENAMES = {
    "ImageNet": "imagenet.csv",
    "ImageNetV2": "imagenetv2.csv",
}


def load_dataset(path: Path):
    df = pd.read_csv(path)
    proxy_loss = 1.0 - df["confidence"].to_numpy(dtype=float)
    mistakes = (df["Y"].to_numpy() != df["Yhat"].to_numpy())
    return proxy_loss, mistakes


def run_online_trial(
    proxy_loss,
    mistakes,
    epsilon,
    audit_prob,
    eta,
    rho,
    rng,
    init_lambda=None,
):
    n = len(proxy_loss)
    order = rng.permutation(n)
    scores = np.maximum(proxy_loss[order], rho)
    errs = mistakes[order]

    if init_lambda is None:
        init_lambda = 1.0 / max(epsilon, 1e-12)

    lam = float(init_lambda)
    sum_h = 0.0
    sum_hhat = 0.0
    sum_zhat = 0.0
    sum_g = 0.0
    ai_attempts = 0
    audits = 0
    deferrals = 0
    expert_queries = 0
    released_ai = 0

    for score, is_mistake in zip(scores, errs):
        # AI cost is zero and expert cost is one. The fixed-price rule uses AI
        # exactly when lambda * proxy_loss < 1.
        use_ai = lam * score < 1.0
        if use_ai:
            ai_attempts += 1
            audited = rng.random() < audit_prob
            if audited:
                audits += 1
                expert_queries += 1
                audit_weight = 1.0 / audit_prob
                hhat_t = audit_weight * float(is_mistake)
                zhat_t = audit_weight * (float(is_mistake) - epsilon)
                g_t = 0.0
            else:
                released_ai += 1
                hhat_t = 0.0
                zhat_t = 0.0
                g_t = float(is_mistake)
            h_t = float(is_mistake)
        else:
            deferrals += 1
            expert_queries += 1
            h_t = 0.0
            hhat_t = 0.0
            zhat_t = -epsilon
            g_t = 0.0

        sum_h += h_t
        sum_hhat += hhat_t
        sum_zhat += zhat_t
        sum_g += g_t
        lam = max(0.0, lam + eta * zhat_t)

    lambda_def = 1.0 / rho
    lambda_bound = max(float(init_lambda), lambda_def + eta * (1.0 - epsilon) / audit_prob)
    theory_bound = (
        epsilon
        + lambda_bound / (eta * n)
        + (1.0 / audit_prob) * np.sqrt(2.0 * np.log(1.0 / 0.05) / n)
    )

    return {
        "epsilon0": epsilon,
        "eta": eta,
        "rho": rho,
        "audit_prob": audit_prob,
        "init_lambda": init_lambda,
        "final_lambda": lam,
        "theory_h_bound_delta_0.05": theory_bound,
        "counterfactual_ai_error": sum_h / n,
        "ipw_error_estimate": sum_hhat / n,
        "centered_update_estimate": sum_zhat / n,
        "final_error_after_correction": sum_g / n,
        "ai_attempt_rate": ai_attempts / n,
        "audit_rate": audits / n,
        "deferral_rate": deferrals / n,
        "expert_query_rate": expert_queries / n,
        "budget_saved": 1.0 - expert_queries / n,
        "released_ai_rate": released_ai / n,
        "violated_final": float((sum_g / n) > epsilon + 1e-12),
        "violated_counterfactual": float((sum_h / n) > epsilon + 1e-12),
    }


def summarize_trials(rows):
    df = pd.DataFrame(rows)
    group_cols = ["dataset", "epsilon", "audit_prob"]
    return (
        df.groupby(group_cols)
        .agg(
            n=("n", "first"),
            model_error=("model_error", "first"),
            trials=("trial", "count"),
            eta=("eta", "first"),
            rho=("rho", "first"),
            init_lambda=("init_lambda", "first"),
            theory_h_bound_delta_0_05=("theory_h_bound_delta_0.05", "first"),
            violation_rate_final=("violated_final", "mean"),
            violation_rate_counterfactual=("violated_counterfactual", "mean"),
            mean_final_error=("final_error_after_correction", "mean"),
            q95_final_error=("final_error_after_correction", lambda x: np.quantile(x, 0.95)),
            mean_counterfactual_ai_error=("counterfactual_ai_error", "mean"),
            mean_ipw_error_estimate=("ipw_error_estimate", "mean"),
            mean_centered_update_estimate=("centered_update_estimate", "mean"),
            mean_budget_saved=("budget_saved", "mean"),
            mean_expert_query_rate=("expert_query_rate", "mean"),
            mean_audit_rate=("audit_rate", "mean"),
            mean_deferral_rate=("deferral_rate", "mean"),
            mean_ai_attempt_rate=("ai_attempt_rate", "mean"),
            mean_released_ai_rate=("released_ai_rate", "mean"),
            mean_final_lambda=("final_lambda", "mean"),
        )
        .reset_index()
    )


def make_plot(summary, out_path):
    datasets = list(summary["dataset"].drop_duplicates())
    fig, axes = plt.subplots(
        len(datasets),
        2,
        figsize=(10, 4 * len(datasets)),
        squeeze=False,
        constrained_layout=True,
    )

    for row, dataset in enumerate(datasets):
        sub_dataset = summary[summary["dataset"] == dataset]
        for audit_prob, sub in sub_dataset.groupby("audit_prob"):
            sub = sub.sort_values("epsilon")
            label = f"audit p={audit_prob:g}"
            axes[row, 0].plot(
                sub["epsilon"],
                sub["mean_budget_saved"],
                marker="o",
                label=label,
            )
            axes[row, 1].plot(
                sub["epsilon"],
                sub["mean_final_error"],
                marker="o",
                label=label,
            )
            axes[row, 1].plot(
                sub["epsilon"],
                sub["mean_counterfactual_ai_error"],
                marker="x",
                linestyle="--",
                alpha=0.7,
            )

        eps_values = np.sort(sub_dataset["epsilon"].unique())
        axes[row, 1].plot(
            eps_values,
            eps_values,
            color="black",
            linewidth=1,
            alpha=0.35,
            label="target",
        )

        axes[row, 0].set_title(f"{dataset}: expert budget saved")
        axes[row, 0].set_xlabel("Target error epsilon")
        axes[row, 0].set_ylabel("Budget saved")
        axes[row, 0].set_ylim(0.0, 1.0)
        axes[row, 0].grid(True, alpha=0.25)
        axes[row, 0].legend(fontsize=8)

        axes[row, 1].set_title(f"{dataset}: final and counterfactual error")
        axes[row, 1].set_xlabel("Target error epsilon")
        axes[row, 1].set_ylabel("Error")
        axes[row, 1].grid(True, alpha=0.25)
        axes[row, 1].legend(fontsize=8)

    fig.savefig(out_path, dpi=200)
    plt.close(fig)


def run(args):
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    data_dir = Path(args.data_dir)
    datasets = {
        name: data_dir / filename
        for name, filename in DATASET_FILENAMES.items()
    }

    rng = np.random.default_rng(args.seed)
    trial_rows = []

    for dataset, path in datasets.items():
        proxy_loss, mistakes = load_dataset(path)
        n = len(proxy_loss)
        model_error = float(mistakes.mean())

        for epsilon in args.epsilons:
            for audit_prob in args.audit_probs:
                for trial in range(args.trials):
                    result = run_online_trial(
                        proxy_loss=proxy_loss,
                        mistakes=mistakes,
                        epsilon=epsilon,
                        audit_prob=audit_prob,
                        eta=args.eta,
                        rho=args.rho,
                        rng=rng,
                        init_lambda=args.init_lambda,
                    )
                    trial_rows.append(
                        {
                            "dataset": dataset,
                            "trial": trial,
                            "epsilon": epsilon,
                            "n": n,
                            "model_error": model_error,
                            **result,
                        }
                    )

    trials_df = pd.DataFrame(trial_rows)
    summary = summarize_trials(trial_rows)

    trials_path = out_dir / "simple_online_pac_trials.csv"
    summary_path = out_dir / "simple_online_pac_summary.csv"
    plot_path = out_dir / "simple_online_pac_summary.png"

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
    parser.add_argument("--trials", type=int, default=100)
    parser.add_argument("--seed", type=int, default=357)
    parser.add_argument("--eta", type=float, default=1.0)
    parser.add_argument("--rho", type=float, default=0.01)
    parser.add_argument("--init-lambda", type=float, default=None)
    parser.add_argument(
        "--audit-probs",
        type=float,
        nargs="+",
        default=[0.1, 0.2, 0.5],
    )
    parser.add_argument(
        "--epsilons",
        type=float,
        nargs="+",
        default=[0.05, 0.10, 0.15],
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=DEFAULT_DATA_DIR,
        help="Directory containing imagenet.csv and imagenetv2.csv.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
    )
    return parser.parse_args()


if __name__ == "__main__":
    run(parse_args())
