import os
from tkinter import Frame, Label
from PIL import Image, ImageTk


class DialogueFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#F5E6D3")
        self.parent = parent
        self.config(width=100, height=200)
        self.pack(side="bottom", fill="x")

        dir = os.path.dirname(__file__)
        root = os.path.dirname(dir)
        src = os.path.join(root, "src", "dialogue_box.png")

        if os.path.exists(src):
            self.original_image = Image.open(src)
            self.bg_photo = ImageTk.PhotoImage(self.original_image)
            self.bg_label = Label(self, image=self.bg_photo, background="#F5E6D3")
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            self.bind("<Configure>", self.resize_background)
        else:
            self.bg_label = Label(self, background="#E8D5C4")
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            self.original_image = None

        self.label = Label(
            self,
            text="",
            bg='#E8D5C4',
            fg="#3E2723",
            font=("Segoe UI", 16),
            wraplength=800,
            justify="center"
        )
        self.label.place(relx=0.5, rely=0.5, anchor="center")

    def resize_background(self, event):
        if self.original_image:
            width = event.width
            height = event.height
            resized_image = self.original_image.resize((width, height), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(resized_image)
            self.bg_label.config(image=self.bg_photo)

    def check_parent_bg(self):
        parent_bg = self.parent.cget("background")
        current_bg = self.cget("background")
        if parent_bg != current_bg:
            self.config(bg=parent_bg)
            if not self.original_image:
                self.bg_label.config(bg="#E8D5C4")

        self.after(200, self.check_parent_bg)

    def update_text(self, new_text):
        self.label.config(text=new_text)