import random


class Event:
    def __init__(self):
        self.events = [
            {
                'name': 'wolf_attack',
                'handler': self._wolf,
                'weight': 1
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

    def _fish_rod(self):
        print("🎣 Tu trouves une canne à pêche !")
        return
