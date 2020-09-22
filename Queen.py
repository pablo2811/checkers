import copy

from Piece import Piece


class Queen(Piece):
    def __init__(self, x, y, col):
        super().__init__(x, y, col)
        self.canBeat = 0
        self.moves = None

    def longest_chain(self, board):
        all_chains = []
        in_board = lambda x: 7 >= x >= 0
        def util(current, x, y, badxdir, badydir, chain):
            for i in [1, -1]:
                for j in [1, -1]:
                    if i != badxdir or j != badydir:
                        l = 1
                        while in_board(x + l * i) and in_board(y + l * j) and not board[x + l * i][y + l * j]:
                            l += 1
                        if in_board(x + l * i) and in_board(y + l * j) and board[x + l * i][y + l * j] == -self.col:
                            opx = x + l * i
                            opy = y + l * j
                            l += 1
                            while in_board(x + l * i) and in_board(y + l * j) and not board[x + l * i][y + l * j]:
                                new_chain = copy.deepcopy(chain)
                                new_chain.append((x + l * i, y + l * j))
                                new_board = copy.deepcopy(current)
                                new_board[opx][opy] = 0
                                new_board[x][y] = 0
                                new_board[x + l * i][y + l * j] = self.col
                                util(new_board, x + l * i, y + l * j, -i, -j, new_chain)
                                l += 1
            all_chains.append(chain)
        util(board,self.x,self.y,None,None,[])
        m = 0
        for chain in all_chains:
            m = max(m, len(chain))
        temp = copy.deepcopy(all_chains)
        for t in temp:
            if len(t) < m:
                all_chains.remove(t)
        return all_chains

    def move(self, board):
        temp = self.longest_chain(board)
        if len(temp):
            self.canBeat = len(temp[0])
            res = temp
        else:
            self.canBeat = 0
            res = []
            in_board = lambda x: 7 >= x >= 0
            for i in [1, -1]:
                for j in [1, -1]:
                    leng = 1
                    while in_board(self.x + leng * i) and in_board(self.y + leng * j) and not board[self.x + leng * i][
                        self.y + leng * j]:
                        res.append([(self.x + leng * i, self.y + leng * j)])
                        leng += 1
        self.moves = res

