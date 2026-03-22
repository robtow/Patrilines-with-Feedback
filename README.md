# Patrilines with Feedback

A small exploratory model accompanying the essay:

*Patrilines with Feedback; or, A Short Inquiry into the Y-Chromosome Bottleneck, Considered as a Control System.*

## Purpose

This repository explores whether the observed reduction in Y-chromosome lineage diversity can arise from the steady operation of coupled reproductive filters, rather than requiring large-scale episodic events such as warfare.

The aim is structural demonstration, not historical reconstruction.

More specifically, the project asks whether bounded intervals of tighter cultural and institutional filtering can compress male-line diversity, whether that compression can alter later system behavior by reducing recoverability, and whether some of the observed global shape is better understood as the aggregate behavior of several partially coupled social basins rather than one universal competitive field.

---

## Current Model Families

The project now includes two architectural families.

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

### 2. Multi-basin Daisyworld family

This is the first topological step beyond the single-basin oversimplification.

It includes:

- three partially coupled social basins
- local lineage dynamics within each basin
- staggered local compression windows
- weak symmetric cross-basin coupling
- global observables computed from aggregate lineage counts across basins
- local basin observables retained for comparison

This is not geography in the map-room sense. A basin here is a partially bounded reproductive field. It may be regional, ritual, status-based, linguistic, or otherwise social.

---

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

In the Daisyworld family, additional basin-level quantities include:

- basin-specific effective lineages
- basin-specific active lineage counts
- basin-specific damage
- basin-specific peak pruning times
- basin-specific rolling main-pruning times
- basin-specific window losses

---

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

> A cleaner “recovery-channel only” interpretation of hysteresis is not strong enough at current scale. The best current single-basin match requires damage to affect persistence more directly.

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

### 10. Daisyworld local timing is still wrong

Current Daisyworld has now been pushed through two further tests:

- a harsher **local sustained-pruning metric** based on rolling decline
- a simple **basin slack gradient** via different basin population sizes

Both were useful failures.

They showed:
- the local-timing problem is not mainly a measurement artifact
- a simple local-slack gradient is not enough
- basin pruning still occurs too early relative to local windows
- aggregate improvement is still coming more from superposition than from cleanly staggered local regime shifts

That is a real result.

The likely missing ingredient is now clearer:

> the local window must alter not just selective pressure, but basin closure itself.

In other words, institutional tightening probably needs to make the local reproductive field more closed, not merely more skewed.

### 11. Current honest result

The current honest claim is:

- bounded compression is real
- the compression window does most of the work
- survivor concentration remains strong
- mild initial variation does not simply dictate the ending
- partial hysteresis is plausible
- topology clearly matters
- but durable post-window lock-in has not yet been demonstrated
- and Daisyworld local timing remains wrong

So the current claim is bounded compression plus partial scar, with strong evidence that missing topology was part of the earlier problem, but with local basin closure still under-modeled.

---

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

The key result so far is this:

> The long-run behavior of lineage diversity depends not only on formal reproductive constraints, but on the structure of informal reproduction, the alignment between formal and informal signals, whether a bounded interval of tightening pushes the system into a state from which breadth is harder to recover, and whether lineages inhabit one universal bowl or several partially closed basins.

More sharply:

> Some of the empirical global bounded-compression shape may indeed be an aggregate effect of coupled basins rather than one synchronized universal regime shift.

And more sharply still:

> The next missing thing in Daisyworld is not more basin breadth difference, but window-driven local closure.

That is now a live modeling conclusion, not rhetorical embroidery.

---

## Note on “damage”

If a damage term appears in the model, it does **not** mean hidden death, generic badness, or melodramatic injury.

It is a compressed state variable for reduced recoverability after exceptional compression.

The sharpest reading remains cultural overfitting:

- the system becomes better at preserving its current hierarchy
- and worse at regenerating breadth once breadth has been lost

But the experiments now suggest that this overfitting is not expressed only through weaker re-diffusion. It also appears to make marginality itself stickier.

That is a stronger and uglier result, and sounds more like history.

At the same time, Daisyworld shows that some of what had been loaded onto “damage” in the single-basin model was really missing topology in disguise.

---

## Current status

Exploratory model with working dynamics.

Version sketch:

- `v0.3` — mean-field + noise, smooth compression
- `v0.4` — threshold, uneven collapse
- `v0.5` — shaped fragility, clustered pruning
- `v0.6` — leakage / EPP introduces competing flow and three regimes
- `v0.7` — dual-signal model shows that signal alignment systematically shifts long-run diversity
- `v0.8` — bounded compression introduced; exposed brittle initialization pathology
- `v0.8b` — healthier initial ecology, mild heterogeneity, amplification hygiene
- `v0.9` — thresholded hysteresis / damage term interpreted as reduced recoverability under exceptional compression; best current single-basin behavioral result
- `v0.10` — damage moved to recovery-channel suppression only; cleaner interpretation, weaker payoff
- `v0.11` — restrained hybrid; informative, but still not superior to `v0.9`
- `v0.12` — three-basin Daisyworld; global shape improves, survivor monopoly weakens, local basin timing still too early
- `v0.13` — local sustained-pruning metric plus basin-slack gradient; shows local timing problem is real and slack alone is insufficient

The current model demonstrates:

- punctuated-looking lineage compression can emerge from internal dynamics
- bounded compression can dominate the trajectory
- survivor concentration can remain strong
- mild initial variation need not simply dictate the ending
- partial hysteresis is plausible
- where hysteresis enters the system matters more than the mere existence of hysteresis
- topology matters more than the single-basin toy allowed
- Daisyworld local timing failure is real, not just a metric artifact

The current model does **not yet** demonstrate:
- strong post-window pruning lag
- durable post-window lock-in
- irreversible loss of recoverability
- clean local staggering of basin pruning relative to local windows
- window-driven basin closure

---

## Current best model families

At present:

- **best single-basin family:** `v0.9`
- **best architectural advance:** `v0.12` / `v0.13` Daisyworld family

So the repo is currently licensed to say two things at once:

> Thresholded hysteresis acting on persistence gives the best current single-basin match to bounded compression plus partial scar.

and

> Multi-basin Daisyworld suggests that some of the global empirical shape may arise more naturally from coupled local basins than from one universal competitive field.

Those are compatible claims.

---

## Current next step

The next serious question is no longer merely whether hysteresis exists. It does, weakly.

The next question is whether the best future model should:
- remain in the `v0.9` family and refine direct persistence effects,
- refine Daisyworld so that local basin timing becomes credible,
- or combine the two without turning the model into soup.

More sharply:

> Can a basin’s tightening window alter local closure, not merely local skew, in a way that makes local pruning line up with local timing rather than merely improving the aggregate curve by superposition?

That is the current frontier.

---

## Structure

- `model/` — simulation code
- `notes/` — working notes and logs
- `papers/` — reference PDFs
- `figures/` — generated plots

---

## Figures

Figures are generated from simulation code. Selected figures (`sim_*.png`) are versioned when they correspond to specific model states and comparison points.
