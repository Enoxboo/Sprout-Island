"""Tests unitaires pour player."""
from models.player import Player
from config import (SATIETY_MAX, HYDRATION_MAX, ENERGY_MAX,
                    SATIETY_MIN, HYDRATION_MIN, ENERGY_MIN,
                    SATIETY_GAIN, HYDRATION_GAIN, ENERGY_GAIN,
                    SATIETY_LOSS, HYDRATION_LOSS, ENERGY_LOSS)


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

    assert player.satiety == 50 + SATIETY_GAIN
    assert player.energy == 100 - ENERGY_LOSS
    print("✓ Fish OK")


def test_drink():
    player = Player("Test")
    player.hydration = 50
    player.energy = 100

    player._drink()

    assert player.hydration == 50 + HYDRATION_GAIN
    assert player.energy == 100 - ENERGY_LOSS
    print("✓ Drink OK")


def test_sleep():
    player = Player("Test")
    player.energy = 50
    player.satiety = 100
    player.hydration = 100

    player._sleep()

    assert player.energy == 50 + ENERGY_GAIN
    assert player.satiety == 100 - SATIETY_LOSS
    assert player.hydration == 100 - HYDRATION_LOSS
    print("✓ Sleep OK")


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
    player.satiety = SATIETY_MIN + 1
    player.hydration = HYDRATION_MIN + 1
    player.energy = ENERGY_MIN + 1

    player._sleep()
    player._fish()

    assert player.satiety >= SATIETY_MIN
    assert player.hydration >= HYDRATION_MIN
    assert player.energy >= ENERGY_MIN
    print("✓ Clamp min OK")


def test_do_action_valid():
    player = Player("Test")
    player.satiety = 50

    result = player.do_action("fish")

    assert result == True
    assert player.satiety == 50 + SATIETY_GAIN
    print("✓ do_action valide OK")


def test_do_action_invalid():
    player = Player("Test")

    result = player.do_action("invalid_action")

    assert result == False
    print("✓ do_action invalide OK")


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
        test_clamp_max()
        test_clamp_min()
        test_do_action_valid()
        test_do_action_invalid()
        test_all_actions()

        print("\n🎉 Tous les tests sont passés !\n")
        return True

    except AssertionError as e:
        print(f"\n❌ Échec du test: {e}\n")
        return False


if __name__ == "__main__":
    run_all_tests()
