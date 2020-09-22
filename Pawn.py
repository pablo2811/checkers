import copy
from Piece import Piece


class Pawn(Piece):
    def __init__(self, x, y, col):
        super().__init__(x, y, col)
        self.canBeat = 0
        self.moves = None

    def longest_chain(self, board):

        def util(current, x, y, badx, bady, chain):
            for i in [1, -1]:
                for j in [1, -1]:
                    if in_board(x + 2 * i) and in_board(y + 2 * j) and current[x + i][y + j] == -self.col and not \
                            current[x + 2 * i][y + 2 * j]:
                        if x + 2 * i != badx or y + 2 * j != bady:
                            next_chain = copy.deepcopy(chain)
                            next_chain.append((x + 2 * i, y + 2 * j))
                            n = copy.deepcopy(current)
                            n[x + i][y + j] = 0
                            n[x][y] = 0
                            n[x + 2 * i][y + 2 * j] = self.col
                            util(n, x + 2 * i, y + 2 * j, x, y, next_chain)
            nonlocal lc, longest_len
            if len(chain) > longest_len:
                longest_len = len(chain)
                lc = [chain]
            elif len(chain) == longest_len and len(chain) > 0:
                lc.append(chain)

        longest_len = 0
        in_board = lambda x: 7 >= x >= 0
        lc = []
        util(board, self.x, self.y, None, None, [])

        return lc

    def move(self, board):
        in_board = lambda x: 7 >= x >= 0
        res = []
        temp = self.longest_chain(board)
        if not len(temp):
            self.canBeat = 0
            for l in [1, -1]:
                if in_board(self.x + self.col) and in_board(self.y + l) and not board[self.x + self.col][self.y + l]:
                    res.append([(self.x + self.col, self.y + l)])
        else:
            self.canBeat = len(temp[0])
            res = temp
        if not len(res):
            res = None
        self.moves = res
