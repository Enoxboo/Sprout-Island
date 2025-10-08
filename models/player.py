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
        self.satiety += 10
        if self.satiety > 100:
            self.satiety = 100
        self.energy -= 10
        if self.energy < 0:
            self.energy = 0

    def _drink(self):
        self.hydration += 10
        if self.hydration > 100:
            self.hydration = 100
        self.energy -= 10
        if self.energy < 0:
            self.energy = 0

    def _sleep(self):
        self.energy += 10
        if self.energy > 100:
            self.energy = 100
        self.satiety -= 10
        if self.satiety < 0:
            self.satiety = 0
        self.hydration -= 10
        if self.hydration > 100:
            self.hydration = 100

    def _explore(self):
        pass

    def do_action(self, action_name):
        pass