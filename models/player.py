from config import (SATIETY_MAX, HYDRATION_MAX, ENERGY_MAX,
                    SATIETY_MIN, HYDRATION_MIN, ENERGY_MIN,
                    SATIETY_GAIN, HYDRATION_GAIN, ENERGY_GAIN,
                    SATIETY_LOSS, HYDRATION_LOSS, ENERGY_LOSS)
from game.events import Event

from utils.helpers import clamp


class Player:
    def __init__(self, name):
        self.name: str = name
        self.satiety: int = SATIETY_MAX
        self.hydration: int = HYDRATION_MAX
        self.energy: int = ENERGY_MAX
        self.actions = {
            "fish": self._fish,
            "drink": self._drink,
            "sleep": self._sleep,
            "explore": self._explore,
        }

    def is_dead(self):
        return self.satiety <= SATIETY_MIN or self.hydration <= HYDRATION_MIN or self.energy <= ENERGY_MIN

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
        event_result = Event().trigger_explore_event()

        if event_result['type'] == 'item':
            self._handle_item_found(event_result)
        elif event_result['type'] == 'weather':
            self._handle_weather(event_result)

        self.energy = clamp(self.energy - ENERGY_LOSS, ENERGY_MIN, ENERGY_MAX)

    def do_action(self, action_name):
        action = self.actions.get(action_name)
        if action:
            action()
            return True
        return False

    def _handle_item_found(self, event_result):
        item = event_result['item']

        if item == 'fruit':
            self.satiety = clamp(self.satiety + 5, SATIETY_MIN, SATIETY_MAX)
            print(f"→ Tu manges le fruit (+5 satiété)")

    def _handle_weather(self, event_result):
        effect = event_result['effect']

        if effect == 'rain':
            self.hydration = clamp(self.hydration + 10, HYDRATION_MIN, HYDRATION_MAX)
            print(f"→ Tu récupères de l'eau de pluie (+10 hydratation)")

    def status(self):
        print(f"Player status: {self.name}. {self.satiety}. {self.hydration}. {self.energy}.")
