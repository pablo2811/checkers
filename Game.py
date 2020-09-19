import math

from board import Board


class GameLogic:
    def __init__(self, save=False):
        if save:
            pass
            # add saving
        else:
            self.board = Board()
            self.move = -1
            self.chosen_pawn = None
            self.moved_chosen = False
            self.possible_moves()

    def possible_moves(self):
        m = 0
        for fig in self.board.pieces:
            if fig.col == self.move:
                if fig.x == 4 and fig.y == 3:
                    print("herw")
                fig.move(self.board.board)
                m = max(m, fig.canBeat)
        if m > 0:
            for fig in self.board.pieces:
                if fig.canBeat < m:
                    fig.moves = None

    def switch(self):
        self.move *= -1
        self.chosen_pawn = None
        self.moved_chosen = False
        self.possible_moves()
    
    def showpositions(self,x,y):
        if self.board.board[x][y] == self.move:
            return self.board.get_fig(x,y).moves
        return None

    def set_chosen_pawn(self,x,y):
        if self.board.board[x][y] == self.move:
            self.chosen_pawn = self.board.get_fig(x,y)

    def move_chosen_pawn(self,x,y):
        if math.fabs(self.chosen_pawn.x - x) > 1 :
            to_kill = self.board.get_fig(int((1/2)*(x+self.chosen_pawn.x)),int((1/2)*(y+self.chosen_pawn.y)))
            self.board.pieces.remove(to_kill)
        self.chosen_pawn.change_pos(x,y)
        self.board.update_board_matrix()

    def check_end_move(self):
        if self.moved_chosen and not len(self.chosen_pawn.moves):
            return True
        else:
            return False






