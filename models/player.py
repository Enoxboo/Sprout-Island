"""Modèle représentant le joueur et ses actions."""
from config import (SATIETY_MAX, HYDRATION_MAX, ENERGY_MAX,
                    SATIETY_MIN, HYDRATION_MIN, ENERGY_MIN,
                    FISH_SATIETY_GAIN, FISH_ENERGY_LOSS,
                    DRINK_HYDRATION_GAIN, DRINK_ENERGY_LOSS,
                    SLEEP_ENERGY_GAIN, EXPLORE_ENERGY_LOSS,
                    DAILY_SATIETY_LOSS, DAILY_HYDRATION_LOSS,
                    DAILY_ENERGY_LOSS, HEATWAVE_DAILY_HYDRATION_PENALTY)

from utils.helpers import clamp


class Player:
    """
    Représente le joueur avec ses statistiques et actions disponibles.

    Attributes:
        name (str): Nom du joueur
        satiety (int): Niveau de satiété (0-100)
        hydration (int): Niveau d'hydratation (0-100)
        energy (int): Niveau d'énergie (0-100)
    """

    def __init__(self, name):
        self.name: str = name
        self.satiety: int = SATIETY_MAX
        self.hydration: int = HYDRATION_MAX
        self.energy: int = ENERGY_MAX
        self.rain_effect_days: int = 0
        self.heatwave_effect_days: int = 0
        self.actions = {
            "fish": self._fish,
            "drink": self._drink,
            "sleep": self._sleep,
            "explore": self._explore,
        }

    def is_dead(self):
        return self.satiety <= SATIETY_MIN or self.hydration <= HYDRATION_MIN or self.energy <= ENERGY_MIN

    def _fish(self):
        """Pêcher du poisson : augmente la satiété, coûte de l'énergie."""
        self.satiety = clamp(self.satiety + FISH_SATIETY_GAIN, SATIETY_MIN, SATIETY_MAX)
        self.energy = clamp(self.energy - FISH_ENERGY_LOSS, ENERGY_MIN, ENERGY_MAX)

    def _drink(self):
        """Boire de l'eau : augmente l'hydratation, coûte de l'énergie."""
        self.hydration = clamp(self.hydration + DRINK_HYDRATION_GAIN, HYDRATION_MIN, HYDRATION_MAX)
        self.energy = clamp(self.energy - DRINK_ENERGY_LOSS, ENERGY_MIN, ENERGY_MAX)

    def _sleep(self):
        """Dormir : récupère de l'énergie. Les pertes quotidiennes ne sont PAS appliquées après cette action."""
        self.energy = clamp(self.energy + SLEEP_ENERGY_GAIN, ENERGY_MIN, ENERGY_MAX)
        # Important : pas de pertes ici, elles seront gérées différemment dans game_manager

    def _explore(self):
        """Explorer l'île : coûte de l'énergie, peut déclencher des événements."""
        self.energy = clamp(self.energy - EXPLORE_ENERGY_LOSS, ENERGY_MIN, ENERGY_MAX)
        return None

    def do_action(self, action_name):
        action = self.actions.get(action_name)
        if action:
            result = action()
            return result
        return None

    def apply_daily_losses(self):
        """Applique les pertes quotidiennes automatiques à toutes les jauges."""
        self.satiety = clamp(self.satiety - DAILY_SATIETY_LOSS, SATIETY_MIN, SATIETY_MAX)

        hydration_loss = DAILY_HYDRATION_LOSS

        if self.rain_effect_days > 0:
            hydration_loss = 0
            self.rain_effect_days -= 1
        elif self.heatwave_effect_days > 0:
            hydration_loss += HEATWAVE_DAILY_HYDRATION_PENALTY
            self.heatwave_effect_days -= 1

        self.hydration = clamp(self.hydration - hydration_loss, HYDRATION_MIN, HYDRATION_MAX)
        self.energy = clamp(self.energy - DAILY_ENERGY_LOSS, ENERGY_MIN, ENERGY_MAX)

    def status(self):
        print(f"Player status: {self.name}. {self.satiety}. {self.hydration}. {self.energy}.")
