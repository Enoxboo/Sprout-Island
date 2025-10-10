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
                'handler': self._fish_rod,
                'weight': 1
            },
            {
                'name': 'start_raining',
                'handler': self._fish_rod,
                'weight': 2
            },
            {
                'name': 'found_fruit',
                'handler': self._fish_rod,
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
        return

    def _boar(self):
        print("Tu rencontres un sanglier !")
        return

    def _rain(self):
        print("Il pleut")
        return

    def _fruit(self):
        print("Tu trouves un fruit")
        return

    def _fish_rod(self):
        print("🎣 Tu trouves une canne à pêche !")
        return
