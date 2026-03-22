# Staged Eligibility Graph Design

## Purpose

This note defines the next structural move after `v0.18`.

The point is not to add more scalar harshness.
The point is to make tightening inside a basin occur in stages.

Hypothesis:

> a basin does not reorganize all at once; tightening propagates through its internal admissibility graph in layers.

This is the smallest honest “nested dolls” extension of the eligibility-graph model.

## Why this move

`v0.18` rehabilitated the eligibility-graph architecture after the overly harsh baseline of `v0.17`.

It showed that:
- the graph can matter without forcing immediate collapse
- global bounded compression remains plausible
- local severity is differentiated

But it also showed that:
- local sustained pruning still does not stagger cleanly
- the late basin still does not truly wait its turn

That suggests the remaining problem is not merely basin-to-basin timing.
It is also the fact that each basin’s internal graph still switches too coarsely.

The current graph says:
- open before window
- tight during window

That is still too blunt.

## Core idea

Inside each basin, tightening should happen in phases.

Not everything narrows at once.
Bridging edges weaken first.
Internal or same-class persistence remains viable longer.
The basin therefore has an internal wavefront rather than a single switch.

This is a better representation of nested social constraint.

## Basin interior classes

Keep the current three classes:

- core
- intermediate
- periphery

These remain:
- fixed at initialization
- topological roles, not ethnographic claims
- non-mobile for this pass

No class mobility is added yet.

## Class proportions

Keep the existing proportions:

- core: 20%
- intermediate: 40%
- periphery: 40%

## Graph states

Use three graph states instead of two:

- `E_open`
- `E_mid`
- `E_tight`

### Open matrix

```text
[[1.00, 0.95, 0.90],
 [0.95, 1.00, 0.92],
 [0.90, 0.92, 1.00]]
