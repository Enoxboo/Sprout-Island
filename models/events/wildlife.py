"""Événements liés à la faune."""
from models.events.base import Event


class AnimalEncounterEvent(Event):
    def __init__(self):
        super().__init__(
            "Rencontre dangereuse",
            "Un animal sauvage apparaît devant vous!"
        )

    def trigger(self, player):
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
