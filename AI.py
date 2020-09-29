import copy


class CheckersAI:
    def __init__(self, game, maxDepth):
        self.root_board = State(copy.deepcopy(game), None, 0, None, None)
        self.max_depth = maxDepth

    def minimax(self, current):
        if current.depth == self.max_depth:
            current.best_route = current
            return current.game.board.value, current.game.board.tie
        current.create_children()
        if not len(current.childrenStates):
            return current.game.board.value, current.game.board.tie
        else:
            if current.type == 1:
                M = -100000
                T = -100000
                best = None
                for c in current.childrenStates:
                    main, tie = self.minimax(c)
                    if main > M:
                        best = c
                        M = main
                        T = tie
                    elif main == M and tie > T:
                        best = c
                        T = tie
                current.best_route = best
                return M, T
            else:
                M = 100000
                T = 100000
                best = None
                for c in current.childrenStates:
                    main, tie = self.minimax(c)
                    if main < M:
                        best = c
                        M = main
                        T = tie
                    elif main == M and tie < T:
                        best = c
                        T = tie
                current.best_route = best
                return M, T

    def fig_move(self):
        self.minimax(self.root_board)
        if self.root_board.best_route is not None:
            return self.root_board.best_route.fig, self.root_board.best_route.chom
        else:
            return None, None


class State:
    def __init__(self, game, parent, depth, chain_of_moves, fig):
        self.game = copy.deepcopy(game)
        self.game.board.set_value(n=10)
        self.type = self.game.move
        self.parent = parent
        self.childrenStates = []
        self.depth = depth
        self.best_route = None
        self.chom = chain_of_moves
        self.fig = fig

    def create_children(self):
        self.game.possible_moves()
        for fig in self.game.board.pieces:
            if fig.col == self.type:
                if fig.moves is not None:
                    for c in fig.moves:
                        next_board = copy.deepcopy(self.game)
                        next_board.set_chosen_pawn(fig.x, fig.y)
                        for x in c:
                            next_board.move_chosen_pawn(x[0], x[1])
                        new_state = State(next_board, self, self.depth + 1, copy.deepcopy(c), copy.deepcopy(fig))
                        self.childrenStates.append(new_state)
