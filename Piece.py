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
