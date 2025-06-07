import tkinter as tk
from tkinter import messagebox
from settings import GameSettings



def show(callback):
    """
    Launches the start screen for game settings
    Args:
        callback (function): is a function that should be called after this function
    """
    start_root = tk.Tk()
    start_root.title("Game of Life")

    tk.Label(start_root, text="Game of Life", font=("Arial", 32)).pack()

    settings_frame = tk.Frame(start_root, bg="gray60")
    settings_frame.pack(padx=20, pady=20)

    options = {}



    def add_setting(name, value, key):
        """
        Adds a labeled input field to the settings window

        Args:
            name (str): The label to display
            value (any): The default value
            key (str): The key used to identify this input in the game settings
        """
        row = tk.Frame(settings_frame)
        row.pack(fill=tk.X, padx=10, pady=10)
        tk.Label(row, text=name).pack(side=tk.LEFT)
        entry = tk.Entry(row)
        entry.insert(0, str(value))
        entry.pack(side=tk.RIGHT, expand=True, fill=tk.X)
        options[key] = entry

    add_setting("Rows amount: ", 30, "rows")
    add_setting("Column amount: ", 30, "cols")
    add_setting("Rules: ", "23/3", "rules")


    def start():
        """
        Creates GameSettings object and starts game
        """
        try:
            rows = int(options["rows"].get())
            cols = int(options["cols"].get())
            survive_str, birth_str = options["rules"].get().strip().split('/')
            survive = set(int(n) for n in survive_str)
            birth = set(int(n) for n in birth_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid input")
            return

        settings = GameSettings(rows=rows, cols=cols, survive=survive, birth=birth)
        start_root.destroy()
        callback(settings)



    tk.Button(start_root, text="Start", command=start, bg="green", fg="white").pack(pady=10)



    start_root.mainloop()


