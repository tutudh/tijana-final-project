#!/usr/bin/env python3
"""Minimal long-running propose -> prove -> review loop for theory research.

Each stage is one fresh, isolated agent CLI call (Claude Code or Codex).
State lives in plain files under the run directory; every call is preserved
append-only. The loop stops on: enough independent review passes (success),
exhausted candidates or proof attempts, the call budget, or repeated invalid
outputs. A reviewer PASS is a workflow status; promotion of any result
requires human review.
"""

from __future__ import annotations

import argparse
import dataclasses
import json
import re
import subprocess
import sys
import tempfile
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

LOOP_ROOT = Path(__file__).resolve().parent
DEFAULT_OUTPUT_ROOT = LOOP_ROOT / "runs"

STAGE_PROMPTS = {
    "propose": "prompts/propose.md",
    "prove": "prompts/prove.md",
    "review": "prompts/review.md",
}
CONTRACT_FILES = (
    "contracts/research-constitution.md",
    "contracts/assumption-policy.md",
    "contracts/comparator-policy.md",
    "contracts/literature-policy.md",
)

STATUS_TOKENS = {
    "propose": {"proposed", "exhausted"},
    "prove": {"complete", "blocked", "refuted"},
    "review": {"pass", "revise", "reject"},
}

EXIT_CODES = {
    "success": 0,
    "exhausted": 3,
    "budget": 4,
    "error": 5,
    "interrupted": 6,
}

MAX_CONSECUTIVE_INVALID = 3

STATUS_RE = re.compile(r"(?im)^[\s>#*]*(?:status|verdict)[\s*]*:[\s*]*([a-z_]+)")

API_KEY_ENV_VARS = ("OPENAI_API_KEY", "CODEX_API_KEY")


@dataclasses.dataclass(frozen=True)
class Limits:
    max_candidates: int = 4
    max_proof_attempts: int = 4
    reviews_to_pass: int = 2


@dataclasses.dataclass(frozen=True)
class Config:
    backend: str
    limits: Limits
    max_calls: int
    timeout_seconds: int
    max_budget_usd_per_call: float | None
    model: str | None
    effort: str
    claude_bin: str
    codex_bin: str
    mock_dir: Path | None


def parse_status(text: str) -> str | None:
    """Extract the first STATUS:/VERDICT: token from a stage artifact."""

    match = STATUS_RE.search(text)
    return match.group(1).lower() if match else None


def decide_next(
    stage: str,
    status: str,
    *,
    proof_attempts: int,
    passes: int,
    candidates_started: int,
    limits: Limits,
) -> tuple[str, str]:
    """Pure routing: map a validated stage status to the next action."""

    def retire(reason: str) -> tuple[str, str]:
        if candidates_started >= limits.max_candidates:
            return "stop_exhausted", f"{reason}; candidate budget exhausted"
        return "new_candidate", reason

    if stage == "propose":
        if status == "proposed":
            return "prove", "candidate accepted for proof work"
        return "stop_exhausted", "designer reports no admissible candidate remains"
    if stage == "prove":
        if status == "complete":
            return "review", "complete proof candidate ready for fresh review"
        if status == "refuted":
            return retire("theorem candidate refuted")
        if proof_attempts >= limits.max_proof_attempts:
            return retire("proof attempts exhausted while blocked")
        return "prove", "retry proof against the recorded obligations"
    if stage == "review":
        if status == "pass":
            if passes >= limits.reviews_to_pass:
                return "stop_success", "required independent review passes reached"
            return "review", "request another independent review"
        if status == "reject":
            return retire("reviewer rejected the candidate")
        if proof_attempts >= limits.max_proof_attempts:
            return retire("proof attempts exhausted after revise verdicts")
        return "prove", "revise the proof using review feedback"
    raise ValueError(f"Unknown stage: {stage}")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def new_run_id() -> str:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"{stamp}-{uuid.uuid4().hex[:8]}"


def save_state(run_dir: Path, state: dict[str, Any]) -> None:
    state["updated_at"] = utc_now()
    temporary = run_dir / f".state-{uuid.uuid4().hex}.tmp"
    temporary.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temporary.replace(run_dir / "state.json")


def log(run_dir: Path, message: str) -> None:
    line = f"{utc_now()} {message}"
    with (run_dir / "log.md").open("a", encoding="utf-8") as handle:
        handle.write(line + "\n")
    print(line, flush=True)


def create_run(output_root: Path, run_id: str | None, brief_path: Path) -> tuple[Path, dict[str, Any]]:
    identifier = run_id or new_run_id()
    run_dir = (output_root / identifier).resolve()
    run_dir.mkdir(parents=True, exist_ok=False)
    inputs = run_dir / "inputs"
    for relative in (*STAGE_PROMPTS.values(), *CONTRACT_FILES):
        source = LOOP_ROOT / relative
        target = inputs / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    (inputs / "brief.md").write_text(brief_path.read_text(encoding="utf-8"), encoding="utf-8")
    (run_dir / "calls").mkdir()
    (run_dir / "graveyard.md").write_text("# Retired candidates\n", encoding="utf-8")
    (run_dir / "log.md").write_text("", encoding="utf-8")
    state: dict[str, Any] = {
        "version": 1,
        "run_id": identifier,
        "created_at": utc_now(),
        "updated_at": utc_now(),
        "status": "running",
        "next_action": "propose",
        "calls_made": 0,
        "candidates_started": 0,
        "proof_attempts": 0,
        "passes": 0,
        "consecutive_invalid": 0,
        "candidate_call": None,
        "proof_call": None,
        "review_call": None,
        "total_cost_usd": 0.0,
    }
    save_state(run_dir, state)
    return run_dir, state


def _read_inputs(run_dir: Path, relative: str) -> str:
    return (run_dir / "inputs" / relative).read_text(encoding="utf-8")


def _call_output(run_dir: Path, call_rel: str) -> str:
    return (run_dir / call_rel / "output.md").read_text(encoding="utf-8")


def compose_request(stage: str, run_dir: Path, state: dict[str, Any]) -> str:
    """Assemble the bounded, stage-specific request for one fresh call."""

    blocks = [_read_inputs(run_dir, STAGE_PROMPTS[stage]).rstrip()]

    def add(label: str, content: str) -> None:
        blocks.append(f"# Context: {label}\n\n{content.rstrip()}")

    for relative in CONTRACT_FILES:
        add(relative, _read_inputs(run_dir, relative))
    add("research brief", _read_inputs(run_dir, "brief.md"))

    if stage == "propose":
        graveyard = (run_dir / "graveyard.md").read_text(encoding="utf-8")
        if "## " in graveyard:
            add("retired candidates (do not repeat or trivially perturb these)", graveyard)
    elif stage == "prove":
        add("theorem candidate to prove", _call_output(run_dir, state["candidate_call"]))
        if state["proof_call"]:
            add(
                "previous proof attempt (yours to reuse, repair, or discard)",
                _call_output(run_dir, state["proof_call"]),
            )
        if state["review_call"]:
            add(
                "reviewer feedback that must be addressed point by point",
                _call_output(run_dir, state["review_call"]),
            )
    elif stage == "review":
        add("theorem candidate", _call_output(run_dir, state["candidate_call"]))
        add("proof candidate under review", _call_output(run_dir, state["proof_call"]))
    else:
        raise ValueError(f"Unknown stage: {stage}")

    return "\n\n".join(blocks) + "\n"


def _subscription_environment() -> dict[str, str]:
    import os

    environment = os.environ.copy()
    for variable in API_KEY_ENV_VARS:
        environment.pop(variable, None)
    return environment


def invoke_claude(request: str, cfg: Config) -> dict[str, Any]:
    command = [
        cfg.claude_bin,
        "-p",
        "--output-format",
        "json",
        "--strict-mcp-config",
        "--allowed-tools",
        "WebSearch,WebFetch",
    ]
    if cfg.max_budget_usd_per_call:
        command.extend(["--max-budget-usd", str(cfg.max_budget_usd_per_call)])
    if cfg.model:
        command.extend(["--model", cfg.model])
    with tempfile.TemporaryDirectory(prefix="theory-loop-") as temp_name:
        try:
            completed = subprocess.run(
                command,
                input=request,
                text=True,
                capture_output=True,
                check=False,
                cwd=temp_name,
                timeout=cfg.timeout_seconds,
            )
        except subprocess.TimeoutExpired:
            return {
                "output": "",
                "ok": False,
                "error": f"claude call timed out after {cfg.timeout_seconds}s",
                "cost_usd": 0.0,
                "stdout": "",
                "stderr": "",
            }
    output = ""
    cost = 0.0
    error = ""
    ok = completed.returncode == 0
    try:
        payload = json.loads(completed.stdout)
        output = payload.get("result") or ""
        cost = float(payload.get("total_cost_usd") or 0.0)
        if payload.get("is_error"):
            ok = False
            error = f"claude reported is_error (subtype={payload.get('subtype')})"
    except (json.JSONDecodeError, TypeError):
        ok = False
        error = "claude stdout was not valid JSON"
    if completed.returncode != 0 and not error:
        error = (completed.stderr or "").strip() or "claude CLI exited nonzero"
    return {
        "output": output,
        "ok": ok,
        "error": error,
        "cost_usd": cost,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }


def invoke_codex(request: str, cfg: Config) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="theory-loop-") as temp_name:
        work_dir = Path(temp_name)
        output_path = work_dir / "last-message.md"
        command = [
            cfg.codex_bin,
            "--search",
            "exec",
            "--ephemeral",
            "--ignore-user-config",
            "--skip-git-repo-check",
            "--sandbox",
            "read-only",
            "--json",
            "--model",
            cfg.model or "gpt-5.6-sol",
            "--config",
            f"model_reasoning_effort={json.dumps(cfg.effort)}",
            "--config",
            'approval_policy="never"',
            "--cd",
            str(work_dir),
            "--output-last-message",
            str(output_path),
            "-",
        ]
        try:
            completed = subprocess.run(
                command,
                input=request,
                text=True,
                capture_output=True,
                check=False,
                cwd=work_dir,
                env=_subscription_environment(),
                timeout=cfg.timeout_seconds,
            )
        except subprocess.TimeoutExpired:
            return {
                "output": "",
                "ok": False,
                "error": f"codex call timed out after {cfg.timeout_seconds}s",
                "cost_usd": 0.0,
                "stdout": "",
                "stderr": "",
            }
        output = output_path.read_text(encoding="utf-8") if output_path.exists() else ""
    ok = completed.returncode == 0 and bool(output.strip())
    error = "" if ok else ((completed.stderr or "").strip() or "codex CLI call failed")
    return {
        "output": output,
        "ok": ok,
        "error": error,
        "cost_usd": 0.0,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }


def invoke_backend(request: str, cfg: Config, call_number: int) -> dict[str, Any]:
    if cfg.backend == "mock":
        assert cfg.mock_dir is not None
        path = cfg.mock_dir / f"{call_number:04d}.md"
        if not path.is_file():
            return {
                "output": "",
                "ok": False,
                "error": f"mock response missing: {path}",
                "cost_usd": 0.0,
                "stdout": "",
                "stderr": "",
            }
        return {
            "output": path.read_text(encoding="utf-8"),
            "ok": True,
            "error": "",
            "cost_usd": 0.0,
            "stdout": "",
            "stderr": "",
        }
    if cfg.backend == "claude":
        return invoke_claude(request, cfg)
    if cfg.backend == "codex":
        return invoke_codex(request, cfg)
    raise ValueError(f"Unknown backend: {cfg.backend}")


def _extract_sections(text: str, headings: tuple[str, ...]) -> str:
    parts = []
    for heading in headings:
        match = re.search(
            rf"(?ims)^#{{1,4}}\s*{re.escape(heading)}\b.*?(?=^#{{1,4}}\s|\Z)",
            text,
        )
        if match:
            parts.append(match.group(0).rstrip())
    if parts:
        return "\n\n".join(parts)
    return text.strip()[:600]


def bury_candidate(run_dir: Path, state: dict[str, Any], cause: str, reason: str) -> None:
    entry = [
        "",
        f"## Retired candidate {state['candidates_started']} — {cause}",
        "",
        f"- Reason: {reason}",
        f"- Candidate: {state['candidate_call']}",
        f"- Last proof attempt: {state['proof_call']}",
        f"- Last review: {state['review_call']}",
        "",
        "### Candidate summary",
        "",
        _extract_sections(
            _call_output(run_dir, state["candidate_call"]),
            ("Theorem candidate", "Theorem", "Setting and assumption ladder"),
        ),
    ]
    if state["proof_call"]:
        entry.extend(
            (
                "",
                "### Evidence from the last proof attempt",
                "",
                _extract_sections(
                    _call_output(run_dir, state["proof_call"]),
                    ("Counterexample", "Open obligations", "Self-audit"),
                ),
            )
        )
    if state["review_call"]:
        entry.extend(
            (
                "",
                "### Reviewer objection",
                "",
                _extract_sections(
                    _call_output(run_dir, state["review_call"]),
                    ("Verdict rationale", "Smallest failure"),
                ),
            )
        )
    with (run_dir / "graveyard.md").open("a", encoding="utf-8") as handle:
        handle.write("\n".join(entry) + "\n")


def write_final(run_dir: Path, state: dict[str, Any]) -> None:
    proof_number = int(Path(state["proof_call"]).name.split("-")[0])
    reviews = []
    for call_dir in sorted((run_dir / "calls").iterdir()):
        if not call_dir.name.endswith("-review"):
            continue
        if int(call_dir.name.split("-")[0]) <= proof_number:
            continue
        output = call_dir / "output.md"
        if output.is_file():
            reviews.append((call_dir.name, output.read_text(encoding="utf-8")))
    sections = [
        "# Surviving proof candidate — pending human review",
        "",
        "This artifact was produced by an autonomous loop. It is a model-",
        "generated proof candidate that passed "
        f"{state['passes']} independent fresh-context review(s). It is NOT an "
        "established theorem or novelty claim until a human reviews and",
        "promotes it.",
        "",
        f"- Run: {state['run_id']}",
        f"- Candidate: {state['candidate_call']}",
        f"- Proof: {state['proof_call']}",
        f"- Calls made: {state['calls_made']}; total cost: ${state['total_cost_usd']:.2f}",
        "",
        "## Theorem candidate",
        "",
        _call_output(run_dir, state["candidate_call"]).rstrip(),
        "",
        "## Proof candidate",
        "",
        _call_output(run_dir, state["proof_call"]).rstrip(),
    ]
    for name, text in reviews:
        sections.extend(("", f"## Review: {name}", "", text.rstrip()))
    (run_dir / "FINAL.md").write_text("\n".join(sections) + "\n", encoding="utf-8")


def _next_call_number(run_dir: Path) -> int:
    numbers = [0]
    for path in (run_dir / "calls").iterdir():
        prefix = path.name.split("-", 1)[0]
        if prefix.isdigit():
            numbers.append(int(prefix))
    return max(numbers) + 1


def finish(run_dir: Path, state: dict[str, Any], status: str, message: str) -> int:
    state["status"] = status
    save_state(run_dir, state)
    log(run_dir, f"loop finished: {status} — {message}")
    return EXIT_CODES[status]


def run_loop(run_dir: Path, state: dict[str, Any], cfg: Config) -> int:
    log(
        run_dir,
        f"loop running: backend={cfg.backend} model={cfg.model or 'default'} "
        f"max_calls={cfg.max_calls} limits={dataclasses.asdict(cfg.limits)}",
    )
    while True:
        if state["calls_made"] >= cfg.max_calls:
            return finish(
                run_dir,
                state,
                "budget",
                f"call budget {cfg.max_calls} reached; resume with --resume and a larger --max-calls",
            )
        stage = state["next_action"]
        number = _next_call_number(run_dir)
        call_rel = f"calls/{number:04d}-{stage}"
        call_dir = run_dir / call_rel
        call_dir.mkdir(parents=True, exist_ok=False)
        request = compose_request(stage, run_dir, state)
        (call_dir / "request.md").write_text(request, encoding="utf-8")
        log(run_dir, f"call {number:04d} {stage} started (attempt context: "
                     f"candidates={state['candidates_started']} proofs={state['proof_attempts']} passes={state['passes']})")
        started = time.monotonic()
        result = invoke_backend(request, cfg, number)
        duration = time.monotonic() - started
        (call_dir / "output.md").write_text(result["output"], encoding="utf-8")
        if result["stdout"]:
            (call_dir / "raw-stdout.txt").write_text(result["stdout"], encoding="utf-8")
        if result["stderr"]:
            (call_dir / "raw-stderr.txt").write_text(result["stderr"], encoding="utf-8")
        state["calls_made"] += 1
        state["total_cost_usd"] += result["cost_usd"]
        status = parse_status(result["output"]) if result["ok"] else None
        valid = status in STATUS_TOKENS[stage]
        (call_dir / "meta.json").write_text(
            json.dumps(
                {
                    "number": number,
                    "stage": stage,
                    "backend": cfg.backend,
                    "model": cfg.model,
                    "ok": result["ok"],
                    "error": result["error"],
                    "status": status if valid else None,
                    "raw_status": status,
                    "duration_seconds": round(duration, 1),
                    "cost_usd": result["cost_usd"],
                    "completed_at": utc_now(),
                },
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
        if not valid:
            state["consecutive_invalid"] += 1
            detail = result["error"] or f"unrecognized status marker: {status!r}"
            log(run_dir, f"call {number:04d} {stage} invalid ({duration:.0f}s): {detail}")
            if state["consecutive_invalid"] >= MAX_CONSECUTIVE_INVALID:
                return finish(
                    run_dir,
                    state,
                    "error",
                    f"{MAX_CONSECUTIVE_INVALID} consecutive invalid outputs",
                )
            save_state(run_dir, state)
            continue
        state["consecutive_invalid"] = 0
        if stage == "propose" and status == "proposed":
            state["candidates_started"] += 1
            state["candidate_call"] = call_rel
            state["proof_call"] = None
            state["review_call"] = None
            state["proof_attempts"] = 0
            state["passes"] = 0
        elif stage == "prove":
            state["proof_attempts"] += 1
            state["proof_call"] = call_rel
            state["review_call"] = None
        elif stage == "review":
            state["review_call"] = call_rel
            if status == "pass":
                state["passes"] += 1
            elif status == "revise":
                state["passes"] = 0
        action, reason = decide_next(
            stage,
            status,
            proof_attempts=state["proof_attempts"],
            passes=state["passes"],
            candidates_started=state["candidates_started"],
            limits=cfg.limits,
        )
        log(
            run_dir,
            f"call {number:04d} {stage} -> {status} "
            f"({duration:.0f}s, ${result['cost_usd']:.2f}); {reason}",
        )
        if action == "new_candidate":
            bury_candidate(run_dir, state, cause=f"{stage}: {status}", reason=reason)
            action = "propose"
        elif action == "stop_exhausted" and stage != "propose" and state["candidate_call"]:
            bury_candidate(run_dir, state, cause=f"{stage}: {status}", reason=reason)
        if action == "stop_success":
            write_final(run_dir, state)
            state["next_action"] = "human_review"
            return finish(
                run_dir,
                state,
                "success",
                f"see {run_dir / 'FINAL.md'} — pending human review",
            )
        if action == "stop_exhausted":
            state["next_action"] = "propose"
            return finish(run_dir, state, "exhausted", reason)
        state["next_action"] = action
        save_state(run_dir, state)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--backend", choices=("claude", "codex", "mock"), default="claude")
    parser.add_argument("--model", help="Backend model override (codex default: gpt-5.6-sol).")
    parser.add_argument("--effort", default="xhigh", help="Codex reasoning effort.")
    parser.add_argument("--brief", type=Path, default=LOOP_ROOT / "brief.md")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--run-id")
    parser.add_argument("--resume", type=Path, help="Existing run directory to continue.")
    parser.add_argument("--max-candidates", type=int, default=4)
    parser.add_argument("--max-proof-attempts", type=int, default=4)
    parser.add_argument("--reviews-to-pass", type=int, default=2)
    parser.add_argument("--max-calls", type=int, default=40)
    parser.add_argument("--timeout-seconds", type=int, default=5400)
    parser.add_argument(
        "--max-budget-usd-per-call",
        type=float,
        help="Optional per-call API spend cap for the claude backend "
        "(irrelevant on subscription auth).",
    )
    parser.add_argument("--claude-bin", default="claude")
    parser.add_argument("--codex-bin", default="codex")
    parser.add_argument("--mock-dir", type=Path, help="Directory of NNNN.md mock responses.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.backend == "mock" and args.mock_dir is None:
        print("--backend mock requires --mock-dir", file=sys.stderr)
        return 2
    cfg = Config(
        backend=args.backend,
        limits=Limits(
            max_candidates=args.max_candidates,
            max_proof_attempts=args.max_proof_attempts,
            reviews_to_pass=args.reviews_to_pass,
        ),
        max_calls=args.max_calls,
        timeout_seconds=args.timeout_seconds,
        max_budget_usd_per_call=args.max_budget_usd_per_call,
        model=args.model,
        effort=args.effort,
        claude_bin=args.claude_bin,
        codex_bin=args.codex_bin,
        mock_dir=args.mock_dir.resolve() if args.mock_dir else None,
    )
    if args.resume:
        run_dir = args.resume.resolve()
        state = json.loads((run_dir / "state.json").read_text(encoding="utf-8"))
        if state["status"] == "success":
            print(f"Run already succeeded: {run_dir / 'FINAL.md'}")
            return 0
        state["status"] = "running"
        if state["next_action"] not in STAGE_PROMPTS:
            state["next_action"] = "propose"
    else:
        run_dir, state = create_run(args.output_dir.resolve(), args.run_id, args.brief)
        print(f"Run directory: {run_dir}", flush=True)
    try:
        return run_loop(run_dir, state, cfg)
    except KeyboardInterrupt:
        print("", flush=True)
        return finish(run_dir, state, "interrupted", "interrupted; continue with --resume")


if __name__ == "__main__":
    sys.exit(main())
