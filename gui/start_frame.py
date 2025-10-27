from tkinter import Frame, Label

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
