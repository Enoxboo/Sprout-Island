import random
from abc import ABC, abstractmethod


class Event(ABC):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def trigger(self, player):
        pass


class RainEvent(Event):
    def __init__(self):
        super().__init__(
            "Pluie rafraîchissante",
            "Une pluie bienfaisante commence à tomber sur l'île."
        )

    def trigger(self, player):
        from config import HYDRATION_GAIN, HYDRATION_MAX
        from utils.helpers import clamp

        old_hydration = player.hydration
        player.hydration = clamp(
            player.hydration + HYDRATION_GAIN,
            0,
            HYDRATION_MAX
        )
        gain = player.hydration - old_hydration

        return {
            "message": (
                f"☔ {self.description}\n\n"
                f"Vous collectez de l'eau fraîche dans vos mains.\n"
                f"💧 Hydratation +{gain}"
            ),
            "type": "positive"
        }

class AnimalEncounterEvent(Event):
    def __init__(self):
        super().__init__(
            "Rencontre dangereuse",
            "Un animal sauvage vous attaque!"
        )

    def trigger(self, player):
        from config import ENERGY_LOSS, ENERGY_MIN
        from utils.helpers import clamp

        old_energy = player.energy
        damage = ENERGY_LOSS * 2
        player.energy = clamp(
            player.energy - damage,
            ENERGY_MIN,
            player.energy
        )
        loss = old_energy - player.energy

        return {
            "message": (
                f"🐗 {self.description}\n\n"
                f"Vous réussissez à le repousser mais vous êtes épuisé.\n"
                f"⚡ Énergie -{loss}"
            ),
            "type": "negative"
        }


class EventManager:
    def __init__(self):
        self.events = [
            (RainEvent(), 30),
            (AnimalEncounterEvent(), 20),
        ]
        self.no_event_chance = 50

    def trigger_random_event(self, player):
        total_weight = sum(weight for _, weight in self.events) + self.no_event_chance

        roll = random.randint(1, total_weight)

        if roll <= self.no_event_chance:
            return {
                "message": "🌴 Vous explorez les environs de l'île...\n\nRien de particulier à signaler pour le moment.",
                "type": "neutral"
            }

        cumulative_weight = self.no_event_chance
        for event, weight in self.events:
            cumulative_weight += weight
            if roll <= cumulative_weight:
                return event.trigger(player)

        return {
            "message": "🌴 Vous explorez les environs tranquillement.",
            "type": "neutral"
        }
