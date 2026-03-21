# Patrilines with Feedback

A small exploratory model accompanying the essay:

*Patrilines with Feedback; or, A Short Inquiry into the Y-Chromosome Bottleneck, Considered as a Control System.*

## Purpose

This repository explores whether the observed reduction in Y-chromosome lineage diversity can arise from the steady operation of coupled reproductive filters, rather than requiring large-scale episodic events such as warfare.

The aim is structural demonstration, not historical reconstruction.

---

## Current Model (v0.7)

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
- A **dual-signal structure**:
  - a formal signal governing institutional reproduction
  - an informal signal governing leakage / EPP
  - tunable correlation between the two

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

   Three regimes were observed in v0.6:

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

5. **Signal alignment matters even when leakage mixture is held fixed**

   In v0.7, the leakage channel samples an informal signal that may be aligned with, partially correlated with, or independent of formal lineage success.

   With leakage rate and mixture held constant:

   - **Independent informal signal (`corr = 0.0`)**  
     - preserves the highest entropy  
     - preserves the highest effective lineage count  
     - stabilizes the largest number of active lineages  

   - **Partial alignment (`corr = 0.5`)**  
     - yields an intermediate steady state  
     - reduces diversity relative to the independent case  

   - **Full alignment (`corr = 1.0`)**  
     - produces the strongest compression  
     - yields the lowest long-run diversity of the three  

   The decisive variable is therefore not leakage alone, but whether the informal channel samples the same signal as the formal system.

---

## Interpretation

The system now has four interacting dynamical layers:

- Mean-field filtering → global compression  
- Thresholded fragility → local positive feedback and clustered collapse  
- Leakage → cross-lineage transport  
- Signal alignment → determines whether informal reproduction diffuses or reinforces formal inequality  

The key result is:

> The long-term behavior of lineage diversity depends not only on formal reproductive constraints, but on the bias structure of informal reproduction and on the degree of alignment between formal and informal signals.

More sharply:

> Informal reproduction is not inherently egalitarian. If it follows the same signal as formal reproduction, it amplifies inequality. If it is sufficiently uncorrelated, it stabilizes diversity.

A second way to put the same point is that the model now behaves as a multi-controller system. One channel allocates reproduction formally; another redistributes it informally. The long-run result depends on how closely the second controller listens to the first.

---

## NOTE

This model does not represent intention or morality; it is a minimal model of reproductive flow under constrained access, with a secondary leakage channel whose bias and signal alignment determine system behavior.

---

## Next Step

Explore stronger separation between formal and informal selection by extending the informal signal further:

- test anti-correlated informal signals
- allow informal attractiveness to persist or drift across generations
- examine whether competing signals produce stronger tension, oscillation, or more persistent diversity

Hypothesis:

> When formal and informal selection signals diverge more strongly, the system may exhibit sustained tension rather than simple convergence toward either collapse or equilibrium.

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
v0.7 — dual-signal model shows that signal alignment systematically shifts long-run diversity  

The current model demonstrates that:

> punctuated-looking lineage collapse can emerge from internal dynamics, and that its persistence, arrest, or moderation depends on the structure of informal reproductive channels.

The system exhibits distinct regimes under variation of a small number of parameters:

- leakage bias: diffusion, equilibrium, amplification  
- signal alignment: independent, intermediate, aligned

---

## Figures

Figures are generated from simulation code. Selected figures (`sim_*.png`) are versioned when they correspond to specific model states.
