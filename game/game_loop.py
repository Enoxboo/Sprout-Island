from tkinter import Tk
from gui.start_frame import StartFrame


def run_game():
    """Initialise et lance la boucle de jeu."""
    root = Tk()
    configure_window(root)
    start_frame = StartFrame(root)
    root.mainloop()


def configure_window(root):
    """Configure les paramètres de la page principal."""
    root.title("Sprout Island")
    root.geometry("800x600")
    root.config(background="#F5E6D3")
