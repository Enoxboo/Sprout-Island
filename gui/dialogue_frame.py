from tkinter import Frame , Label
from PIL import Image, ImageTk

class DialogueFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent , bg=parent.cget("background"))
        self.parent = parent
        self.config(width=100, height=200)
        self.pack(side="bottom", fill="x")

        self.original_image = Image.open("../src/dialogue_box.png")
        self.bg_photo = ImageTk.PhotoImage(self.original_image)

        self.bg_label = Label(self, image=self.bg_photo , background=parent.cget("background"))
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)


        self.label = Label(self, text="" , bg='#E8CFA6', fg="Black" , font=("Sprout", 20))
        self.label.place(relx=0.5, rely=0.5, anchor="center")


        self.bind("<Configure>", self.resize_background)

    """ Resize the background image to fit the frame 
    @param event The event object containing the new width and height of the frame
    @date 2024-06-10
    @author Alexandre RIVIERE
    """
    def resize_background(self, event):
        width = event.width
        height = event.height

        resized_image = self.original_image.resize((width, height), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(resized_image)

        self.bg_label.config(image=self.bg_photo)

    """ Check if the parent background color has changed and update the frame background color accordingly"""
    def check_parent_bg(self):
        parent_bg = self.parent.cget("background")
        current_bg = self.cget("background")
        if parent_bg != current_bg:
            self.config(bg=parent_bg)
            self.bg_label.config(bg=parent_bg)
            self.label.config(bg=parent_bg)

        self.after(200, self.check_parent_bg)

    def update_text(self, new_text):
        self.label.config(text=new_text)

