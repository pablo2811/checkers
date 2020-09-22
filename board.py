from Pawn import Pawn


class Board:
    def __init__(self, pieces=None):

        if pieces is not None:
            self.pieces = pieces
        else:
            self.pieces = []
            k = 0
            for i in range(5, 8):
                j = k
                while j < 8:
                    new_piece = Pawn(i, j, -1)
                    self.pieces.append(new_piece)
                    j += 2
                k = int(not k)
            z = 1
            for k in range(0, 3):
                j = z
                while j < 8:
                    new_piece = Pawn(k, j, 1)
                    self.pieces.append(new_piece)
                    j += 2
                z = int(not z)

        self.board = [[0 for _ in range(8)] for __ in range(8)]
        self.update_board_matrix()
        self.value = None

    def set_value(self, n=3):
        v = 0
        for fig in self.pieces:
            if type(fig) is Pawn:
                inc = 1
            else:
                inc = n
            if fig.col == 1:
                v += n
            else:
                v -= n
        self.value = v

    def get_fig(self, x, y):
        for fig in self.pieces:
            if fig.x == x and fig.y == y:
                return fig
        return None

    def update_board_matrix(self):
        self.board = [[0 for _ in range(8)] for __ in range(8)]
        for piece in self.pieces:
            self.board[piece.x][piece.y] = piece.col
