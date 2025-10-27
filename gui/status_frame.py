import tkinter as tk
from tkinter import ttk


class StatusFrame(tk.Frame):
    def __init__(self, parent, player, **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(bg="#2cdf85", padx=10, pady=10)
        self.energy_var = tk.DoubleVar(value=player.energy)
        self.satiety_var = tk.DoubleVar(value=player.satiety)
        self.hydration_var = tk.DoubleVar(value=player.hydration)
        self.player = player
        self._create_widgets()

    def _create_stat_bar(self, name, variable, color):
        frame = tk.Frame(self, bg="#2cdf85")
        frame.pack(fill="x", pady=5)

        label = tk.Label(frame, text=name, width=8, anchor="w", bg="#333333", fg="white")
        label.pack(side="left", padx=(0, 5))

        progress = ttk.Progressbar(frame, variable=variable, maximum=100, length=200)
        progress.pack(side="left", fill="x", expand=True)

        style_name = f"{name.lower()}.Horizontal.TProgressbar"
        style = ttk.Style()
        style.configure(style_name, background=color, troughcolor="#666666")
        progress.configure(style=style_name)

        value_label = tk.Label(frame, bg="#333333", fg="white", width=5)

        def update_label(*args):
            value_label.config(text=f"{variable.get():.0f}%")

        variable.trace_add("write", update_label)
        update_label()
        value_label.pack(side="right")

        return progress

    def _create_widgets(self):
        title_label = tk.Label(self, text="STATUT DU JOUEUR", font=("Arial", 12, "bold"),
                               bg="#333333", fg="white")
        title_label.pack(pady=(0, 10))

        self._create_stat_bar("ENERGY", self.energy_var, "#4CAF50")
        self._create_stat_bar("SATIÉTÉ", self.satiety_var, "#FF9800")
        self._create_stat_bar("SOIF", self.hydration_var, "#2196F3")

    def update_from_player(self):
        self.energy_var.set(self.player.energy)
        self.satiety_var.set(self.player.satiety)
        self.hydration_var.set(self.player.hydration)
        self.update()
        self.update_idletasks()
