# Theory Loop

A minimal, long-running **propose → prove → review** loop for the joint
error-plus-cost online-labeling theorem target (see [brief.md](brief.md)).
Roughly 600 lines of stdlib Python replace the earlier harness/scaffold
orchestration; the research contracts are reused verbatim under
[contracts/](contracts/).

Every stage is one **fresh, isolated agent CLI call** (Claude Code by
default) executed in an empty temporary directory — the prover never sees the
designer's rationale beyond the candidate artifact, and each reviewer sees
only the contracts, the brief, the candidate, and the proof. Anchoring
isolation comes from process boundaries instead of framework code.

## The loop

```text
propose ──> prove ──┬─ complete ──> review ──┬─ pass ×N ──> STOP: FINAL.md (human review)
   ^                │                        ├─ revise ───> prove (with feedback)
   │                ├─ blocked ───> prove    └─ reject ───> propose (buried in graveyard)
   │                └─ refuted ──────────────────────────> propose (buried in graveyard)
   └── graveyard of retired candidates is shown to the next propose
```

- A candidate dies after `--max-proof-attempts` blocked/revise rounds, on
  `refuted`, or on `reject`; its theorem and the evidence against it are
  appended to `graveyard.md` so later proposals do not repeat it.
- Success requires `--reviews-to-pass` (default **2**) consecutive
  independent fresh-context passes.
- The loop stops on success, on `--max-candidates` exhausted, on the
  `--max-calls` budget, or after 3 consecutive invalid outputs.

## Quick start

Offline smoke (no model calls) and tests:

```bash
python3 -m unittest discover -s theory_loop/tests
```

### Codex CLI

The Codex backend uses the saved ChatGPT login rather than an API key. Make
sure the Codex CLI is available in Terminal, authenticate once, and confirm
the login:

```bash
codex --version
codex login
codex login status
```

On macOS, the ChatGPT desktop app may bundle Codex without adding it to the
`PATH` used by Terminal. If zsh reports `command not found: codex`, enable the
bundled CLI for the current terminal session:

```bash
export PATH="/Applications/ChatGPT.app/Contents/Resources:$PATH"
codex --version
codex login status
```

The exported `PATH` is inherited by the Python runner and background jobs
started from this terminal. To avoid changing `PATH`, instead add the following
option to every new or resumed loop command:

```text
--codex-bin "/Applications/ChatGPT.app/Contents/Resources/codex"
```

Start with one foreground call so that you can inspect the first proposal.
Hitting this one-call ceiling exits with code `4` by design and preserves a
resumable run:

```bash
python3 theory_loop/run.py \
  --backend codex \
  --max-calls 1
```

For example, the complete first-call command without a `PATH` change is:

```bash
python3 theory_loop/run.py \
  --backend codex \
  --codex-bin "/Applications/ChatGPT.app/Contents/Resources/codex" \
  --max-calls 1
```

The command prints a directory such as
`theory_loop/runs/20260715T210000Z-1234abcd`. Continue it by passing that path
to `--resume`. `--max-calls` is the new total ceiling for the whole run, not an
additional number of calls:

```bash
python3 theory_loop/run.py \
  --backend codex \
  --resume theory_loop/runs/RUN_ID \
  --max-calls 40
```

For a real long run in the background on macOS, `caffeinate` keeps the laptop
awake and the console log stays under `/private/tmp`:

```bash
nohup caffeinate -i python3 theory_loop/run.py \
  --backend codex \
  --max-calls 40 > /private/tmp/theory-loop.out 2>&1 &

tail -f /private/tmp/theory-loop.out
```

Run these commands from the repository root. Use `--model` to override the
default `gpt-5.6-sol` model and `--effort` to override the default `xhigh`
reasoning effort. Codex's official non-interactive-mode documentation is at
<https://learn.chatgpt.com/docs/non-interactive-mode>.

### Claude Code

Claude Code remains the default backend. A foreground run can omit
`--backend claude`:

```bash
python3 theory_loop/run.py --max-calls 40
```

## Backends

- `--backend claude` (default): `claude -p --output-format json
  --strict-mcp-config --allowed-tools WebSearch,WebFetch`, fresh session per
  call, run from an empty temp directory. `--model` optionally overrides the
  CLI default; `--max-budget-usd-per-call` caps API spend per call.
- `--backend codex`: the scaffold's invocation (`codex --search exec
  --ephemeral --sandbox read-only`, ChatGPT-subscription environment). It
  requires a current Codex CLI and a saved ChatGPT login. User configuration is
  ignored, every stage receives live web-search access, and API-key environment
  variables are removed. Default model `gpt-5.6-sol`, `--effort xhigh`.
- `--backend mock --mock-dir DIR`: replays `0001.md`, `0002.md`, … as stage
  outputs; used by the tests and for offline dry runs.

## Run artifacts (append-only)

```text
theory_loop/runs/<run-id>/
  state.json               # resumable loop state
  log.md                   # one line per event (also printed to stdout)
  inputs/                  # frozen copies of brief, prompts, contracts
  calls/0001-propose/      # request.md, output.md, meta.json, raw streams
  graveyard.md             # retired candidates and the evidence against them
  FINAL.md                 # on success: candidate + proof + passing reviews
```

Exit codes: `0` success, `3` exhausted, `4` call budget reached, `5` repeated
invalid outputs, `6` interrupted (resume with `--resume`).

## Honesty boundary

A reviewer `pass` is a workflow status. `FINAL.md` is a model-generated
**proof candidate pending human review** — nothing may be promoted into the
paper, `docs/RESEARCH_STATE.md`, or any novelty claim without human review,
per the research constitution.
