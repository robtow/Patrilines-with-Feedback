import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# Parameters
# -----------------------------

NUM_LINEAGES = 100
POP_SIZE = 1000
GENERATIONS = 100
TRIALS = 40

NOISE_SIGMA = 0.2

# Leakage / informal channel
EPP_RATE = 0.03
EPP_STATUS_WEIGHT = 0.5
SIGNAL_CORRELATION = 0.5

# Bounded compression window
WINDOW_START = 30
WINDOW_END = 60

BASE_SKEW = 1.00
WINDOW_SKEW = 1.05
POST_SKEW = 1.00

# Fragility parameters
MIN_LINEAGE_SIZE = 10
MIN_PENALTY = 0.05
BASE_FRAGILITY_ALPHA = 0.5
FRAGILITY_GAIN = 2.0

# Plotting / runs
SAMPLE_RUNS = 8
RANDOM_SEED = 42

FIGURE_PATH = Path("figures/sim_v0_8.png")
SUMMARY_PATH = Path("notes/v0_8_summary.json")


# -----------------------------
# Utilities
# -----------------------------

def normalize(probs: np.ndarray) -> np.ndarray:
    probs = np.array(probs, dtype=float)
    total = probs.sum()
    if total <= 0:
        return np.ones_like(probs) / len(probs)
    return probs / total


def shannon_entropy(counts: np.ndarray) -> float:
    counts = np.array(counts, dtype=float)
    total = counts.sum()
    if total == 0:
        return 0.0
    p = counts / total
    p = p[p > 0]
    return float(-(p * np.log(p)).sum())


def effective_lineages(counts: np.ndarray) -> float:
    return float(np.exp(shannon_entropy(counts)))


def current_skew(gen: int) -> float:
    if gen < WINDOW_START:
        return BASE_SKEW
    if gen < WINDOW_END:
        return WINDOW_SKEW
    return POST_SKEW


def fragility_multiplier(counts: np.ndarray, alpha: float) -> np.ndarray:
    counts = np.array(counts, dtype=float)
    ratio = counts / MIN_LINEAGE_SIZE
    ratio = np.clip(ratio, 0.0, 1.0)

    shaped = ratio ** alpha
    shaped = np.where(counts >= MIN_LINEAGE_SIZE, 1.0, shaped)
    shaped = np.maximum(shaped, MIN_PENALTY)
    return shaped


def compute_attractiveness(counts: np.ndarray) -> np.ndarray:
    """
    Informal selection signal.
    SIGNAL_CORRELATION controls alignment with formal lineage size.
    """
    base = normalize(counts)
    noise = np.random.lognormal(mean=0.0, sigma=0.5, size=len(counts))

    if SIGNAL_CORRELATION == 0.0:
        attr = noise
    elif SIGNAL_CORRELATION > 0.0:
        attr = (base ** SIGNAL_CORRELATION) * noise
    else:
        inv = 1.0 / (base + 1e-9)
        inv = normalize(inv)
        attr = (inv ** abs(SIGNAL_CORRELATION)) * noise

    return normalize(attr)


def top_k_shares(counts: np.ndarray) -> dict:
    counts = np.array(counts, dtype=float)
    total = counts.sum()
    if total <= 0:
        return {"top1": 0.0, "top3": 0.0, "top5": 0.0}

    sorted_counts = np.sort(counts)[::-1]
    return {
        "top1": float(sorted_counts[:1].sum() / total),
        "top3": float(sorted_counts[:3].sum() / total),
        "top5": float(sorted_counts[:5].sum() / total),
    }


def first_difference(series: np.ndarray) -> np.ndarray:
    return np.diff(series, prepend=series[0])


def second_difference(series: np.ndarray) -> np.ndarray:
    d1 = first_difference(series)
    return np.diff(d1, prepend=d1[0])


def late_run_slope(series: np.ndarray, start: int = 70) -> float:
    x = np.arange(start, len(series))
    y = series[start:]
    if len(x) < 2:
        return 0.0
    m, _b = np.polyfit(x, y, 1)
    return float(m)


# -----------------------------
# Single run
# -----------------------------

def run_once() -> dict:
    counts = np.ones(NUM_LINEAGES, dtype=float) * (POP_SIZE // NUM_LINEAGES)

    entropy_hist = []
    neff_hist = []
    active_hist = []
    alpha_hist = []
    skew_hist = []
    concentration_hist = []

    for gen in range(GENERATIONS):
        skew = current_skew(gen)

        # Global concentration state
        current_neff = effective_lineages(counts)
        concentration = 1.0 - (current_neff / NUM_LINEAGES)
        concentration = np.clip(concentration, 0.0, 1.0)

        # Endogenous fragility from concentration
        effective_alpha = BASE_FRAGILITY_ALPHA + FRAGILITY_GAIN * concentration

        # Formal channel
        formal_probs = normalize(counts)
        formal_probs = formal_probs ** skew
        formal_probs *= fragility_multiplier(counts, effective_alpha)

        if NOISE_SIGMA > 0:
            noise = np.random.lognormal(mean=0.0, sigma=NOISE_SIGMA, size=len(formal_probs))
            formal_probs *= noise

        formal_probs = normalize(formal_probs)

        # Informal channel
        attractiveness = compute_attractiveness(counts)
        uniform_probs = np.ones(NUM_LINEAGES, dtype=float) / NUM_LINEAGES

        epp_probs = (
            EPP_STATUS_WEIGHT * attractiveness
            + (1.0 - EPP_STATUS_WEIGHT) * uniform_probs
        )
        epp_probs = normalize(epp_probs)

        # Combined channel
        total_probs = (1.0 - EPP_RATE) * formal_probs + EPP_RATE * epp_probs
        total_probs = normalize(total_probs)

        counts = np.random.multinomial(POP_SIZE, total_probs)

        entropy_hist.append(shannon_entropy(counts))
        neff_hist.append(effective_lineages(counts))
        active_hist.append(int(np.count_nonzero(counts)))
        alpha_hist.append(float(effective_alpha))
        skew_hist.append(float(skew))
        concentration_hist.append(float(concentration))

    entropy = np.array(entropy_hist)
    neff = np.array(neff_hist)
    active = np.array(active_hist)
    alpha = np.array(alpha_hist)
    skew = np.array(skew_hist)
    concentration = np.array(concentration_hist)

    d_neff = first_difference(neff)
    d_active = first_difference(active)
    dd_neff = second_difference(neff)

    shares = top_k_shares(counts)

    window_midpoint = (WINDOW_START + WINDOW_END) / 2.0
    peak_pruning_gen = int(np.argmin(d_neff))
    pruning_lag = float(peak_pruning_gen - window_midpoint)

    total_entropy_loss = float(entropy[0] - entropy[-1])
    if abs(total_entropy_loss) < 1e-12:
        pre_entropy_loss = 0.0
        window_entropy_loss = 0.0
        post_entropy_loss = 0.0
    else:
        pre_entropy_loss = float(entropy[0] - entropy[WINDOW_START])
        window_entropy_loss = float(entropy[WINDOW_START] - entropy[WINDOW_END - 1])
        post_entropy_loss = float(entropy[WINDOW_END - 1] - entropy[-1])

    summary = {
        "top1": shares["top1"],
        "top3": shares["top3"],
        "top5": shares["top5"],
        "peak_pruning_gen": peak_pruning_gen,
        "pruning_lag": pruning_lag,
        "max_curvature_gen": int(np.argmax(np.abs(dd_neff))),
        "late_neff_slope": late_run_slope(neff),
        "late_active_slope": late_run_slope(active),
        "entropy_loss_total": total_entropy_loss,
        "entropy_loss_pre": pre_entropy_loss,
        "entropy_loss_window": window_entropy_loss,
        "entropy_loss_post": post_entropy_loss,
    }

    return {
        "entropy": entropy,
        "neff": neff,
        "active": active,
        "alpha": alpha,
        "skew": skew,
        "concentration": concentration,
        "d_neff": d_neff,
        "d_active": d_active,
        "summary": summary,
    }


# -----------------------------
# Experiments
# -----------------------------

def aggregate_scalar(values: list[float]) -> dict:
    arr = np.array(values, dtype=float)
    return {
        "mean": float(arr.mean()),
        "std": float(arr.std()),
        "min": float(arr.min()),
        "max": float(arr.max()),
    }


def run_experiments() -> dict:
    np.random.seed(RANDOM_SEED)

    runs = [run_once() for _ in range(TRIALS)]

    def stack(key: str) -> np.ndarray:
        return np.stack([r[key] for r in runs], axis=0)

    entropy_runs = stack("entropy")
    neff_runs = stack("neff")
    active_runs = stack("active")
    alpha_runs = stack("alpha")
    skew_runs = stack("skew")
    concentration_runs = stack("concentration")
    d_neff_runs = stack("d_neff")
    d_active_runs = stack("d_active")

    summaries = [r["summary"] for r in runs]

    summary_stats = {
        key: aggregate_scalar([s[key] for s in summaries])
        for key in summaries[0].keys()
    }

    return {
        "runs": runs,
        "entropy_mean": entropy_runs.mean(axis=0),
        "entropy_std": entropy_runs.std(axis=0),
        "neff_mean": neff_runs.mean(axis=0),
        "neff_std": neff_runs.std(axis=0),
        "active_mean": active_runs.mean(axis=0),
        "active_std": active_runs.std(axis=0),
        "alpha_mean": alpha_runs.mean(axis=0),
        "skew_mean": skew_runs.mean(axis=0),
        "concentration_mean": concentration_runs.mean(axis=0),
        "d_neff_mean": d_neff_runs.mean(axis=0),
        "d_active_mean": d_active_runs.mean(axis=0),
        "summary_stats": summary_stats,
    }


def run_sample_trajectories(n_runs: int) -> list[dict]:
    return [run_once() for _ in range(n_runs)]


# -----------------------------
# Output / Plotting
# -----------------------------

def save_summary_json(results: dict) -> None:
    payload = {
        "params": {
            "NUM_LINEAGES": NUM_LINEAGES,
            "POP_SIZE": POP_SIZE,
            "GENERATIONS": GENERATIONS,
            "TRIALS": TRIALS,
            "NOISE_SIGMA": NOISE_SIGMA,
            "EPP_RATE": EPP_RATE,
            "EPP_STATUS_WEIGHT": EPP_STATUS_WEIGHT,
            "SIGNAL_CORRELATION": SIGNAL_CORRELATION,
            "WINDOW_START": WINDOW_START,
            "WINDOW_END": WINDOW_END,
            "BASE_SKEW": BASE_SKEW,
            "WINDOW_SKEW": WINDOW_SKEW,
            "POST_SKEW": POST_SKEW,
            "MIN_LINEAGE_SIZE": MIN_LINEAGE_SIZE,
            "MIN_PENALTY": MIN_PENALTY,
            "BASE_FRAGILITY_ALPHA": BASE_FRAGILITY_ALPHA,
            "FRAGILITY_GAIN": FRAGILITY_GAIN,
        },
        "summary_stats": results["summary_stats"],
    }
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(json.dumps(payload, indent=2))
    print(f"Saved summary to {SUMMARY_PATH}")


def plot_results(results: dict, samples: list[dict]) -> None:
    FIGURE_PATH.parent.mkdir(parents=True, exist_ok=True)

    gens = np.arange(GENERATIONS)

    fig, axes = plt.subplots(6, 1, figsize=(12, 18))

    title_suffix = (
        f"window=({WINDOW_START},{WINDOW_END}), "
        f"epp={EPP_RATE}, mix={EPP_STATUS_WEIGHT}, corr={SIGNAL_CORRELATION}"
    )

    # 1. Entropy
    ax = axes[0]
    ax.plot(gens, results["entropy_mean"], label="Entropy")
    ax.fill_between(
        gens,
        results["entropy_mean"] - results["entropy_std"],
        results["entropy_mean"] + results["entropy_std"],
        alpha=0.2,
    )
    ax.axvspan(WINDOW_START, WINDOW_END, alpha=0.12)
    ax.set_title(f"Entropy over time ({title_suffix})")
    ax.set_ylabel("H")

    # 2. Effective lineages
    ax = axes[1]
    ax.plot(gens, results["neff_mean"], label="N_eff")
    ax.fill_between(
        gens,
        results["neff_mean"] - results["neff_std"],
        results["neff_mean"] + results["neff_std"],
        alpha=0.2,
    )
    ax.axvspan(WINDOW_START, WINDOW_END, alpha=0.12)
    ax.set_title("Effective lineages")
    ax.set_ylabel("N_eff")

    # 3. Active lineages
    ax = axes[2]
    ax.plot(gens, results["active_mean"], label="Active")
    ax.fill_between(
        gens,
        results["active_mean"] - results["active_std"],
        results["active_mean"] + results["active_std"],
        alpha=0.2,
    )
    ax.axvspan(WINDOW_START, WINDOW_END, alpha=0.12)
    ax.set_title("Active lineages")
    ax.set_ylabel("Count")

    # 4. Derivatives
    ax = axes[3]
    ax.plot(gens, results["d_neff_mean"], label="dN_eff/dt")
    ax.plot(gens, results["d_active_mean"], label="dActive/dt")
    ax.axvspan(WINDOW_START, WINDOW_END, alpha=0.12)
    ax.set_title("Pruning derivatives")
    ax.set_ylabel("Δ per gen")
    ax.legend()

    # 5. State variables
    ax = axes[4]
    ax.plot(gens, results["alpha_mean"], label="Fragility alpha")
    ax.plot(gens, results["concentration_mean"], label="Concentration")
    ax.plot(gens, results["skew_mean"], label="Skew")
    ax.axvspan(WINDOW_START, WINDOW_END, alpha=0.12)
    ax.set_title("System state")
    ax.set_ylabel("Value")
    ax.legend()

    # 6. Sample trajectories
    ax = axes[5]
    for i, s in enumerate(samples):
        ax.plot(gens, s["active"], label=f"run {i+1}")
    ax.axvspan(WINDOW_START, WINDOW_END, alpha=0.12)
    ax.set_title("Sample active-lineage trajectories")
    ax.set_xlabel("Generation")
    ax.set_ylabel("Active")
    ax.legend(ncol=4, fontsize=8)

    plt.tight_layout()
    plt.savefig(FIGURE_PATH, dpi=150)
    print(f"Saved plot to {FIGURE_PATH}")
    plt.show()

    ss = results["summary_stats"]
    print("\nSummary statistics across runs:")
    for key in [
        "top1",
        "top3",
        "top5",
        "peak_pruning_gen",
        "pruning_lag",
        "max_curvature_gen",
        "late_neff_slope",
        "late_active_slope",
        "entropy_loss_pre",
        "entropy_loss_window",
        "entropy_loss_post",
    ]:
        val = ss[key]
        print(
            f"{key:20s} mean={val['mean']:.3f} std={val['std']:.3f} "
            f"min={val['min']:.3f} max={val['max']:.3f}"
        )


# -----------------------------
# Main
# -----------------------------

if __name__ == "__main__":
    results = run_experiments()
    samples = run_sample_trajectories(SAMPLE_RUNS)
    save_summary_json(results)
    plot_results(results, samples)

