# Cost-Aware PAC Labeling

This repository contains the paper, slides, code, data, and tracked results for
the STATS 357 project report **Online PAC Labeling from a Linear Programming
Perspective**. The project studies how to combine cheap model-generated labels
with costly expert labels while controlling average released-label error.

For the dated research snapshot and current evidence, see
[`docs/RESEARCH_STATE.md`](docs/RESEARCH_STATE.md). For the detailed path to a
research-paper draft, see
[`docs/RESEARCH_PRIORITIES.md`](docs/RESEARCH_PRIORITIES.md).

## Repository Contents

- `main.tex` / `main.pdf`: primary 16-page project paper and compiled artifact.
- `slides/`: presentation sources, compiled deck, and presenter notes.
  `slides/slides.tex` is the Beamer entry point and includes the three
  `slides_*.tex` section files; `slides/slides.pdf` is the compiled deck.
- `slides/presenter_notes.tex` / `slides/presenter_notes.pdf`: companion talk
  notes.
- `experiments/run_simple_offline_pac_experiment.py`: one-source offline PAC
  comparison.
- `experiments/run_simple_online_pac_experiment.py`: audited online dual-price
  experiment.
- `experiments/run_two_source_offline_pac_experiment.py`: synthetic
  complementary two-source routing experiment.
- `experiments/data/`: ImageNet and ImageNetV2 prediction tables.
- `experiments/results/`: tracked trial-level CSVs, summaries, and figures used
  by the paper.
- `ref.bib` and `ref/pac label.pdf`: bibliography and local PAC-labeling
  reference paper.
- `docs/RESEARCH_STATE.md`: dated research question, technical status,
  evidence, limitations, and concise priority summary.
- `docs/RESEARCH_PRIORITIES.md`: detailed novelty, theory, related-work, and
  experimental roadmap toward a research-paper draft.
- `AGENTS.md`: repository instructions for coding agents.

## Setup

Install the dependencies used by the three current experiment scripts:

```bash
python3 -m pip install -r requirements.txt
```

The package names in `requirements.txt` are not version-pinned. The legacy
script `experiments/data/run_hw4_experiments.py` additionally uses `scipy` and
`scikit-learn`; it is not part of the current workflow.

## Build the Paper, Slides, and Presenter Notes

Run from the repository root:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error slides/slides.tex
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error \
  slides/presenter_notes.tex
```

These commands update the compiled PDFs in the repository. For a diagnostic
paper build that leaves tracked artifacts untouched, use a temporary output
directory:

```bash
mkdir -p /private/tmp/tijana-main-build
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=/private/tmp/tijana-main-build main.tex
```

The paper, slide, and presenter-notes builds were last verified on 2026-07-13.

## Data and Output Paths

The experiment scripts locate `experiments/data/` relative to their own files,
so default data discovery does not depend on the repository name or current
working directory. Use `--data-dir` to override the input location and
`--output-dir` to override the corresponding default under
`experiments/results/`.

## Reproduce the Tracked Experiments

The tracked results use 500 trials. Run these commands only when intentionally
regenerating the corresponding outputs under `experiments/results/`:

```bash
python3 experiments/run_simple_offline_pac_experiment.py --trials 500

python3 experiments/run_simple_online_pac_experiment.py \
  --trials 500 \
  --audit-probs 0.1 0.2 0.5

python3 experiments/run_two_source_offline_pac_experiment.py --trials 500
```

The two-source experiment is synthetic. Read the interpretation constraints in
[`docs/RESEARCH_STATE.md`](docs/RESEARCH_STATE.md) before reporting its results.

## Smoke Tests

Use these one-trial checks for routine validation; they write only to
`/private/tmp`:

```bash
python3 experiments/run_simple_offline_pac_experiment.py \
  --trials 1 \
  --epsilons 0.1 \
  --output-dir /private/tmp/simple_offline_pac

python3 experiments/run_simple_online_pac_experiment.py \
  --trials 1 \
  --epsilons 0.1 \
  --audit-probs 0.2 \
  --output-dir /private/tmp/simple_online_pac

python3 experiments/run_two_source_offline_pac_experiment.py \
  --trials 1 \
  --epsilons 0.1 \
  --output-dir /private/tmp/two_source_offline_pac
```

All three smoke tests were verified from both inside and outside the repository
on 2026-07-13.
