# v0.12-v0.15 Daisyworld Notes

## Purpose

v0.12 was the first architectural move beyond the single-basin mean-field world.

The goal was not “more realism” in the vulgar sense. The goal was to ask whether some of the observed global bounded-compression shape arises more naturally once lineages inhabit several partially closed reproductive fields rather than one universal bowl.

v0.13, v0.14, and v0.15 then tested what the basins were still missing locally.

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

So the current problem is no longer “nothing local matters.”

The problem is now sharper:
- the later basin still lacks enough pre-window buffering

## Current interpretation

Daisyworld now supports four claims:

1. The archipelago matters.
   Some global bounded-compression shape is more naturally produced in several partially closed basins than in one universal bowl.

2. Topology alone is not enough.
   Aggregate improvement can still arise from superposition without honest local timing.

3. Local closure matters.
   A basin’s tightening interval must alter not just skew, but openness.

4. Local marginality matters.
   A basin’s tightening interval must also change how harshly near-edge lineages are treated.

What remains missing is:
- stronger protection of late-basin breadth before its own tightening interval arrives

## Immediate lesson

The machine is still too much of a globe and not enough of an archipelago.

v0.12 was the first honest correction of that.
v0.13 showed that local timing would not be saved by prettier metrics or simple slack gradients.
v0.14 showed that local closure is part of the answer.
v0.15 showed that local marginality is also part of the answer.

The next serious Daisyworld step is therefore:
- not more generic in-window harshness
- but more honest pre-window buffering for the later basin
