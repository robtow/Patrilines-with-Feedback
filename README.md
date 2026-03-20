# Patrilines with Feedback

A small exploratory model accompanying the essay:

*Patrilines with Feedback; or, A Short Inquiry into the Y-Chromosome Bottleneck, Considered as a Control System.*

## Purpose

This repository explores whether the observed reduction in Y-chromosome lineage diversity can arise from the steady operation of coupled reproductive filters, rather than requiring large-scale episodic events such as warfare.

The aim is structural demonstration, not historical reconstruction.

---

## Current Model (v0.6)

The simulation now includes:

- A population divided into lineages
- Generational reproduction via multinomial sampling
- A controllable **skew parameter** (filter gain)
- **Multiplicative lineage-specific noise**
- **Thresholded fragility**, increasing as lineage size falls
- A **leakage channel (EPP)**:
  - fraction of births reassigned biologically
  - mixture of:
    - random diffusion
    - status-weighted reproduction

Tracked quantities:

- Shannon entropy
- Effective number of lineages (e^H)
- Active lineage count

---

## Observations

1. **Continuous filtering alone is sufficient to reduce lineage diversity**

   Even weak skew produces sustained compression.

2. **Thresholded fragility produces clustered collapse**

   Lineages linger near viability, then decline accelerates, producing uneven pruning.

3. **Leakage introduces a competing flow**

   The system is no longer purely compressive; diversity can be replenished.

4. **The effect of leakage depends strongly on its bias**

   Three regimes are observed:

   - **Random leakage (diffusive)**  
     - weak lineages receive inflow  
     - collapse is arrested  
     - system stabilizes at moderate diversity  

   - **Mixed leakage**  
     - diffusion and amplification compete  
     - system settles into an intermediate steady state  

   - **Status-weighted leakage (amplifying)**  
     - informal reproduction reinforces dominant lineages  
     - collapse accelerates  
     - diversity declines more rapidly  

   These regimes arise without changing the primary filtering or threshold dynamics; only the bias of the leakage channel is varied.

---

## Interpretation

The system now has three interacting dynamical layers:

- Mean-field filtering → global compression  
- Thresholded fragility → local positive feedback and clustered collapse  
- Leakage → cross-lineage transport  

The key result is:

> The long-term behavior of lineage diversity depends not only on formal reproductive constraints, but on the bias structure of informal reproduction.

More sharply:

> Informal reproduction is not inherently egalitarian. If it follows the same status signal as formal reproduction, it amplifies inequality. If it is sufficiently uncorrelated, it stabilizes diversity.

---

## NOTE

This model does not represent intention or morality; it is a minimal model of reproductive flow under constrained access, with a secondary leakage channel whose bias determines system behavior.

---

## Next Step

Decouple the signal used by the leakage channel from formal lineage size:

- introduce a second latent trait (e.g. “attractiveness” or local fitness)
- allow informal reproduction to sample a partially independent signal

Hypothesis:

> When formal and informal selection signals diverge, the system may exhibit persistent tension between stabilization and concentration.

---

## Structure

- `model/` — simulation code  
- `notes/` — working notes and logs  
- `papers/` — reference PDFs  
- `figures/` — generated plots  

---

## Status

Exploratory model with working dynamics.

v0.3 — mean-field + noise (smooth compression)  
v0.4 — threshold (uneven collapse)  
v0.5 — shaped fragility (clustered pruning)  
v0.6 — leakage (EPP) introduces competing flow and three regimes  

The current model demonstrates that:

> punctuated-looking lineage collapse can emerge from internal dynamics, and that its persistence or arrest depends on the bias of informal reproductive channels.

The system exhibits three distinct regimes under variation of a single parameter (leakage bias): diffusion, equilibrium, and amplification.

---

## Figures

Figures are generated from simulation code. Selected figures (`sim_*.png`) are versioned when they correspond to specific model states.
