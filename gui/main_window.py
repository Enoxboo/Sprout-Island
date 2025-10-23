import os
from tkinter import Tk
from gui.button_frame import ButtonsFrame
from gui.dialogue_frame import DialogueFrame
from gui.status_frame import StatusFrame
from models.player import Player


class MainWindow:
    def __init__(self ,player):
        self.main_window = Tk()
        self.main_window.title("Sprout Island")
        self.main_window.geometry("1080x720")
        self.main_window.minsize(480, 360)
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Dossier gui
        project_root = os.path.dirname(script_dir)  # Racine du projet
        ico_path = os.path.join(project_root, "src", "teemo_basic.ico")
        self.main_window.iconbitmap(ico_path)
        self.main_window.config(background="#2cdf85")
        player1 = player
        self.status_frame = StatusFrame(self.main_window , player1)
        self.status_frame.pack(side="top", fill="x")
        self.dialogue_frame = DialogueFrame(self.main_window)
        self.dialogue_frame.update_text("Welcome to Sprout Island!")
        self.buttons_frame = ButtonsFrame(self.main_window)
    def run(self):
        self.main_window.mainloop()
