# Patrilines with Feedback

A small exploratory model accompanying the essay:

*Patrilines with Feedback; or, A Short Inquiry into the Y-Chromosome Bottleneck, Considered as a Control System.*

## Purpose

This repository explores whether the observed reduction in Y-chromosome lineage diversity can arise from the steady operation of coupled reproductive filters, rather than requiring large-scale episodic events such as warfare.

The aim is structural demonstration, not historical reconstruction.

More specifically, the project asks whether bounded intervals of tighter cultural and institutional filtering can compress male-line diversity, whether that compression can alter later system behavior by reducing recoverability, and whether some of the observed global shape is better understood as the aggregate behavior of several partially coupled social basins rather than one universal competitive field.

## Current model families

The project now includes three architectural families.

### 1. Single-basin family

This is the original mean-field line of work. It includes:

- a population divided into lineages
- generational reproduction via multinomial sampling
- a controllable skew parameter
- multiplicative lineage-specific noise
- thresholded fragility as lineage size falls
- a leakage channel (EPP):
  - fraction of births reassigned biologically
  - mixture of:
    - random diffusion
    - status-weighted reproduction
- a dual-signal structure:
  - a formal signal governing institutional reproduction
  - an informal signal governing leakage / EPP
  - tunable correlation between the two
- a bounded compression window
- mild heterogeneous initial lineage sizes
- initial-position hygiene:
  - lower / middle / upper initial terciles
  - later survival and share tracked by starting position
- a thresholded damage / hysteresis term:
  - interpreted as reduced recoverability under exceptional compression
  - not hidden mortality
  - not generic “badness”

### 2. Scalar/topological Daisyworld family

This is the first topological step beyond the single-basin oversimplification.

It includes:

- three partially coupled social basins
- local lineage dynamics within each basin
- staggered local compression windows
- weak symmetric cross-basin coupling
- basin slack asymmetry
- window-driven local closure
- window-gated local marginality / fragility gain
- global observables computed from aggregate lineage counts across basins
- local basin observables retained for comparison

This is not geography in the map-room sense. A basin here is a partially bounded reproductive field. It may be regional, ritual, status-based, linguistic, or otherwise social.

### 3. Nested-topology eligibility-graph family

This is the first explicit attempt to represent culture as changed connectivity rather than as a mere pressure scalar.

It includes:

- three basins
- three fixed internal eligibility classes per basin
- class-based admissibility graphs inside each basin
- distinct formal and informal traversal of those graphs
- staged, and now edge-phased, internal tightening of the graph during the window
- the same broad basin framework used in Daisyworld, but with internal topology rather than scalar closure alone doing more of the work

This branch is now a real mechanism family, not decorative machinery. It remains provisional and only partially successful in the larger historical sense.

## Tracked quantities

Across current versions, tracked quantities include:

- Shannon entropy
- effective number of lineages (`e^H`)
- active lineage count
- pruning derivatives
- pre-window / window / post-window entropy loss
- peak pruning generation
- pruning lag relative to window midpoint
- survivor concentration:
  - top-1 share
  - top-3 share
  - top-5 share
- initial / final correlation
- initial and final Gini
- survival rate by initial tercile
- final share by initial tercile
- damage statistics

In the multi-basin families, additional basin-level quantities include:

- basin-specific effective lineages
- basin-specific active lineage counts
- basin-specific damage
- basin-specific peak pruning times
- basin-specific rolling main-pruning times
- basin-specific window losses
- mean basin self-retention / closure

## What the model now shows

### 1. Continuous filtering is sufficient for compression

Even weak skew produces sustained lineage compression.

### 2. Thresholded fragility produces clustered pruning

Lineages can linger near viability, then decline accelerates, producing uneven pruning rather than a perfectly smooth fade.

### 3. Leakage introduces a competing flow

The system is no longer purely compressive; diversity can be partially replenished.

### 4. Leakage bias matters

Three regimes emerged in earlier versions:

- **random leakage**
  - weak lineages receive inflow
  - collapse is softened
  - diversity is better preserved

- **mixed leakage**
  - diffusion and amplification compete
  - the system settles into an intermediate regime

- **status-weighted leakage**
  - informal reproduction reinforces dominant lineages
  - collapse accelerates
  - diversity declines more rapidly

### 5. Signal alignment matters even when leakage mixture is held fixed

With leakage rate and mixture held constant:

- **independent informal signal (`corr = 0.0`)**
  - preserves the highest entropy
  - preserves the highest effective lineage count
  - stabilizes the largest number of active lineages

- **partial alignment (`corr = 0.5`)**
  - yields an intermediate steady state
  - reduces diversity relative to the independent case

- **full alignment (`corr = 1.0`)**
  - produces the strongest compression
  - yields the lowest long-run diversity of the three

The decisive variable is therefore not leakage alone, but whether the informal channel samples the same signal as the formal system.

### 6. Bounded compression can be made the dominant event

Later versions moved beyond simple continuous thinning and asked whether a bounded interval of tighter institutional filtering could become the main compression event.

With healthier initialization and milder baseline fragility, the model now produces runs in which the bounded window, rather than generation-zero pathology, does most of the work.

### 7. Initial-condition hygiene matters

Earlier versions exposed a failure mode in which the system began life already too close to the fragility threshold. That produced misleading early collapse.

This was corrected by:
- broader initial ecology
- mild heterogeneous starts
- explicit tracking of whether later inequality is merely inherited from the initial draw

The result is a cleaner distinction between ordinary variation and later structural amplification.

### 8. Hysteresis is plausible, but where it enters matters

The thresholded damage law is the first hysteresis version that behaves like a real state variable rather than theatrical fog.

It is interpreted as reduced recoverability under exceptional compression:
- accumulated rigidity
- reduced re-diffusion
- slower reopening of lineage opportunity

But experiments also showed something sharper:

- `v0.9`, where damage acts directly on persistence / fragility in a controlled way, gives the best current single-basin behavioral result
- `v0.10`, where damage acts only by suppressing diffusive recovery in the informal channel, is conceptually cleaner but behaviorally too weak
- `v0.11`, a restrained hybrid, improves on `v0.10` but does not beat `v0.9`

So the present unpleasant lesson is this:

> A cleaner recovery-channel-only interpretation of hysteresis is not strong enough at current scale. The best current single-basin match requires damage to affect persistence more directly.

That is uglier than the more elegant story, and likely closer to history.

### 9. Topology matters

The multi-basin Daisyworld model is the first clear demonstration that the single-basin world was topologically too polite.

Compared with the best single-basin family, Daisyworld:

- improves the **global** bounded-compression shape
- weakens survivor monopoly
- preserves more lineages overall
- suggests that some of what looked like scalar scar in the single-basin model was really missing topology

The aggregate result is cleaner:
- pre-window loss is lower
- window loss dominates more naturally
- global pruning timing improves materially

### 10. Scalar Daisyworld local timing is hard

Scalar Daisyworld was pushed through several disciplined tests:

- a harsher local sustained-pruning metric based on rolling decline
- a basin slack gradient
- window-driven local closure
- window-gated local marginality / fragility gain
- basin-specific baseline fragility buffering

These produced a sequence of useful failures and partial improvements.

Current lesson:
- the local-timing problem was not mainly a metric artifact
- simple basin slack was not enough
- window-driven closure helped
- window-gated marginality helped more
- the sustained local pruning metric began to separate somewhat
- but the late basin still eroded too early

So the best scalar Daisyworld reading became:

> local closure and local marginality both matter, but the later basin still lacks enough pre-window buffering.

That was a real result, but not a full solution.

### 10a. Eligibility graphs appear to be a real structural family

The next structural move after scalar closure was to give each basin a tiny internal eligibility graph.

This was the first explicit attempt to represent culture as changed connectivity rather than as mere pressure.

The sequence now looks like this:

- `v0.17` showed that an eligibility graph can matter a great deal, but the first baseline graph was too restrictive and front-loaded collapse
- `v0.18` made the baseline graph genuinely open and restored bounded compression as the main event
- `v0.19` staged tightening inside the graph and improved sustained local timing relative to a one-shot graph switch
- `v0.20` phased the tightening of different edge families and is the first graph version to produce the correct **mean sustained basin ordering**

This is a real structural gain.

The graph branch now supports the claim that:

> tightening inside a basin is better represented as phased narrowing of admissible connectivity than as a single scalar increase in harshness.

But this remains only a partial success:
- local staggering is now stronger, but not beyond dispute
- rebound remains too easy in absolute terms
- the graph branch produces a relatively sharp sparse-winner regime

### 11. Current honest result

The current honest claim is:

- bounded compression is real
- the compression window does most of the work
- survivor concentration remains strong
- mild initial variation does not simply dictate the ending
- partial hysteresis is plausible
- topology clearly matters
- the graph branch now demonstrates that phased collapse of internal bridges can improve local timing
- but durable post-window lock-in has not yet been demonstrated
- and no branch yet licenses triumphant historical overclaim

So the current claim is bounded compression plus partial scar, with strong evidence that missing topology was part of the earlier problem, and now stronger evidence that the topology inside a basin may itself be layered and sequential rather than uniform.

## Interpretation

The system now has several interacting dynamical layers:

- mean-field filtering -> global compression
- thresholded fragility -> local positive feedback and clustered collapse
- leakage -> cross-lineage transport
- signal alignment -> determines whether informal reproduction diffuses or reinforces formal inequality
- bounded institutional tightening -> finite interval of stronger compression
- initial-position amplification -> tests whether ordinary variation hardens into lineage fate
- thresholded damage / hysteresis -> reduced recoverability after exceptional compression
- basin structure -> partially closed reproductive fields with weak coupling
- window-driven closure -> temporary increase in local self-retention
- window-gated marginality -> local tightening makes near-edge lineages more vulnerable
- eligibility graphs -> phased narrowing of admissible connectivity inside a basin
- edge-phased tightening -> different internal bridges collapse on different schedules

The key result so far is this:

> The long-run behavior of lineage diversity depends not only on formal reproductive constraints, but on the structure of informal reproduction, the alignment between formal and informal signals, whether a bounded interval of tightening pushes the system into a state from which breadth is harder to recover, and whether lineages inhabit one universal bowl or several partially closed basins.

More sharply:

> Some of the empirical global bounded-compression shape may indeed be an aggregate effect of coupled basins rather than one synchronized universal regime shift.

And more sharply still:

> The graph branch suggests that the remaining missing structure was not additional scalar force, but timed collapse of different admissible routes inside nested local topologies.

That is now a live modeling conclusion, not rhetorical embroidery.

## Note on “damage”

If a damage term appears in the model, it does **not** mean hidden death, generic badness, or melodramatic injury.

It is a compressed state variable for reduced recoverability after exceptional compression.

The sharpest reading remains cultural overfitting:

- the system becomes better at preserving its current hierarchy
- and worse at regenerating breadth once breadth has been lost

But the experiments now suggest that this overfitting is not expressed only through weaker re-diffusion. It also appears to make marginality itself stickier.

That is a stronger and uglier result, and sounds more like history.

At the same time, Daisyworld shows that some of what had been loaded onto “damage” in the single-basin model was really missing topology in disguise.

## Current status

Exploratory model with working dynamics.

Version sketch:

- `v0.3` - mean-field + noise, smooth compression
- `v0.4` - threshold, uneven collapse
- `v0.5` - shaped fragility, clustered pruning
- `v0.6` - leakage / EPP introduces competing flow and three regimes
- `v0.7` - dual-signal model shows that signal alignment systematically shifts long-run diversity
- `v0.8` - bounded compression introduced; exposed brittle initialization pathology
- `v0.8b` - healthier initial ecology, mild heterogeneity, amplification hygiene
- `v0.9` - thresholded hysteresis / damage term interpreted as reduced recoverability under exceptional compression; best current single-basin behavioral result
- `v0.10` - damage moved to recovery-channel suppression only; cleaner interpretation, weaker payoff
- `v0.11` - restrained hybrid; informative, but still not superior to `v0.9`
- `v0.12` - three-basin Daisyworld; global shape improves, survivor monopoly weakens, local basin timing still too early
- `v0.13` - local sustained-pruning metric plus basin-slack gradient; shows local timing problem is real and slack alone is insufficient
- `v0.14` - window-driven local closure; first honest hint of local timing separation
- `v0.15` - window-gated local fragility gain; partial sustained local separation, but late basin still erodes too early
- `v0.16` - basin-specific baseline fragility buffering; improves coarse local staggering but not sustained late-basin delay
- `v0.17` - first eligibility-graph Daisyworld; graph proved potent, but baseline was too restrictive and front-loaded collapse
- `v0.18` - softened open eligibility graph; rehabilitated the graph branch by restoring bounded-window dominance
- `v0.19` - staged eligibility graph; phased internal tightening improves sustained local timing relative to one-shot graph switching
- `v0.20` - edge-phased eligibility graph; first graph version to produce correct mean sustained basin ordering

The current model demonstrates:

- punctuated-looking lineage compression can emerge from internal dynamics
- bounded compression can dominate the trajectory
- survivor concentration can remain strong
- mild initial variation need not simply dictate the ending
- partial hysteresis is plausible
- where hysteresis enters the system matters more than the mere existence of hysteresis
- topology matters more than the single-basin toy allowed
- admissibility structure is a real mechanism family
- staged internal tightening outperforms one-shot graph tightening
- edge-phased graph tightening outperforms matrix-wide staged tightening on local ordering

The current model does **not yet** demonstrate:
- strong post-window pruning lag
- durable post-window lock-in
- irreversible loss of recoverability
- a final settled winner among the scalar Daisyworld and graph branches
- anything like “solving history,” which would be preposterous

## Current best model families

At present:

- **best single-basin family:** `v0.9`
- **best scalar/topological Daisyworld family:** `v0.15`
- **best nested-topology graph family:** `v0.20`

So the repo is currently licensed to say three things at once:

> Thresholded hysteresis acting on persistence gives the best current single-basin match to bounded compression plus partial scar.

> Multi-basin Daisyworld suggests that some of the global empirical shape may arise more naturally from coupled local basins than from one universal competitive field.

> The edge-phased eligibility-graph branch suggests that tightening may work by phased narrowing of admissible connectivity inside those basins rather than by scalar pressure alone.

Those are compatible claims.

## Current next step

The next serious question is no longer merely whether hysteresis exists. It does, weakly.

The next question is whether the best future model should:
- remain in the `v0.9` family and refine direct persistence effects,
- retain `v0.15` as the best scalar/topological multi-basin family,
- or treat `v0.20` as the leading structural branch for essay revision and future comparative work.

More sharply:

> Has the graph branch now earned a temporary stopping point, where documentation and essay synthesis should advance faster than additional mechanism growth?

That is the current frontier.

## Structure

- `model/` - simulation code
- `notes/` - working notes and logs
- `papers/` - reference PDFs
- `figures/` - generated plots

## Figures

Figures are generated from simulation code. Selected figures (`sim_*.png`) are versioned when they correspond to specific model states and comparison points.
