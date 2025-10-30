"""Gestionnaire de l'état global du jeu (jours, victoire, défaite)."""
from config import DAYS_TO_WIN


class GameManager:
    def __init__(self):
        self.game_over = False
        self.days = 0
        self.game_over_reason = ""

    def increment_day(self):
        self.days += 1

    def check_win_condition(self):
        if self.days >= DAYS_TO_WIN:
            self.end_game(reason="victory")
            return True
        return False

    def is_game_over(self):
        return self.game_over

    def end_game(self, reason=""):
        self.game_over = True
        self.game_over_reason = reason

    def check_loss_condition(self, player):
        if player.is_dead():
            self.end_game(reason="defeat")
            return True
        return False

    def get_days(self):
        return self.days
