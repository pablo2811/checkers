from abc import abstractmethod


class Piece:
    def __init__(self, x, y, col):
        self.x = x
        self.y = y
        self.col = col

    @abstractmethod
    def longest_chain(self,board):
        ...
