import random


class Event:
    def __init__(self):
        self.events = [
            {
                'name': 'wolf_attack',
                'handler': self._wolf,
                'weight': 2
            },
            {
                'name': 'boar_attack',
                'handler': self._boar,
                'weight': 1
            },
            {
                'name': 'start_raining',
                'handler': self._rain,
                'weight': 2
            },
            {
                'name': 'found_fruit',
                'handler': self._fruit,
                'weight': 3
            },
            {
                'name': 'found_fish_rod',
                'handler': self._fish_rod,
                'weight': 1
            },
        ]

    def trigger_daily_event(self):
        event = random.choices(
            self.events,
            weights=[e['weight'] for e in self.events]
        )[0]

        return event['handler']()

    def _wolf(self):
        print("🐺 Tu rencontres un loup !")
        return {'type': 'combat', 'enemy': 'wolf'}

    def _boar(self):
        print("🐗 Tu rencontres un sanglier !")
        return {'type': 'combat', 'enemy': 'boar'}

    def _rain(self):
        print("🌧️ Il commence à pleuvoir...")
        return {'type': 'weather', 'effect': 'rain'}

    def _fruit(self):
        print("🍎 Tu trouves un fruit !")
        return {'type': 'item', 'item': 'fruit'}

    def _fish_rod(self):
        print("🎣 Tu trouves une canne à pêche !")
        return {'type': 'item', 'item': 'fish_rod'}