# v0.12-v0.20 Daisyworld Notes

## Purpose

v0.12 was the first architectural move beyond the single-basin mean-field world.

The goal was not “more realism” in the vulgar sense. The goal was to ask whether some of the observed global bounded-compression shape arises more naturally once lineages inhabit several partially closed reproductive fields rather than one universal bowl.

v0.13 through v0.16 then tested what the scalar Daisyworld family was still missing locally.
v0.17 through v0.20 opened the graph branch inside those basins.

## Architecture

Three basins.
Weak symmetric coupling.
Staggered local tightening windows.
Shared internal machinery, then progressively less shared local closure conditions.

These basins are not necessarily geographic. They are partially bounded social reproductive fields.

## What improved in v0.12

Compared with the single-basin family, v0.12 improved the global story:

- aggregate bounded compression looked less forced
- pre-window global loss was lower
- window-dominated global loss was clearer
- aggregate peak pruning generation moved materially rightward
- survivor monopoly weakened
- diversity was preserved more naturally

This was enough to show that the single-basin world was topologically too polite.

## What did not improve enough in v0.12

The local basin story was not right.

Current issue:
- basin-specific peak pruning still occurred too early relative to each basin’s own local window

So the aggregate improvement seemed to arise more from superposition of several similar local declines than from cleanly staggered local transitions.

That was an important distinction.

## What v0.13 tested

v0.13 added exactly two things:

- a harsher local sustained-pruning metric using rolling decline
- a basin slack gradient via different local population sizes

This was a disciplined attempt to separate three possibilities:
- bad local metric
- too-similar basins
- genuinely wrong local dynamics

### v0.13 result

A useful failure.

It showed:
- the local-timing problem was not mainly a measurement artifact
- the rolling main-pruning metric did not rescue the local story
- a simple local slack gradient was not enough
- basin pruning still occurred too early relative to local windows

## What v0.14 tested

v0.14 added:
- window-driven local closure

Meaning:
- when a basin’s tightening window turned on, that basin became more locally closed

### v0.14 result

This was the first Daisyworld version to show a modest honest hint of local timing separation.

So closure was part of the missing ingredient, but not the whole thing.

## What v0.15 tested

v0.15 added:
- window-gated local marginality / fragility gain

Meaning:
- a basin’s tightening interval now altered not only skew and closure, but also how harshly local marginality was treated

### v0.15 result

This is the first Daisyworld version where the sustained local pruning metric starts to separate in the right direction, at least partially.

Current reading:
- local closure helps
- local marginality helps more
- basin 1 now moves later in a real way
- basin 2 still erodes too early

## What v0.16 tested

v0.16 added:
- basin-specific baseline fragility buffering

### v0.16 result

The later basin was protected better under the coarse metric, but sustained local delay still did not stagger cleanly.

So the scalar Daisyworld family remained informative and real, but still incomplete.

## Graph branch after v0.16

The next structural move after scalar Daisyworld refinement was the eligibility-graph branch.

Its history matters.

### v0.17

v0.17 showed that the graph idea was real, but baseline admissibility was too restrictive.

This was a useful negative result:
- the graph mattered strongly
- but the baseline world was too socially sorted from generation zero

### v0.18

v0.18 rehabilitated the branch by making the baseline graph genuinely open.

This showed:
- the graph could matter without front-loading collapse
- bounded compression could remain the main event
- the graph family was a legitimate structural family rather than decoration

### v0.19

v0.19 staged internal graph tightening.

This showed:
- staged internal tightening performs better than one-shot graph switching
- phased narrowing inside the basin is a more plausible structural move
- local sustained timing improves partially without reintroducing early-collapse pathology

### v0.20

v0.20 phased the tightening of different edge families.

This showed:
- matrix-wide staged tightening was still too coarse
- edge-phased collapse performs better than whole-matrix staging
- the graph branch can now produce the correct mean sustained basin ordering

So the current state of the inquiry is now split three ways:

- single-basin hysteresis family
- scalar/topological Daisyworld family
- nested-topology eligibility-graph family

The graph branch is now a real part of the repo’s conceptual structure.
It is not yet the uncontested winning family, but it has clearly earned continued attention.

## Current interpretation

Daisyworld now supports several claims:

1. The archipelago matters.
   Some global bounded-compression shape is more naturally produced in several partially closed basins than in one universal bowl.

2. Topology alone is not enough.
   Aggregate improvement can still arise from superposition without honest local timing.

3. Local closure matters.
   A basin’s tightening interval must alter not just skew, but openness.

4. Local marginality matters.
   A basin’s tightening interval must also change how harshly near-edge lineages are treated.

5. Admissibility topology matters.
   A basin may need internal structured connectivity, not merely scalar closure.

6. Staged tightening matters.
   The graph should not switch all at once; narrowing that propagates in phases performs better.

7. Edge-phased tightening matters even more.
   The internal bridges of a basin do not all collapse on the same schedule.

What remains missing is:
- stronger post-window persistence
- a final settled comparative judgment across branches
- and a principled stopping point before the graph branch drifts into overfitting

## Immediate lesson

The machine is still too much of a globe and not enough of an archipelago.

v0.12 was the first honest correction of that.
v0.13 showed that local timing would not be saved by prettier metrics or simple slack gradients.
v0.14 showed that local closure is part of the answer.
v0.15 showed that local marginality is also part of the answer.
v0.17-v0.20 showed that internal admissibility structure is a real nested-topology branch, and that edge-phased tightening is the strongest version of that branch so far.

The next serious step, if any, must therefore be judged against a much higher bar than earlier scalar refinements.
