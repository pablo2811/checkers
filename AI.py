import copy


class CheckersAI:
    def __init__(self, game, maxDepth):
        self.root_board = State(copy.deepcopy(game), None, 1, 0)
        self.max_depth = maxDepth
        self.best_route = []

    def minimax(self,current):
        if current.depth == self.max_depth:
            return current.game.board.value
        current.create_children()
        if current.type == 1:
            M = -100000
            best = None
            for c in current.childrenStates:
                temp = self.minimax(c)
                if temp > M:
                    best = c
                    M = temp
            return M
        else:
            M = 100000
            for c in current.childrenStates:
                M = min(c.game.board.value, M)
            return M


class State:
    def __init__(self, game, parent, type, depth):
        self.game = copy.deepcopy(game)
        self.game.board.set_value()
        self.type = type
        self.parent = parent
        self.childrenStates = []
        self.depth = depth

    def create_children(self):
        self.game.possible_moves()
        for fig in self.game.board.pieces:
            if fig.col == type:
                self.game.set_chosen_pawn(fig.x, fig.y)
                if fig.moves is not None:
                    for c in fig.moves:
                        next_board = copy.deepcopy(self)
                        for x in c:
                            next_board.game.move_chosen_pawn(x[0], x[1])
                        new_state = State(next_board, self, -self.type, self.depth + 1)
                        self.childrenStates.append(new_state)
