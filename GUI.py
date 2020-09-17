import arcade,Game
from arcade.gui import *

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


class Gui(arcade.View):
    def __init__(self):
        super().__init__()
        self.game = Game.GameLogic()
        self.board = None


    def on_draw(self):
        arcade.start_render()
        self.board = arcade.load_texture("board.jpg")
        self.board.draw_sized(SW//2,SH//2,SW,SH)
    def on_update(self, delta_time: float):
        


class Menu(arcade.View):
    def __init__(self):
        super().__init__()
        self.button_list = []
        self.setup()

    def setup(self):
        new_game = NewGameButton("New game", SW // 2, 2 * SH // 3, SW // 3, SH // 7, self)
        self.button_list.append(new_game)
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
