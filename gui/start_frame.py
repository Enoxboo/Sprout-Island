"""Écran de démarrage avec options nouvelle partie / charger partie."""
from tkinter import Frame, Label, Button, Entry

from game.game_manager import GameManager
from utils.save_manager import SaveManager
from models.player import Player
from gui.main_window import MainWindow


class StyledStartButton(Button):
    def __init__(self, parent, text, command, bg_color="#7FB3D5", **kwargs):
        super().__init__(
            parent,
            text=text,
            command=command,
            font=("Segoe UI", 14, "bold"),
            bg=bg_color,
            fg="white",
            activebackground=bg_color,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=30,
            pady=12,
            cursor="hand2",
            **kwargs
        )

        self.default_bg = bg_color
        self.hover_bg = self._darken_color(bg_color)

        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)

    def _darken_color(self, color):
        color = color.lstrip('#')
        r, g, b = tuple(int(color[i:i + 2], 16) for i in (0, 2, 4))
        r = max(0, int(r * 0.85))
        g = max(0, int(g * 0.85))
        b = max(0, int(b * 0.85))
        return f'#{r:02x}{g:02x}{b:02x}'

    def _on_enter(self, event):
        self.config(bg=self.hover_bg)

    def _on_leave(self, event):
        self.config(bg=self.default_bg)


class StartFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(background="#F5E6D3")
        self.pack(fill="both", expand=True)

        self.has_save = SaveManager.save_exists()

        main_container = Frame(self, bg="#F5E6D3")
        main_container.place(relx=0.5, rely=0.5, anchor="center")

        self.title_label = Label(
            main_container,
            text="🌴 Sprout Island 🌴",
            font=("Segoe UI", 36, "bold"),
            background="#F5E6D3",
            foreground="#3E2723"
        )
        self.title_label.pack(pady=(0, 10))

        self.subtitle_label = Label(
            main_container,
            text="Survivez 20 jours sur l'île déserte",
            font=("Segoe UI", 14),
            background="#F5E6D3",
            foreground="#5D4037"
        )
        self.subtitle_label.pack(pady=(0, 40))

        self.new_game_button = StyledStartButton(
            main_container,
            text="🌱 Nouvelle Partie",
            command=self.start_new_game,
            bg_color="#7FB3D5"
        )
        self.new_game_button.pack(pady=8)

        if self.has_save:
            self.load_game_button = StyledStartButton(
                main_container,
                text="📂 Charger Partie",
                command=self.load_existing_game,
                bg_color="#8FBC8F"
            )
            self.load_game_button.pack(pady=8)

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
        self.title_label.pack_forget()
        self.subtitle_label.pack_forget()

        form_container = Frame(self, bg="#F5E6D3")
        form_container.place(relx=0.5, rely=0.5, anchor="center")

        self.name_label = Label(
            form_container,
            text="Entrez votre nom :",
            font=("Segoe UI", 18, "bold"),
            background="#F5E6D3",
            foreground="#3E2723"
        )
        self.name_label.pack(pady=(0, 15))

        self.name_entry = Entry(
            form_container,
            font=("Segoe UI", 14),
            width=25,
            relief="flat",
            bd=2,
            bg="white",
            fg="#3E2723",
            insertbackground="#3E2723"
        )
        self.name_entry.pack(pady=10, ipady=8)
        self.name_entry.focus()
        self.name_entry.bind("<Return>", lambda e: self.create_new_player())

        self.confirm_button = StyledStartButton(
            form_container,
            text="✓ Commencer l'aventure",
            command=self.create_new_player,
            bg_color="#7FB3D5"
        )
        self.confirm_button.pack(pady=15)

    def create_new_player(self):
        player_name = self.name_entry.get().strip()

        if not player_name:
            if not hasattr(self, 'error_label'):
                self.error_label = Label(
                    self,
                    text="⚠️ Le nom ne peut pas être vide!",
                    font=("Segoe UI", 12),
                    background="#F5E6D3",
                    foreground="#E57373"
                )
                self.error_label.place(relx=0.5, rely=0.7, anchor="center")
            return

        if hasattr(self, 'error_label'):
            self.error_label.destroy()

        new_player = Player(player_name)
        root = self.winfo_toplevel()
        root.destroy()
        main_window = MainWindow(new_player)
        main_window.run()
