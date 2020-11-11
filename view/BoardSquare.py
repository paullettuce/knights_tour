from constants import *
from model.ChessBoardPosition import ChessBoardPosition
from view.pyglet_util import create_pyglet_square


class BoardSquare:
    def __init__(self, position: ChessBoardPosition):
        self.h_index = position.h_index
        self.v_index = position.v_index
        self.color = self._pick_color()
        self.pyglet_rectangle = None

    def __eq__(self, other):
        return self.h_index == other.h_index and self.v_index == other.v_index

    def draw(self):
        if not self.pyglet_rectangle:
            self.pyglet_rectangle = create_pyglet_square(
                self.h_index * SQUARE_SIZE,
                self.v_index * SQUARE_SIZE,
                SQUARE_SIZE,
                self.color,
                border_color=SQUARE_BORDER_COLOR)
        self.pyglet_rectangle.color = self.color
        self.pyglet_rectangle.draw()

    def set_color(self, color):
        self.color = color

    def reset_color(self):
        self.color = self._pick_color()

    def _pick_color(self):
        if (self.h_index + self.v_index) % 2 == 0:
            return BLACK
        else:
            return WHITE
