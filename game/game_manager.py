from config import DAYS_TO_WIN


class GameManager:
    def __init__(self):
        self.game_over = False
        self.days = 0

    def increment_day(self):
        """Incrémente le compteur de jours"""
        self.days += 1

    def check_win_condition(self):
        """Vérifie si la condition de victoire est atteinte"""
        if self.days >= DAYS_TO_WIN:
            self.game_over = True
            return True
        return False

    def is_game_over(self):
        """Retourne l'état du jeu"""
        return self.game_over

    def end_game(self):
        """Termine le jeu manuellement"""
        self.game_over = True

    def get_days(self):
        """Retourne le nombre de jours écoulés"""
        return self.days