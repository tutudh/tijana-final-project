# Cost-Aware PAC Labeling

This repository contains the paper, slides, code, data, and tracked results for
the STATS 357 project report **Online PAC Labeling from a Linear Programming
Perspective**. The project studies how to combine cheap model-generated labels
with costly expert labels while controlling average released-label error. The
work is being developed toward an AISTATS 2026 submission.

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
- `theory_loop/`: minimal autonomous `propose -> prove -> review` loop with
  fresh-context Claude Code and Codex CLI backends, resumable state, bounded
  call budgets, and append-only Markdown artifacts.
- `theory_scaffold/`: lightweight research-discovery and proof-certification
  scaffold with human-readable Markdown artifacts and fresh proof review.
- `theory_harness/`: preserved legacy routed harness; it remains available
  until the new scaffold is accepted and an archive decision is made.
- `.agents/skills/derive-online-labeling-theory/`: repository-level Codex skill
  that defines the theory workflow and review gates.
- `AGENTS.md`: repository instructions for coding agents.

## Setup

Install the dependencies used by the three current experiment scripts:

```bash
python3 -m pip install -r requirements.txt
```

The package names in `requirements.txt` are not version-pinned. The legacy
script `experiments/data/run_hw4_experiments.py` additionally uses `scipy` and
`scikit-learn`; it is not part of the current workflow.

## Optional Autonomous Theory Loop

`theory_loop/` is the smallest autonomous theory workflow in the repository.
It repeatedly proposes one joint error-plus-cost theorem candidate, attempts a
proof, and sends complete proof candidates to fresh-context reviewers. Failed
or rejected candidates are summarized in a graveyard so later proposals do
not simply repeat them. A successful run still produces only a proof candidate
pending human review.

The loop uses only Python's standard library. Run its offline tests before a
live model call:

```bash
python3 -m unittest discover -s theory_loop/tests
```

For the Codex backend, authenticate the Codex CLI with ChatGPT, then confirm
the saved login:

```bash
codex login
codex login status
```

On macOS, the ChatGPT desktop app may bundle Codex without adding it to the
`PATH` used by Terminal. If `codex` is not found, enable the bundled CLI for
the current terminal session and check it again:

```bash
export PATH="/Applications/ChatGPT.app/Contents/Resources:$PATH"
codex --version
codex login status
```

Alternatively, leave `PATH` unchanged and pass the executable directly to the
loop with
`--codex-bin "/Applications/ChatGPT.app/Contents/Resources/codex"` on every
new or resumed invocation.

Start with one foreground call. Reaching the one-call budget exits with status
code `4` by design and leaves a resumable run under `theory_loop/runs/`:

```bash
python3 theory_loop/run.py \
  --backend codex \
  --max-calls 1
```

The equivalent command that does not depend on `PATH` is:

```bash
python3 theory_loop/run.py \
  --backend codex \
  --codex-bin "/Applications/ChatGPT.app/Contents/Resources/codex" \
  --max-calls 1
```

The command prints the run directory. After inspecting its first proposal,
continue the same run with a larger total call ceiling:

```bash
python3 theory_loop/run.py \
  --backend codex \
  --resume theory_loop/runs/RUN_ID \
  --max-calls 40
```

For a long macOS run, keep the machine awake and write the console log under
`/private/tmp`:

```bash
nohup caffeinate -i python3 theory_loop/run.py \
  --backend codex \
  --max-calls 40 > /private/tmp/theory-loop.out 2>&1 &

tail -f /private/tmp/theory-loop.out
```

Every Codex stage uses a fresh ephemeral session in an empty temporary
directory, with a read-only sandbox and live web search available. API-key
environment variables are removed so the saved ChatGPT login is used. The
default Codex model is `gpt-5.6-sol` with reasoning effort `xhigh`; override
these with `--model` and `--effort` when needed. See
[`theory_loop/README.md`](theory_loop/README.md) for routing, artifacts, limits,
exit codes, and the Claude Code and mock backends.

## Optional Theory Scaffold

The lightweight scaffold has no dependencies beyond Python's standard library.
It separates open research from proof certification:

```text
frame -> design -> freeze_candidate -> prove -> review -> human_review
   |        |                         |
   +--------+-> mechanism_search      +-> proof_search -> prove
```

`frame` builds an interpretable assumption ladder and attacks the target before
algorithm design. `design` produces a small number of structurally distinct
candidates. Mechanism search and proof search require a precise failed-
derivation memo or blocked obligation. A human then freezes one exact candidate
before the fresh-context proof and independent review stages begin.

Run an offline preflight in `/private/tmp`. It assembles and saves the exact
request but does not authenticate, call a model, or enable networking:

```bash
python3 theory_scaffold/run.py \
  --stage frame \
  --dry-run \
  --output-dir /private/tmp/tijana-theory-scaffold
```

The command prints the new run directory. For manual mode, prepare a Markdown
artifact from the matching file under `theory_scaffold/templates/`, then record
it as a new immutable attempt:

```bash
python3 theory_scaffold/run.py \
  --run-dir /private/tmp/tijana-theory-scaffold/RUN_ID \
  --stage frame \
  --mode manual \
  --input /path/to/frame-result.md
```

Continue with the runner's suggested stage. The discovery stages are `frame`,
`design`, and `mechanism_search`; the certification stages are
`freeze_candidate`, `prove`, `proof_search`, and `review`. Freeze a completed
candidate-readiness packet only after inspecting it:

```bash
python3 theory_scaffold/run.py \
  --run-dir /private/tmp/tijana-theory-scaffold/RUN_ID \
  --stage freeze_candidate \
  --mode manual \
  --input /path/to/candidate-packet.md \
  --human-approved
```

Optional Codex CLI mode creates a fresh ephemeral, read-only request for every
stage. Only the two targeted-search stages receive web access. API-key
environment variables are removed, and the runner requires ChatGPT login:

```bash
codex login
codex login status

python3 theory_scaffold/run.py \
  --run-dir /private/tmp/tijana-theory-scaffold/RUN_ID \
  --stage design \
  --mode codex
```

Validate a run and execute the offline test suite with:

```bash
python3 theory_scaffold/validate.py \
  /private/tmp/tijana-theory-scaffold/RUN_ID

python3 -m unittest discover -s theory_scaffold/tests
```

Each attempt retains its prompt, stage-specific context, exact request, output,
timestamps, hashes, and fresh-context metadata. Failed and revised artifacts
are never overwritten. Deterministic checks enforce assumption classification,
comparator and cost parity, candidate freezing, source locations, context
isolation, and the final human-approval boundary; they do not decide
mathematical truth or novelty. See
[`theory_scaffold/ARCHITECTURE.md`](theory_scaffold/ARCHITECTURE.md) for the
context allowlist and two-layer design. The legacy `theory_harness/` remains
unchanged pending separate approval to archive or remove it.

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
