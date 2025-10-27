import threading
from tkinter import Frame, Label, Button, Canvas


class RoundedButton(Canvas):
    def __init__(self, parent, text, bg_color="#E8CFA6", command=None, width=200, height=80,
                 corner_radius=15, font=("Arial", 25)):
        super().__init__(
            parent,
            width=width,
            height=height,
            bg=parent.cget("background"),
            highlightthickness=0,
            bd=0
        )
        self.command = command

        self.bg_item = self.create_rounded_rect(5, 5, width - 5, height - 5, corner_radius, fill=bg_color, outline="")
        self.text_item = self.create_text(width // 2, height // 2, text=text, font=font, fill="black")

        self.bind("<Button-1>", self._on_click)

    def create_rounded_rect(self, x1, y1, x2, y2, radius, **kwargs):
        points = [
            x1 + radius, y1,
            x2 - radius, y1,
            x2, y1 + radius,
            x2, y2 - radius,
            x2 - radius, y2,
            x1 + radius, y2,
            x1, y2 - radius,
            x1, y1 + radius
        ]
        return self.create_polygon(points, smooth=True, **kwargs)

    def _on_click(self, event):
        if self.command:
            self.command()


class ButtonsFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(background="#2cdf85")
        self.pack(side="bottom", fill="both", expand=True)

        self.action_callback = None
        self.buttons = {}

        actions = [
            ("fish", "🎣 Pêcher"),
            ("drink", "💧 Boire"),
            ("sleep", "😴 Dormir"),
            ("explore", "🗺️ Explorer"),
            ("quit", "🚪 Quitter")
        ]

        for action, text in actions:
            btn = Button(
                self,
                text=text,
                font=("Arial", 14),
                background="#4a90e2",
                foreground="white",
                padx=20,
                pady=10,
                command=lambda a=action: self.on_button_click(a)
            )
            btn.pack(side="left", padx=10, pady=20, expand=True)
            self.buttons[action] = btn

    def set_action_callback(self, callback):
        self.action_callback = callback

    def on_button_click(self, action):
        if self.action_callback:
            self.action_callback(action)

    def disable_buttons(self):
        for button in self.buttons.values():
            button.config(state="disabled")

    def enable_buttons(self):
        for button in self.buttons.values():
            button.config(state="normal")