from constants import *
from view.pyglet_util import create_pyglet_square


class BoardSquare:
    def __init__(self, horizontal_index, vertical_index):
        self.horizontal_index = horizontal_index
        self.vertical_index = vertical_index
        self.color = self._pick_color()
        self.pyglet_rectangle = None

    def __eq__(self, other):
        return self.horizontal_index == other.horizontal_index and self.vertical_index == other.vertical_index

    def draw(self):
        if not self.pyglet_rectangle:
            self.pyglet_rectangle = create_pyglet_square(
                self.horizontal_index * SQUARE_SIZE,
                self.vertical_index * SQUARE_SIZE,
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
        if (self.horizontal_index + self.vertical_index) % 2 == 0:
            return BLACK
        else:
            return WHITE
