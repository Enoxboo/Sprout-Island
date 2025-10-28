from abc import ABC, abstractmethod


class Event(ABC):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def trigger(self, player):
        pass


class EventManager:
    def __init__(self):
        self.events = []

    def trigger_random_event(self, player):
        return {
            "message": "🌴 Vous explorez les environs de l'île...\nRien de particulier à signaler pour le moment.",
            "type": "neutral"
        }
