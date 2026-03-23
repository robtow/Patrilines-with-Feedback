# Model Notes

## Current control structure

Formal channel:
- skew
- fragility threshold / shaped fragility
- multiplicative noise

Informal channel:
- leakage rate
- leakage mixture
- informal signal

State variables:
- concentration from effective lineage diversity
- thresholded damage / hysteresis as reduced recoverability under exceptional compression

Topological structure:
- single-basin family
- scalar/topological Daisyworld family with weak coupling and staggered local windows
- nested-topology eligibility-graph family with internal admissibility classes and phased graph degradation

## Main results so far

- weak continuous filtering is sufficient for compression
- thresholded fragility produces clustered pruning
- leakage introduces competing flow
- leakage bias determines whether the channel diffuses or amplifies inequality
- signal alignment between formal and informal channels shifts long-run diversity monotonically
- bounded compression can now be made the dominant event rather than an afterthought
- hysteresis can be made nontrivial without saturating into nonsense
- where hysteresis enters the system matters more than the mere existence of hysteresis
- topology matters more than the single-basin toy admitted
- Daisyworld local timing failure is real, but closure plus local marginality begin to separate local timing
- admissibility structure is real
- staged tightening inside the graph works better than one-shot graph switching
- edge-phased tightening works better than matrix-wide staged tightening

## Current regimes

v0.6:
- random leakage -> diffusion
- mixed leakage -> equilibrium
- status-weighted leakage -> amplification

v0.7:
- corr 0.0 -> highest diversity
- corr 0.5 -> intermediate
- corr 1.0 -> strongest compression

## What v0.8 exposed

The first v0.8 runs were useful precisely because they failed in an informative way.

The machine was still panicking almost immediately. Peak pruning occurred near generation 2, long before the bounded pressure window. That meant the model, as initially parameterized, was not yet showing stored fragility after bounded compression. It was front-loading the damage.

The pathology was straightforward:
- initial mean lineage size sat too close to the fragility threshold
- the system began already near brittleness
- endogenous fragility then amplified early drift rather than emerging later from compression

In plain language: the machine was born sick.

That was not a subtle result, but it was a real one.

## Conceptual reset

The initial state should represent a relatively broad, redundant male-line ecology.

That fits the larger historical intuition: pruning is not primordial. It arises because cultural complexity, inheritance, legitimacy, residence rules, status differentiation, and related machinery create larger and more stratified systems with memory. The point of the bounded pressure window is to stand in for the tightening and co-alignment of those institutions.

So the model should begin in a world with slack:
- many coexisting male lines
- local weakness survivable
- mild variation present but not yet destiny
- no immediate synchronized fall over a threshold edge

## Heterogeneous starts and epistemic hygiene

A perfectly uniform initialization is mathematically tidy but conceptually stupid if it puts every lineage on the same knife-edge. It turns the first random fluctuation into a synchronized firing squad.

So later versions use mild initial heterogeneity.

But that raises a new danger: once the start is heterogeneous, it becomes easy to call every later inequality “emergent” when in fact some of it was simply inherited from the draw.

That sort of sloppiness is not permitted.

Initial heterogeneity is not yet hierarchy. It is merely variation. The question is whether bounded cultural tightening takes ordinary variation and hardens it into lineage fate.

## The real question now

The question is no longer whether the system can compress male-line diversity. It plainly can.

The question is whether a bounded interval of increased filtering, understood as tighter memetic and institutional coherence, can push a broad, mildly heterogeneous system into a lower-entropy state that then alters its later response to perturbation.

In blunt terms:
- does the system become brittle because it has been compressed?
- does pruning lag the forcing window?
- does bounded tightening convert mild stochastic differences into durable stratification?
- does reduced diversity become harder to escape once the system has narrowed?
- and is the observed global shape really one regime, or the aggregate of several coupled basins?

That is the real test.

## Topological signatures to track

The model is now being asked not just for lower diversity, but for a topology:

- bounded compression
- slope steepening
- knees
- pruning lag
- survivor concentration
- plateau versus continued collapse
- change in the derivative of inequality
- persistence or rebound after the compression interval
- local versus global timing in coupled basins

The field already gives shape classes:
- bounded paternal compression
- no comparable maternal collapse
- sparse survivor set
- later survivor fan-out

The question is whether this machine can emit something recognizably similar.

## Metrics that now matter

### 1. Pruning lag

If the steepest pruning occurs exactly during the forcing window, then the window is merely forcing the system.

If the steepest pruning occurs after the window, then the system has stored fragility.

That is worth knowing.

### 2. Survivor fan-out

Not just low entropy, but concentrated survivors:
- top-1 share
- top-3 share
- top-5 share
- final rank-size curve

### 3. Survival conditional on initial position

This is the nastier metric, and probably the more interesting one.

Divide the initial distribution into lower, middle, and upper thirds.
Then ask:
- how often does each group survive?
- how much final share does each group command?

If bounded tightening turns mild initial variation into very sharp stratification of survival odds, then one can say, honestly, that the cultural machinery has converted ordinary variation into lineage fate.

### 4. Amplification rather than mere outcome

Do not merely measure final inequality.
Measure amplification.

For example:
- initial top-1 share vs final top-1 share
- initial spread vs final spread
- rank correlation between initial size and final outcome
- survival odds by initial tercile

The question is not whether inequality exists. Of course it does.
The question is whether the social machine changes its slope, memory, and stickiness.

### 5. Damage behavior

If damage is present, it must be inspected as a state variable rather than assumed to be meaningful.

Relevant checks:
- final damage
- max damage
- whether damage saturates uselessly
- whether damage reduces rebound
- whether damage actually delays pruning rather than merely deepening concentration
- whether the placement of damage in the transfer function changes behavior materially

### 6. Basin behavior

If basins are present, local and aggregate timing must both be inspected.

Relevant checks:
- basin single-step pruning times
- basin rolling main-pruning times
- basin window losses
- aggregate peak pruning time
- aggregate lag improvement
- whether the aggregate improvement comes from true local staggering or merely superposition of similar local declines

## Damage term: what it is allowed to mean

If a damage term enters the model, it is not to mean generic badness, hidden mortality, or melodramatic injury. It must mean something narrower and more defensible.

The strongest interpretation so far is this:

Damage is accumulated loss of recoverability in the male-line social-ecological system, arising from prior compression of lineage diversity.

That loss of recoverability can stand in for several concrete things that share the same dynamical property: they do not reset immediately when external pressure relaxes.

These include:
- weaker alliance options
- thinner marriage prospects
- reduced lineage legitimacy
- poorer continuity of resource transmission
- lower network redundancy
- increased sensitivity to perturbation after compression

But the sharpest interpretation is this:

### Damage as cultural overfitting

A tightly structured male-line society may become very good at preserving its current hierarchy and very bad at recovering breadth once that breadth has been lost.

In that sense the system overfits to its own reduced diversity.

That is not mystical. It is engineering. A controller can become highly competent at maintaining one regime and highly incompetent at escaping it. The more tightly tuned it is to preserving current winners, the worse it becomes at re-opening lineage opportunity once redundancy has been reduced.

So if damage is added, it should act as:
- accumulated rigidity
- reduced capacity for re-diffusion
- slower recovery after compression
- greater stickiness of inequality

That is the right interpretation because it links the symbolic and biological sides without pretending they are literally the same substance.

The symbolic machine compresses lineages.
Compression lowers redundancy.
Lower redundancy makes the system less forgiving.
Then the symbolic machine reads that narrowed state back as natural order and tightens further.

That is a nasty little loop, and it sounds more like history than either noble savages or instant horse-borne apocalypse.

## What v0.9, v0.10, and v0.11 now show

### v0.9

Thresholded damage acting directly on persistence / fragility gives the best current single-basin behavioral result.

It no longer saturates to 1.0 in every run. Damage remains an interior state variable, bounded compression remains window-dominant, survivor concentration remains strong, and the post-window result is best described as partial scar rather than durable lock-in.

### v0.10

Damage moved out of fragility and into suppression of the diffusive informal channel.

This was conceptually cleaner, because it matched the overfitting / reduced-recovery reading more directly.

But it was behaviorally too weak.
At present scale, the leakage channel is too marginal to carry the burden of hysteresis by itself.

### v0.11

A restrained hybrid, with damage acting mostly on re-diffusion and only modestly on fragility.

This improved on v0.10 but still did not beat v0.9.

## Current single-basin ranking

At present:

- v0.9 is the best current single-basin model family
- v0.11 is informative but inferior
- v0.10 is the useful negative control

So the current unpleasant lesson is:

A cleaner recovery-channel interpretation of hysteresis is not strong enough by itself. The best current single-basin match requires damage to affect persistence more directly.

That is uglier than the more elegant story, and likely closer to history.

## What v0.12-v0.16 scalar Daisyworld now show

### v0.12

Three weakly coupled basins immediately improved the global story:
- aggregate bounded compression looked less forced
- pre-window global loss was lower
- window-dominated global loss was clearer
- aggregate peak pruning generation moved materially rightward
- survivor monopoly weakened
- diversity was preserved more naturally

This was enough to show that the single-basin world was topologically too polite.

But the local basin story was not right:
- basin-specific peak pruning still occurred too early relative to local windows
- aggregate lag improvement appeared to come more from superposition than from cleanly staggered local transitions

### v0.13

v0.13 added:
- a harsher local sustained-pruning metric using rolling decline
- a basin slack gradient via different local population sizes

These were useful failures.

They showed:
- the local-timing problem was not mainly a metric artifact
- simple basin slack was not enough
- basin pruning still occurred too early relative to local windows

### v0.14

v0.14 added:
- window-driven local closure

This was the first Daisyworld version to show a modest honest hint of local timing separation.
It helped, but not enough.

### v0.15

v0.15 added:
- window-gated local marginality / fragility gain

This is the first Daisyworld version where the sustained local pruning metric starts to separate in the right direction, at least partially.

Current reading:
- local closure helps
- local marginality helps more
- basin 1 now moves later in a real way
- basin 2 still erodes too early

### v0.16

v0.16 added:
- basin-specific baseline fragility buffering

This improved coarse local staggering, especially under the single-step metric, but sustained local delay remained incomplete.

Current scalar Daisyworld reading:
- closure matters
- local marginality matters
- pre-window buffering matters
- but the later basin still does not truly wait its turn

## What v0.17-v0.20 now show

### v0.17

The first eligibility-graph implementation was too harsh at baseline.

The important point is not that the graph failed, but how it failed:
- the baseline world was not open enough
- the machine collapsed too early
- admissibility structure was being imposed from generation zero too strongly

### v0.18

Softening the open graph rehabilitated the branch.

This showed:
- the graph can matter structurally without poisoning the baseline
- bounded compression can remain the main event
- the graph family is a legitimate mechanism family, not ornament

### v0.19

Staging tightening inside the graph improved the branch further.

This showed:
- one-shot graph switching was too coarse
- phased internal tightening produces more credible sustained local timing
- nested local topology matters

### v0.20

Phasing the collapse of different edge families improved the branch further still.

This showed:
- matrix-wide staged tightening was still too coarse
- cross-class bridges must collapse on different schedules
- edge-phased tightening is the first graph version to produce correct mean sustained basin ordering

Current graph-branch reading:
- admissibility structure is real
- staged tightening is better than one-shot tightening
- edge-phased tightening is better than matrix-wide staged tightening
- the remaining missing thing is no longer obviously more scalar force
- but rebound remains too easy and the branch still needs disciplined stopping rules

## Current ranking

At present:

- best single-basin family: v0.9
- best scalar/topological Daisyworld family: v0.15
- best nested-topology graph family: v0.20

Those are not contradictory. They are different accomplishments.

## Current honest result

The project now supports these claims:

- bounded compression can arise from internal coupled filtering
- survivor concentration can remain strong without requiring the usual bloody male bloodbath
- partial hysteresis is plausible
- where hysteresis enters matters
- single-basin mean-field structure was a major topological oversimplification
- multi-basin Daisyworld makes the global shape more plausible
- local closure plus local marginality begin to produce local timing separation
- admissibility structure is a real mechanism family
- staged internal tightening outperforms one-shot graph switching
- edge-phased internal tightening is the first graph mechanism to get mean sustained ordering right
- but local basin timing and durable post-window scar remain unsolved in the larger sense

So the machine now appears to know:
- how to compress,
- how to leave a scar,
- how topology changes the global appearance,
- and how internal admissibility structure begins to matter,

but not yet how to deliver historical closure without inviting overfitting.

## Working hypothesis

The strongest form of the current hypothesis is this:

A bounded interval of cultural tightening does not merely reduce diversity while active. It changes the transfer function by which male lines persist. As entropy falls, redundancy falls. As redundancy falls, fragility rises. Once the system is sufficiently compressed, the same perturbations become more dangerous, and mild initial variation is more easily converted into durable pruning and survivor concentration.

Current experiments add a second strong claim:

Some of the apparent global bounded-compression shape may arise more naturally from several partially closed reproductive basins than from one universal competitive field.

If so, some of the scalar memory terms in the single-basin model were compensating for missing topology.

Current graph-branch experiments add a third claim:

If basin topology is to do more than smooth the aggregate curve, tightening may need to operate by phased narrowing of admissible connectivity inside the basin, and perhaps by edge-specific collapse schedules rather than uniform graph switching.

## Discipline for the next pass

The next model must satisfy these conditions:

- the pre-window world must be broad enough that diversity is not immediately self-eroding
- the fragility threshold must represent real marginality, not the default starting condition
- initial heterogeneity must be mild, visible, and reported
- results must be judged over an ensemble, not by one dramatic run
- damage must remain an informative state variable rather than saturating trivially
- rebound versus persistence must be measured explicitly
- placement of hysteresis in the transfer function must be treated as a first-order modeling choice
- basin structure must earn its keep by improving local as well as aggregate timing
- local closure must be tested directly rather than smuggled in as vague extra pressure
- graph elaboration must now clear a much higher bar than earlier scalar refinements

Or, more bluntly:

Do not confuse initial variation with emergent structure.
Do not confuse amplification with creation.
Do not confuse one vivid run with a regime.
Do not confuse a decorative memory term with a real scar.
Do not confuse elegance of interpretation with behavioral adequacy.
Do not let topology become another excuse for post hoc curve matching.
