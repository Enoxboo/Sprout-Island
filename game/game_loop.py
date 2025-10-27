from tkinter import Tk
from gui.start_frame import StartFrame


def run_game():
    root = Tk()
    root.title("Sprout Island")
    root.geometry("800x600")
    root.config(background="#2cdf85")

    start_frame = StartFrame(root)

    root.mainloop()
