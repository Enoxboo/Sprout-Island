"""Frame affichant les barres de statut du joueur (énergie, satiété, hydratation)."""
import tkinter as tk
from tkinter import Canvas
from gui.shapes import create_rounded_rect


class StatusFrame(tk.Frame):
    """Affiche et met à jour les barres de progression des statistiques du joueur."""

    def __init__(self, parent, player, **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(bg="#F5E6D3", padx=20, pady=15)
        self.energy_var = tk.DoubleVar(value=player.energy)
        self.satiety_var = tk.DoubleVar(value=player.satiety)
        self.hydration_var = tk.DoubleVar(value=player.hydration)
        self.player = player
        self._create_widgets()

    def _create_stat_bar(self, icon, name, variable, color):
        frame = tk.Frame(self, bg="#F5E6D3")
        frame.pack(fill="x", pady=8)

        label_text = f"{icon} {name}"
        label = tk.Label(
            frame,
            text=label_text,
            font=("Segoe UI", 12, "bold"),
            width=12,
            anchor="w",
            bg="#F5E6D3",
            fg="#3E2723"
        )
        label.pack(side="left", padx=(0, 10))

        bar_container = tk.Frame(frame, bg="#F5E6D3")
        bar_container.pack(side="left", fill="x", expand=True)

        canvas = Canvas(
            bar_container,
            height=28,
            bg="#F5E6D3",
            highlightthickness=0,
            bd=0
        )
        canvas.pack(fill="x", expand=True)

        value_label = tk.Label(
            frame,
            bg="#F5E6D3",
            fg="#3E2723",
            font=("Segoe UI", 11, "bold"),
            width=6
        )
        value_label.pack(side="right", padx=(10, 0))

        def update_bar(*args):
            canvas.delete("all")
            width = canvas.winfo_width()
            height = canvas.winfo_height()

            if width <= 1:
                canvas.after(10, update_bar)
                return

            radius = 10
            canvas.create_rectangle(
                0, 0, width, height,
                fill="#D4C5B3", outline="", tags="bg"
            )

            progress_width = int((variable.get() / 100) * width)
            if progress_width > 0:
                create_rounded_rect(
                    canvas, 2, 2, progress_width - 2, height - 2,
                    radius, fill=color, outline=""
                )

            value_label.config(text=f"{variable.get():.0f}%")

        variable.trace_add("write", update_bar)

        canvas.bind("<Configure>", update_bar)

        canvas.after(10, update_bar)

        return canvas

    def _create_widgets(self):
        title_label = tk.Label(
            self,
            text="📊 Statut du Joueur",
            font=("Segoe UI", 14, "bold"),
            bg="#F5E6D3",
            fg="#3E2723"
        )
        title_label.pack(pady=(0, 15))

        self._create_stat_bar("⚡", "Énergie", self.energy_var, "#8FBC8F")
        self._create_stat_bar("🍖", "Satiété", self.satiety_var, "#FFB6A3")
        self._create_stat_bar("💧", "Hydration", self.hydration_var, "#7FB3D5")

    def update_from_player(self):
        self.energy_var.set(self.player.energy)
        self.satiety_var.set(self.player.satiety)
        self.hydration_var.set(self.player.hydration)
        self.update()
        self.update_idletasks()
