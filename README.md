# Cost-Aware PAC Labeling

This repository contains the code, data, results, and LaTeX source for the
STATS 357 project report:

**Online PAC Labeling from a Linear Programming Perspective**

The report studies offline and online cost-aware PAC labeling through a
linear-programming and dual-price perspective.

## Contents

- `main.tex`: main report source.
- `main.pdf`: compiled report.
- `audited_online_pac_labeling.tex`: online-auditing source material used in
  the report.
- `experiments/run_simple_offline_pac_experiment.py`: offline calibration experiment with
  the original PAC threshold baseline.
- `experiments/run_simple_online_pac_experiment.py`: audited online dual-price experiment.
- `experiments/run_two_source_offline_pac_experiment.py`: two-source offline experiment
  that synthesizes complementary cheap sources from the ImageNet tables and
  compares the LP/dual-price method against single-source PAC baselines.
- `data/imagenet.csv` and `data/imagenetv2.csv`: ImageNet data used by
  the experiments.
- `experiments/results/simple_offline_pac/`: offline summary, trial CSV, and plot.
- `experiments/results/simple_online_pac/`: online summary, trial CSV, and plot.
- `experiments/results/two_source_offline_pac/`: two-source summary, trial CSV, an
  auxiliary file recording the constructed two-source statistics, and plot.

## Reproduce The Experiments

Install Python dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Run the offline experiment:

```bash
python3 experiments/run_simple_offline_pac_experiment.py --trials 500 --output-dir experiments/results/simple_offline_pac
```

Run the online audited experiment:

```bash
python3 experiments/run_simple_online_pac_experiment.py --trials 500 --audit-probs 0.1 0.2 0.5 --output-dir experiments/results/simple_online_pac
```

Run the two-source offline experiment:

```bash
python3 experiments/run_two_source_offline_pac_experiment.py --trials 500 --output-dir experiments/results/two_source_offline_pac
```

The two-source experiment synthesizes a pair of complementary cheap sources
from each base ImageNet table (each source is competent on one parity half of
the true classes and low-confidence near-random on the other). The script
compares the LP fixed-price monotone-UCB rule from Section~2 of the report
against the single-source monotone PAC baseline applied to each source and
against a Bonferroni-corrected best-of-singles baseline.

## Compile The Report

The report expects the result plots under `experiments/results/simple_offline_pac/`,
`experiments/results/simple_online_pac/`, and
`experiments/results/two_source_offline_pac/`.

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```
