# Patrilines with Feedback

A small exploratory model accompanying the essay:

*Patrilines with Feedback; or, A Short Inquiry into the Y-Chromosome Bottleneck, Considered as a Control System.*

## Purpose

This repository explores whether the observed reduction in Y-chromosome lineage diversity can arise from the steady operation of coupled reproductive filters, rather than requiring large-scale episodic events such as warfare.

The aim is structural demonstration, not historical reconstruction.

More specifically, the project asks whether bounded intervals of tighter cultural and institutional filtering can compress male-line diversity, and whether that compression can alter later system behavior by reducing recoverability.

---

## Current Model

The simulation now includes:

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
- a bounded compression window:
  - interpreted as a bounded interval of tighter memetic / institutional coherence
- mild heterogeneous initial lineage sizes:
  - broad initial ecology
  - visible but not yet fate-like variation
- initial-position hygiene:
  - lineages grouped by lower / middle / upper initial terciles
  - later survival and share tracked by starting position
- a thresholded damage / hysteresis term:
  - interpreted as reduced recoverability under exceptional compression
  - not hidden mortality
  - not generic “badness”

Tracked quantities include:

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

This has now been corrected by:
- broader initial ecology
- mild heterogeneous starts
- explicit tracking of whether later inequality is merely inherited from the initial draw

The result is a cleaner distinction between ordinary variation and later structural amplification.

### 8. Hysteresis is plausible, but currently partial

The current thresholded damage law is the first hysteresis version that behaves like a real state variable rather than theatrical fog.

It is interpreted as reduced recoverability under exceptional compression:
- accumulated rigidity
- reduced re-diffusion
- slower reopening of lineage opportunity

Current result:
- bounded compression is real
- survivor concentration remains strong
- some rebound is reduced
- but durable post-window lock-in has **not** yet been demonstrated

So the current honest claim is **partial scar**, not grand irreversible ruin.

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

The key result so far is this:

> The long-run behavior of lineage diversity depends not only on formal reproductive constraints, but on the structure of informal reproduction, the alignment between formal and informal signals, and whether a bounded interval of tightening pushes the system into a state from which breadth is harder to recover.

More sharply:

> Informal reproduction is not inherently egalitarian. If it follows the same signal as formal reproduction, it amplifies inequality. If it is sufficiently uncorrelated, it stabilizes diversity.

And more sharply still:

> Bounded compression can be made the dominant event. The harder question is whether compressed systems merely rebound afterward, or whether they become overfit to their own reduced diversity and therefore harder to reopen.

That last question remains live.

---

## Note on “damage”

If a damage term appears in the model, it does **not** mean hidden death, generic badness, or melodramatic injury.

It is a compressed state variable for reduced recoverability after exceptional compression.

The sharpest current reading is cultural overfitting:

- the system becomes better at preserving its current hierarchy
- and worse at regenerating breadth once breadth has been lost

That is the only interpretation under which the term is worth keeping.

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
- `v0.9` — thresholded hysteresis / damage term interpreted as reduced recoverability under exceptional compression

The current model demonstrates:

- punctuated-looking lineage compression can emerge from internal dynamics
- bounded compression can dominate the trajectory
- survivor concentration can remain strong
- mild initial variation need not simply dictate the ending
- partial hysteresis is plausible

The current model does **not yet** demonstrate:
- strong post-window pruning lag
- durable post-window lock-in
- irreversible loss of recoverability

So the present claim is bounded compression plus partial scar, not final proof of deep hysteretic trapping.

---

## Current next step

The next serious question is not whether compression can occur. It can.

The next question is whether the memory term should act less like extra fragility and more like impaired recovery or reduced re-diffusion after compression.

In other words:
- does reduced diversity merely concentrate survivors,
- or does it alter the derivative of recovery itself?

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
