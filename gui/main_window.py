from tkinter import Tk
from button_frame import ButtonsFrame
from dialogue_frame import DialogueFrame
from gui.status_frame import StatusFrame
from models.player import Player


class MainWindow:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title("Sprout Island")
        self.main_window.geometry("1080x720")
        self.main_window.minsize(480, 360)
        self.main_window.iconbitmap("../src/teemo_basic.ico")
        self.main_window.config(background="#2cdf85")
        player1 = Player("Player 1")
        self.status_frame = StatusFrame(self.main_window , player1)
        self.status_frame.pack(side="top", fill="x")
        self.dialogue_frame = DialogueFrame(self.main_window)
        self.dialogue_frame.update_text("Welcome to Sprout Island!")
        self.buttons_frame = ButtonsFrame(self.main_window)



    def run(self):
        self.main_window.mainloop()



if __name__ == "__main__":
    app = MainWindow()
    app.run()