from game.game_manager import GameManager
from models.player import Player
from config import DAYS_TO_WIN

def test_increment_day():
    gm = GameManager()
    assert gm.get_days() == 0
    gm.increment_day()
    assert gm.get_days() == 1

def test_win_condition():
    gm = GameManager()
    gm.days = DAYS_TO_WIN
    assert gm.check_win_condition() == True
    assert gm.is_game_over() == True
    assert gm.game_over_reason == "victory"

def test_loss_condition():
    gm = GameManager()
    player = Player("Test")
    player.energy = 0
    assert gm.check_loss_condition(player) == True
    assert gm.is_game_over() == True
    assert gm.game_over_reason == "defeat"

def run_all_tests():
    print("\n=== Lancement des tests ===\n")

    try:
        test_increment_day()
        test_win_condition()
        test_loss_condition()

        print("\n🎉 Tous les tests sont passés !\n")
        return True

    except AssertionError as e:
        print(f"\n❌ Échec du test: {e}\n")
        return False
