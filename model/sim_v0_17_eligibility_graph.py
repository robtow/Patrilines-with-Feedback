import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# Parameters
# -----------------------------

NUM_BASINS = 3
POP_SIZE_PER_BASIN = [800, 1000, 1200]  # local slack gradient: tighter, middle, broader
NUM_LINEAGES = 50
GENERATIONS = 100
TRIALS = 40

NOISE_SIGMA = 0.2

# Leakage / informal channel
EPP_RATE = 0.03
EPP_STATUS_WEIGHT = 0.5
SIGNAL_CORRELATION = 0.5

# Bounded compression windows by basin
WINDOW_STARTS = [24, 34, 44]
WINDOW_ENDS = [54, 64, 74]

BASE_SKEW = 1.00
WINDOW_SKEWS = [1.08, 1.07, 1.05]
POST_SKEW = 1.00

# Fragility parameters
MIN_LINEAGE_SIZE = 5
MIN_PENALTY = 0.10
BASE_FRAGILITY_ALPHA = 0.10
FRAGILITY_GAIN = 0.90

# Basin-specific baseline fragility buffering
BASIN_BASE_FRAGILITY_MULTIPLIERS = [1.00, 0.90, 0.75]

# NOTE: graph pass weakens scalar special-window harshness.
# No extra window fragility multiplier in this first graph version.

# Damage / hysteresis parameters
DAMAGE_CONC_THRESHOLD = 0.45
DAMAGE_ACCUM_GAIN = 0.035
DAMAGE_DECAY = 0.05
DAMAGE_ALPHA_GAIN = 0.30

# Initial heterogeneity
INITIAL_HETEROGENEITY_SIGMA = 0.20

# Basin coupling
BASE_BASIN_COUPLING = np.array(
    [
        [0.96, 0.02, 0.02],
        [0.02, 0.96, 0.02],
        [0.02, 0.02, 0.96],
    ],
    dtype=float,
)

# Window-driven local closure
WINDOW_CLOSED_DIAG = 0.99

# Local timing metric
ROLLING_PRUNING_WINDOW = 5

# Eligibility graph
CLASS_NAMES = ["core", "intermediate", "periphery"]
NUM_CLASSES = 3
CLASS_PROPORTIONS = [0.20, 0.40, 0.40]

E_OPEN = np.array(
    [
        [1.00, 0.75, 0.40],
        [0.75, 0.90, 0.60],
        [0.40, 0.60, 0.80],
    ],
    dtype=float,
)

E_TIGHT = np.array(
    [
        [1.00, 0.45, 0.10],
        [0.45, 0.75, 0.20],
        [0.10, 0.20, 0.55],
    ],
    dtype=float,
)

E_INFORMAL_TIGHT = 0.5 * E_OPEN + 0.5 * E_TIGHT

# Plotting / runs
SAMPLE_RUNS = 6
RANDOM_SEED = 42

FIGURE_PATH = Path("figures/sim_v0_17.png")
SUMMARY_PATH = Path("notes/v0_17_summary.json")


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


def gini(values: np.ndarray) -> float:
    x = np.array(values, dtype=float)
    if np.allclose(x.sum(), 0.0):
        return 0.0
    x = np.sort(x)
    n = len(x)
    index = np.arange(1, n + 1)
    return float((np.sum((2 * index - n - 1) * x)) / (n * np.sum(x)))


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


def safe_correlation(a: np.ndarray, b: np.ndarray) -> float:
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    if np.std(a) < 1e-12 or np.std(b) < 1e-12:
        return 0.0
    return float(np.corrcoef(a, b)[0, 1])


def fragility_multiplier(counts: np.ndarray, alpha: float) -> np.ndarray:
    counts = np.array(counts, dtype=float)
    ratio = counts / MIN_LINEAGE_SIZE
    ratio = np.clip(ratio, 0.0, 1.0)
    shaped = ratio ** alpha
    shaped = np.where(counts >= MIN_LINEAGE_SIZE, 1.0, shaped)
    shaped = np.maximum(shaped, MIN_PENALTY)
    return shaped


def compute_attractiveness(counts: np.ndarray) -> np.ndarray:
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


def initial_counts_from_distribution(pop_size: int) -> np.ndarray:
    weights = np.random.lognormal(
        mean=0.0,
        sigma=INITIAL_HETEROGENEITY_SIGMA,
        size=NUM_LINEAGES,
    )
    weights = normalize(weights)
    counts = np.random.multinomial(pop_size, weights)
    return counts


def tercile_labels(initial_counts: np.ndarray) -> np.ndarray:
    order = np.argsort(initial_counts)
    labels = np.zeros(len(initial_counts), dtype=int)
    n = len(initial_counts)
    t1 = n // 3
    t2 = 2 * n // 3
    labels[order[:t1]] = 0
    labels[order[t1:t2]] = 1
    labels[order[t2:]] = 2
    return labels


def tercile_stats(initial_labels: np.ndarray, final_counts: np.ndarray) -> dict:
    out = {}
    total = final_counts.sum()
    for tercile, name in [(0, "lower"), (1, "middle"), (2, "upper")]:
        mask = initial_labels == tercile
        group_counts = final_counts[mask]
        survivors = np.count_nonzero(group_counts)
        group_total = group_counts.sum()
        out[f"{name}_survival_rate"] = float(survivors / mask.sum())
        out[f"{name}_final_share"] = float(group_total / total) if total > 0 else 0.0
    return out


def in_window(gen: int, basin_idx: int) -> bool:
    return WINDOW_STARTS[basin_idx] <= gen < WINDOW_ENDS[basin_idx]


def current_skew(gen: int, basin_idx: int) -> float:
    if gen < WINDOW_STARTS[basin_idx]:
        return BASE_SKEW
    if gen < WINDOW_ENDS[basin_idx]:
        return WINDOW_SKEWS[basin_idx]
    return POST_SKEW


def current_fragility_gain(_gen: int, basin_idx: int) -> float:
    return FRAGILITY_GAIN * BASIN_BASE_FRAGILITY_MULTIPLIERS[basin_idx]


def rolling_main_pruning_time(series: np.ndarray, window: int = ROLLING_PRUNING_WINDOW) -> int:
    if len(series) <= window:
        return int(np.argmin(first_difference(series)))

    diffs = np.diff(series)
    rolling = np.convolve(diffs, np.ones(window), mode="valid")
    idx = int(np.argmin(rolling))
    midpoint = idx + window // 2 + 1
    return int(midpoint)


def coupling_for_generation(gen: int) -> np.ndarray:
    mat = BASE_BASIN_COUPLING.copy()
    for b in range(NUM_BASINS):
        if in_window(gen, b):
            off_diag_sum = 1.0 - WINDOW_CLOSED_DIAG
            share = off_diag_sum / (NUM_BASINS - 1)
            mat[b, :] = share
            mat[b, b] = WINDOW_CLOSED_DIAG
    return mat


def build_lineage_classes() -> np.ndarray:
    """
    Fixed class membership shared across basins for the first pass.
    """
    n_core = int(round(NUM_LINEAGES * CLASS_PROPORTIONS[0]))
    n_intermediate = int(round(NUM_LINEAGES * CLASS_PROPORTIONS[1]))
    n_periphery = NUM_LINEAGES - n_core - n_intermediate

    classes = np.zeros(NUM_LINEAGES, dtype=int)
    classes[:n_core] = 0
    classes[n_core:n_core + n_intermediate] = 1
    classes[n_core + n_intermediate:] = 2

    # shuffle once for reproducible but non-ordered assignment
    perm = np.random.permutation(NUM_LINEAGES)
    out = np.empty_like(classes)
    out[perm] = classes
    return out


def class_weights(counts: np.ndarray, lineage_classes: np.ndarray) -> np.ndarray:
    totals = np.zeros(NUM_CLASSES, dtype=float)
    for c in range(NUM_CLASSES):
        totals[c] = counts[lineage_classes == c].sum()
    return normalize(totals)


def current_formal_matrix(gen: int, basin_idx: int) -> np.ndarray:
    return E_TIGHT if in_window(gen, basin_idx) else E_OPEN


def current_informal_matrix(gen: int, basin_idx: int) -> np.ndarray:
    return E_INFORMAL_TIGHT if in_window(gen, basin_idx) else E_OPEN


def class_connectivity_scores(matrix: np.ndarray, class_weights_vec: np.ndarray, lineage_classes: np.ndarray) -> np.ndarray:
    class_scores = matrix @ class_weights_vec
    return class_scores[lineage_classes]


# -----------------------------
# Single run
# -----------------------------

def run_once() -> dict:
    lineage_classes = build_lineage_classes()

    basin_counts = np.stack(
        [initial_counts_from_distribution(pop) for pop in POP_SIZE_PER_BASIN],
        axis=0,
    )

    initial_global_counts = basin_counts.sum(axis=0)
    initial_labels = tercile_labels(initial_global_counts)

    entropy_hist = []
    neff_hist = []
    active_hist = []
    alpha_hist = []
    damage_hist = []
    global_concentration_hist = []
    mean_diag_coupling_hist = []

    basin_entropy_hist = [[] for _ in range(NUM_BASINS)]
    basin_neff_hist = [[] for _ in range(NUM_BASINS)]
    basin_active_hist = [[] for _ in range(NUM_BASINS)]
    basin_damage_hist = [[] for _ in range(NUM_BASINS)]
    basin_skew_hist = [[] for _ in range(NUM_BASINS)]
    basin_fragility_gain_hist = [[] for _ in range(NUM_BASINS)]

    basin_damage = np.zeros(NUM_BASINS, dtype=float)

    for gen in range(GENERATIONS):
        next_counts = np.zeros_like(basin_counts)

        for b in range(NUM_BASINS):
            counts = basin_counts[b].copy()
            skew = current_skew(gen, b)
            local_fragility_gain = current_fragility_gain(gen, b)
            formal_matrix = current_formal_matrix(gen, b)
            informal_matrix = current_informal_matrix(gen, b)

            current_neff = effective_lineages(counts)
            concentration = 1.0 - (current_neff / NUM_LINEAGES)
            concentration = float(np.clip(concentration, 0.0, 1.0))

            excess_concentration = max(0.0, concentration - DAMAGE_CONC_THRESHOLD)
            basin_damage[b] = basin_damage[b] + DAMAGE_ACCUM_GAIN * excess_concentration - DAMAGE_DECAY * basin_damage[b]
            basin_damage[b] = float(np.clip(basin_damage[b], 0.0, 1.0))

            effective_alpha = (
                BASE_FRAGILITY_ALPHA
                + local_fragility_gain * concentration
                + DAMAGE_ALPHA_GAIN * basin_damage[b]
            )

            # Class connectivity scores
            cw = class_weights(counts, lineage_classes)
            formal_connectivity = class_connectivity_scores(formal_matrix, cw, lineage_classes)
            informal_connectivity = class_connectivity_scores(informal_matrix, cw, lineage_classes)

            # Formal channel
            formal_probs = normalize(counts)
            formal_probs = formal_probs ** skew
            formal_probs *= fragility_multiplier(counts, effective_alpha)
            formal_probs *= formal_connectivity

            if NOISE_SIGMA > 0:
                noise = np.random.lognormal(mean=0.0, sigma=NOISE_SIGMA, size=len(formal_probs))
                formal_probs *= noise

            formal_probs = normalize(formal_probs)

            # Informal channel on softened graph
            attractiveness = compute_attractiveness(counts)
            epp_probs = (
                EPP_STATUS_WEIGHT * attractiveness
                + (1.0 - EPP_STATUS_WEIGHT) * normalize(informal_connectivity)
            )
            epp_probs = normalize(epp_probs)

            total_probs = (1.0 - EPP_RATE) * formal_probs + EPP_RATE * epp_probs
            total_probs = normalize(total_probs)

            next_counts[b] = np.random.multinomial(POP_SIZE_PER_BASIN[b], total_probs)

            basin_entropy_hist[b].append(shannon_entropy(next_counts[b]))
            basin_neff_hist[b].append(effective_lineages(next_counts[b]))
            basin_active_hist[b].append(int(np.count_nonzero(next_counts[b])))
            basin_damage_hist[b].append(float(basin_damage[b]))
            basin_skew_hist[b].append(float(skew))
            basin_fragility_gain_hist[b].append(float(local_fragility_gain))

        coupling = coupling_for_generation(gen)
        coupled_counts = np.zeros_like(next_counts, dtype=float)
        for lineage in range(NUM_LINEAGES):
            source_vector = next_counts[:, lineage].astype(float)
            transferred = coupling @ source_vector
            coupled_counts[:, lineage] = transferred

        basin_counts = np.zeros_like(next_counts)
        for b in range(NUM_BASINS):
            probs = normalize(coupled_counts[b])
            basin_counts[b] = np.random.multinomial(POP_SIZE_PER_BASIN[b], probs)

        global_counts = basin_counts.sum(axis=0)

        entropy_hist.append(shannon_entropy(global_counts))
        neff_hist.append(effective_lineages(global_counts))
        active_hist.append(int(np.count_nonzero(global_counts)))
        alpha_hist.append(float(np.mean([
            BASE_FRAGILITY_ALPHA
            + current_fragility_gain(gen, b) * np.clip(1.0 - (effective_lineages(basin_counts[b]) / NUM_LINEAGES), 0.0, 1.0)
            + DAMAGE_ALPHA_GAIN * basin_damage[b]
            for b in range(NUM_BASINS)
        ])))
        damage_hist.append(float(np.mean(basin_damage)))
        global_concentration_hist.append(
            float(np.clip(1.0 - (effective_lineages(global_counts) / NUM_LINEAGES), 0.0, 1.0))
        )
        mean_diag_coupling_hist.append(float(np.mean(np.diag(coupling))))

    final_global_counts = basin_counts.sum(axis=0)

    entropy = np.array(entropy_hist)
    neff = np.array(neff_hist)
    active = np.array(active_hist)
    alpha = np.array(alpha_hist)
    damage = np.array(damage_hist)
    global_concentration = np.array(global_concentration_hist)
    mean_diag_coupling = np.array(mean_diag_coupling_hist)

    basin_entropy = [np.array(x) for x in basin_entropy_hist]
    basin_neff = [np.array(x) for x in basin_neff_hist]
    basin_active = [np.array(x) for x in basin_active_hist]
    basin_damage_series = [np.array(x) for x in basin_damage_hist]
    basin_skew = [np.array(x) for x in basin_skew_hist]
    basin_fragility_gain = [np.array(x) for x in basin_fragility_gain_hist]

    d_neff = first_difference(neff)
    d_active = first_difference(active)
    dd_neff = second_difference(neff)

    shares = top_k_shares(final_global_counts)
    terciles = tercile_stats(initial_labels, final_global_counts)

    global_window_midpoint = float(np.mean([(s + e) / 2.0 for s, e in zip(WINDOW_STARTS, WINDOW_ENDS)]))
    peak_pruning_gen = int(np.argmin(d_neff))
    pruning_lag = float(peak_pruning_gen - global_window_midpoint)

    total_entropy_loss = float(entropy[0] - entropy[-1])

    pre_cut = min(WINDOW_STARTS)
    post_cut = max(WINDOW_ENDS) - 1

    pre_entropy_loss = float(entropy[0] - entropy[pre_cut])
    window_entropy_loss = float(entropy[pre_cut] - entropy[post_cut])
    post_entropy_loss = float(entropy[post_cut] - entropy[-1])

    initial_shares = top_k_shares(initial_global_counts)

    basin_single_step_pruning = []
    basin_main_pruning = []
    basin_entropy_loss_window = []
    for b in range(NUM_BASINS):
        b_d_neff = first_difference(basin_neff[b])
        basin_single_step_pruning.append(int(np.argmin(b_d_neff)))
        basin_main_pruning.append(int(rolling_main_pruning_time(basin_neff[b], ROLLING_PRUNING_WINDOW)))

        b_pre = WINDOW_STARTS[b]
        b_post = WINDOW_ENDS[b] - 1
        basin_entropy_loss_window.append(float(basin_entropy[b][b_pre] - basin_entropy[b][b_post]))

    summary = {
        "top1": shares["top1"],
        "top3": shares["top3"],
        "top5": shares["top5"],
        "initial_top1": initial_shares["top1"],
        "initial_top3": initial_shares["top3"],
        "initial_gini": gini(initial_global_counts),
        "final_gini": gini(final_global_counts),
        "initial_final_corr": safe_correlation(initial_global_counts, final_global_counts),
        "peak_pruning_gen": peak_pruning_gen,
        "pruning_lag": pruning_lag,
        "max_curvature_gen": int(np.argmax(np.abs(dd_neff))),
        "late_neff_slope": late_run_slope(neff),
        "late_active_slope": late_run_slope(active),
        "entropy_loss_total": total_entropy_loss,
        "entropy_loss_pre": pre_entropy_loss,
        "entropy_loss_window": window_entropy_loss,
        "entropy_loss_post": post_entropy_loss,
        "initial_mean_count": float(initial_global_counts.mean()),
        "initial_std_count": float(initial_global_counts.std()),
        "final_damage": float(damage[-1]),
        "max_damage": float(damage.max()),
        "mean_diag_coupling_final": float(mean_diag_coupling[-1]),
        "mean_diag_coupling_max": float(mean_diag_coupling.max()),
        "basin0_single_step_pruning": float(basin_single_step_pruning[0]),
        "basin1_single_step_pruning": float(basin_single_step_pruning[1]),
        "basin2_single_step_pruning": float(basin_single_step_pruning[2]),
        "basin0_main_pruning": float(basin_main_pruning[0]),
        "basin1_main_pruning": float(basin_main_pruning[1]),
        "basin2_main_pruning": float(basin_main_pruning[2]),
        "basin0_window_loss": float(basin_entropy_loss_window[0]),
        "basin1_window_loss": float(basin_entropy_loss_window[1]),
        "basin2_window_loss": float(basin_entropy_loss_window[2]),
        **terciles,
    }

    return {
        "entropy": entropy,
        "neff": neff,
        "active": active,
        "alpha": alpha,
        "damage": damage,
        "global_concentration": global_concentration,
        "mean_diag_coupling": mean_diag_coupling,
        "d_neff": d_neff,
        "d_active": d_active,
        "basin_entropy": basin_entropy,
        "basin_neff": basin_neff,
        "basin_active": basin_active,
        "basin_damage": basin_damage_series,
        "basin_skew": basin_skew,
        "basin_fragility_gain": basin_fragility_gain,
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

    summaries = [r["summary"] for r in runs]
    summary_stats = {
        key: aggregate_scalar([s[key] for s in summaries])
        for key in summaries[0].keys()
    }

    basin_entropy_mean = []
    basin_neff_mean = []
    basin_active_mean = []
    basin_damage_mean = []
    basin_skew_mean = []
    basin_fragility_gain_mean = []
    for b in range(NUM_BASINS):
        basin_entropy_mean.append(np.stack([r["basin_entropy"][b] for r in runs]).mean(axis=0))
        basin_neff_mean.append(np.stack([r["basin_neff"][b] for r in runs]).mean(axis=0))
        basin_active_mean.append(np.stack([r["basin_active"][b] for r in runs]).mean(axis=0))
        basin_damage_mean.append(np.stack([r["basin_damage"][b] for r in runs]).mean(axis=0))
        basin_skew_mean.append(np.stack([r["basin_skew"][b] for r in runs]).mean(axis=0))
        basin_fragility_gain_mean.append(np.stack([r["basin_fragility_gain"][b] for r in runs]).mean(axis=0))

    return {
        "runs": runs,
        "entropy_mean": stack("entropy").mean(axis=0),
        "entropy_std": stack("entropy").std(axis=0),
        "neff_mean": stack("neff").mean(axis=0),
        "neff_std": stack("neff").std(axis=0),
        "active_mean": stack("active").mean(axis=0),
        "active_std": stack("active").std(axis=0),
        "alpha_mean": stack("alpha").mean(axis=0),
        "damage_mean": stack("damage").mean(axis=0),
        "global_concentration_mean": stack("global_concentration").mean(axis=0),
        "mean_diag_coupling_mean": stack("mean_diag_coupling").mean(axis=0),
        "d_neff_mean": stack("d_neff").mean(axis=0),
        "d_active_mean": stack("d_active").mean(axis=0),
        "basin_entropy_mean": basin_entropy_mean,
        "basin_neff_mean": basin_neff_mean,
        "basin_active_mean": basin_active_mean,
        "basin_damage_mean": basin_damage_mean,
        "basin_skew_mean": basin_skew_mean,
        "basin_fragility_gain_mean": basin_fragility_gain_mean,
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
            "NUM_BASINS": NUM_BASINS,
            "POP_SIZE_PER_BASIN": POP_SIZE_PER_BASIN,
            "NUM_LINEAGES": NUM_LINEAGES,
            "GENERATIONS": GENERATIONS,
            "TRIALS": TRIALS,
            "NOISE_SIGMA": NOISE_SIGMA,
            "EPP_RATE": EPP_RATE,
            "EPP_STATUS_WEIGHT": EPP_STATUS_WEIGHT,
            "SIGNAL_CORRELATION": SIGNAL_CORRELATION,
            "WINDOW_STARTS": WINDOW_STARTS,
            "WINDOW_ENDS": WINDOW_ENDS,
            "BASE_SKEW": BASE_SKEW,
            "WINDOW_SKEWS": WINDOW_SKEWS,
            "POST_SKEW": POST_SKEW,
            "MIN_LINEAGE_SIZE": MIN_LINEAGE_SIZE,
            "MIN_PENALTY": MIN_PENALTY,
            "BASE_FRAGILITY_ALPHA": BASE_FRAGILITY_ALPHA,
            "FRAGILITY_GAIN": FRAGILITY_GAIN,
            "BASIN_BASE_FRAGILITY_MULTIPLIERS": BASIN_BASE_FRAGILITY_MULTIPLIERS,
            "DAMAGE_CONC_THRESHOLD": DAMAGE_CONC_THRESHOLD,
            "DAMAGE_ACCUM_GAIN": DAMAGE_ACCUM_GAIN,
            "DAMAGE_DECAY": DAMAGE_DECAY,
            "DAMAGE_ALPHA_GAIN": DAMAGE_ALPHA_GAIN,
            "INITIAL_HETEROGENEITY_SIGMA": INITIAL_HETEROGENEITY_SIGMA,
            "BASE_BASIN_COUPLING": BASE_BASIN_COUPLING.tolist(),
            "WINDOW_CLOSED_DIAG": WINDOW_CLOSED_DIAG,
            "ROLLING_PRUNING_WINDOW": ROLLING_PRUNING_WINDOW,
            "CLASS_PROPORTIONS": CLASS_PROPORTIONS,
            "E_OPEN": E_OPEN.tolist(),
            "E_TIGHT": E_TIGHT.tolist(),
            "E_INFORMAL_TIGHT": E_INFORMAL_TIGHT.tolist(),
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

    ax = axes[0]
    ax.plot(gens, results["entropy_mean"], label="Global entropy")
    ax.fill_between(
        gens,
        results["entropy_mean"] - results["entropy_std"],
        results["entropy_mean"] + results["entropy_std"],
        alpha=0.2,
    )
    for s, e in zip(WINDOW_STARTS, WINDOW_ENDS):
        ax.axvspan(s, e, alpha=0.06)
    ax.set_title("v0.17 Eligibility-Graph Daisyworld: global entropy")
    ax.set_ylabel("H")

    ax = axes[1]
    for b in range(NUM_BASINS):
        ax.plot(gens, results["basin_neff_mean"][b], label=f"basin {b}")
        ax.axvspan(WINDOW_STARTS[b], WINDOW_ENDS[b], alpha=0.06)
    ax.set_title("Basin effective lineages")
    ax.set_ylabel("N_eff")
    ax.legend()

    ax = axes[2]
    ax.plot(gens, results["active_mean"], label="Global active")
    ax.fill_between(
        gens,
        results["active_mean"] - results["active_std"],
        results["active_mean"] + results["active_std"],
        alpha=0.2,
    )
    for s, e in zip(WINDOW_STARTS, WINDOW_ENDS):
        ax.axvspan(s, e, alpha=0.06)
    ax.set_title("Global active lineages")
    ax.set_ylabel("Count")

    ax = axes[3]
    ax.plot(gens, results["d_neff_mean"], label="dN_eff/dt")
    ax.plot(gens, results["d_active_mean"], label="dActive/dt")
    for s, e in zip(WINDOW_STARTS, WINDOW_ENDS):
        ax.axvspan(s, e, alpha=0.06)
    ax.set_title("Global pruning derivatives")
    ax.set_ylabel("Δ per gen")
    ax.legend()

    ax = axes[4]
    ax.plot(gens, results["alpha_mean"], label="Mean fragility alpha")
    ax.plot(gens, results["damage_mean"], label="Mean damage")
    ax.plot(gens, results["global_concentration_mean"], label="Global concentration")
    ax.plot(gens, results["mean_diag_coupling_mean"], label="Mean diag coupling")
    for b in range(NUM_BASINS):
        ax.plot(gens, results["basin_skew_mean"][b], linestyle="--", label=f"skew b{b}")
    for s, e in zip(WINDOW_STARTS, WINDOW_ENDS):
        ax.axvspan(s, e, alpha=0.06)
    ax.set_title("System state")
    ax.set_ylabel("Value")
    ax.legend(ncol=3, fontsize=8)

    ax = axes[5]
    for i, s in enumerate(samples):
        ax.plot(gens, s["active"], label=f"run {i+1}")
    for s, e in zip(WINDOW_STARTS, WINDOW_ENDS):
        ax.axvspan(s, e, alpha=0.06)
    ax.set_title("Sample global active-lineage trajectories")
    ax.set_xlabel("Generation")
    ax.set_ylabel("Active")
    ax.legend(ncol=3, fontsize=8)

    plt.tight_layout()
    plt.savefig(FIGURE_PATH, dpi=150)
    print(f"Saved plot to {FIGURE_PATH}")
    plt.show()

    ss = results["summary_stats"]
    print("\nSummary statistics across runs:")
    for key in [
        "initial_mean_count",
        "initial_std_count",
        "initial_top1",
        "top1",
        "top3",
        "top5",
        "initial_gini",
        "final_gini",
        "initial_final_corr",
        "lower_survival_rate",
        "middle_survival_rate",
        "upper_survival_rate",
        "lower_final_share",
        "middle_final_share",
        "upper_final_share",
        "peak_pruning_gen",
        "pruning_lag",
        "max_curvature_gen",
        "late_neff_slope",
        "late_active_slope",
        "entropy_loss_pre",
        "entropy_loss_window",
        "entropy_loss_post",
        "final_damage",
        "max_damage",
        "mean_diag_coupling_final",
        "mean_diag_coupling_max",
        "basin0_single_step_pruning",
        "basin1_single_step_pruning",
        "basin2_single_step_pruning",
        "basin0_main_pruning",
        "basin1_main_pruning",
        "basin2_main_pruning",
        "basin0_window_loss",
        "basin1_window_loss",
        "basin2_window_loss",
    ]:
        val = ss[key]
        print(
            f"{key:24s} mean={val['mean']:.3f} std={val['std']:.3f} "
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
