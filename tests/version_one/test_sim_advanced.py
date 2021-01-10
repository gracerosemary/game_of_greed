import pytest
from flo import diff
from game_of_greed.game import Game
from game_of_greed.game_logic import GameLogic
pytestmark = [pytest.mark.version_one]
def test_repeat_roller():
    """Allow setting aside scoring dice and rolling the rest
    """
<<<<<<< HEAD
<<<<<<< HEAD
    errors = diff(Game().play, path="tests/version_3/repeat_roller.sim.txt")
=======
    errors = diff(Game().play, path="tests/version_one/repeat_roller.sim.txt")
>>>>>>> e55c8fcdb3bd539212bbb2edec393ceb70a8c3ee
=======
    errors = diff(Game().play, path="tests/version_one/repeat_roller.sim.txt")
>>>>>>> e55c8fcdb3bd539212bbb2edec393ceb70a8c3ee
    assert not errors, errors[0]
def test_hot_dice():
    """When all dice are used without a zilch
    then user gets 6 fresh dice and continues turn.
    """
<<<<<<< HEAD
<<<<<<< HEAD
    errors = diff(Game().play, path="tests/version_3/hot_dice.sim.txt")
=======
    errors = diff(Game().play, path="tests/version_one/hot_dice.sim.txt")
>>>>>>> e55c8fcdb3bd539212bbb2edec393ceb70a8c3ee
=======
    errors = diff(Game().play, path="tests/version_one/hot_dice.sim.txt")
>>>>>>> e55c8fcdb3bd539212bbb2edec393ceb70a8c3ee
    assert not errors, errors[0]
def test_cheat_and_fix():
    """Cheating (or typos) should not be allowed.
    Therefore the user’s input must be validated
    If invalid prompt user for re-entry
    """
<<<<<<< HEAD
<<<<<<< HEAD
    errors = diff(Game().play, path="tests/version_3/cheat_and_fix.sim.txt")
=======
    errors = diff(Game().play, path="tests/version_one/cheat_and_fix.sim.txt")
>>>>>>> e55c8fcdb3bd539212bbb2edec393ceb70a8c3ee
=======
    errors = diff(Game().play, path="tests/version_one/cheat_and_fix.sim.txt")
>>>>>>> e55c8fcdb3bd539212bbb2edec393ceb70a8c3ee
    assert not errors, errors[0]
def test_zilcher():
    """
    No scoring dice results in a ‘zilch’
    which wipes away shelved points
    and ends turn
    """
<<<<<<< HEAD
<<<<<<< HEAD
    errors = diff(Game().play, path="tests/version_3/zilcher.sim.txt")
=======
    errors = diff(Game().play, path="tests/version_one/zilcher.sim.txt")
>>>>>>> e55c8fcdb3bd539212bbb2edec393ceb70a8c3ee
=======
    errors = diff(Game().play, path="tests/version_one/zilcher.sim.txt")
>>>>>>> e55c8fcdb3bd539212bbb2edec393ceb70a8c3ee
    assert not errors, errors[0]