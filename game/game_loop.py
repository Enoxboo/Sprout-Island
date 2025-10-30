from tkinter import Tk
from gui.start_frame import StartFrame


def run_game():
    """Initialize and launch the main game loop."""
    root = Tk()
    configure_window(root)
    start_frame = StartFrame(root)
    root.mainloop()


def configure_window(root):
    """Configure the main window settings."""
    root.title("Sprout Island")
    root.geometry("800x600")
    root.config(background="#F5E6D3")
