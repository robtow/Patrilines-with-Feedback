# Empirical Observables

This note exists to stop me from comparing stories to stories.

The papers do not owe me agreement with my mechanism. What they do offer is a small set of visible observables. The model should be judged against those.

## Core principle

Do not compare:
- my causal story
- their causal story

Compare:
- model outputs
- paper-visible observables

If the machine cannot emit the same kinds of shapes the papers actually display, then the elegance of the mechanism is beside the point.

## Paper-facing target families

### 1. Karmin 2015: skyline / bounded-compression target

Karmin is the skyline paper.

What matters here is not merely that a male bottleneck happened. What matters is the visible shape in the cumulative Bayesian skyline plots and the explicit asymmetry between Y and mtDNA.

Visible targets from the paper:

- a second strong bottleneck in Y-chromosome lineages dating to the last 10 ky
- Y-based effective population size lower than mtDNA throughout, and much lower during the bottleneck interval
- a reduction in Y around roughly 8–4 kya in the global skyline discussion
- female effective size continuing upward where the male channel dips
- at the bottleneck, female Ne reported as up to 17-fold higher than male Ne

### 2. Poznik 2016: punctuated-burst target

Poznik is the burst paper.

What matters here is not merely low diversity. What matters is that a sparse set of lineages expands explosively, in multiple continental regions, with the branching pattern itself interpreted as rapid growth.

Visible targets from the paper:

- explosive male-lineage expansions in the last 15 ky
- these expansions occur in all five continental superpopulations sampled
- the expansions are drawn as discrete nodes, not as a smooth general recovery
- the paper models these as rapid phases followed by more moderate phases
- the circles in the figure encode minimum sons per generation, so the target is not just concentration but concentrated post-pruning fan-out

### 3. Wang 2013: starburst / top-3 target

Wang is the cleanest concrete regional starburst target.

Visible targets from the paper:

- three star-like expansions under O3-M324
- dates of approximately 5.4 kya, 6.5 kya, and 6.8 kya
- together these account for more than 40% of present Han Chinese patrilines
- the paper explicitly treats these as rapid expansions within a very short interval
- all Paleolithic divergences are described as binary, with the late-Neolithic starbursts standing out as a different topological regime

This gives a very hard target:
- top-3 survivor concentration can be historically meaningful, not merely a toy statistic

### 4. Zeng 2018: rival mechanism / structured-extinction target

Zeng is not primarily a target-figure paper for me; it is the nearest rival structural account.

Still, it provides empirical-shape expectations:

- Y bottleneck around 5000–7000 BP across Old World regions
- mitochondrial lineages remain comparatively stable or continue rising
- star-like Y expansions during the same broad period
- the mechanism they propose depends on structured patrilineal demes with female exogamy
- the paper explicitly states that many Y clades may have gone extinct during the bottleneck period, which would bias coalescent reconstructions toward an apparent bottleneck

This matters because it means:
- extinction of clades, not merely low male counts, is part of the target class
- some global shape may come from structured groups, not one universal bowl

## Model-facing proxy observables

The machine does not emit Bayesian skyline plots or real phylogenetic trees. Fine. Then it must emit proxies that are structurally comparable.

## A. Skyline proxy

This is the Karmin-facing observable family.

Use:
- entropy time series
- effective lineage count (`N_eff`)
- active lineage count

Derive:
- compression onset
- compression end
- compression duration
- fraction of total loss occurring inside the main compression interval
- steepest slope
- knee location / maximum curvature
- rebound fraction after the interval

Interpretation:
- Karmin-like success means bounded compression, not endless drift
- and rebound should be limited, not immediate return to baseline

## B. Survivor-burst proxy

This is the Poznik/Wang-facing observable family.

Use:
- final lineage size distribution
- post-pruning growth of surviving lines
- concentration among survivors

Derive:
- top-1 share
- top-3 share
- top-5 share
- survivor count
- rank-size steepness
- share captured by top survivors in the generations immediately after the main drop

Interpretation:
- Poznik-like success means a sparse set of winners fanning out
- Wang-like success means top-3 concentration can become very large in a historically recognizable way

## C. Sex-asymmetry target

The current model does not yet include an explicit female channel. That is a missing piece, not a reason to dodge the issue.

For now the empirical requirement must be written down explicitly:

- the eventual model should show bounded compression in the male channel without a comparable collapse in the female channel

Until that exists, any comparison to Karmin remains partial.

## D. Topology target

This is the single-basin versus Daisyworld comparison family.

Use:
- aggregate peak pruning time
- aggregate lag
- basin-specific peak pruning times
- basin-specific window losses
- aggregate rebound
- survivor concentration under topology

Interpretation:
- topology earns its keep only if it improves not merely aggregate smoothness but also local plausibility
- aggregate improvement by superposition alone is not enough

## Current scoreboard

### Karmin-facing

What the papers want:
- bounded Y compression in the last 10 ky
- strong male/female asymmetry
- limited rebound

What the model currently has:
- bounded compression, yes
- male/female asymmetry, not yet modeled directly
- rebound still too strong

### Poznik-facing

What the papers want:
- punctuated expansions of a sparse surviving set
- cross-regional or cross-basin plausibility
- concentrated post-pruning fan-out

What the model currently has:
- survivor concentration, yes
- bounded compression preceding concentration, yes
- punctuated multi-regime local timing, not yet convincing

### Wang-facing

What the papers want:
- top-3-like starburst behavior around the late Neolithic
- very high concentration of descent into a few star expansions

What the model currently has:
- the single-basin family can produce top-3-heavy outcomes
- Daisyworld weakens top-3 monopoly, which may be globally more honest but regionally less Wang-like

This is important:
- Wang is a regional strong-starburst target
- Daisyworld may fit global shape better while fitting Wang worse
- that is not necessarily contradiction; it may simply mean regional and aggregate targets differ

### Zeng-facing

What the paper wants:
- structured patrilineal demes
- extinction of Y clades rather than simple male-count collapse
- female exogamy preserving mitochondrial mixing

What the model currently has:
- single-basin family: structured extinction only in scalar form
- Daisyworld: first honest move toward structured basins
- local basin timing still too early

## Immediate ranking discipline

Every model family should now be judged on the same table.

Suggested rows:
- bounded compression present?
- fraction of loss inside window
- rebound after window
- peak pruning timing
- top-3 share
- top-5 share
- survivor count
- local-vs-global timing plausibility
- need for scalar damage
- explicit female asymmetry present?

Suggested columns:
- empirical target
- v0.9
- v0.12
- comment

## Current blunt conclusion

The repo is no longer allowed to say merely:
- “this looks suggestive”

It is now required to say:
- which observable family is being matched
- which is only partially matched
- and which is still missing entirely

At present:
- v0.9 is the best single-basin behavioral family
- v0.12 is the best architectural advance
- Karmin-like bounded compression is partially matched
- Poznik-like survivor bursts are partially matched
- Wang-like top-3 regional starburst is still more naturally approached in single-basin than in Daisyworld
- Zeng-like structured demes are only now beginning to be represented honestly
- female-channel comparison is still absent and must eventually be added rather than politely ignored
