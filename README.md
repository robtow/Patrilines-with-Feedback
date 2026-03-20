# Patrilines with Feedback

A small exploratory model accompanying the essay:

*Patrilines with Feedback; or, A Short Inquiry into the Y-Chromosome Bottleneck, Considered as a Control System.*

## Purpose

This repository explores whether the observed reduction in Y-chromosome lineage diversity can arise from the steady operation of coupled reproductive filters, rather than requiring large-scale episodic events such as warfare.

The aim is structural demonstration, not historical reconstruction.

---

## Current Model (v0.3)

The current simulation implements:

- A population divided into lineages
- Generational reproduction via multinomial sampling
- A controllable **skew parameter** (interpreted as filter gain)
- Optional **multiplicative lineage-specific noise**
- Tracking of:
  - Shannon entropy
  - Effective number of lineages (e^H)
  - Active lineage count

---

## Observations (v0.3)

1. **Continuous filtering alone is sufficient to reduce lineage diversity**

   Even very weak skew (1.02–1.05) produces sustained decline in effective lineage count.

2. **No catastrophic events are required**

   The system collapses under steady bias alone, supporting the hypothesis that lineage compression can emerge without warfare.

3. **Noise introduces trajectory variability but not punctuated collapse**

   With stochastic variation:
   - trajectories diverge
   - small irregularities appear

   However, decline remains largely smooth.

---

## Interpretation

The current model corresponds to a **mean-field control system** with stochastic variation.

It demonstrates:

> Continuous filtering → smooth compression of lineage diversity

But does **not yet produce punctuated pruning**.

---

## Next Step

Introduce a **nonlinear viability threshold**:

- Small lineages become disproportionately fragile
- Below-threshold lineages experience reduced reproductive success

Hypothesis:

> Punctuated collapse emerges from the interaction of continuous filtering and threshold effects

---

## Structure

- `model/` — simulation code
- `notes/` — working notes and logs
- `papers/` — reference PDFs
- `figures/` — generated plots

---

## Status

Early-stage exploratory model.

v0.3 establishes baseline behavior (continuous compression + stochastic variation).  
v0.4 will introduce threshold dynamics.

