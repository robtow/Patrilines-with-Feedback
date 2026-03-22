# Eligibility Graph Spec

## Purpose

This note freezes the first minimal eligibility-graph implementation before code.

The point is to test a structural hypothesis, not to improvise one more patch.

Hypothesis:

> shrinking internal admissibility inside basins can produce cleaner delayed local pruning than additional scalar window-harshness.

## Basin interior classes

Each basin contains three internal classes:

- core
- intermediate
- periphery

These are topological roles, not ethnographic claims.

At first:
- class membership is assigned once at initialization
- class membership remains fixed
- no promotion, degradation, or mobility is allowed

## Class proportions

Use fixed proportions within each basin:

- core: 20%
- intermediate: 40%
- periphery: 40%

This is enough hierarchy to matter without turning the model into pageant.

## Open eligibility matrix

Before tightening, use:

```text
[[1.00, 0.75, 0.40],
 [0.75, 0.90, 0.60],
 [0.40, 0.60, 0.80]]
