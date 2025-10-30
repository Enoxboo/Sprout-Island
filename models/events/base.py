"""Classe de base pour tous les événements."""
from abc import ABC, abstractmethod


class Event(ABC):
    """Classe abstraite pour tous les événements du jeu."""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def trigger(self, player):
        """Déclenche l'événement et modifie l'état du joueur."""
        pass
