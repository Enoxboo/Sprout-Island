"""Fenêtre principale du jeu assemblant tous les composants GUI."""
import os
from tkinter import Tk
from gui.button_frame import ButtonsFrame
from gui.dialogue_frame import DialogueFrame
from gui.status_frame import StatusFrame
from game.game_manager import GameManager
from models.events import EventManager
from models.player import Player
from utils.save_manager import SaveManager


class MainWindow:
    """
    Fenêtre principale du jeu qui coordonne l'interface et la logique.
    Gère les interactions entre le joueur, les événements et l'affichage.
    """

    def __init__(self, player, game_manager=None):
        self.main_window = Tk()
        self.main_window.title("Sprout Island")
        self.main_window.geometry("1080x720")
        self.main_window.minsize(480, 360)

        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(script_dir)
        ico_path = os.path.join(project_root, "src", "teemo_basic.ico")
        self.main_window.iconbitmap(ico_path)
        self.main_window.config(background="#F5E6D3")

        self.player = player
        self.game_manager = game_manager if game_manager else GameManager()
        self.event_manager = EventManager()

        self.status_frame = StatusFrame(self.main_window, self.player)
        self.status_frame.pack(side="top", fill="x")

        self.dialogue_frame = DialogueFrame(self.main_window)
        self.dialogue_frame.update_text(f"Bienvenue {self.player.name}! Jour {self.game_manager.get_days()}")

        self.buttons_frame = ButtonsFrame(self.main_window)
        self.buttons_frame.set_action_callback(self.handle_action)

        self.main_window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def run(self):
        self.main_window.mainloop()

    def on_closing(self):
        self.main_window.destroy()

    def handle_action(self, action):
        if action == "quit":
            self.main_window.quit()
            return

        if action == "replay":
            self.restart_game()
            return

        if action in ["flee", "hunt"]:
            result = self.event_manager.handle_event_choice(self.player, action)

            if result:
                self.buttons_frame.hide_choice_buttons()
                self.status_frame.update_from_player()
                self._check_end_game_conditions(result["message"])
            return

        if action in self.player.actions:
            self.game_manager.increment_day()

            self.game_manager.apply_new_day_penalties(self.player)

            result = self.player.do_action(action)
            self.status_frame.update_from_player()
            SaveManager.save_game(self.player, self.game_manager)

            if action == "explore":
                event_result = self.event_manager.trigger_random_event(self.player)
                self.status_frame.update_from_player()

                if event_result.get("type") == "choice":
                    self.dialogue_frame.update_text(event_result["message"])
                    self.buttons_frame.show_choice_buttons(event_result["choices"])
                    return

                self._check_end_game_conditions(event_result["message"])
            else:
                default_message = f"☀️ Jour {self.game_manager.get_days()} - Que voulez-vous faire?"
                self._check_end_game_conditions(default_message)

    def _check_end_game_conditions(self, default_message):
        """Vérifie les conditions de fin de partie et affiche le message approprié."""
        if self.game_manager.check_loss_condition(self.player):
            self.dialogue_frame.update_text(
                f"💀 Game Over - Vous n'avez pas survécu plus de {self.game_manager.get_days()} jours...")
            SaveManager.delete_save()
            self.show_game_over_buttons()
        elif self.game_manager.check_win_condition():
            self.dialogue_frame.update_text(
                f"🎉 Victoire! Vous avez survécu {self.game_manager.get_days()} jours!")
            SaveManager.delete_save()
            self.show_game_over_buttons()
        else:
            self.dialogue_frame.update_text(default_message)

    def show_game_over_buttons(self):
        """Affiche les boutons Rejouer et Quitter à la fin de partie."""
        self.buttons_frame.show_choice_buttons(["replay"])

    def restart_game(self):
        """Redémarre une nouvelle partie avec le même joueur."""
        player_name = self.player.name

        self.player = Player(player_name)

        self.game_manager = GameManager()

        self.event_manager = EventManager()

        self.status_frame.player = self.player
        self.status_frame.update_from_player()

        self.buttons_frame.hide_choice_buttons()
        self.buttons_frame.enable_buttons()

        self.dialogue_frame.update_text(f"Bienvenue {self.player.name}! Jour {self.game_manager.get_days()}")
