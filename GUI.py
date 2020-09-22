import arcade, Game
from arcade.gui import *
import Queen

SW = 1000
SH = 1000
TITLE = "Checkers"


class NewGameButton(UIFlatButton):
    def __init__(self, text, cx, cy, w, h, view):
        super().__init__(text, cx, cy, w, h)
        self.view = view

    def on_press(self):
        gui = Gui()
        self.view.window.show_view(gui)


class QuitButton(UIFlatButton):
    def __init__(self, text, cx, cy, w, h):
        super().__init__(text, cx, cy, w, h)

    def on_press(self):
        arcade.finish_render()


class SettingsButton(UIFlatButton):
    def __init__(self, text, cx, cy, w, h):
        super().__init__(text, cx, cy, w, h)
        self.pressed = False

    def on_press(self):
        self.pressed = not self.pressed


class MainMenuButton(UIFlatButton):

    def __init__(self, text, cx, cy, w, h, view):
        super().__init__(text, cx, cy, w, h)
        self.pressed = False
        self.gui = view

    def on_press(self):
        self.pressed = not self.pressed
        self.gui.window.show_view(Menu())


class After(arcade.View):
    def __init__(self):
        super().__init__()
        self.button_list = []
        self.setup()

    def setup(self):
        main_menu = MainMenuButton("Main menu", SW // 2, 11 * SH // 21, SW // 3, SH // 7, self)
        self.button_list.append(main_menu)
        restart = NewGameButton("Restart", SW // 2, 2 * SH // 3, SW // 3, SH // 7, self)
        self.button_list.append(restart)
        exit = QuitButton("Exit", SW // 2, 8 * SH // 21, SW // 3, SH // 7)
        self.button_list.append(exit)

    def on_draw(self):
        arcade.start_render()
        for button in self.button_list:
            button.draw()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        for button in self.button_list:
            if button.center_x - button.width // 2 < x < button.center_x + button.width // 2:
                if button.center_y - button.height // 2 < y < button.center_y + button.height // 2:
                    button.on_press()




class Gui(arcade.View):
    def __init__(self):
        super().__init__()
        self.game = Game.GameLogic()
        self.board = None
        self.cellsize = SH // 8
        self.show_possible = False
        self.dots = None

    def on_draw(self):
        arcade.start_render()
        if self.game.winner is not None:
            self.window.show_view(After())
            # add restart end-game view
        self.board = arcade.load_texture("board.jpg")
        blackPawn = arcade.load_texture("black.png")
        blackQueen = arcade.load_texture("blackQueen.png")
        redQueen = arcade.load_texture("redQueen.png")
        redPawn = arcade.load_texture("red.png")
        self.board.draw_sized(SW // 2, SH // 2, SW, SH)
        img = [None, [blackPawn, blackQueen], [redPawn, redQueen]]
        for piece in self.game.board.pieces:
            if type(piece) is Queen.Queen:
                i = 1
            else:
                i = 0
            img[piece.col][i].draw_sized(self.cellsize * piece.y + self.cellsize // 2,
                                         SW - self.cellsize * piece.x - self.cellsize // 2, self.cellsize,
                                         self.cellsize)
        if self.show_possible:
            dots = arcade.load_texture("dot.png")
            for z in self.dots:
                for p in z:
                    dots.draw_sized(self.cellsize * p[1] + self.cellsize // 2,
                                    SW - self.cellsize * p[0] - self.cellsize // 2, self.cellsize // 2,
                                    self.cellsize // 2)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        X = (SH - y) // self.cellsize
        Y = x // self.cellsize
        if self.show_possible or self.game.moved_chosen:
            if self.game.is_in_any_chain(X, Y) or self.game.moved_chosen:
                if self.game.is_first_in_any_chain(X, Y):
                    self.game.modify_chains(X, Y)
                    self.game.move_chosen_pawn(X, Y)
                    self.game.moved_chosen = True
                    if self.game.check_end_move():
                        self.game.switch()
                        self.show_possible = False
                        self.dots = None

            else:
                self.show_possible = False
                self.dots = None

        else:
            self.dots = self.game.showpositions(X, Y)
            if self.dots is not None:
                self.show_possible = True
                self.game.set_chosen_pawn(X, Y)


class Menu(arcade.View):
    def __init__(self):
        super().__init__()
        self.button_list = []
        self.setup()

    def setup(self):
        new_game = NewGameButton("New game", SW // 2, 2 * SH // 3, SW // 3, SH // 7, self)
        self.button_list.append(new_game)
        pvp = SettingsButton("PVP", 5 * SW // 12, 11 * SH // 21, SW // 6, SH // 7)
        computer = SettingsButton("Computer", 7 * SW // 12, 11 * SH // 21, SW // 6, SH // 7)
        self.button_list.append(pvp)
        self.button_list.append(computer)
        about = UIFlatButton("About", SW // 2, 8 * SH // 21, SW // 3, SH // 7)
        self.button_list.append(about)  # later on
        quitbutt = QuitButton("Quit", SW // 2, 5 * SH // 21, SW // 3, SH // 7)
        self.button_list.append(quitbutt)

    def on_draw(self):
        arcade.start_render()
        for button in self.button_list:
            button.draw()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        for button in self.button_list:
            if button.center_x - button.width // 2 < x < button.center_x + button.width // 2:
                if button.center_y - button.height // 2 < y < button.center_y + button.height // 2:
                    button.on_press()


def main():
    window = arcade.Window(SW, SH, TITLE)
    window.show_view(Menu())
    arcade.run()


if __name__ == "__main__":
    main()
