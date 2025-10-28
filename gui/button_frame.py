import tkinter as tk
from tkinter import Frame


class StyledButton(tk.Canvas):
    def __init__(self, parent, text, command=None, bg_color="#7FB3D5",
                 hover_color="#6BA3C5", width=150, height=50):
        super().__init__(
            parent,
            width=width,
            height=height,
            bg="#F5E6D3",
            highlightthickness=0,
            bd=0
        )

        self.command = command
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.is_disabled = False
        self.corner_radius = 12

        self.shadow = self._create_rounded_rect(
            4, 4, width - 4, height - 4,
            self.corner_radius, fill="#D4C5B3", outline=""
        )

        self.button_bg = self._create_rounded_rect(
            2, 2, width - 2, height - 2,
            self.corner_radius, fill=bg_color, outline=""
        )

        self.text_item = self.create_text(
            width // 2, height // 2,
            text=text,
            font=("Segoe UI", 12, "bold"),
            fill="#FFFFFF"
        )

        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<Button-1>", self._on_click)

    def _create_rounded_rect(self, x1, y1, x2, y2, radius, **kwargs):
        points = [
            x1 + radius, y1,
            x2 - radius, y1,
            x2, y1,
            x2, y1 + radius,
            x2, y2 - radius,
            x2, y2,
            x2 - radius, y2,
            x1 + radius, y2,
            x1, y2,
            x1, y2 - radius,
            x1, y1 + radius,
            x1, y1
        ]
        return self.create_polygon(points, smooth=True, **kwargs)

    def _on_enter(self, event):
        if not self.is_disabled:
            self.itemconfig(self.button_bg, fill=self.hover_color)
            self.delete(self.shadow)
            self.delete(self.button_bg)
            self.shadow = self._create_rounded_rect(
                3, 3, self.winfo_width() - 3, self.winfo_height() - 3,
                self.corner_radius, fill="#D4C5B3", outline=""
            )
            self.button_bg = self._create_rounded_rect(
                1, 1, self.winfo_width() - 1, self.winfo_height() - 1,
                self.corner_radius, fill=self.hover_color, outline=""
            )
            self.tag_raise(self.text_item)
            self.config(cursor="hand2")

    def _on_leave(self, event):
        if not self.is_disabled:
            self.itemconfig(self.button_bg, fill=self.bg_color)
            self.delete(self.shadow)
            self.delete(self.button_bg)
            self.shadow = self._create_rounded_rect(
                4, 4, self.winfo_width() - 4, self.winfo_height() - 4,
                self.corner_radius, fill="#D4C5B3", outline=""
            )
            self.button_bg = self._create_rounded_rect(
                2, 2, self.winfo_width() - 2, self.winfo_height() - 2,
                self.corner_radius, fill=self.bg_color, outline=""
            )
            self.tag_raise(self.text_item)
            self.config(cursor="")

    def _on_click(self, event):
        if not self.is_disabled and self.command:
            self.delete(self.shadow)
            self.delete(self.button_bg)
            self.shadow = self._create_rounded_rect(
                4, 4, self.winfo_width() - 4, self.winfo_height() - 4,
                self.corner_radius, fill="#D4C5B3", outline=""
            )
            self.button_bg = self._create_rounded_rect(
                3, 3, self.winfo_width() - 3, self.winfo_height() - 3,
                self.corner_radius, fill=self.hover_color, outline=""
            )
            self.tag_raise(self.text_item)

            def reset():
                self.delete(self.shadow)
                self.delete(self.button_bg)
                self.shadow = self._create_rounded_rect(
                    4, 4, self.winfo_width() - 4, self.winfo_height() - 4,
                    self.corner_radius, fill="#D4C5B3", outline=""
                )
                self.button_bg = self._create_rounded_rect(
                    2, 2, self.winfo_width() - 2, self.winfo_height() - 2,
                    self.corner_radius, fill=self.bg_color, outline=""
                )
                self.tag_raise(self.text_item)

            self.after(100, reset)
            self.command()

    def disable(self):
        self.is_disabled = True
        self.delete(self.button_bg)
        self.button_bg = self._create_rounded_rect(
            2, 2, self.winfo_width() - 2, self.winfo_height() - 2,
            self.corner_radius, fill="#CCCCCC", outline=""
        )
        self.itemconfig(self.text_item, fill="#999999")
        self.tag_raise(self.text_item)
        self.config(cursor="")

    def enable(self):
        self.is_disabled = False
        self.delete(self.button_bg)
        self.button_bg = self._create_rounded_rect(
            2, 2, self.winfo_width() - 2, self.winfo_height() - 2,
            self.corner_radius, fill=self.bg_color, outline=""
        )
        self.itemconfig(self.text_item, fill="#FFFFFF")
        self.tag_raise(self.text_item)


class ButtonsFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(background="#F5E6D3", padx=20, pady=20)
        self.pack(side="bottom", fill="x")

        self.action_callback = None
        self.buttons = {}

        actions_config = [
            ("fish", "Pêcher", "#7FB3D5", "#6BA3C5"),
            ("drink", "Boire", "#A8D5E2", "#92BFD2"),
            ("sleep", "Dormir", "#B39DDB", "#9E88CB"),
            ("explore", "Explorer", "#8FBC8F", "#7AAC7A"),
            ("quit", "Quitter", "#FFB6A3", "#EFA693")
        ]

        button_container = Frame(self, bg="#F5E6D3")
        button_container.pack(expand=True)

        for action, text, bg_color, hover_color in actions_config:
            btn = StyledButton(
                button_container,
                text=text,
                command=lambda a=action: self.on_button_click(a),
                bg_color=bg_color,
                hover_color=hover_color
            )
            btn.pack(side="left", padx=8)
            self.buttons[action] = btn

    def set_action_callback(self, callback):
        self.action_callback = callback

    def on_button_click(self, action):
        if self.action_callback:
            self.action_callback(action)

    def disable_buttons(self):
        for button in self.buttons.values():
            button.disable()

    def enable_buttons(self):
        for button in self.buttons.values():
            button.enable()

    def show_choice_buttons(self, choices):
        for button in self.buttons.values():
            button.pack_forget()

        choice_config = {
            "flee": ("Fuir", "#FFB6A3", "#EFA693"),
            "hunt": ("Chasser", "#8FBC8F", "#7AAC7A")
        }

        button_container = None
        for child in self.winfo_children():
            if isinstance(child, Frame):
                button_container = child
                break

        if button_container is None:
            button_container = Frame(self, bg="#F5E6D3")
            button_container.pack(expand=True)

        for choice in choices:
            if choice in choice_config:
                text, bg_color, hover_color = choice_config[choice]
                btn = StyledButton(
                    button_container,
                    text=text,
                    command=lambda c=choice: self.on_choice_click(c),
                    bg_color=bg_color,
                    hover_color=hover_color
                )
                btn.pack(side="left", padx=8)
                self.buttons[f"choice_{choice}"] = btn

    def hide_choice_buttons(self):
        for key in list(self.buttons.keys()):
            if key.startswith("choice_"):
                self.buttons[key].destroy()
                del self.buttons[key]

        actions_order = ["fish", "drink", "sleep", "explore", "quit"]
        for action in actions_order:
            if action in self.buttons:
                self.buttons[action].pack(side="left", padx=8)

    def on_choice_click(self, choice):
        if self.action_callback:
            self.action_callback(choice)

    def set_action_callback(self, callback):
        self.action_callback = callback
