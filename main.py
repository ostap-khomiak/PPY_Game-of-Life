import tkinter as tk
from start_screen import show
from logic import GameLogic
from gui import GameGUI



def start(settings):

    print("Start")
    root = tk.Tk()
    root.title("Game of Life")

    logic = GameLogic(settings)
    gui = GameGUI(root, logic)

    root.mainloop()


if __name__ == "__main__":
    show(start)

