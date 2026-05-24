# Cost-Aware PAC Labeling

This repository contains the code, data, results, and LaTeX source for the
STATS 357 project report:

**Cost-Aware PAC Labeling from a Linear-Programming Perspective**

The report studies offline and online cost-aware PAC labeling through a
linear-programming and dual-price perspective.

## Contents

- `main.tex`: main report source.
- `main.pdf`: compiled report.
- `audited_online_pac_labeling.tex`: online-auditing source material used in
  the report.
- `run_simple_offline_pac_experiment.py`: offline calibration experiment with
  the original PAC threshold baseline.
- `run_simple_online_pac_experiment.py`: audited online dual-price experiment.
- `HW4_副本/imagenet.csv` and `HW4_副本/imagenetv2.csv`: ImageNet data used by
  the experiments.
- `results/simple_offline_pac/`: offline summary, trial CSV, and plot.
- `results/simple_online_pac/`: online summary, trial CSV, and plot.

## Reproduce The Experiments

Install Python dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Run the offline experiment:

```bash
python3 run_simple_offline_pac_experiment.py --trials 500 --output-dir results/simple_offline_pac
```

Run the online audited experiment:

```bash
python3 run_simple_online_pac_experiment.py --trials 500 --audit-probs 0.1 0.2 0.5 --output-dir results/simple_online_pac
```

## Compile The Report

The report expects the result plots under `results/simple_offline_pac/` and
`results/simple_online_pac/`.

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```
