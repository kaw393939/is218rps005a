"""Real rule outcomes and request/result checks for RPS-001."""

import pytest

import app as web
from game import determine_winner


@pytest.mark.unit
def test_rock_against_rock():
    """Matching rocks tie."""
    assert determine_winner("rock", "rock") == "tie"


@pytest.mark.unit
def test_rock_against_paper():
    """Paper covers the player's rock."""
    assert determine_winner("rock", "paper") == "lose"


@pytest.mark.unit
def test_rock_against_scissors():
    """Rock beats scissors."""
    assert determine_winner("rock", "scissors") == "win"


@pytest.mark.unit
def test_paper_against_rock():
    """Paper covers rock."""
    assert determine_winner("paper", "rock") == "win"


@pytest.mark.unit
def test_paper_against_paper():
    """Matching papers tie."""
    assert determine_winner("paper", "paper") == "tie"


@pytest.mark.unit
def test_paper_against_scissors():
    """Scissors cut the player's paper."""
    assert determine_winner("paper", "scissors") == "lose"


@pytest.mark.unit
def test_scissors_against_rock():
    """Rock beats the player's scissors."""
    assert determine_winner("scissors", "rock") == "lose"


@pytest.mark.unit
def test_scissors_against_paper():
    """Scissors cut paper."""
    assert determine_winner("scissors", "paper") == "win"


@pytest.mark.unit
def test_scissors_against_scissors():
    """Matching scissors tie."""
    assert determine_winner("scissors", "scissors") == "tie"


@pytest.mark.integration
def test_submitted_rock_loses_to_paper(monkeypatch):
    """A real request uses the rules and displays the predicted loss."""
    monkeypatch.setitem(web.app.config, "TESTING", True)
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")
    with web.app.test_client() as client:
        response = client.post("/", data={"move": "rock"})
    html = response.get_data(as_text=True)
    assert response.status_code == 200
    assert 'data-outcome="lose"' in html
    assert "Computer wins" in html
    assert "You chose" in html and "Rock" in html
    assert "Computer chose" in html and "Paper" in html
    assert "game rules not built yet" not in html
