from abc import abstractmethod


class Piece:
    def __init__(self, x, y, col):
        self.x = x
        self.y = y
        self.col = col
        self.canBeat = 0

    @abstractmethod
    def move(self, board):
        ...

    @abstractmethod
    def longest_chain(self, board):
        ...

    def change_pos(self, x, y):
        self.x = x
        self.y = y

    def rotate_self(self):
        self.x = 7 - self.x
        self.y = 7 - self.y