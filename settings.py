class GameSettings:
    def __init__(self, rows=30, cols=30, survive=(2,3), birth=3):
        self.rows = rows
        self.cols = cols
        self.survive = survive
        self.birth = birth
