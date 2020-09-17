import copy

import Piece


class Queen(Piece):
    def __init__(self, x, y, col):
        super().__init__(x, y, col)
        self.canBeat = 0
        self.moves = None

    def longest_chain(self, board):

        def util(current, x, y, badx, bady, chain):
            for i in [1, -1]:
                for j in [1, -1]:
                    if i != badx or j != bady:
                        steps = 1
                        while in_board(x + steps * i) and in_board(y + steps * j) and not current[x + steps * i][
                            y + steps * j]:
                            steps += 1
                        if in_board(x + (steps + 1) * i) and in_board(y + (steps + 1) * j) and not \
                        current[x + (steps + 1) * i][y + (steps + 1) * j] and current[x + steps * i][
                            y + steps * j] == -self.col:
                            posx_kill = x + steps * i
                            posy_kill = y + steps * j
                            while in_board(x + (steps + 1) * i) and in_board(y + (steps + 1) * j) and not \
                            current[x + (steps + 1) * i][y + (steps + 1) * j]:
                                nextMap = copy.deepcopy(current)
                                chain.append((x + (steps + 1) * i, y + (steps + 1) * j))
                                nextMap[x + (steps + 1) * i][y + (steps + 1) * j] = self.col
                                nextMap[x][y] = 0
                                nextMap[posx_kill][posy_kill] = 0
                                util(nextMap, x + (steps + 1) * i, y + (steps + 1) * j, i, j, chain)
            nonlocal lc
            if len(chain) > len(lc):
                lc = chain

        in_board = lambda x: 7 >= x >= 0
        lc = []
        util(board, self.x, self.y, None, None, [])
        return lc

    def move(self, board):
        temp = self.longest_chain(board)
        if len(temp):
            self.canBeat = len(temp)
            res = temp
        else:
            self.canBeat = 0
            res = []
            in_board = lambda x: 7 >= x >= 0
            for i in [1, -1]:
                for j in [1, -1]:
                    steps = 1
                    while in_board(self.x + steps * i) and in_board(self.y + steps * j) and not \
                    board[self.x + steps * i][self.y + steps * j]:
                        res.append((self.x + steps * i, self.y + steps * j))
                        steps += 1
        super(Queen, self).moves = res
