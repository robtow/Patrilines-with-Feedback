import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Parameters
# -----------------------------

NUM_LINEAGES = 100
POP_SIZE = 1000
GENERATIONS = 100
TRIALS = 20

SKEW_VALUES = [1.0, 1.02, 1.05, 1.1, 1.2]

# Multiplicative lineage-specific noise.
# 0.0 = deterministic mean-field model
# try 0.1, 0.2, 0.3
NOISE_SIGMA = 0.2

# For the sample-run panel
SAMPLE_SKEW = 1.05
SAMPLE_RUNS = 6

RANDOM_SEED = 42


# -----------------------------
# Utilities
# -----------------------------

def shannon_entropy(counts):
    counts = np.array(counts, dtype=float)
    total = counts.sum()
    if total == 0:
        return 0.0
    p = counts / total
    p = p[p > 0]
    return -(p * np.log(p)).sum()


def effective_lineages(counts):
    return np.exp(shannon_entropy(counts))


# -----------------------------
# Single run
# -----------------------------

def run_once(skew, noise_sigma):
    counts = np.ones(NUM_LINEAGES, dtype=float) * (POP_SIZE // NUM_LINEAGES)

    entropy_hist = []
    neff_hist = []
    active_hist = []

    for _ in range(GENERATIONS):
        probs = counts / counts.sum()

        # Mean-field concentration
        probs = probs ** skew

        # Lineage-specific multiplicative noise
        if noise_sigma > 0:
            noise = np.random.lognormal(mean=0.0, sigma=noise_sigma, size=len(probs))
            probs = probs * noise

        probs = probs / probs.sum()

        counts = np.random.multinomial(POP_SIZE, probs)

        entropy_hist.append(shannon_entropy(counts))
        neff_hist.append(effective_lineages(counts))
        active_hist.append(np.count_nonzero(counts))

    return (
        np.array(entropy_hist),
        np.array(neff_hist),
        np.array(active_hist),
    )


# -----------------------------
# Run experiments
# -----------------------------

def run_experiments():
    np.random.seed(RANDOM_SEED)

    results = {}

    for skew in SKEW_VALUES:
        entropy_accum = np.zeros(GENERATIONS)
        neff_accum = np.zeros(GENERATIONS)
        active_accum = np.zeros(GENERATIONS)

        for _ in range(TRIALS):
            e, n, a = run_once(skew, NOISE_SIGMA)
            entropy_accum += e
            neff_accum += n
            active_accum += a

        results[skew] = {
            "entropy": entropy_accum / TRIALS,
            "neff": neff_accum / TRIALS,
            "active": active_accum / TRIALS,
        }

    return results


def run_sample_trajectories(skew, noise_sigma, runs):
    samples = []
    for _ in range(runs):
        e, n, a = run_once(skew, noise_sigma)
        samples.append({
            "entropy": e,
            "neff": n,
            "active": a,
        })
    return samples


# -----------------------------
# Plotting
# -----------------------------

def plot_results(results, samples):
    fig, axes = plt.subplots(4, 1, figsize=(12, 12))

    # Entropy averages
    ax = axes[0]
    for skew, data in results.items():
        ax.plot(data["entropy"], label=f"skew={skew}")
    ax.set_title(f"Shannon Entropy (average over {TRIALS} trials, noise_sigma={NOISE_SIGMA})")
    ax.set_ylabel("H")
    ax.legend()

    # Effective lineages averages
    ax = axes[1]
    for skew, data in results.items():
        ax.plot(data["neff"], label=f"skew={skew}")
    ax.set_title("Effective Number of Lineages (e^H)")
    ax.set_ylabel("N_eff")

    # Active lineages averages
    ax = axes[2]
    for skew, data in results.items():
        ax.plot(data["active"], label=f"skew={skew}")
    ax.set_title("Active Lineages")
    ax.set_ylabel("Count")

    # Sample trajectories for one skew
    ax = axes[3]
    for i, sample in enumerate(samples):
        ax.plot(sample["active"], label=f"run {i+1}")
    ax.set_title(f"Sample Active-Lineage Trajectories at skew={SAMPLE_SKEW}")
    ax.set_xlabel("Generation")
    ax.set_ylabel("Active lineages")
    ax.legend(ncol=3, fontsize=8)

    plt.tight_layout()
    plt.savefig("figures/sim_v0_3.png", dpi=150)
    print("Saved plot to figures/sim_v0_3.png")
    plt.show()


# -----------------------------
# Main
# -----------------------------

if __name__ == "__main__":
    results = run_experiments()
    samples = run_sample_trajectories(SAMPLE_SKEW, NOISE_SIGMA, SAMPLE_RUNS)
    plot_results(results, samples)
