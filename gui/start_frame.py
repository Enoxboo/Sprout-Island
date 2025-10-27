from tkinter import Frame, Label, Button, Entry

from game.game_manager import GameManager
from utils.save_manager import SaveManager
from models.player import Player
from gui.main_window import MainWindow

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

        if self.has_save:
            self.load_game_button = Button(
                self,
                text="Charger Partie",
                font=("Arial", 16),
                background="#e2a04a",
                foreground="white",
                padx=20,
                pady=10,
                command=self.load_existing_game
            )
            self.load_game_button.pack(pady=10)

    def load_existing_game(self):
        save_data = SaveManager.load_game()

        if save_data is None:
            print("Erreur lors du chargement de la sauvegarde!")
            return

        loaded_player = SaveManager.load_player()
        game_manager = GameManager()
        game_manager.days = save_data['game']['days']

        root = self.winfo_toplevel()
        root.destroy()

        main_window = MainWindow(loaded_player, game_manager)
        main_window.run()

    def start_new_game(self):
        self.new_game_button.pack_forget()
        if self.has_save:
            self.load_game_button.pack_forget()

        self.name_label = Label(
            self,
            text="Entrez votre nom :",
            font=("Arial", 18),
            background="#2cdf85",
            foreground="white"
        )
        self.name_label.pack(pady=20)

        self.name_entry = Entry(
            self,
            font=("Arial", 16),
            width=20
        )
        self.name_entry.pack(pady=10)
        self.name_entry.focus()

        self.confirm_button = Button(
            self,
            text="Valider",
            font=("Arial", 16),
            background="#4a90e2",
            foreground="white",
            padx=20,
            pady=10,
            command=self.create_new_player
        )
        self.confirm_button.pack(pady=10)

    def create_new_player(self):
        player_name = self.name_entry.get().strip()

        if not player_name:
            if not hasattr(self, 'error_label'):
                self.error_label = Label(
                    self,
                    text="⚠️ Le nom ne peut pas être vide!",
                    font=("Arial", 12),
                    background="#2cdf85",
                    foreground="#ff4444"
                )
                self.error_label.pack(pady=5)
            return

        if hasattr(self, 'error_label'):
            self.error_label.destroy()

        new_player = Player(player_name)
        root = self.winfo_toplevel()
        root.destroy()
        main_window = MainWindow(new_player)
        main_window.run()
