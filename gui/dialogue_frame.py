from tkinter import Frame, Canvas, Label
from gui.shapes import create_rounded_rect


class DialogueFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#F5E6D3")
        self.parent = parent
        self.pack(side="bottom", fill="x", padx=20, pady=20)

        self.canvas = Canvas(
            self,
            height=120,
            bg="#F5E6D3",
            highlightthickness=0,
            bd=0
        )
        self.canvas.pack(fill="x", expand=True)

        self.label = Label(
            self.canvas,
            text="",
            bg="#FFFFFF",
            fg="#3E2723",
            font=("Segoe UI", 14),
            wraplength=900,
            justify="center",
            padx=30,
            pady=20
        )

        self.canvas.bind("<Configure>", self._redraw_bubble)
        self.after(10, self._redraw_bubble)

    def _redraw_bubble(self, event=None):
        self.canvas.delete("all")

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        if width <= 1:
            self.canvas.after(10, self._redraw_bubble)
            return

        margin = 10
        bubble_x1 = margin
        bubble_y1 = margin
        bubble_x2 = width - margin
        bubble_y2 = height - margin
        radius = 20

        create_rounded_rect(
            self.canvas,
            bubble_x1 + 3, bubble_y1 + 3,
            bubble_x2 + 3, bubble_y2 + 3,
            radius, fill="#D4C5B3", outline=""
        )

        create_rounded_rect(
            self.canvas,
            bubble_x1, bubble_y1, bubble_x2, bubble_y2,
            radius, fill="#FFFFFF", outline=""
        )

        create_rounded_rect(
            self.canvas,
            bubble_x1, bubble_y1, bubble_x2, bubble_y2,
            radius, fill="", outline="#D4C5B3", width=2
        )

        self.label.place(
            relx=0.5, rely=0.5, anchor="center",
            width=width - 60
        )

    def update_text(self, new_text):
        self.label.config(text=new_text)