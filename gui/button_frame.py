"""Boutons d'action personnalisés avec effets visuels (hover, click)."""
import tkinter as tk
from tkinter import Frame
from gui.shapes import create_rounded_rect


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

        self.shadow = create_rounded_rect(
            self, 4, 4, width - 4, height - 4,
            self.corner_radius, fill="#D4C5B3", outline=""
        )

        self.button_bg = create_rounded_rect(
            self, 2, 2, width - 2, height - 2,
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

    def _on_enter(self, event):
        if not self.is_disabled:
            self.itemconfig(self.button_bg, fill=self.hover_color)
            self.delete(self.shadow)
            self.delete(self.button_bg)
            self.shadow = create_rounded_rect(
                self, 3, 3, self.winfo_width() - 3, self.winfo_height() - 3,
                self.corner_radius, fill="#D4C5B3", outline=""
            )
            self.button_bg = create_rounded_rect(
                self, 1, 1, self.winfo_width() - 1, self.winfo_height() - 1,
                self.corner_radius, fill=self.hover_color, outline=""
            )
            self.tag_raise(self.text_item)
            self.config(cursor="hand2")

    def _on_leave(self, event):
        if not self.is_disabled:
            self.itemconfig(self.button_bg, fill=self.bg_color)
            self.delete(self.shadow)
            self.delete(self.button_bg)
            self.shadow = create_rounded_rect(
                self, 4, 4, self.winfo_width() - 4, self.winfo_height() - 4,
                self.corner_radius, fill="#D4C5B3", outline=""
            )
            self.button_bg = create_rounded_rect(
                self, 2, 2, self.winfo_width() - 2, self.winfo_height() - 2,
                self.corner_radius, fill=self.bg_color, outline=""
            )
            self.tag_raise(self.text_item)
            self.config(cursor="")

    def _on_click(self, event):
        if not self.is_disabled and self.command:
            self.delete(self.shadow)
            self.delete(self.button_bg)
            self.shadow = create_rounded_rect(
                self, 4, 4, self.winfo_width() - 4, self.winfo_height() - 4,
                self.corner_radius, fill="#D4C5B3", outline=""
            )
            self.button_bg = create_rounded_rect(
                self, 3, 3, self.winfo_width() - 3, self.winfo_height() - 3,
                self.corner_radius, fill=self.hover_color, outline=""
            )
            self.tag_raise(self.text_item)

            def reset():
                self.delete(self.shadow)
                self.delete(self.button_bg)
                self.shadow = create_rounded_rect(
                    self, 4, 4, self.winfo_width() - 4, self.winfo_height() - 4,
                    self.corner_radius, fill="#D4C5B3", outline=""
                )
                self.button_bg = create_rounded_rect(
                    self, 2, 2, self.winfo_width() - 2, self.winfo_height() - 2,
                    self.corner_radius, fill=self.bg_color, outline=""
                )
                self.tag_raise(self.text_item)

            self.after(100, reset)
            self.command()

    def disable(self):
        self.is_disabled = True
        self.delete(self.button_bg)
        self.button_bg = create_rounded_rect(
            self, 2, 2, self.winfo_width() - 2, self.winfo_height() - 2,
            self.corner_radius, fill="#CCCCCC", outline=""
        )
        self.itemconfig(self.text_item, fill="#999999")
        self.tag_raise(self.text_item)
        self.config(cursor="")

    def enable(self):
        self.is_disabled = False
        self.delete(self.button_bg)
        self.button_bg = create_rounded_rect(
            self, 2, 2, self.winfo_width() - 2, self.winfo_height() - 2,
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

        main_container = Frame(self, bg="#F5E6D3")
        main_container.pack(expand=True)

        self.action_container = Frame(main_container, bg="#F5E6D3")
        self.action_container.pack(side="left", expand=True)

        self.quit_container = Frame(main_container, bg="#F5E6D3")
        self.quit_container.pack(side="left", padx=(20, 0))

        actions_config = [
            ("fish", "Pêcher", "#FFB6A3", "#EFA693"),
            ("drink", "Boire", "#7FB3D5", "#6BA3C5"),
            ("sleep", "Dormir", "#8FBC8F", "#7AAC7A"),
            ("explore", "Explorer", "#B39DDB", "#9E88CB")
        ]

        for action, text, bg_color, hover_color in actions_config:
            btn = StyledButton(
                self.action_container,
                text=text,
                command=lambda a=action: self.on_button_click(a),
                bg_color=bg_color,
                hover_color=hover_color
            )
            btn.pack(side="left", padx=8)
            self.buttons[action] = btn

        quit_btn = StyledButton(
            self.quit_container,
            text="Quitter",
            command=lambda: self.on_button_click("quit"),
            bg_color="#E57373",
            hover_color="#D96363"
        )
        quit_btn.pack()
        self.buttons["quit"] = quit_btn

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
        for key in list(self.buttons.keys()):
            if key != "quit":
                self.buttons[key].pack_forget()

        self.buttons["quit"].pack_forget()

        choice_config = {
            "flee": ("Fuir", "#FFB6A3", "#EFA693"),
            "hunt": ("Chasser", "#8FBC8F", "#7AAC7A"),
            "replay": ("🔄 Rejouer", "#7FB3D5", "#6BA3C5")
        }

        for choice in choices:
            if choice in choice_config:
                text, bg_color, hover_color = choice_config[choice]
                btn = StyledButton(
                    self.action_container,
                    text=text,
                    command=lambda c=choice: self.on_choice_click(c),
                    bg_color=bg_color,
                    hover_color=hover_color
                )
                btn.pack(side="left", padx=8)
                self.buttons[f"choice_{choice}"] = btn

        if "replay" in choices:
            self.buttons["quit"].pack()

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
