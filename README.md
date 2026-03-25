# Patrilines with Feedback

A small exploratory modeling repo accompanying the essay *Patrilines with Feedback; or, A Short Inquiry into the Y-Chromosome Bottleneck, Considered as a Control System*.

The project asks a narrow question: can strong compression in Y-chromosome lineage diversity arise from weak, structured, culturally mediated filtering, without treating massacre-warfare as a necessary premise?

This repo contains runnable toy models, working notes, generated figures, reference papers, and the essay draft built around them.

## Current status

The main architectural families now look like this:

- **v0.9**: best current single-basin behavioral family
- **v0.15**: best current scalar/topological Daisyworld family
- **v0.20**: best current nested-topology eligibility-graph family

These are not final truths. They are the current best representational bargains.

## Repository layout

- `model/` — simulation code
- `notes/` — working notes, version summaries, rails, and logs
- `figures/` — generated model figures
- `papers/` — reference PDFs
- `essay/` — essay draft, ODT master, and figure plans
- `requirements.txt` — Python dependencies

## Quick start

Create and activate a virtual environment, then install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run a current model directly, for example:

```bash
python model/sim_v0_20_edge_phased_graph.py
```

Outputs and derived figures can then be saved into `figures/` as needed.

## What this repo is for

This is not a polished package. It is a runnable research bench.

The point is to let a reader inspect the machinery, vary assumptions, reproduce figures, and decide where the model is earning its keep and where it is not. The exposed knobs are part of the argument.

## Where to read more

- `PROJECT_OVERVIEW.md` — long-form project context, architecture, and version history
- `essay/` — the essay draft and figure plans
- `notes/` — version-by-version working notes and rails

## References

The main external anchors are:

- Karmin et al. (2015)
- Poznik et al. (2016)
- Wang et al. (2013)
- Zeng, Aw, and Feldman (2018)

See `papers/` and the essay appendix for fuller reference detail.
