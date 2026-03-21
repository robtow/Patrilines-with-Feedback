# Project Log

## 2026-03-20

Initialized repository.

Collected core papers:
- Karmin 2015
- Zeng 2018
- Poznik 2016
- Wang 2013

Initial hypothesis:

Y-lineage reduction as outcome of coupled reproductive filters
rather than purely episodic clan warfare.

Next step:
- read Karmin carefully
- extract simple dataset
- build minimal simulation

## 2026-03-20 (model v0.3)

Implemented:
- skewed reproduction
- stochastic lineage-level noise

Results:
- weak skew sufficient for long-term diversity reduction
- no need for explicit catastrophic events
- trajectories vary but remain largely smooth

Conclusion:
- current model is mean-field + noise
- punctuated collapse not yet present

Next:
- introduce viability threshold
- test for punctuated pruning behavior


## 2026-03-20 (model v0.5)

Implemented:
- shaped fragility (state-dependent threshold)
- fragility increases as lineage size falls

Result:
- clear shift from smooth decay to uneven, clustered pruning
- lineages linger near threshold, then collapse more rapidly
- timing of collapse varies across runs

Interpretation:
- threshold introduces local positive feedback
- produces heterogeneous collapse timing
- explains appearance of punctuated demographic events without external shocks

Next:
- introduce leakage across lineages (EPP / reassignment)
- examine interaction between leakage and fragility

## 2026-03-20 (model v0.6)

Implemented:
- EPP / leakage channel
- mixture of random and status-weighted reproduction

Parameters:
- EPP_RATE
- EPP_STATUS_WEIGHT

Experiments:

Case A (random leakage):
- collapse arrested
- system stabilizes at moderate diversity (~40–45 lineages)

Case B (mixed leakage):
- intermediate steady state (~20–30 lineages)
- balance between diffusion and amplification

Case C (status-weighted leakage):
- collapse accelerates
- trajectories converge toward low lineage counts

Result:

- leakage introduces a competing flow into the system
- behavior depends strongly on bias of leakage channel
- system exhibits three distinct regimes:
  diffusion, equilibrium, amplification

Interpretation:

- informal reproduction is not inherently stabilizing
- if aligned with status, it reinforces inequality
- if uncorrelated, it preserves diversity

Next:

- decouple informal selection signal from formal lineage size
- explore dual-signal dynamics

## 2026-03-20 (model v0.7)

Implemented:
- dual-signal model
- separate informal signal for leakage / EPP
- tunable correlation between formal lineage success and informal selection

Parameters:
- SIGNAL_CORRELATION
- EPP_RATE
- EPP_STATUS_WEIGHT

Experiments:

Case A (corr = 0.0; informal signal independent):
- highest entropy of the three runs
- highest effective lineage count
- active lineages stabilize at the highest level
- leakage acts most diffusively

Case B (corr = 0.5; partial alignment):
- intermediate steady state
- diversity lower than in the independent case
- leakage remains partly diffusive, partly reinforcing

Case C (corr = 1.0; full alignment):
- strongest compression of the three runs
- lowest long-run active-lineage count
- informal channel reinforces formal inequality most strongly

Result:

- signal alignment shifts the long-run regime cleanly
- with leakage mixture held fixed, increasing alignment monotonically reduces diversity
- the decisive variable is not leakage alone, but whether the informal channel samples the same signal as the formal system

Interpretation:

- the system behaves as a multi-controller structure
- formal reproduction allocates lineage success through one signal
- informal reproduction redistributes success through another
- when the two signals align, concentration increases
- when they diverge, diversity is preserved more strongly

Next:

- test anti-correlated informal signal
- consider persistence or drift in the informal signal across generations
- update essay draft to incorporate v0.7 results
