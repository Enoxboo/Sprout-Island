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

        self.bg_item = self.create_rounded_rect(5, 5, width-5, height-5, corner_radius, fill=bg_color, outline="")
        self.text_item = self.create_text(width//2, height//2, text=text, font=font, fill="black")

        self.bind("<Button-1>", self._on_click)

    def create_rounded_rect(self, x1, y1, x2, y2, radius, **kwargs):
        points = [
            x1+radius, y1,
            x2-radius, y1,
            x2, y1+radius,
            x2, y2-radius,
            x2-radius, y2,
            x1+radius, y2,
            x1, y2-radius,
            x1, y1+radius
        ]
        return self.create_polygon(points, smooth=True, **kwargs)

    def _on_click(self, event):
        if self.command:
            self.command()


class ButtonsFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=parent.cget("background"))
        self.parent = parent
        self.config(width=50, height=50)
        self.pack(side="bottom", fill="x", pady=(0, 50))

        self.player_choice = None
        self.choice_event = threading.Event()

        self.button1 = RoundedButton(self, text="Fish", command=lambda: self.make_choice("fish"))
        self.button2 = RoundedButton(self, text="Explore", command=lambda: self.make_choice("explore"))
        self.button3 = RoundedButton(self, text="Sleep", command=lambda: self.make_choice("sleep"))
        self.button4 = RoundedButton(self, text="Drink", command=lambda: self.make_choice("drink"))


        self.button1.place(relx=0.125, rely=0.5, anchor="center")
        self.button2.place(relx=0.375, rely=0.5, anchor="center")
        self.button3.place(relx=0.625, rely=0.5, anchor="center")
        self.button4.place(relx=0.875, rely=0.5, anchor="center")

    def make_choice(self, choice):
        self.player_choice = choice
        print(f"Player chose: {choice}")
        self.choice_event.set()

    def get_player_choice(self):

        self.player_choice = None
        self.choice_event.clear()

        while not self.choice_event.is_set():
            self.parent.update()
            self.parent.update_idletasks()

        return self.player_choice

    def check_parent_bg(self):
        parent_bg = self.parent.cget("background")
        current_bg = self.cget("background")
        if parent_bg != current_bg:
            self.config(bg=parent_bg)
        self.after(200, self.check_parent_bg)