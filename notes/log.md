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


