# Y-Chromosome Essay: Structure, Heuristics, and Procedure

## Purpose
This document defines the working structure and editorial procedure for the serious essay on Y-chromosome bottleneck modeling. It is intended as a crash-safe planning artifact and should be treated as the current working specification for future drafting.

## Core Identity of the Piece
This is not a puff piece, not a magazine summary, and not a detached academic paper. It is a serious hybrid document with three simultaneous functions:

1. **Personal narrative of discovery and iterative engineering**
2. **Technical exposition of model families, methods, observables, and code structure**
3. **Reproducible bridge to the GitHub repo, so a reader skilled in the art can replicate and extend the work**

The governing standard:

> The piece must read like a story told by an engineer who is also a writer, not like an essayist glancing at some code from across the room.

## Voice Calibration
The essay voice should be informed by:
- Voltaire
- John Boyd
- Norbert Wiener
- Darwin on the *Beagle*

This means:
- first-person investigative prose
- acerbic edge where warranted
- observational density
- sequentially motivated technical exposition
- explicit epistemic correction when a prior model turns out to be a useful lie
- structural and control-loop analysis over psychologizing
- no bland institutional prose
- no puffery

## Non-Negotiable Editorial Constraints
- Preserve the user's storytelling verbatim when already strong and load-bearing
- Preserve paragraph architecture; do not fragment into emphatic one-line paragraphs
- Do not replace vivid original phrasing with tidier paraphrase
- Interpolate new material rather than rewriting existing narrative voice
- Dense, reasoned paragraphs should remain the default unit
- Personal narrative is not decorative; it is part of the inquiry structure
- Technical detail must be sufficient that a reader can map essay claims onto repo structure and methods

## What the Essay Must Accomplish
A serious reader should finish the piece understanding:
- what the Y-chromosome bottleneck is and is not
- why the male-line / mtDNA asymmetry matters
- why massacre-first explanations are too blunt as exclusive accounts
- why the problem is properly framed as a control-system question
- what each model family was designed to test
- what each model family omitted
- what each family taught
- why the scalar models became insufficient
- why topology across and within basins matters
- why v0.20 currently leads
- what empirical observables the models are trying to match
- how the code and notes are organized
- how to reproduce and extend the results
- why the work does not “solve history”

## Current Comparative Standing to Preserve Explicitly
- **v0.9** = best single-basin behavioral family
- **v0.15** = best scalar/topological Daisyworld family
- **v0.20** = best nested-topology eligibility-graph family; first graph version to produce correct mean sustained basin ordering

## Project Conclusions to Preserve Explicitly
- weak coupled filtering can compress male-line diversity without requiring massacre-first explanations
- informal reproduction is not magic diffusion through the same space; it is partial traversal of edges the formal order is trying to narrow
- hysteresis placement matters
- single-basin mean field is a topological oversimplification
- topology across basins matters
- internal admissibility topology inside basins also matters
- edge-phased tightening outperforms one-shot and matrix-wide staged graph tightening
- overfitting risk is real, so complexity should now advance slowly and under explicit stopping rules

## Proposed Table of Contents
1. **Opening: Two nights ago, or two-dark-thirty**
   - Preserve the existing storytelling passage verbatim
   - Establish the asymmetry and the irritation with melodramatic public folklore

2. **What Actually Collapsed**
   - Distinguish male lineage collapse from male population collapse
   - Distinguish Y-lineage behavior from mtDNA behavior
   - Define the observational problem clearly

3. **Why the Standard Story Is Too Blunt**
   - Critique massacre-first / conquest-first exclusivity
   - Keep room for war without granting explanatory monopoly

4. **Why I Built a Model**
   - Preserve the existing “historical pageant / heroic moustaches” material
   - Introduce control-system framing
   - Explain culture as filtering machinery rather than commentary

5. **Model Family I: Weak Bias and Thresholded Fragility**
   - Inputs, state variables, update cycle
   - What this family demonstrates
   - What it still misses
   - Figure candidates: lineage count, entropy over time

6. **Informal Channel, Female Choice, and Signal Separation**
   - Formal vs informal reproduction
   - Leakage as secondary traversal
   - Aligned vs partially aligned vs independent signals
   - Figure candidates: outcome differences under varying alignment

7. **Punctuated Pruning and Hysteresis**
   - Why clustered losses matter
   - Where hysteresis enters
   - Why this changes the shape of the result

8. **The Spherical Cow Problem**
   - Methodological caution
   - Why single-basin mean field is a useful lie
   - Transition to topology

9. **Topology Matters: Basins, Admissibility, Eligibility Graphs**
   - Explain basin topology
   - Explain internal admissibility topology
   - Explain why informal reproduction is partial edge traversal, not smooth diffusion
   - Figure candidates: schematic scalar vs graph topology diagram

10. **Comparative Model Families: v0.9, v0.15, v0.20**
    - Why each family mattered
    - What each family gets right
    - What each family still misses
    - Preserve explicit comparative framing

11. **Why v0.20 Currently Leads**
    - Explain nested-topology eligibility graph
    - Explain correct mean sustained basin ordering
    - Explain why edge-phased tightening beats one-shot and matrix-wide staged tightening
    - Figure candidates: comparison plots across tightening modes

12. **Empirical Observables and Matching Criteria**
    - Explicitly state what is being matched
    - Clarify what counts as success and what does not
    - Tie to notes/empirical_observables.md

13. **Code Structure and Reproducibility**
    - Guided tour of repo structure
    - Which files matter and why
    - How figures are generated
    - How a reader can reproduce and extend the work
    - Include pseudocode-style exposition in prose

14. **Stopping Rules, Overfitting, and Why This Does Not Solve History**
    - Explicit stopping rules
    - Distinguish mechanism plausibility from historical proof
    - Reject oracle-style overclaiming

15. **Closing Return**
    - Return to the original irritation with noisy folklore
    - Reaffirm the value of runnable machinery over just-so stories

## Heuristics for Drafting
### Narrative Heuristics
- Keep the opening pressure and storytelling intact
- Let the personal narrative recur lightly as the thread of inquiry
- Use first person naturally, not performatively
- Let false starts and corrections appear where they educate the reader

### Technical Heuristics
- Every technical section should answer: what was modeled, why it was modeled, what it showed, what it failed to capture, and what forced the next model
- Use compact pseudocode-style prose to explain update cycles and control flow
- Name observables explicitly
- Tie claims to specific families and repo documents
- Keep family comparisons explicit rather than collapsing into a winner-only story

### Expository Heuristics
- Each section should contain claim, mechanism, and implication
- Avoid bloggy one-line emphasis paragraphs
- Use examples and figures to teach, not decorate
- When using scorn, attach it to a substantive analytic point
- Avoid jargon when plain engineering language will do

### Epistemic Heuristics
- State clearly when an earlier model was useful but structurally insufficient
- Treat correction as gain
- Separate mechanism class from historical identification
- Preserve overfitting caution throughout

## Figure Strategy
Figures should be integrated into argument, not appended as decoration.

Likely figure classes:
- entropy / lineage diversity trajectories
- clustered pruning / survivor expansion plots
- comparative plots for v0.9 vs v0.15 vs v0.20
- schematic of scalar basin vs nested eligibility graph
- edge-phased vs one-shot vs matrix-wide staged tightening comparisons
- possible repo/code architecture diagram if useful

For each figure in the final essay, include:
- what question the figure answers
- what the reader should notice
- what conclusion it supports
- where the generating code lives

## Procedure for Incremental Work
1. Finalize section architecture and editorial heuristics
2. Draft section-by-section rather than full-pass rewriting
3. Preserve existing strong prose verbatim where possible
4. Insert technical expansions only where needed
5. Add figure placeholders and captions during section drafting, not afterward
6. Add pseudocode-style explanation where model mechanics need clarity
7. Cross-check each drafted section against repo notes
8. Maintain explicit comparison framing across model families
9. Revisit overall flow only after core sections are drafted
10. Do final pass for voice consistency, compression of redundancy, and claim discipline

## Likely Source Notes to Use Explicitly
- notes/empirical_observables.md
- notes/v0_9_vs_v0_12_comparison.md
- notes/eligibility_graph_design.md
- notes/eligibility_graph_spec.md
- notes/staged_eligibility_graph_design.md
- notes/edge_phased_graph_design.md
- notes/v0_17_v0_20_graph_notes.md

## Immediate Next Task
Discuss and refine this structure, then begin with one section at a time rather than attempting another full essay pass.

## Second-Pass Integration Notes
- Re-examine earlier sections in a second pass for explicit model-version anchors where they improve reproducibility and comparison without cluttering the prose.
- Start this practice with Section 7, then revisit Sections 5 and 6 later if warranted.
- Add an illustration placeholder to Section 7 showing the effect of hysteresis on time-series shape, ideally comparing smoother thinning against more clustered, history-shaped loss.
- In the second pass over the full essay, check whether earlier sections also need figure placeholders or light version provenance markers.

