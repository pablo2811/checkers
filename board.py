from pawn import Pawn


class Board:
    def __init__(self, pieces=None):

        if pieces is not None:
            self.pieces = pieces
        else:
            self.pieces = []
            j = 0
            for i in range(5, 8):
                while j < 8:
                    new_piece = Pawn(i, j, -1)
                    self.pieces.append(new_piece)
                    j += 2
                j = int(not j)
            j = 0
            for k in range(0, 3):
                while j < 8:
                    new_piece = Pawn(k, j, 1)
                    self.pieces.append(new_piece)
                    j += 2
                j = int(not j)

        self.board = [[0 for _ in range(8)] for __ in range(8)]
        for piece in self.pieces:
            self.board[piece.x][piece.y] = piece.col

    def get_fig(self, x, y):
        for fig in self.pieces:
            if fig.x == x and fig.y == y:
                return fig
        return None
