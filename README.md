# Patrilines with Feedback

A small exploratory model accompanying the essay:

*Patrilines with Feedback; or, A Short Inquiry into the Y-Chromosome Bottleneck, Considered as a Control System.*

## Purpose

This repository explores whether the observed reduction in Y-chromosome lineage diversity can arise from the steady operation of coupled reproductive filters, rather than requiring large-scale episodic events such as warfare.

The aim is structural demonstration, not historical reconstruction.

---

## Current Model (v0.5)

The current simulation implements:

- A population divided into lineages
- Generational reproduction via multinomial sampling
- A controllable **skew parameter** (filter gain)
- **Multiplicative lineage-specific noise**
- **Thresholded fragility**, increasing as lineage size falls
- Tracking of:
  - Shannon entropy
  - Effective number of lineages (e^H)
  - Active lineage count

---

## Observations

1. **Continuous filtering alone is sufficient to reduce lineage diversity**

   Even very weak skew (1.02–1.05) produces sustained decline.

2. **No catastrophic events are required**

   Collapse emerges under steady bias alone.

3. **Magnitude of skew required is small**

   A few percent bias is sufficient to produce long-term concentration.

4. **Noise introduces divergence but not structure**

   Stochastic variation produces trajectory variability, but by itself does not create punctuated behavior.

5. **Thresholded fragility produces clustered collapse**

   When fragility increases below a viability threshold:
   - lineages linger near threshold
   - then decline accelerates
   - extinctions cluster in time

   This produces **uneven, locally accelerated pruning**.

---

## Interpretation

The system now has three layers:

- Mean-field filtering → slow compression  
- Stochastic variation → divergence across runs  
- Thresholded fragility → local positive feedback  

Together these produce:

> continuous global compression with locally accelerated collapse

The result is not a smooth exponential decay, but a system in which:

> collapse appears episodic without requiring external shocks

---

## Next Step

Introduce **leakage across lineages** (e.g. extra-pair paternity or social reassignment):

- allows weak lineages to persist longer
- redistributes reproductive success across lineages
- may stabilize or reshape collapse dynamics

Hypothesis:

> Leakage competes with thresholded fragility, producing a balance between persistence and collapse

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

The current model demonstrates that:

> punctuated-looking lineage collapse can emerge from internal dynamics without external catastrophic events

---

## Figures

Figures are generated from simulation code. Selected figures (`sim_*.png`) are versioned when they correspond to specific model states.
