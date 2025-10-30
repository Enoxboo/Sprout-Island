"""Gestionnaire d'événements aléatoires."""
import random
from models.events.weather import RainEvent, HeatwaveEvent
from models.events.wildlife import AnimalEncounterEvent
from models.events.resources import FindFruitEvent


class EventManager:
    def __init__(self):
        self.events = [
            (RainEvent(), 30),
            (AnimalEncounterEvent(), 20),
            (FindFruitEvent(), 25),
            (HeatwaveEvent(), 20),
        ]
        self.no_event_chance = 5
        self.pending_event = None

    def trigger_random_event(self, player):
        available_events = []
        filtered_weight = 0

        for event, weight in self.events:
            if isinstance(event, RainEvent) and (player.rain_effect_days > 0 or player.heatwave_effect_days > 0):
                filtered_weight += weight
                continue
            if isinstance(event, HeatwaveEvent) and (player.heatwave_effect_days > 0 or player.rain_effect_days > 0):
                filtered_weight += weight
                continue
            available_events.append((event, weight))

        if not available_events:
            return {
                "message": "🌴 Vous explorez les environs de l'île...\n\nRien de particulier à signaler pour le moment.",
                "type": "neutral"
            }

        adjusted_no_event_chance = self.no_event_chance + filtered_weight

        total_weight = sum(weight for _, weight in available_events) + adjusted_no_event_chance
        roll = random.randint(1, total_weight)

        if roll <= adjusted_no_event_chance:
            return {
                "message": "🌴 Vous explorez les environs de l'île...\n\nRien de particulier à signaler pour le moment.",
                "type": "neutral"
            }

        cumulative_weight = adjusted_no_event_chance
        for event, weight in available_events:
            cumulative_weight += weight
            if roll <= cumulative_weight:
                result = event.trigger(player)
                if result.get("type") == "choice":
                    self.pending_event = event
                return result

        return {
            "message": "🌴 Vous explorez les environs tranquillement.",
            "type": "neutral"
        }

    def handle_event_choice(self, player, choice):
        if self.pending_event and hasattr(self.pending_event, 'handle_choice'):
            result = self.pending_event.handle_choice(player, choice)
            self.pending_event = None
            return result
        return None
