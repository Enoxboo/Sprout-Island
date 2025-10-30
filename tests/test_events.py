"""Tests unitaires pour events."""
from models.events import Event, RainEvent, EventManager
from models.player import Player
from config import HYDRATION_GAIN, HYDRATION_MAX, HYDRATION_MIN


def test_rain_event_init():
    event = RainEvent()
    assert event.name == "Pluie rafraîchissante"
    assert event.description == "Une pluie bienfaisante commence à tomber sur l'île."
    print("✓ Initialisation RainEvent OK")


def test_rain_event_trigger():
    player = Player("Test")
    player.hydration = 50

    event = RainEvent()
    result = event.trigger(player)

    assert player.hydration == 50 + HYDRATION_GAIN

    assert "message" in result
    assert "type" in result
    assert result["type"] == "positive"
    assert "☔" in result["message"]
    assert "💧" in result["message"]
    print("✓ Déclenchement RainEvent OK")


def test_rain_event_clamp_max():
    player = Player("Test")
    player.hydration = HYDRATION_MAX

    event = RainEvent()
    result = event.trigger(player)

    assert player.hydration == HYDRATION_MAX
    assert player.hydration <= HYDRATION_MAX
    print("✓ RainEvent clamp max OK")


def test_rain_event_near_max():
    player = Player("Test")
    player.hydration = HYDRATION_MAX - 10

    event = RainEvent()
    result = event.trigger(player)

    assert player.hydration == HYDRATION_MAX
    assert "+10" in result["message"]
    print("✓ RainEvent gain partiel OK")


def test_event_manager_init():
    manager = EventManager()

    assert len(manager.events) == 1
    assert manager.no_event_chance == 70

    event, weight = manager.events[0]
    assert isinstance(event, RainEvent)
    assert weight == 30
    print("✓ Initialisation EventManager OK")


def test_event_manager_probabilities():
    manager = EventManager()

    total_weight = sum(weight for _, weight in manager.events) + manager.no_event_chance

    assert total_weight == 100
    print("✓ Probabilités EventManager OK")


def test_event_manager_trigger():
    manager = EventManager()
    player = Player("Test")
    initial_hydration = player.hydration

    no_event_count = 0
    rain_event_count = 0

    for _ in range(50):
        player.hydration = 50
        result = manager.trigger_random_event(player)

        assert "message" in result
        assert "type" in result

        if result["type"] == "neutral":
            no_event_count += 1
        elif result["type"] == "positive":
            rain_event_count += 1

    assert no_event_count > 0

    assert rain_event_count > 0

    print(f"✓ EventManager trigger OK (Neutres: {no_event_count}, Pluie: {rain_event_count})")


def test_event_manager_no_event():
    manager = EventManager()
    manager.no_event_chance = 100
    manager.events = []

    player = Player("Test")
    initial_hydration = player.hydration

    result = manager.trigger_random_event(player)

    assert player.hydration == initial_hydration
    assert result["type"] == "neutral"
    assert "🌴" in result["message"]
    print("✓ EventManager aucun événement OK")


def test_event_manager_guaranteed_rain():
    manager = EventManager()
    manager.no_event_chance = 0
    manager.events = [(RainEvent(), 100)]

    player = Player("Test")
    player.hydration = 50

    result = manager.trigger_random_event(player)

    assert player.hydration == 50 + HYDRATION_GAIN
    assert result["type"] == "positive"
    assert "☔" in result["message"]
    print("✓ EventManager pluie forcée OK")


def test_explore_integration():
    player = Player("Test")
    initial_energy = player.energy

    result = player._explore()

    from config import ENERGY_LOSS
    assert player.energy == initial_energy - ENERGY_LOSS

    assert result is not None
    assert "message" in result
    assert "type" in result
    print("✓ Intégration _explore OK")


def run_all_tests():
    print("\n=== Tests du système d'événements ===\n")

    try:
        test_rain_event_init()
        test_rain_event_trigger()
        test_rain_event_clamp_max()
        test_rain_event_near_max()
        test_event_manager_init()
        test_event_manager_probabilities()
        test_event_manager_trigger()
        test_event_manager_no_event()
        test_event_manager_guaranteed_rain()
        test_explore_integration()

        print("\n🎉 Tous les tests sont passés !\n")
        return True

    except AssertionError as e:
        print(f"\n❌ Échec du test: {e}\n")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    run_all_tests()
