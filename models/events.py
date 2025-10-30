"""Système d'événements aléatoires du jeu."""
import random
from abc import ABC, abstractmethod


class Event(ABC):
    """Classe abstraite pour tous les événements du jeu."""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def trigger(self, player):
        """Déclenche l'événement et modifie l'état du joueur."""
        pass


class RainEvent(Event):
    def __init__(self):
        super().__init__(
            "Pluie rafraîchissante",
            "Une pluie bienfaisante commence à tomber sur l'île."
        )

    def trigger(self, player):
        from config import RAIN_HYDRATION_GAIN, HYDRATION_MAX
        from utils.helpers import clamp

        old_hydration = player.hydration
        player.hydration = clamp(
            player.hydration + RAIN_HYDRATION_GAIN,
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
    """Événement de rencontre animale avec choix interactif (fuir/chasser)."""

    def __init__(self):
        super().__init__(
            "Rencontre dangereuse",
            "Un animal sauvage apparaît devant vous!"
        )

    def trigger(self, player):
        """Retourne les options de choix au joueur."""
        return {
            "message": (
                f"🐗 {self.description}\n\n"
                f"Voulez-vous fuir ou tenter de le chasser?"
            ),
            "type": "choice",
            "event_type": "animal_encounter",
            "choices": ["flee", "hunt"]
        }

    def handle_choice(self, player, choice):
        """
        Traite le choix du joueur (fuir ou chasser).

        Args:
            player: Instance du joueur
            choice: "flee" ou "hunt"

        Returns:
            dict: Résultat de l'action avec message et type
        """
        from config import (ANIMAL_FLEE_ENERGY_LOSS, ANIMAL_HUNT_ENERGY_LOSS,
                            ANIMAL_HUNT_SATIETY_GAIN, SATIETY_MAX, ENERGY_MIN)
        from utils.helpers import clamp

        if choice == "flee":
            old_energy = player.energy
            player.energy = clamp(
                player.energy - ANIMAL_FLEE_ENERGY_LOSS,
                ENERGY_MIN,
                player.energy
            )
            loss = old_energy - player.energy

            return {
                "message": (
                    f"🏃 Vous prenez la fuite!\n\n"
                    f"L'animal ne vous poursuit pas.\n"
                    f"⚡ Énergie -{loss}"
                ),
                "type": "negative"
            }

        elif choice == "hunt":
            old_energy = player.energy
            old_satiety = player.satiety

            player.energy = clamp(
                player.energy - ANIMAL_HUNT_ENERGY_LOSS,
                ENERGY_MIN,
                player.energy
            )
            player.satiety = clamp(
                player.satiety + ANIMAL_HUNT_SATIETY_GAIN,
                0,
                SATIETY_MAX
            )

            energy_loss = old_energy - player.energy
            satiety_gain = player.satiety - old_satiety

            return {
                "message": (
                    f"⚔️ Vous chassez l'animal avec succès!\n\n"
                    f"Vous récupérez de la viande fraîche.\n"
                    f"⚡ Énergie -{energy_loss}\n"
                    f"🍖 Satiété +{satiety_gain}"
                ),
                "type": "positive"
            }

        return {
            "message": "❌ Choix invalide.",
            "type": "neutral"
        }


class EventManager:
    """Gère le déclenchement aléatoire des événements selon leurs probabilités."""

    def __init__(self):
        self.events = [
            (RainEvent(), 30),
            (AnimalEncounterEvent(), 20),
        ]
        self.no_event_chance = 50
        self.pending_event = None

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
            self.pending_event = None  # Reset l'événement en attente
            return result
        return None