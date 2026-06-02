import argparse
from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy.stats import norm
from sklearn.linear_model import LogisticRegression


EPSILON = 0.05
ALPHA = 0.05
TRIALS = 1000
SEED = 35704


@dataclass(frozen=True)
class Bounds:
    hoeffding_q: int
    clt_q: int


def first_exceeding_error_count(m: int, method: str) -> int:
    """Return the smallest sampled-error count k with UCB(k/m) > epsilon."""
    if method == "hoeffding":
        rad = np.sqrt(np.log(1.0 / ALPHA) / (2.0 * m))
        vals = np.arange(m + 1) / m + rad
    elif method == "clt":
        p = np.arange(m + 1) / m
        vals = p + norm.ppf(1.0 - ALPHA) * np.sqrt(np.maximum(p * (1.0 - p), 0.0) / m)
    else:
        raise ValueError(method)
    hits = np.flatnonzero(vals > EPSILON)
    if len(hits) == 0:
        return m + 1
    return int(hits[0])


def get_bounds(m: int) -> Bounds:
    return Bounds(
        hoeffding_q=first_exceeding_error_count(m, "hoeffding"),
        clt_q=first_exceeding_error_count(m, "clt"),
    )


def one_trial(scores: np.ndarray, mistakes: np.ndarray, sample_idx: np.ndarray, q: int):
    if q <= 0:
        return 0.0, 0.0
    sampled_mistake_scores = scores[sample_idx[mistakes[sample_idx]]]
    if len(sampled_mistake_scores) < q:
        threshold = np.inf
    else:
        threshold = np.partition(sampled_mistake_scores, q - 1)[q - 1]
    ai_used = scores < threshold
    err = np.mean(mistakes & ai_used)
    saved = np.mean(ai_used)
    return err, saved


def summarize(values):
    arr = np.asarray(values)
    return np.quantile(arr[:, 0], 1.0 - ALPHA, method="higher"), np.mean(arr[:, 1])


def run_fixed_score(scores, mistakes, trials=TRIALS, seed=SEED):
    rng = np.random.default_rng(seed)
    n = len(scores)
    m = n // 10
    bounds = get_bounds(m)
    out = {"hoeffding": [], "clt": []}
    for _ in range(trials):
        sample_idx = rng.integers(0, n, size=m)
        out["hoeffding"].append(one_trial(scores, mistakes, sample_idx, bounds.hoeffding_q))
        out["clt"].append(one_trial(scores, mistakes, sample_idx, bounds.clt_q))
    return {method: summarize(vals) for method, vals in out.items()}


def run_noisy_scores(base_scores, mistakes, taus, trials=TRIALS, seed=SEED):
    rng = np.random.default_rng(seed)
    n = len(base_scores)
    m = n // 10
    bounds = get_bounds(m)
    rows = []
    for tau in taus:
        out = {"hoeffding": [], "clt": []}
        for _ in range(trials):
            scores = base_scores + tau * rng.standard_normal(n)
            sample_idx = rng.integers(0, n, size=m)
            out["hoeffding"].append(one_trial(scores, mistakes, sample_idx, bounds.hoeffding_q))
            out["clt"].append(one_trial(scores, mistakes, sample_idx, bounds.clt_q))
        for method, vals in out.items():
            q95, saved = summarize(vals)
            rows.append((tau, method, q95, saved))
    return rows


EPS = 1e-6


def _logit(c: np.ndarray) -> np.ndarray:
    cc = np.clip(c, EPS, 1.0 - EPS)
    return np.log(cc / (1.0 - cc))


def _fit_platt(source_scores, source_mistakes):
    source_C = 1.0 - source_scores
    lr = LogisticRegression(C=1.0, solver="lbfgs", max_iter=1000)
    lr.fit(_logit(source_C).reshape(-1, 1), source_mistakes.astype(int))
    return lr


def platt_scaling(source_scores, source_mistakes, target_scores):
    """Single-parameter logistic on logit(C), predicting the mistake indicator.

    This is the one-dimensional analog of temperature scaling for the top-1
    confidence (we do not have full logits). Output is the calibrated estimate
    of Pr(mistake | C).
    """
    lr = _fit_platt(source_scores, source_mistakes)
    target_C = 1.0 - target_scores
    return lr.predict_proba(_logit(target_C).reshape(-1, 1))[:, 1]


def platt_binning(source_scores, source_mistakes, target_scores, num_bins=20):
    """Platt scaling followed by histogram binning on the calibrated score."""
    lr = _fit_platt(source_scores, source_mistakes)
    source_C = 1.0 - source_scores
    target_C = 1.0 - target_scores
    platt_source = lr.predict_proba(_logit(source_C).reshape(-1, 1))[:, 1]
    platt_target = lr.predict_proba(_logit(target_C).reshape(-1, 1))[:, 1]

    quantiles = np.quantile(platt_source, np.linspace(0, 1, num_bins + 1))
    edges = np.unique(quantiles)
    if len(edges) <= 2:
        return platt_target
    source_bins = np.searchsorted(edges[1:-1], platt_source, side="right")
    global_rate = source_mistakes.mean()
    rates = np.full(len(edges) - 1, global_rate)
    for b in range(len(rates)):
        mask = source_bins == b
        if np.any(mask):
            rates[b] = source_mistakes[mask].mean()
    target_bins = np.searchsorted(edges[1:-1], platt_target, side="right")
    return rates[target_bins]


def multiaccuracy(
    source_scores,
    source_yhat,
    source_mistakes,
    target_scores,
    target_yhat,
    n_iter=300,
    alpha=0.005,
    gamma_n_min=5,
):
    """Multiaccuracy with predicted-class groups.

    Each predicted class is a group G_y = {x : Yhat(x) = y}. We iteratively
    pick the class with the largest mean residual (mistake - f) on the source
    set and shift f by that residual on the corresponding group of both source
    and target points. Iterations stop when all eligible groups have residual
    below alpha.
    """
    K = int(max(source_yhat.max(), target_yhat.max())) + 1
    f_source = source_scores.copy()
    f_target = target_scores.copy()

    group_counts = np.bincount(source_yhat, minlength=K).astype(float)
    eligible = group_counts >= gamma_n_min
    if not eligible.any():
        return f_target

    mistake_sums = np.bincount(
        source_yhat, weights=source_mistakes.astype(float), minlength=K
    )

    for _ in range(n_iter):
        f_source_sums = np.bincount(source_yhat, weights=f_source, minlength=K)
        with np.errstate(divide="ignore", invalid="ignore"):
            deltas = np.where(
                eligible, (mistake_sums - f_source_sums) / group_counts, 0.0
            )
        abs_deltas = np.abs(deltas)
        y_star = int(np.argmax(abs_deltas))
        if abs_deltas[y_star] < alpha:
            break
        delta = deltas[y_star]
        mask_s = source_yhat == y_star
        mask_t = target_yhat == y_star
        f_source[mask_s] = np.clip(f_source[mask_s] + delta, 0.0, 1.0)
        f_target[mask_t] = np.clip(f_target[mask_t] + delta, 0.0, 1.0)
    return f_target


def run_recalibrated_inplace(scores, yhat, mistakes, trials=TRIALS, seed=SEED):
    """In-sample calibration: the same m=0.1n pilot sample is used both to fit
    each score transformation and to compute the PAC upper bound. This mirrors
    parts 3.1 and 3.2 exactly, with the calibration step inserted between
    sampling and threshold selection.
    """
    rng = np.random.default_rng(seed)
    n = len(scores)
    m = n // 10
    bounds = get_bounds(m)
    methods = ["raw", "platt", "platt-binning", "multiaccuracy"]
    out = {method: {"hoeffding": [], "clt": []} for method in methods}

    for _ in range(trials):
        sample_idx = rng.integers(0, n, size=m)
        sampled_scores = scores[sample_idx]
        sampled_yhat = yhat[sample_idx]
        sampled_mistakes = mistakes[sample_idx]

        score_map = {
            "raw": scores,
            "platt": platt_scaling(sampled_scores, sampled_mistakes, scores),
            "platt-binning": platt_binning(sampled_scores, sampled_mistakes, scores),
            "multiaccuracy": multiaccuracy(
                sampled_scores,
                sampled_yhat,
                sampled_mistakes,
                scores,
                yhat,
            ),
        }
        for method, s in score_map.items():
            out[method]["hoeffding"].append(
                one_trial(s, mistakes, sample_idx, bounds.hoeffding_q)
            )
            out[method]["clt"].append(
                one_trial(s, mistakes, sample_idx, bounds.clt_q)
            )

    rows = []
    for method in methods:
        for bound_method, vals in out[method].items():
            q95, saved = summarize(vals)
            rows.append((method, bound_method, q95, saved))
    return rows


def load_dataset(path):
    df = pd.read_csv(path)
    y = df["Y"].to_numpy()
    yhat = df["Yhat"].to_numpy()
    confidence = df["confidence"].to_numpy()
    scores = 1.0 - confidence
    mistakes = y != yhat
    return scores, yhat.astype(int), mistakes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=TRIALS)
    args = parser.parse_args()

    datasets = {
        "ImageNet": "imagenet.csv",
        "ImageNetV2": "imagenetv2.csv",
    }
    taus = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]

    loaded = {dname: load_dataset(path) for dname, path in datasets.items()}
    summary_rows = []
    noisy_rows = []

    for dname, data in loaded.items():
        scores, yhat, mistakes = data
        n = len(scores)
        m = n // 10
        bounds = get_bounds(m)
        print(f"{dname}: n={n}, model_error={mistakes.mean():.4f}, m={m}, "
              f"q_H={bounds.hoeffding_q}, q_CLT={bounds.clt_q}")

        fixed = run_fixed_score(scores, mistakes, trials=args.trials, seed=SEED)
        for method, (q95, saved) in fixed.items():
            summary_rows.append((dname, method, q95, saved))

        for tau, method, q95, saved in run_noisy_scores(scores, mistakes, taus, trials=args.trials, seed=SEED + 1):
            noisy_rows.append((dname, tau, method, q95, saved))

    recal_rows = []
    for dname, (scores, yhat, mistakes) in loaded.items():
        for score_method, bound_method, q95, saved in run_recalibrated_inplace(
            scores, yhat, mistakes, trials=args.trials, seed=SEED + 2
        ):
            recal_rows.append((dname, score_method, bound_method, q95, saved))

    pd.DataFrame(summary_rows, columns=["dataset", "bound", "q95_error", "avg_budget_saved"]).to_csv(
        "hw4_main_results.csv", index=False
    )
    pd.DataFrame(noisy_rows, columns=["dataset", "tau", "bound", "q95_error", "avg_budget_saved"]).to_csv(
        "hw4_noisy_results.csv", index=False
    )
    pd.DataFrame(
        recal_rows,
        columns=["dataset", "score_method", "bound", "q95_error", "avg_budget_saved"],
    ).to_csv("hw4_recalibrated_results.csv", index=False)

    print("\nMain results")
    print(pd.read_csv("hw4_main_results.csv").to_string(index=False))
    print("\nNoisy-score results")
    print(pd.read_csv("hw4_noisy_results.csv").to_string(index=False))
    print("\nRecalibrated-score results")
    print(pd.read_csv("hw4_recalibrated_results.csv").to_string(index=False))


if __name__ == "__main__":
    main()
