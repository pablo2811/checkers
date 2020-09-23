import copy
import math
import time
from board import Board
from Queen import Queen
from Pawn import Pawn
import AI


class GameLogic:
    def __init__(self, save=False,move=-1):
        if save:
            pass
            # add saving
        else:
            self.board = Board()
            self.move = move
            self.chosen_pawn = None
            self.moved_chosen = False
            self.possible_moves()
            self.winner = None
            self.AI = None
            self.chain_ai = None

    def possible_moves(self):
        m = 0
        for fig in self.board.pieces:
            if fig.col == self.move:
                fig.move(self.board.board)
                m = max(m, fig.canBeat)
        if self.is_end():
            self.winner = self.move * (-1)
        if m > 0:
            for fig in self.board.pieces:
                if fig.canBeat < m and fig.col == self.move:
                    fig.moves = None

    def check_queen_upgrade(self):
        if (self.move == 1 and self.chosen_pawn.x == 7) or (not self.chosen_pawn.x and self.move == -1):
            Q = Queen(self.chosen_pawn.x, self.chosen_pawn.y, self.move)
            self.board.pieces.append(Q)
            self.board.pieces.remove(self.chosen_pawn)

    def switch(self):
        self.move *= -1
        self.chosen_pawn = None
        self.AI = None
        self.chain_ai = None
        self.moved_chosen = False
        self.possible_moves()

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
        return self.chosen_pawn.moves

    def showpositions(self, x, y):
        if self.board.board[x][y] == self.move:
            return self.board.get_fig(x, y).moves
        return None

    def set_chosen_pawn(self, x, y):
        if self.board.board[x][y] == self.move:
            self.chosen_pawn = self.board.get_fig(x, y)

    def move_chosen_pawn(self, x, y):
        if type(self.chosen_pawn) is Pawn and math.fabs(self.chosen_pawn.x - x) > 1:
            to_kill = self.board.get_fig(int((1 / 2) * (x + self.chosen_pawn.x)),
                                         int((1 / 2) * (y + self.chosen_pawn.y)))
            self.board.pieces.remove(to_kill)
        elif type(self.chosen_pawn) is Queen and math.fabs(self.chosen_pawn.x - x) > 1:
            i = int(math.copysign(1, self.chosen_pawn.x - x))
            j = int(math.copysign(1, self.chosen_pawn.y - y))
            l = 1
            while x + i * l != self.chosen_pawn.x and y + j * l != self.chosen_pawn.y:
                if self.board.board[x + i * l][y + j * l] == -self.chosen_pawn.col:
                    to_kill = self.board.get_fig(x + i * l, y + j * l)
                    self.board.pieces.remove(to_kill)
                    break
                else:
                    l += 1
        self.chosen_pawn.change_pos(x, y)
        self.board.update_board_matrix()

    def moveAI(self):
        if self.chosen_pawn is None:
            self.AI = AI.CheckersAI(self, 3)
            figx, self.chain_ai = self.AI.fig_move()
            self.set_chosen_pawn(figx.x,figx.y)
        else:
            self.move_chosen_pawn(self.chain_ai[0][0], self.chain_ai[0][1])
            self.moved_chosen = True
            self.chain_ai.remove(self.chain_ai[0])
            time.sleep(1)
        if self.chain_ai is not None and not len(self.chain_ai):
            self.switch()



    def check_end_move(self):
        if self.moved_chosen and not len(self.chosen_pawn.moves):
            self.check_queen_upgrade()
            return True
        else:
            return False

    def is_end(self):
        for fig in self.board.pieces:
            if fig.col == self.move:
                if fig.moves is not None:
                    return False
        return True
