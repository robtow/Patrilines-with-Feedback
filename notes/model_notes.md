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

## Main results so far

- weak continuous filtering is sufficient for compression
- thresholded fragility produces clustered pruning
- leakage introduces competing flow
- leakage bias determines whether the channel diffuses or amplifies inequality
- signal alignment between formal and informal channels shifts long-run diversity monotonically
- bounded compression can now be made the dominant event rather than an afterthought
- hysteresis can be made nontrivial without saturating into nonsense

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

## What v0.9 now shows

The current thresholded damage law is the first hysteresis version that behaves like a real state variable rather than theatrical fog.

It no longer saturates to 1.0 in every run. Damage now varies modestly across runs and remains in a nontrivial interior range.

Current pattern:
- broad initial ecology remains healthy
- bounded compression is dominated by the forcing window
- survivor concentration remains strong
- initial-final correlation remains low
- damage now reduces some rebound without becoming a hidden mortality switch

But the result is still only partial scar, not yet durable post-window damage.

The current system produces:
- bounded compression
- concentrated survivors
- some hysteresis
- but still substantial post-window re-diffusion

So the machine now appears to know how to compress and leave a scar, but not yet how to stay seriously hurt.

## Working hypothesis

The strongest form of the current hypothesis is this:

A bounded interval of cultural tightening does not merely reduce diversity while active. It changes the transfer function by which male lines persist. As entropy falls, redundancy falls. As redundancy falls, fragility rises. Once the system is sufficiently compressed, the same perturbations become more dangerous, and mild initial variation is more easily converted into durable pruning and survivor concentration.

If a damage term is required, it should not deepen the fall by magic. It should reduce recoverability and make the compressed state harder to escape.

That is a much stronger claim than “war is unnecessary.”

## Discipline for the next pass

The next model must satisfy these conditions:

- the pre-window world must be broad enough that diversity is not immediately self-eroding
- the fragility threshold must represent real marginality, not the default starting condition
- initial heterogeneity must be mild, visible, and reported
- results must be judged over an ensemble, not by one dramatic run
- damage must remain an informative state variable rather than saturating trivially
- rebound versus persistence must be measured explicitly

Or, more bluntly:

Do not confuse initial variation with emergent structure.
Do not confuse amplification with creation.
Do not confuse one vivid run with a regime.
Do not confuse a decorative memory term with a real scar.
