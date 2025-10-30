"""Tests unitaires pour le système d'événements."""
from models.events.weather import RainEvent, HeatwaveEvent
from models.events.wildlife import AnimalEncounterEvent
from models.events.resources import FindFruitEvent
from models.events.manager import EventManager
from models.player import Player
from config import (RAIN_HYDRATION_GAIN, HYDRATION_MAX, HEATWAVE_HYDRATION_LOSS,
                    HEATWAVE_ENERGY_LOSS, FRUIT_SATIETY_GAIN, FRUIT_HYDRATION_GAIN)


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

    assert player.hydration == 50 + RAIN_HYDRATION_GAIN
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
    print("✓ RainEvent clamp max OK")


def test_heatwave_event_trigger():
    player = Player("Test")
    player.hydration = 80
    player.energy = 80

    event = HeatwaveEvent()
    result = event.trigger(player)

    assert player.hydration == 80 - HEATWAVE_HYDRATION_LOSS
    assert player.energy == 80 - HEATWAVE_ENERGY_LOSS
    assert player.heatwave_effect_days == 3
    assert result["type"] == "negative"
    assert "🌡️" in result["message"]
    print("✓ Déclenchement HeatwaveEvent OK")


def test_animal_encounter_choice():
    player = Player("Test")
    event = AnimalEncounterEvent()

    result = event.trigger(player)
    assert result["type"] == "choice"
    assert "flee" in result["choices"]
    assert "hunt" in result["choices"]
    print("✓ AnimalEncounterEvent choix OK")


def test_animal_flee():
    player = Player("Test")
    player.energy = 80

    event = AnimalEncounterEvent()
    event.trigger(player)
    result = event.handle_choice(player, "flee")

    assert player.energy < 80
    assert result["type"] == "negative"
    assert "🏃" in result["message"]
    print("✓ AnimalEncounterEvent fuite OK")


def test_animal_hunt():
    player = Player("Test")
    player.energy = 80
    player.satiety = 50

    event = AnimalEncounterEvent()
    event.trigger(player)
    result = event.handle_choice(player, "hunt")

    assert player.energy < 80
    assert player.satiety > 50
    assert result["type"] == "positive"
    assert "⚔️" in result["message"]
    print("✓ AnimalEncounterEvent chasse OK")


def test_find_fruit_event():
    player = Player("Test")
    player.satiety = 50
    player.hydration = 50

    event = FindFruitEvent()
    result = event.trigger(player)

    assert player.satiety == 50 + FRUIT_SATIETY_GAIN
    assert player.hydration == 50 + FRUIT_HYDRATION_GAIN
    assert result["type"] == "positive"
    assert "🥭" in result["message"]
    print("✓ FindFruitEvent OK")


def test_event_manager_init():
    manager = EventManager()

    assert len(manager.events) == 4
    assert manager.no_event_chance == 5

    event_types = [type(event).__name__ for event, _ in manager.events]
    assert "RainEvent" in event_types
    assert "HeatwaveEvent" in event_types
    assert "AnimalEncounterEvent" in event_types
    assert "FindFruitEvent" in event_types
    print("✓ Initialisation EventManager OK")


def test_event_manager_weather_exclusion():
    manager = EventManager()
    player = Player("Test")
    player.rain_effect_days = 2

    for _ in range(20):
        result = manager.trigger_random_event(player)

        # Vérifie qu'aucune canicule ne se déclenche pendant la pluie
        if result["type"] != "neutral":
            assert "🌡️" not in result["message"]

    print("✓ EventManager exclusion météo OK")


def test_event_manager_trigger():
    manager = EventManager()
    player = Player("Test")

    event_types = {"neutral": 0, "positive": 0, "negative": 0, "choice": 0}

    for _ in range(100):
        player.hydration = 50
        player.satiety = 50
        player.energy = 50
        result = manager.trigger_random_event(player)

        assert "message" in result
        assert "type" in result
        event_types[result["type"]] += 1

    assert event_types["neutral"] > 0
    print(
        f"✓ EventManager distribution OK (Neutres: {event_types['neutral']}, Positifs: {event_types['positive']}, Négatifs: {event_types['negative']}, Choix: {event_types['choice']})")


def test_event_manager_pending_event():
    manager = EventManager()
    player = Player("Test")

    manager.events = [(AnimalEncounterEvent(), 100)]
    manager.no_event_chance = 0

    result = manager.trigger_random_event(player)
    assert result["type"] == "choice"
    assert manager.pending_event is not None

    choice_result = manager.handle_event_choice(player, "flee")
    assert choice_result is not None
    assert manager.pending_event is None
    print("✓ EventManager gestion pending_event OK")


def run_all_tests():
    print("\n=== Tests du système d'événements ===\n")

    try:
        test_rain_event_init()
        test_rain_event_trigger()
        test_rain_event_clamp_max()
        test_heatwave_event_trigger()
        test_animal_encounter_choice()
        test_animal_flee()
        test_animal_hunt()
        test_find_fruit_event()
        test_event_manager_init()
        test_event_manager_weather_exclusion()
        test_event_manager_trigger()
        test_event_manager_pending_event()

        print("\n🎉 Tous les tests sont passés !\n")
        return True

    except AssertionError as e:
        print(f"\n❌ Échec du test: {e}\n")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    run_all_tests()
