import tkinter as tk
from tkinter import filedialog

CELL_SIZE = 40
ALIVE_COLOR = "green"
DEAD_COLOR = "black"
GRID_COLOR = "gray"

class GameGUI:
    """
    Handles the graphical interface for game board
    """
    def __init__(self, root, logic):
        """
        Initializes the GameGUI

        Args:
            root (tk.Tk): The root tkinter window
            logic (GameLogic): The game logic object
        """
        self.root = root
        self.logic = logic

        self.canvas = tk.Canvas(
            root,
            width=self.logic.cols * CELL_SIZE,
            height=self.logic.rows * CELL_SIZE,
            bg=DEAD_COLOR
        )
        self.canvas.pack()

        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=5)

        tk.Button(control_frame, text="Toggle running", command=self.toggle_running).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Save", command=self.save_grid).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Load", command=self.load_grid).pack(side=tk.LEFT, padx=5)

        self.is_running = False
        self.root.bind("<space>", self.toggle_running)
        self.canvas.bind("<Button-1>", self.toggle_cell)

        self.draw_grid()
        self.update()

    def draw_grid(self):
        """
        Draws the current state of the board onto the canvas.
        """

        self.canvas.delete("all")
        for row in range(self.logic.rows):
            for col in range(self.logic.cols):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                fill = ALIVE_COLOR if self.logic.grid[row][col] else DEAD_COLOR
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline=GRID_COLOR)

    def toggle_cell(self, event):
        """
        Toggles a cell's state between alive and dead on mouse click.

        Args:
            event (tk.Event): The tkinter mouse event.
        """
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE

        if 0 <= row < self.logic.rows and 0 <= col < self.logic.cols:
            self.logic.grid[row][col] = 0 if self.logic.grid[row][col] == 1 else 1
            self.draw_grid()

    def save_grid(self):
        """
        Saves the current board state to a text file
        """
        path = filedialog.asksaveasfilename(defaultextension=".txt")
        if not path:
            return
        with open(path, "w") as file:
            for row in self.logic.grid:
                file.write(" ".join(map(str, row)) + "\n")

    def load_grid(self):
        """
        Loads the board state from a text file
        """
        path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not path:
            return
        with open(path, "r") as file:
            lines = file.readlines()
            for r, line in enumerate(lines):
                values = list(map(int, line.strip().split()))
                if r < self.logic.rows:
                    for c in range(min(len(values), self.logic.cols)):
                        self.logic.grid[r][c] = values[c]
        self.draw_grid()


    def toggle_running(self, event=None):
        """
        Starts or stops the game simulation when called

        Args:
            event (tk.Event): The tkinter key event (optional)
        """
        self.is_running = not self.is_running
        if self.is_running:
            self.run_step()

    def run_step(self):
        """
        Executes a single step of the game and schedules the next one if running.
        """
        if self.is_running:
            self.logic.step()
            self.draw_grid()
            self.root.after(100, self.run_step)

    def update(self):
        """
        Redraws the board (used for manual refresh or after loading).
        """
        self.draw_grid()
