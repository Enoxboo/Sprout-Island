from game.events import Event
from models.player import Player


def test_wolf_event():
    event = Event()
    result = event._wolf()

    assert result is not None, "L'événement doit retourner un résultat"
    assert result['type'] == 'combat', "Le loup doit être un événement de combat"
    assert result['enemy'] == 'wolf', "L'ennemi doit être un loup"


def test_boar_event():
    event = Event()
    result = event._boar()

    assert result is not None, "L'événement doit retourner un résultat"
    assert result['type'] == 'combat', "Le sanglier doit être un événement de combat"
    assert result['enemy'] == 'boar', "L'ennemi doit être un sanglier"


def test_rain_event():
    event = Event()
    result = event._rain()

    assert result is not None, "L'événement doit retourner un résultat"
    assert result['type'] == 'weather', "La pluie doit être un événement météo"
    assert result['effect'] == 'rain', "L'effet doit être la pluie"



def test_fruit_event():
    event = Event()
    result = event._fruit()

    assert result is not None, "L'événement doit retourner un résultat"
    assert result['type'] == 'item', "Le fruit doit être un événement objet"
    assert result['item'] == 'fruit', "L'objet doit être un fruit"



def test_fish_rod_event():
    event = Event()
    result = event._fish_rod()

    assert result is not None, "L'événement doit retourner un résultat"
    assert result['type'] == 'item', "La canne doit être un événement objet"
    assert result['item'] == 'fish_rod', "L'objet doit être une canne à pêche"



def test_crampte_event():
    event = Event()
    result = event._crampte()

    assert result is not None, "L'événement doit retourner un résultat"
    assert result['type'] == 'item', "Les cramptés doivent être un événement objet"
    assert result['item'] == 'crampte', "L'objet doit être des cramptés"



def test_trigger_explore_event():
    event = Event()
    result = event.trigger_explore_event()

    assert result is not None, "Un événement doit être déclenché"
    assert 'type' in result, "Le résultat doit avoir un type"
    assert result['type'] in ['combat', 'item', 'weather'], "Le type doit être valide"



def test_all_events_can_trigger():
    event = Event()
    event_names_found = set()

    for _ in range(500):
        result = event.trigger_explore_event()

        if result.get('enemy') == 'wolf':
            event_names_found.add('wolf')
        elif result.get('enemy') == 'boar':
            event_names_found.add('boar')
        elif result.get('effect') == 'rain':
            event_names_found.add('rain')
        elif result.get('item') == 'fruit':
            event_names_found.add('fruit')
        elif result.get('item') == 'fish_rod':
            event_names_found.add('fish_rod')
        elif result.get('item') == 'crampte':
            event_names_found.add('crampte')

    assert len(event_names_found) >= 4, f"Seulement {len(event_names_found)} événements trouvés: {event_names_found}"


def test_player_explore_reduces_energy():
    player = Player("Test")
    initial_energy = player.energy

    player._explore()

    assert player.energy < initial_energy, "L'exploration doit réduire l'énergie"


def test_player_rain_increases_hydration():
    player = Player("Test")
    player.hydration = 50
    initial_hydration = player.hydration

    player._handle_weather({'type': 'weather', 'effect': 'rain'})

    assert player.hydration > initial_hydration, "La pluie doit augmenter l'hydratation"


def run_all_tests():
    try:
        test_wolf_event()
        test_boar_event()
        test_rain_event()
        test_fruit_event()
        test_fish_rod_event()
        test_crampte_event()
        test_trigger_explore_event()
        test_all_events_can_trigger()
        test_player_explore_reduces_energy()
        test_player_rain_increases_hydration()

        print("\n🎉 Tous les tests sont passés !\n")
        return True

    except AssertionError as e:
        print(f"\n❌ Échec du test: {e}\n")
        return False
