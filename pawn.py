import copy
import Piece

class Pawn(Piece):
    def __init__(self, x, y, col):
        super().__init__(x, y, col)

    def longest_chain(self, board):

        def util(current, x, y, badx, bady, chain):
            for i in [1, -1]:
                for j in [1, -1]:
                    if in_board(x + 2 * i) and in_board(y + 2 * j) and current[x + i][y + i] == -self.col and not \
                            current[x + 2 * i][y + 2 * j]:
                        if x + 2 * i != badx or y + 2 * j != bady:
                            chain.append((x + 2 * i, y + 2 * j))
                        n = copy.deepcopy(current)
                        n[x + i][y + j] = 0
                        n[x][y] = 0
                        n[x + 2 * i][y + 2 * j] = self.col
                        util(n, x + 2 * i, y + 2 * j, x, y, chain)
            nonlocal lc
            if len(chain) > len(lc):
                lc = chain

        in_board = lambda x: 7 >= x >= 0
        lc = []
        util(board,self.x,self.y,None,None,[])
        return lc

    def move(self,board):
        in_board = lambda x: 7 >= x >= 0
        res = []
        temp = self.longest_chain(board)
        if not len(temp):
            for l in [1,-1]:
                if in_board(self.x+self.col) and in_board(self.y+l) and not board[self.x+self.col][self.y+l]:
                    res.append((self.x+self.col,self.y+l))
        else:
            res = temp
        return res



