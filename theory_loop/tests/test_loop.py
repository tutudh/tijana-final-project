"""Offline tests for the theory loop driver (mock backend, no model calls)."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from theory_loop.run import Limits, decide_next, main, parse_status


LIMITS = Limits(max_candidates=4, max_proof_attempts=4, reviews_to_pass=2)


class ParseStatusTest(unittest.TestCase):
    def test_plain_status_line(self):
        self.assertEqual(parse_status("STATUS: complete\n\nBody"), "complete")

    def test_verdict_line_case_and_bold(self):
        self.assertEqual(parse_status("**Verdict:** PASS\nrest"), "pass")

    def test_first_occurrence_wins(self):
        text = "STATUS: blocked\n...\nSTATUS: complete\n"
        self.assertEqual(parse_status(text), "blocked")

    def test_missing_status_returns_none(self):
        self.assertIsNone(parse_status("A proof without any marker."))

    def test_status_not_at_start_of_document(self):
        text = "# Proof result\n\nSTATUS: refuted\n"
        self.assertEqual(parse_status(text), "refuted")


class DecideNextTest(unittest.TestCase):
    def test_proposed_goes_to_prove(self):
        self.assertEqual(
            decide_next("propose", "proposed", proof_attempts=0, passes=0,
                        candidates_started=1, limits=LIMITS)[0],
            "prove",
        )

    def test_propose_exhausted_stops(self):
        self.assertEqual(
            decide_next("propose", "exhausted", proof_attempts=0, passes=0,
                        candidates_started=1, limits=LIMITS)[0],
            "stop_exhausted",
        )

    def test_complete_proof_goes_to_review(self):
        self.assertEqual(
            decide_next("prove", "complete", proof_attempts=1, passes=0,
                        candidates_started=1, limits=LIMITS)[0],
            "review",
        )

    def test_blocked_proof_retries_prove(self):
        self.assertEqual(
            decide_next("prove", "blocked", proof_attempts=1, passes=0,
                        candidates_started=1, limits=LIMITS)[0],
            "prove",
        )

    def test_blocked_proof_at_attempt_cap_starts_new_candidate(self):
        self.assertEqual(
            decide_next("prove", "blocked", proof_attempts=4, passes=0,
                        candidates_started=1, limits=LIMITS)[0],
            "new_candidate",
        )

    def test_refuted_proof_starts_new_candidate(self):
        self.assertEqual(
            decide_next("prove", "refuted", proof_attempts=1, passes=0,
                        candidates_started=1, limits=LIMITS)[0],
            "new_candidate",
        )

    def test_new_candidate_at_candidate_cap_stops(self):
        self.assertEqual(
            decide_next("prove", "refuted", proof_attempts=1, passes=0,
                        candidates_started=4, limits=LIMITS)[0],
            "stop_exhausted",
        )

    def test_first_pass_requests_second_independent_review(self):
        self.assertEqual(
            decide_next("review", "pass", proof_attempts=1, passes=1,
                        candidates_started=1, limits=LIMITS)[0],
            "review",
        )

    def test_enough_passes_stop_with_success(self):
        self.assertEqual(
            decide_next("review", "pass", proof_attempts=1, passes=2,
                        candidates_started=1, limits=LIMITS)[0],
            "stop_success",
        )

    def test_revise_goes_back_to_prove(self):
        self.assertEqual(
            decide_next("review", "revise", proof_attempts=1, passes=0,
                        candidates_started=1, limits=LIMITS)[0],
            "prove",
        )

    def test_revise_at_attempt_cap_starts_new_candidate(self):
        self.assertEqual(
            decide_next("review", "revise", proof_attempts=4, passes=0,
                        candidates_started=1, limits=LIMITS)[0],
            "new_candidate",
        )

    def test_reject_starts_new_candidate(self):
        self.assertEqual(
            decide_next("review", "reject", proof_attempts=1, passes=1,
                        candidates_started=1, limits=LIMITS)[0],
            "new_candidate",
        )


def _mk(text: str) -> str:
    return text


PROPOSED = "STATUS: proposed\n\n## Theorem candidate\nAn iid-arrival theorem.\n"
COMPLETE = "STATUS: complete\n\n## Exact theorem\nT.\n\n## Main proof\nQED-candidate.\n"
BLOCKED = "STATUS: blocked\n\n## Open obligations\nLemma 2 concentration step.\n"
REFUTED = "STATUS: refuted\n\n## Counterexample\nTwo-point distribution.\n"
PASS_R = "VERDICT: pass\n\n## Verdict rationale\nChecked every step.\n"
REVISE = "VERDICT: revise\n\n## Smallest failure\nStep 3 uses an unproved bound.\n"
REJECT = "VERDICT: reject\n\n## Verdict rationale\nAssumption is optimizer-local.\n"


class LoopEndToEndTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.mock_dir = self.root / "mock"
        self.mock_dir.mkdir()
        self.runs = self.root / "runs"

    def tearDown(self):
        self._tmp.cleanup()

    def queue(self, *texts: str) -> None:
        for index, text in enumerate(texts, start=1):
            (self.mock_dir / f"{index:04d}.md").write_text(_mk(text), encoding="utf-8")

    def run_loop(self, *extra: str) -> int:
        argv = [
            "--backend", "mock",
            "--mock-dir", str(self.mock_dir),
            "--output-dir", str(self.runs),
            "--run-id", "test-run",
            *extra,
        ]
        return main(argv)

    def read_state(self) -> dict:
        return json.loads((self.runs / "test-run" / "state.json").read_text(encoding="utf-8"))

    def test_happy_path_with_revision_reaches_success(self):
        self.queue(PROPOSED, COMPLETE, REVISE, COMPLETE, PASS_R, PASS_R)
        code = self.run_loop()
        self.assertEqual(code, 0)
        state = self.read_state()
        self.assertEqual(state["status"], "success")
        self.assertEqual(state["calls_made"], 6)
        run_dir = self.runs / "test-run"
        self.assertTrue((run_dir / "FINAL.md").is_file())
        calls = sorted(path.name for path in (run_dir / "calls").iterdir())
        self.assertEqual(len(calls), 6)
        final = (run_dir / "FINAL.md").read_text(encoding="utf-8")
        self.assertIn("pending human review", final)
        self.assertIn("QED-candidate", final)

    def test_refuted_candidate_is_buried_and_next_candidate_succeeds(self):
        self.queue(PROPOSED, REFUTED, PROPOSED, COMPLETE, PASS_R, PASS_R)
        code = self.run_loop()
        self.assertEqual(code, 0)
        state = self.read_state()
        self.assertEqual(state["status"], "success")
        self.assertEqual(state["candidates_started"], 2)
        graveyard = (self.runs / "test-run" / "graveyard.md").read_text(encoding="utf-8")
        self.assertIn("refuted", graveyard)
        self.assertIn("Two-point distribution", graveyard)

    def test_reject_after_pass_resets_pass_count(self):
        self.queue(PROPOSED, COMPLETE, PASS_R, REJECT, PROPOSED, COMPLETE, PASS_R, PASS_R)
        code = self.run_loop()
        self.assertEqual(code, 0)
        self.assertEqual(self.read_state()["candidates_started"], 2)

    def test_budget_stop_and_resume_with_larger_budget(self):
        self.queue(PROPOSED, COMPLETE, PASS_R, PASS_R)
        code = self.run_loop("--max-calls", "1")
        self.assertEqual(code, 4)
        state = self.read_state()
        self.assertEqual(state["status"], "budget")
        self.assertEqual(state["next_action"], "prove")
        code = main([
            "--backend", "mock",
            "--mock-dir", str(self.mock_dir),
            "--resume", str(self.runs / "test-run"),
            "--max-calls", "10",
        ])
        self.assertEqual(code, 0)
        self.assertEqual(self.read_state()["status"], "success")

    def test_three_consecutive_invalid_outputs_abort(self):
        self.queue("no marker", "still nothing", "nope")
        code = self.run_loop()
        self.assertEqual(code, 5)
        self.assertEqual(self.read_state()["status"], "error")

    def test_exhausted_proposal_stops_cleanly(self):
        self.queue("STATUS: exhausted\n\nNo admissible candidate remains.")
        code = self.run_loop()
        self.assertEqual(code, 3)
        self.assertEqual(self.read_state()["status"], "exhausted")

    def test_prove_context_contains_candidate_and_review_feedback(self):
        self.queue(PROPOSED, COMPLETE, REVISE, COMPLETE, PASS_R, PASS_R)
        self.run_loop()
        revision_request = (
            self.runs / "test-run" / "calls" / "0004-prove" / "request.md"
        ).read_text(encoding="utf-8")
        self.assertIn("An iid-arrival theorem", revision_request)
        self.assertIn("Step 3 uses an unproved bound", revision_request)

    def test_review_context_excludes_graveyard_and_prior_reviews(self):
        self.queue(PROPOSED, REFUTED, PROPOSED, COMPLETE, PASS_R, PASS_R)
        self.run_loop()
        second_review = (
            self.runs / "test-run" / "calls" / "0006-review" / "request.md"
        ).read_text(encoding="utf-8")
        self.assertNotIn("Two-point distribution", second_review)
        self.assertNotIn("Checked every step", second_review)


if __name__ == "__main__":
    unittest.main()
