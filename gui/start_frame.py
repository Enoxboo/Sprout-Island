from tkinter import Frame, Label, Button

from utils.save_manager import SaveManager


class StartFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(background="#2cdf85")
        self.pack(fill="both", expand=True)

        self.has_save = SaveManager.save_exists()

        self.title_label = Label(
            self,
            text="Bienvenue sur Sprout Island",
            font=("Arial", 32, "bold"),
            background="#2cdf85",
            foreground="white"
        )
        self.title_label.pack(pady=50)

        self.new_game_button = Button(
            self,
            text="Nouvelle Partie",
            font=("Arial", 16),
            background="#4a90e2",
            foreground="white",
            padx=20,
            pady=10,
            command=self.start_new_game
        )
        self.new_game_button.pack(pady=10)

    def start_new_game(self):
        pass