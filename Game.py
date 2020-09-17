from board import Board


class GameLogic:
    def __init__(self, save=False):
        if save:
            pass
            # add saving
        else:
            self.board = Board()
            self.move = -1

    def possible_moves(self):
        m = 0
        for fig in self.board.pieces:
            if fig.col == self.move:
                fig.move(self.board.board)
                m = max(m, fig.canBeat)
        if m > 0:
            for fig in self.board.pieces:
                if fig.canBeat < m:
                    fig.moves = None

    def switch(self):
        self.move *= -1
        self.possible_moves()
    
    def showpositions(self,x,y):
        self.possible_moves()
        if self.board.board[x][y] == self.move:
            return self.board.get_fig(x,y).moves






