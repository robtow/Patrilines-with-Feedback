# v0.17-v0.19 Eligibility Graph Notes

## Purpose

This note records the first nested-topology branch inside Daisyworld.

The point of the branch was not to add more scalar pressure.
The point was to represent internal basin structure explicitly, using a tiny eligibility graph.

The key idea was:

- a basin is not internally smooth
- lineages are not all equally exchangeable
- tightening should mean loss of admissible edges, not merely stronger scalar filtering

## v0.17

v0.17 was the first eligibility-graph implementation.

Result:
- failure, but informative

What it showed:
- the eligibility graph can matter a great deal
- the first "open" graph was too restrictive
- collapse was front-loaded
- the machine reverted to early pruning before the intended bounded window

Interpretation:
- the graph idea was not empty
- but the baseline world was too socially sorted from generation zero

## v0.18

v0.18 softened the baseline graph substantially.

Result:
- the graph branch was rehabilitated

What it showed:
- early-collapse pathology could be removed
- the bounded window again became the dominant event
- the graph could live inside the model without poisoning the baseline world

But:
- local staggering was still incomplete
- one-shot switching from open to tight remained too coarse

Interpretation:
- the eligibility graph is a real structural mechanism
- but the basin still needed internal timing, not just internal connectivity

## v0.19

v0.19 introduced staged tightening inside the basin graph.

Instead of:
- open before the window
- tight during the window

the graph now moves through phases:
- open
- mid
- tight

Result:
- partial success

What improved:
- sustained local pruning times separate more credibly than in v0.18
- one-shot graph switching was too coarse
- staged tightening performs better than a single internal graph switch
- the basin now behaves more like a nested structure and less like a flat switch

Current reading:
- staged graph tightening is the first nested-topology version to produce partial separation of sustained local pruning without reintroducing early-collapse pathology
- this supports the view that the missing structure was layered internal topology rather than additional scalar harshness

What remains unresolved:
- local ordering is still incomplete
- basin 2 is not yet cleanly latest under the sustained-pruning metric
- rebound remains too easy
- the graph branch still yields a fairly sharp sparse-winner regime

## Current graph-branch lesson

The graph branch has now earned its place.

The sequence is clear:

- v0.17: graph too harsh at baseline
- v0.18: graph baseline made genuinely open
- v0.19: staged graph tightening improves local timing

So the graph is no longer a speculative ornament.
It is a real structural family.

## Present caution

This is not yet a solved local-history machine.

The graph branch currently supports a narrower and more honest claim:

- culture may act by deleting or weakening admissible edges
- internal basin timing matters
- staged tightening is better than one-shot tightening
- nested topology explains more than additional scalar force

But:
- clean local staggering is still not achieved
- further elaboration now risks target-chasing if not tightly disciplined
