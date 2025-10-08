from config import (SATIETY_MAX, HYDRATION_MAX, ENERGY_MAX,
                    SATIETY_MIN, HYDRATION_MIN, ENERGY_MIN,
                    SATIETY_GAIN, HYDRATION_GAIN, ENERGY_GAIN,
                    SATIETY_LOSS, HYDRATION_LOSS, ENERGY_LOSS)

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
        self.satiety += SATIETY_GAIN
        if self.satiety > SATIETY_MAX:
            self.satiety = SATIETY_MAX
        self.energy -= ENERGY_MIN
        if self.energy < ENERGY_MIN:
            self.energy = ENERGY_MIN

    def _drink(self):
        self.hydration += HYDRATION_GAIN
        if self.hydration > HYDRATION_MAX:
            self.hydration = HYDRATION_MAX
        self.energy -= ENERGY_LOSS
        if self.energy < ENERGY_MIN:
            self.energy = ENERGY_MIN

    def _sleep(self):
        self.energy += ENERGY_GAIN
        if self.energy > ENERGY_MAX:
            self.energy = ENERGY_MAX
        self.satiety -= SATIETY_LOSS
        if self.satiety < SATIETY_MIN:
            self.satiety = SATIETY_MIN
        self.hydration -= HYDRATION_LOSS
        if self.hydration > HYDRATION_MIN:
            self.hydration = HYDRATION_MIN

    def _explore(self):
        pass

    def do_action(self, action_name):
        pass