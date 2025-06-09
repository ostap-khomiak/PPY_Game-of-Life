class GameLogic:
    """
    Handles the logic for Game of Life
    """

    def __init__(self, settings):
        """
        Initializes the game logic using provided settings

        Args:
            settings (GameSettings): The settings for the game
        """
        self.rows = settings.rows
        self.cols = settings.cols
        self.survive = settings.survive
        self.birth = settings.birth
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]


    def step(self):
        """
        Advances the game by one generation
        """
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        for row in range(self.rows):
            for col in range(self.cols):
                alive_neighbors = self.count_alive_neighbors(row, col)

                if self.grid[row][col] == 1 and alive_neighbors in self.survive:
                    new_grid[row][col] = 1
                elif self.grid[row][col] == 0 and alive_neighbors in self.birth:
                    new_grid[row][col] = 1

        self.grid = new_grid



    def count_alive_neighbors(self, row, col):
        """
        Counts the number of alive neighboring cells around a cell

        Args:
            row (int): Row index of the cell
            col (int): Column index of the cell

        Returns:
            int: The number of alive neighbors
        """

        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue

                neighbor_row = row + i
                neighbor_col = col + j

                if 0 <= neighbor_row < self.rows and 0 <= neighbor_col < self.cols:
                    count += self.grid[neighbor_row][neighbor_col]

        return count
