import copy
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
            self.winner = None

    def possible_moves(self):
        m = 0
        for fig in self.board.pieces:
            if fig.col == self.move:
                fig.move(self.board.board)
                m = max(m, fig.canBeat)
        if m > 0:
            for fig in self.board.pieces:
                if fig.canBeat < m and fig.col == self.move:
                    fig.moves = None

    def switch(self):
        self.move *= -1
        self.chosen_pawn = None
        self.moved_chosen = False
        self.possible_moves()
        if self.is_end():
            self.winner = self.move * (-1)

    def is_in_any_chain(self, X, Y):
        pos = (X, Y)
        for chain in self.chosen_pawn.moves:
            for c in chain:
                if c == pos:
                    return True
        return False

    def is_first_in_any_chain(self, X, Y):
        pos = (X, Y)
        for chain in self.chosen_pawn.moves:
            if chain[0] == pos:
                return True
        return False

    def modify_chains(self, X, Y):
        pos = (X, Y)
        temp = copy.deepcopy(self.chosen_pawn.moves)
        us = 0
        for i in range(len(temp)):
            if temp[i][0] != pos:
                self.chosen_pawn.moves.remove(temp[i])
                us += 1
            else:
                if len(self.chosen_pawn.moves[i - us]) > 1:
                    self.chosen_pawn.moves[i - us] = self.chosen_pawn.moves[i - us][1:]
                else:
                    self.chosen_pawn.moves.remove(self.chosen_pawn.moves[i - us])
        return  self.chosen_pawn.moves

    def showpositions(self, x, y):
        if self.board.board[x][y] == self.move:
            return self.board.get_fig(x, y).moves
        return None

    def set_chosen_pawn(self, x, y):
        if self.board.board[x][y] == self.move:
            self.chosen_pawn = self.board.get_fig(x, y)
        print(self.chosen_pawn.moves)

    def move_chosen_pawn(self, x, y):
        if math.fabs(self.chosen_pawn.x - x) > 1:
            to_kill = self.board.get_fig(int((1 / 2) * (x + self.chosen_pawn.x)),
                                         int((1 / 2) * (y + self.chosen_pawn.y)))
            self.board.pieces.remove(to_kill)
        self.chosen_pawn.change_pos(x, y)
        self.board.update_board_matrix()

    def check_end_move(self):
        if self.moved_chosen and not len(self.chosen_pawn.moves):
            return True
        else:
            return False

    def is_end(self):
        for fig in self.board.pieces:
            if fig.moves is not None:
                return False
        return True
