# Edge-Phased Graph Design

## Purpose

This note defines the next structural refinement after `v0.19`.

The point is not to add more scalar force.
The point is to refine the *timing of graph degradation* inside a basin.

Hypothesis:

> tightening inside a basin does not proceed by matrix-wide switches; it proceeds by phased narrowing of different edge families.

This is the next honest nested-topology move.

## Why this move

`v0.19` showed that staged internal tightening performs better than a one-shot graph switch.

That was important.

But `v0.19` still stages the whole matrix too coarsely:
- first part of the window -> mid matrix
- second part of the window -> tight matrix

That is better than one-shot tightening, but still too lumped.

If the later basin still does not fully wait its turn, the likely reason is:
- different kinds of admissible routes should collapse on different schedules

So the next refinement is not more pressure.
It is finer propagation through the graph already in hand.

## Basin interior classes

Keep the current three classes:

- core
- intermediate
- periphery

Keep:
- fixed class membership
- same class proportions
- no class mobility for this pass

## Endpoint matrices

Keep the existing endpoint logic:

### Open baseline

```text
[[1.00, 0.95, 0.90],
 [0.95, 1.00, 0.92],
 [0.90, 0.92, 1.00]]
