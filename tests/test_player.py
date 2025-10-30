"""Tests unitaires pour player."""
from models.player import Player
from config import (SATIETY_MAX, HYDRATION_MAX, ENERGY_MAX,
                    SATIETY_MIN, HYDRATION_MIN, ENERGY_MIN,
                    FISH_SATIETY_GAIN, DRINK_HYDRATION_GAIN, SLEEP_ENERGY_GAIN,
                    DAILY_SATIETY_LOSS, DAILY_HYDRATION_LOSS, FISH_ENERGY_LOSS,
                    DRINK_ENERGY_LOSS)


def test_player_init():
    player = Player("Alice")
    assert player.name == "Alice"
    assert player.satiety == SATIETY_MAX
    assert player.hydration == HYDRATION_MAX
    assert player.energy == ENERGY_MAX
    print("✓ Initialisation OK")


def test_fish():
    player = Player("Test")
    player.satiety = 50
    player.energy = 100

    player._fish()

    assert player.satiety == 50 + FISH_SATIETY_GAIN
    assert player.energy == 100 - FISH_ENERGY_LOSS
    print("✓ Fish OK")


def test_drink():
    player = Player("Test")
    player.hydration = 50
    player.energy = 100

    player._drink()

    assert player.hydration == 50 + DRINK_HYDRATION_GAIN
    assert player.energy == 100 - DRINK_ENERGY_LOSS
    print("✓ Drink OK")


def test_sleep():
    """Test que dormir récupère de l'énergie SANS appliquer les pertes quotidiennes."""
    player = Player("Test")
    player.energy = 50
    player.satiety = 100
    player.hydration = 100

    player._sleep()

    # Dormir récupère SEULEMENT l'énergie, pas de pertes
    assert player.energy == min(50 + SLEEP_ENERGY_GAIN, ENERGY_MAX)
    assert player.satiety == 100  # Pas de perte !
    assert player.hydration == 100  # Pas de perte !
    print("✓ Sleep OK")


def test_apply_daily_losses():
    """Test que les pertes quotidiennes sont appliquées correctement."""
    player = Player("Test")
    player.satiety = 100
    player.hydration = 100
    player.energy = 100

    player.apply_daily_losses()

    assert player.satiety == 100 - DAILY_SATIETY_LOSS
    assert player.hydration == 100 - DAILY_HYDRATION_LOSS
    print("✓ Apply daily losses OK")


def test_clamp_max():
    player = Player("Test")
    player.satiety = SATIETY_MAX
    player.hydration = HYDRATION_MAX
    player.energy = ENERGY_MAX

    player._fish()
    player._drink()
    player._sleep()

    assert player.satiety <= SATIETY_MAX
    assert player.hydration <= HYDRATION_MAX
    assert player.energy <= ENERGY_MAX
    print("✓ Clamp max OK")


def test_clamp_min():
    player = Player("Test")
    player.satiety = SATIETY_MIN + 5
    player.hydration = HYDRATION_MIN + 5
    player.energy = ENERGY_MIN + 5

    # Forcer des pertes importantes
    for _ in range(10):
        player.apply_daily_losses()

    assert player.satiety >= SATIETY_MIN
    assert player.hydration >= HYDRATION_MIN
    assert player.energy >= ENERGY_MIN
    print("✓ Clamp min OK")


def test_do_action_valid():
    player = Player("Test")
    player.satiety = 50

    result = player.do_action("fish")

    # do_action retourne None pour les actions normales
    assert result is None
    assert player.satiety == 50 + FISH_SATIETY_GAIN
    print("✓ do_action valide OK")


def test_do_action_invalid():
    player = Player("Test")

    result = player.do_action("invalid_action")

    assert result is None
    print("✓ do_action invalide OK")


def test_is_dead():
    """Test que is_dead() détecte correctement les conditions de mort."""
    player = Player("Test")

    # Joueur vivant
    assert player.is_dead() == False

    # Tester chaque condition de mort
    player.satiety = SATIETY_MIN
    assert player.is_dead() == True

    player.satiety = SATIETY_MAX
    player.hydration = HYDRATION_MIN
    assert player.is_dead() == True

    player.hydration = HYDRATION_MAX
    player.energy = ENERGY_MIN
    assert player.is_dead() == True

    print("✓ is_dead OK")


def test_all_actions():
    player = Player("Test")

    assert "fish" in player.actions
    assert "drink" in player.actions
    assert "sleep" in player.actions
    assert "explore" in player.actions
    print("✓ Toutes les actions présentes OK")


def run_all_tests():
    print("\n=== Lancement des tests ===\n")

    try:
        test_player_init()
        test_fish()
        test_drink()
        test_sleep()
        test_apply_daily_losses()
        test_clamp_max()
        test_clamp_min()
        test_do_action_valid()
        test_do_action_invalid()
        test_is_dead()
        test_all_actions()

        print("\n🎉 Tous les tests sont passés !\n")
        return True

    except AssertionError as e:
        print(f"\n❌ Échec du test: {e}\n")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    run_all_tests()