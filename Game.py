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
        self.chosen_pawn = None
        self.moved_chosen = False
        # for fig in self.board.pieces:
        #     fig.rotate_self()
        self.possible_moves()
    
    def showpositions(self,x,y):
        self.possible_moves()
        if self.board.board[x][y] == self.move:
            return self.board.get_fig(x,y).moves
        return None

    def set_chosen_pawn(self,x,y):
        if self.board.board[x][y] == self.move:
            self.chosen_pawn = self.board.get_fig(x,y)

    def move_chosen_pawn(self,x,y):
        self.chosen_pawn.change_pos(x,y)

    def check_end_move(self):
        if self.moved_chosen and not len(self.chosen_pawn.moves):
            return True
        else:
            return False






