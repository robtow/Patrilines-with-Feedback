# Model Notes

## Current control structure

Formal channel:
- skew
- fragility threshold
- multiplicative noise

Informal channel:
- leakage rate
- leakage mixture
- informal signal

## Main results so far

- weak continuous filtering is sufficient for compression
- thresholded fragility produces clustered pruning
- leakage introduces competing flow
- leakage bias determines whether the channel diffuses or amplifies inequality
- signal alignment between formal and informal channels shifts long-run diversity monotonically

## Current regimes

v0.6:
- random leakage -> diffusion
- mixed leakage -> equilibrium
- status-weighted leakage -> amplification

v0.7:
- corr 0.0 -> highest diversity
- corr 0.5 -> intermediate
- corr 1.0 -> strongest compression
