class Player:
    def __init__(self, name):
        self.name = name
        self.satiety = 100
        self.hydration = 100
        self.energy = 100
        self.actions = {
            "fish": self._fish,
            "drink": self._drink,
            "sleep": self._sleep,
            "explore": self._explore,
        }

    def _fish(self):
        pass

    def _drink(self):
        pass

    def _sleep(self):
        pass

    def _explore(self):
        pass

    def do_action(self, action_name):
        pass