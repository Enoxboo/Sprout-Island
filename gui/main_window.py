import os
from tkinter import Tk
from gui.button_frame import ButtonsFrame
from gui.dialogue_frame import DialogueFrame
from gui.status_frame import StatusFrame
from game.game_manager import GameManager
from utils.save_manager import SaveManager


class MainWindow:
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

        self.status_frame = StatusFrame(self.main_window, self.player)
        self.status_frame.pack(side="top", fill="x")

        self.dialogue_frame = DialogueFrame(self.main_window)
        self.dialogue_frame.update_text(f"Bienvenue {self.player.name}! Jour {self.game_manager.get_days()}")

        self.buttons_frame = ButtonsFrame(self.main_window)
        self.buttons_frame.set_action_callback(self.handle_action)

        self.main_window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def handle_action(self, action):
        if action == "quit":
            self.main_window.quit()
            return

        if action in self.player.actions:
            self.player.do_action(action)
            self.game_manager.increment_day()
            self.status_frame.update_from_player()

            SaveManager.save_game(self.player, self.game_manager)

            if self.game_manager.check_loss_condition(self.player):
                self.dialogue_frame.update_text("Game Over - Vous n'avez pas survécu...")
                SaveManager.delete_save()
                self.buttons_frame.disable_buttons()
            elif self.game_manager.check_win_condition():
                self.dialogue_frame.update_text(f"Victoire! Vous avez survécu {self.game_manager.get_days()} jours!")
                SaveManager.delete_save()
                self.buttons_frame.disable_buttons()
            else:
                self.dialogue_frame.update_text(f"Jour {self.game_manager.get_days()} - Que voulez-vous faire?")

    def on_closing(self):
        self.main_window.destroy()

    def run(self):
        self.main_window.mainloop()