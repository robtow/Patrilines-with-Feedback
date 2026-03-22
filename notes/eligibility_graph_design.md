# Eligibility Graph Design Notes

## Why this move

The current Daisyworld family has reached the point where more scalar tweaks begin to smell of overfitting.

What seems missing is not another gain term, but a more honest internal topology.

A basin is still too smooth.
Its closure is still too scalar.
Its tightening still acts too much like pressure and not enough like changed connectivity.

The proposed move is therefore:

> inside each basin, replace scalar closure with a tiny eligibility graph.

This gives a better meaning to institutional tightening.
It also gives a better meaning to the informal channel.

Most importantly, it lets the model distinguish:
- biological persistence
from
- social admissibility

A lineage may remain numerically alive while becoming reproductively marginal inside the formal order.

That is likely closer to history.

## Core idea

Each basin contains a very small number of internal classes.

Proposed classes:
- core
- intermediate
- periphery

These are topological roles, not ethnographic labels.
They are not “castes” in the historical claim sense.
They are simply positions in a local admissibility graph.

Each lineage belongs to one class.

At first:
- class membership is fixed
- no mobility between classes
- no added complexity from promotion / degradation

This is deliberate.
The first question is whether graph structure itself buys explanatory power.

## What tightening means

At present, tightening means:
- higher skew
- more closure
- more local marginality

In the proposed graph model, tightening should mean something more structural:

> some admissible reproductive edges weaken or disappear.

So the basin does not merely “get harsher.”
It becomes less connected in a patterned way.

That is a much better representation of culture as topology.

## Eligibility matrices

Each basin gets a small class-by-class admissibility matrix.

Rows and columns correspond to:
- core
- intermediate
- periphery

### Open matrix

Before tightening, the local graph is relatively open.

Qualitative pattern:
- core <-> core: strong
- core <-> intermediate: fairly open
- intermediate <-> intermediate: open
- intermediate <-> periphery: moderately open
- core <-> periphery: weaker, but not absent
- periphery <-> periphery: viable enough for persistence

### Tightened matrix

During tightening, the graph narrows.

Qualitative pattern:
- core <-> core: remains strong
- core <-> intermediate: weaker
- intermediate <-> intermediate: still viable
- intermediate <-> periphery: weak
- core <-> periphery: very weak
- periphery <-> periphery: persistent but low-opportunity

The essential point is not the exact numeric values yet.
It is the pattern:

> tightening deletes or weakens cross-status / long-path reproductive routes first.

## Formal vs informal channels

This is the most important conceptual gain.

The informal channel should not merely be a differently weighted version of the same space.
That has been one of the hidden simplifications all along.

A better meaning for “female choice” or informal leakage is this:

> it is not magic diffusion through the same space; it is partial traversal of edges that the formal order is trying to narrow.

That means:

- the formal channel respects the tightened eligibility graph strongly
- the informal channel either:
  - uses a softer version of the same graph, or
  - retains some access across edges that the formal channel is narrowing

This is exactly the kind of asymmetry the current scalar model can only gesture toward.

It also means the informal channel can preserve some breadth without being imagined as a universal solvent of hierarchy.

## What the graph should do

The graph should affect:
- who can expand
- who remains socially central
- who becomes trapped in low-connectivity zones

It should not merely act as a survival tax.

The intended mechanism is:

- tightening narrows admissible exchange
- some lineages become structurally peripheral
- some survive numerically but lose high-value connectivity
- a few remain central
- later expansion comes disproportionately through those central survivors

That is a much better route to survivor burst than simply adding more pressure.

## Relationship to earlier mechanisms

The graph should not merely be piled on top of every earlier mechanism at full strength.
If that happens, nothing is learned.

So the first honest implementation should probably:
- keep three basins
- keep weak inter-basin coupling
- keep staggered windows
- keep mild baseline skew
- weaken or simplify some of the special window-gated scalar harshness
- allow the graph to do real work

Otherwise the graph becomes ornament.

## Minimal first implementation

To keep this honest, the first graph version should be extremely small.

Proposed constraints:
- three basins only
- three internal classes per basin only
- one open matrix family
- one tightened matrix family
- same matrix family across all basins at first
- fixed class membership
- no directed center-periphery hierarchy between basins yet
- no class mobility
- no additional damage term changes unless the graph clearly fails

## Success criteria

The graph version should only be kept if it buys something clearer than curve massage.

Success would mean:

1. later basins remain broad longer under the sustained-pruning metric
2. local pruning times stagger more honestly
3. aggregate bounded compression remains plausible
4. rebound becomes harder for a better reason:
   lost admissible edges do not automatically regrow
5. survivor concentration emerges through connectivity, not merely brute pressure

## Failure criteria

The graph version should be rejected, or at least not elaborated, if:

- it only reproduces existing behavior with more machinery
- it improves visuals without improving local timing
- it requires restoring every old scalar pressure term at full force
- it introduces too many ad hoc exceptions
- it becomes ethnographic pageant rather than topological mechanism

## Why this is worth trying

The current Daisyworld family suggests that:
- topology matters
- closure matters
- local marginality matters

But the map is still too coarse.

The eligibility graph is the next honest structural move because it treats culture as changed connectivity rather than as a mere pressure scalar.

That is elegant, constrained, and testable.

## Present caution

This note proposes a structural move.
It does not yet claim a result.

No README-wide triumphal rewriting should happen yet.
This is still design, not success.

The next adult step is:
- refine this design note
- decide what old mechanisms must be weakened so the graph gets a fair test
- then implement one minimal graph version
- then judge it under the existing empirical scoreboard
