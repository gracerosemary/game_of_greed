import pytest
from flo import diff
from game_of_greed.game import Game
from game_of_greed.game_logic import GameLogic
pytestmark = [pytest.mark.version_one]
def test_repeat_roller():
    """Allow setting aside scoring dice and rolling the rest
    """
    errors = diff(Game().play, path="tests/version_one/repeat_roller.sim.txt")
    assert not errors, errors[0]
def test_hot_dice():
    """When all dice are used without a zilch
    then user gets 6 fresh dice and continues turn.
    """
    errors = diff(Game().play, path="tests/version_one/hot_dice.sim.txt")
    assert not errors, errors[0]
def test_cheat_and_fix():
    """Cheating (or typos) should not be allowed.
    Therefore the user’s input must be validated
    If invalid prompt user for re-entry
    """
    errors = diff(Game().play, path="tests/version_one/cheat_and_fix.sim.txt")
    assert not errors, errors[0]
def test_zilcher():
    """
    No scoring dice results in a ‘zilch’
    which wipes away shelved points
    and ends turn
    """
    errors = diff(Game().play, path="tests/version_one/zilcher.sim.txt")
    assert not errors, errors[0]