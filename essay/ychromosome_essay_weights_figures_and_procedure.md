# Y-Chromosome Essay: Weights, Figures, and Working Procedure

## Purpose
This document captures the current explicit working decisions about section weight, figure inventory, and drafting procedure for the Y-chromosome bottleneck essay. It is intended as a crash-safe planning guide so that future work proceeds incrementally and explicitly rather than through messy full rewrites.

## Working Principle
This is a serious essay, not a puff piece. It must function simultaneously as:
- a personal narrative of discovery and iterative engineering
- a technical exposition of models, observables, and methods
- a reproducible bridge to the GitHub repo, so a reader skilled in the art can replicate and extend the work

The governing standard remains:

> The piece must read like a story told by an engineer who is also a writer, not like an essayist glancing at some code from across the room.

## Section Weights
These are not rigid quotas, but explicit discipline against drift.

### 1. Opening: “Two nights ago, or two-dark-thirty”
**Target weight:** 8 to 10 percent  
Purpose: ignition point; vivid personal opening; establishes asymmetry and irritation with melodramatic public folklore; hands off quickly to the actual problem.

### 2. What Actually Collapsed
**Target weight:** 6 to 8 percent  
Purpose: distinguish male-lineage collapse from male-population collapse; distinguish Y-lineage behavior from mtDNA behavior; define the observational problem clearly.

### 3. Why the Standard Story Is Too Blunt
**Target weight:** 6 to 8 percent  
Purpose: critique massacre-first / conquest-first exclusivity without turning the essay into a polemic; keep room for war without granting explanatory monopoly.

### 4. Why I Built a Model
**Target weight:** 8 to 10 percent  
Purpose: explain why a control-system framing is more useful than event melodrama; justify runnable machinery over verbal fog.

### 5. Model Family I: Weak Bias and Thresholded Fragility
**Target weight:** 12 to 15 percent  
Purpose: teach the first machine, not just the conclusion; explain inputs, update logic, observables, what the model showed, and what it still did not capture.

### 6. Informal Channel, Female Choice, and Signal Separation
**Target weight:** 10 to 12 percent  
Purpose: explain formal versus informal reproduction, leakage as structured secondary traversal, and the role of alignment versus independence.

### 7. Punctuated Pruning and Hysteresis
**Target weight:** 6 to 8 percent  
Purpose: explain the change in behavioral shape once fragility and hysteresis enter; clarify clustered losses.

### 8. The Spherical Cow Problem
**Target weight:** 4 to 6 percent  
Purpose: short, sharp methodological hinge; explain why the early scalar models were useful lies.

### 9. Topology Matters: Basins, Admissibility, Eligibility Graphs
**Target weight:** 12 to 15 percent  
Purpose: teach the topological turn clearly; explain basin topology, internal admissibility topology, and constrained traversal.

### 10. Comparative Model Families: v0.9, v0.15, v0.20
**Target weight:** 8 to 10 percent  
Purpose: preserve explicit comparative framing; explain why each family mattered and what each still misses.

### 11. Why v0.20 Currently Leads
**Target weight:** 8 to 10 percent  
Purpose: explain why v0.20 is the leading nested-topology eligibility-graph family; clarify mean sustained basin ordering and edge-phased tightening.

### 12. Empirical Observables and Matching Criteria
**Target weight:** 6 to 8 percent  
Purpose: define what the models are being asked to match; distinguish success criteria from overclaim.

### 13. Code Structure and Reproducibility
**Target weight:** 8 to 10 percent  
Purpose: provide a guided bridge into the repo; explain where key files live, how figures are generated, and how skilled readers can reproduce and extend the work.

### 14. Stopping Rules, Overfitting, and Why This Does Not Solve History
**Target weight:** 5 to 7 percent  
Purpose: make caution part of the technical argument; distinguish mechanism plausibility from historical proof; keep complexity growth disciplined.

### 15. Closing Return
**Target weight:** 3 to 4 percent  
Purpose: brief return to the original irritation with noisy folklore; reaffirm the value of runnable machinery over just-so stories.

## Preliminary Figure Inventory
This is the current first-pass figure plan. Titles may change later, but figure roles should remain explicit.

### Figure 1: Early scalar-model diversity compression
**Purpose:** show that weak filtering can compress male-line diversity without requiring massacre-first assumptions.  
**Reader should notice:** strong effect from low-gain repeated filtering.  
**Likely source:** earliest scalar family output.

### Figure 2: Thresholded fragility / clustered pruning
**Purpose:** show transition from smooth thinning to clustered losses.  
**Reader should notice:** how punctuated pruning emerges once fragility and hysteresis enter.  
**Likely source:** threshold-enabled runs.

### Figure 3: Formal vs informal channel / signal alignment effects
**Purpose:** show how aligned versus partially independent informal channels change outcomes.  
**Reader should notice:** leakage is not just “noise”; its structure matters.  
**Likely source:** signal-separation runs.

### Figure 4: Scalar basin versus structured admissibility graph
**Purpose:** teach the topological turn conceptually.  
**Reader should notice:** the difference between smooth-space intuition and constrained traversal.  
**Likely source:** probably a schematic, not a raw output plot.

### Figure 5: Comparative family behavior, v0.9 vs v0.15 vs v0.20
**Purpose:** preserve explicit comparative framing across families.  
**Reader should notice:** each family captures something, but v0.20 currently leads on structured ordering.  
**Likely source:** comparative summary outputs and notes.

### Figure 6: Tightening regimes comparison
**Purpose:** compare one-shot, matrix-wide staged, and edge-phased tightening.  
**Reader should notice:** edge-phased tightening behaves better in the relevant sense.  
**Likely source:** graph-family runs.

### Figure 7: Code/update-cycle or repo architecture diagram
**Purpose:** help a skilled reader replicate and extend the work.  
**Reader should notice:** how the parts fit together and where to intervene.  
**Likely source:** likely hand-constructed or generated from repo structure.

## Planned Pseudocode-Style Exposition Blocks
The essay should include at least three explicit pseudocode-style method expositions in prose or compact step form.

### Block A: Early scalar update cycle
Should explain:
- initialize lineage state
- apply formal bias
- check viability threshold
- update survival / reproduction
- compute diversity metrics

### Block B: Formal/informal split
Should explain:
- formal reproduction via lineage/status signal
- informal reproduction via secondary signal
- combined lineage outcomes
- updated diversity and occupancy metrics

### Block C: Graph model with phased tightening
Should explain:
- represent admissible relations as edges
- apply phased narrowing
- allow partial traversal through informal channel
- update basin occupancy and sustained-order metrics

## Preservation vs Fresh-Writing Map
### Mostly preservation plus light interpolation
- Opening
- Why I Built a Model
- some early “culture causes the compression” material

### Mostly fresh writing in the user's established voice
- What Actually Collapsed
- Empirical Observables and Matching Criteria
- The Spherical Cow Problem
- Topology Matters
- Why v0.20 Currently Leads
- Code Structure and Reproducibility
- Stopping Rules, Overfitting, and Why This Does Not Solve History

### Mixed
- Why the Standard Story Is Too Blunt
- Informal Channel, Female Choice, and Signal Separation
- Punctuated Pruning and Hysteresis
- Comparative Model Families

## Incremental Working Procedure
1. Finalize and save planning docs before major drafting
2. Work section-by-section rather than by whole-essay rewrites
3. Preserve existing strong prose verbatim where it is already load-bearing
4. Interpolate new material rather than rewriting narrative voice
5. Insert figure placeholders and provisional captions during section drafting, not after
6. Add pseudocode-style exposition where model mechanics require clarity
7. Cross-check each drafted section against repo notes and code structure
8. Maintain explicit model-family comparison framing
9. Revisit global flow only after core sections exist
10. Do final pass for voice consistency, redundancy compression, and claim discipline

## Immediate Next Drafting Target
The first bounded drafting target should be:

## Section 2: What Actually Collapsed

This section should do four things:
1. distinguish male population collapse from male lineage collapse
2. distinguish Y-chromosome lineage compression from mtDNA behavior
3. explain why this asymmetry is what makes the phenomenon interesting and nontrivial
4. state the observational problem in a form that a model can target, rather than leaving it as journalistic folklore

The last paragraph of Section 2 should hand off naturally into Section 3, where the inadequacy of massacre-first exclusivity becomes more obvious.

## Rationale for Incremental Explicitness
The purpose of this planning discipline is to avoid sloppy recovery after crashes, context loss, or over-large rewrites. The essay should accumulate deliberately, with structure and method made explicit as we go.
