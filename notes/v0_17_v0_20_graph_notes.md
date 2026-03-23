# v0.17-v0.20 Eligibility Graph Notes

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

the graph now moved through phases:
- open
- mid
- tight

Result:
- partial success

What improved:
- sustained local pruning times separated more credibly than in v0.18
- one-shot graph switching was too coarse
- staged tightening performed better than a single internal graph switch
- the basin began to behave more like a nested structure and less like a flat switch

Current reading:
- staged graph tightening was the first nested-topology version to produce partial separation of sustained local pruning without reintroducing early-collapse pathology
- this supported the view that the missing structure was layered internal topology rather than additional scalar harshness

What remained unresolved:
- local ordering was still incomplete
- basin 2 was not yet cleanly latest under the sustained-pruning metric
- rebound remained too easy
- the graph branch still yielded a fairly sharp sparse-winner regime

## v0.20

v0.20 refined the graph branch further by phasing the tightening of different edge families rather than staging the whole matrix as a block.

This was the first version in which the graph degraded in a more biologically and socially plausible way:
- longest or most status-crossing bridges narrowed first
- medium bridges narrowed next
- within-class continuity remained viable longest

Result:
- clear success, though still partial in the larger historical sense

What improved:
- mean sustained basin ordering now falls in the intended direction:
  - basin 0 earliest
  - basin 1 next
  - basin 2 latest
- the coarse single-step metric also orders cleanly
- global bounded compression remains plausible
- early-collapse pathology does not return
- rebound is not worse than v0.19, and may be modestly improved

Interpretation:
- the graph branch has now done the thing it was supposed to do
- the missing structure was not simply “a graph,” but timed degradation of different admissible routes inside the basin
- edge-phased tightening performs better than both one-shot graph switching and matrix-wide staged tightening

This is the first graph version that clearly earns its keep.

## Current graph-branch lesson

The graph branch is now a real part of the model family, not a speculative ornament.

The sequence is now clear:

- v0.17: graph too harsh at baseline
- v0.18: graph baseline made genuinely open
- v0.19: staged graph tightening improves local timing
- v0.20: edge-phased graph tightening is the first version to get mean sustained basin ordering right

So the strongest current graph-branch claim is:

- tightening inside a basin is better represented as phased narrowing of admissible connectivity than as a one-shot graph switch or a purely scalar increase in harshness

## Present caution

This is still not a solved local-history machine.

The graph branch currently supports a narrower and more honest claim:

- culture may act by deleting or weakening admissible edges
- internal basin timing matters
- staged tightening is better than one-shot tightening
- edge-phased tightening is better than matrix-wide staged tightening
- nested topology explains more than additional scalar force

But:
- the graph branch still yields a relatively sharp sparse-winner regime
- rebound remains too easy in absolute terms
- further elaboration now risks target-chasing if not tightly disciplined

## Current standing

At present:

- v0.9 remains the best single-basin behavioral family
- v0.15 remains the best scalar/topological Daisyworld family
- v0.20 is now the best nested-topology eligibility-graph family

That is the current honest ranking.

## Consequence for the essay

The essay can now say something stronger than before.

Not merely:
- bounded filtering in several basins can compress male-line diversity

But:
- phased narrowing of admissible connectivity inside partially closed basins gives a better account of local timing than scalar tightening alone

That is a real gain in structural clarity.
