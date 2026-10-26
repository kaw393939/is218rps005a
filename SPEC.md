# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** one person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan

- Implement all nine outcomes above in `determine_winner(player, computer)` using the player's perspective.
- Predicted example: the player chooses Rock and the computer chooses Paper. Paper covers Rock, so the computer wins and the function returns `lose`. A valid losing round is a positive case.
- Keep the supplied interface and server. Display both choices and the correct result, and let the player start another independent round. No score or saved history.
- Reject missing or unsupported moves, such as `banana`, with HTTP 400 and a helpful invalid-move message so the player can try again. Reuse the supplied validation checks.
- Add nine explicit unit outcomes, a real request/result integration check, and a real-browser round with replay. Fix only the computer's random choice in request/browser tests; exercise the real rules.
- Run `.venv/bin/python check.py` for formatting, analysis, non-browser tests, and Chromium tests. Review the diff against this spec, discuss the Rock-versus-Paper test, then have the student play and describe an actual round.

### Checks

Before coding, agree this small test plan with AI:

| Level | Cases and evidence |
| --- | --- |
| Unit — positive | All nine literal expected results above, including valid losses and ties. |
| Integration — positive | A submitted round uses the real rule function and displays both choices and the correct result. Fix the computer choice for the test. |
| Integration — negative | Reuse supplied missing/unsupported-move tests: HTTP 400 and a helpful explanation, without calling the rules. A crash is not the intended result. |
| E2E — positive | Add a real-browser round and replay in tests/e2e/test_round.py using the supplied live_server/page fixtures. Fix only the computer choice; use real rules and real HTTP. |

Use `unit`, `integration`, and `e2e` pytest markers. Run `.venv/bin/python check.py` for Black, Pylint, fast tests, and browser checks; then review the diff. Keep shared settings and meaningful assertions intact. The student still plays, inspects a rule and its test, and gives feedback. Browser automation does not establish every aspect of usability or application performance.

### Work record

- Issue: [RPS-001: Play a round #1](https://github.com/kaw393939/is218rps005a/issues/1).
- Pull request: [RPS-001: Play a round #2](https://github.com/kaw393939/is218rps005a/pull/2).
- CI: [Python checks run](https://github.com/kaw393939/is218rps005a/actions/runs/40385386038).
- Implementation: [game.py](game.py) implements all nine outcomes for independent rounds using the supplied server and interface.
- Checks: `.venv/bin/python check.py` passed Black, Pylint, 23 non-browser tests, and 6 Chromium tests on 2026-10-26. [Unit and integration tests](tests/test_game.py) cover all nine literal outcomes and the real Rock-versus-Paper request. [Browser round and replay](tests/e2e/test_round.py) verifies a loss followed by a win using real rules. Supplied invalid/missing-input tests remain intact.
- Review: inspected the changed code and both new test files against this spec; `git diff --check` passed. Changes are limited to the rules, feature tests, and this spec.
- Manual browser observation: the student chose Rock, the computer chose Paper, and the page displayed "Computer wins". The student explained that Paper covers Rock and confirmed they could play again.
