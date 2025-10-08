from config import (SATIETY_MAX, HYDRATION_MAX, ENERGY_MAX,
                    SATIETY_MIN, HYDRATION_MIN, ENERGY_MIN,
                    SATIETY_GAIN, HYDRATION_GAIN, ENERGY_GAIN,
                    SATIETY_LOSS, HYDRATION_LOSS, ENERGY_LOSS)

from utils.helpers import clamp


class Player:
    def __init__(self, name):
        self.name = name
        self.satiety = SATIETY_MAX
        self.hydration = HYDRATION_MAX
        self.energy = ENERGY_MAX
        self.actions = {
            "fish": self._fish,
            "drink": self._drink,
            "sleep": self._sleep,
            "explore": self._explore,
        }

    def _fish(self):
        self.satiety = clamp(self.satiety + SATIETY_GAIN, SATIETY_MIN, SATIETY_MAX)
        self.energy = clamp(self.energy - ENERGY_LOSS, ENERGY_MIN, ENERGY_MAX)

    def _drink(self):
        self.hydration = clamp(self.hydration + HYDRATION_GAIN, HYDRATION_MIN, HYDRATION_MAX)
        self.energy = clamp(self.energy - ENERGY_LOSS, ENERGY_MIN, ENERGY_MAX)

    def _sleep(self):
        self.energy = clamp(self.energy + ENERGY_GAIN, ENERGY_MIN, ENERGY_MAX)
        self.satiety = clamp(self.satiety - SATIETY_LOSS, SATIETY_MIN, SATIETY_MAX)
        self.hydration = clamp(self.hydration - HYDRATION_LOSS, HYDRATION_MIN, HYDRATION_MAX)

    def _explore(self):
        pass

    def do_action(self, action_name):
        pass
