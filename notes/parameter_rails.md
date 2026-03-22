# Parameter Rails

This machine is not fitted to hidden Bronze Age constants, because history does not hand out such gifts. What it does offer, if one resists the usual academic incense, is a set of rails. Those rails are enough to keep the model from drifting into decorative nonsense.

## Leakage / EPP

The leakage channel should be treated as low but persistent, not as operatic scandal. Bellis et al. reviewed published paternal-discrepancy studies and reported estimates ranging from **0.8% to 30%**, with a **median of 3.7%** across 17 studies, while also making clear that the literature is heavily biased by sample selection. That is quite enough to justify keeping baseline leakage in the **low single digits** rather than in some lurid tabloid range. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC1733152/))

**Working rail:**
- `EPP_RATE ≈ 0.01–0.05` as a serious default range
- values above that are stress tests, not first assumptions

## Social-structural tightening

The bounded pressure window is not to be interpreted as arbitrary forcing. It stands for a period in which several institutions become more tightly coupled: descent, residence, inheritance, marriage organization, class differentiation, legitimacy. D-PLACE exposes exactly these sorts of variables from the Ethnographic Atlas contribution, including marital residence, inheritance, and social stratification measures. ([d-place.org](https://d-place.org/contributions/EA))

So the correct reading is not “history happened between generations 30 and 60.” The correct reading is: this is a stand-in for a bounded interval in which male-line filtering institutions become more coherent and therefore more effective.

**Working rail:**
- the pressure window represents institutional co-alignment
- do not pretend it is a direct historical timestamp
- do not assign it a fake ethnographic coefficient

## Genetic shape targets

Karmin et al. report a recent bottleneck in Y-chromosome diversity that does not appear comparably in mtDNA, which is the central asymmetry this model must respect. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC4381518/))

The peaceful-explanation paper by Guyon et al. explicitly frames patrilineal segmentary systems as sufficient to explain the post-Neolithic Y bottleneck without warfare, which means the field itself has already moved beyond “war or nothing.” ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC11043392/))

So the empirical target is not merely “low diversity.” It is a more particular shape:
- bounded paternal compression
- no comparable maternal collapse
- sparse survivor set
- post-compression survivor expansion

**Working rail:**
Judge the model against topology, not endpoint alone.

## What the literature does not give me

It does not give me:
- a Bronze Age fragility coefficient
- an exact leakage rate for prehistory
- a neat scalar for “patriarchy”

So I am not going to launder soft historical description into fake numerical authority. That sort of thing is how one gets a very pretty model and a false one.

## Rail from v0.8 and v0.8b

The initial state must represent a broad, redundant male-line ecology rather than a system already perched on the fragility boundary.

That means:
- mean initial lineage size must sit comfortably above the viability threshold
- the initial world must have enough slack that local weakness is survivable
- early collapse must not be built into the initialization

If the machine begins already brittle, then any later “emergent fragility” is an illusion. The system is merely expressing a pathology smuggled in at generation zero.

## Heterogeneity rail

The next pass should use mild initial heterogeneity, but this introduces a new discipline requirement.

Initial heterogeneity is not yet hierarchy. It is merely variation. So the model must report the initial distribution explicitly and then measure whether bounded cultural tightening amplifies that variation into durable pruning and survivor concentration.

**Working rail:**
- initial distribution should be mild, not already heavy-tailed
- initial distribution should be recorded, not silently generated and forgotten
- amplification must be measured, not merely assumed from unequal outcomes

## Damage rail

If a damage term is introduced, it must not function as hidden mortality or fake dramatic seasoning.

It is only admissible if interpreted as accumulated loss of recoverability after compression. The most interesting and defensible reading so far is cultural overfitting.

That means:
- the system becomes more competent at preserving its current hierarchy
- and less competent at regenerating breadth once breadth has been lost

So a damage term, if added, should alter:
- recovery
- stickiness
- re-diffusion
- post-window persistence of inequality

It should not simply deepen the fall by brute force.

## Modeling discipline

The right use of the literature here is narrow and hard-headed:

- leakage should be low but nonzero by default, not flamboyant ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC1733152/))
- bounded pressure should represent institutional tightening, not arbitrary plot shaping ([d-place.org](https://d-place.org/contributions/EA))
- outputs should be judged by shape, especially bounded compression, pruning lag, and survivor fan-out, not by a low endpoint alone ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC4381518/))
- initial variation must not be confused with emergent structure
- one dramatic run must not be confused with a regime

A blunter version, for my own future reference:

> The literature does not hand me a Bronze Age fragility constant. It does, however, tell me that leakage should probably be low but real, that male-line filtering institutions commonly co-occur, and that the empirical target is not merely collapse but a particular topology: bounded compression plus survivor burst. It also tells me not to begin the machine with everyone already hanging over the cliff and then pretend later brittleness is profound. And if I add a damage term, it had better mean reduced recoverability and institutional overfitting, not stage fog. That is enough to keep the model from wandering off into just-so theater.

