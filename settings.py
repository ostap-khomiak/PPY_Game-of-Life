class GameSettings:
    """
    A class to store settings for the Game of Life
    """
    def __init__(self, rows=30, cols=30, survive=(2,3), birth=3):
        """
        Initializes the GameSettings

        Args:
            rows (int): Number of rows on the board
            cols (int): Number of columns on the board
            survive (tuple or int): Neighbor counts for cell survival
            birth (tuple or int): Neighbor counts for cell birth
        """

        self.rows = rows
        self.cols = cols
        self.survive = survive
        self.birth = birth
