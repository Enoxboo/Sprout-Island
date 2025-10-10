from tkinter import Tk
from button_frame import ButtonsFrame
from dialogue_frame import DialogueFrame


class MainWindow:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title("Sprout Island")
        self.main_window.geometry("1080x720")
        self.main_window.minsize(480, 360)
        self.main_window.iconbitmap("../src/teemo_basic.ico")
        self.main_window.config(background="#2cdf85")
        self.dialogue_frame = DialogueFrame(self.main_window)
        self.dialogue_frame.update_text("Welcome to Sprout Island!")
        self.buttons_frame = ButtonsFrame(self.main_window)


    def run(self):
        self.main_window.mainloop()



if __name__ == "__main__":
    app = MainWindow()
    app.run()