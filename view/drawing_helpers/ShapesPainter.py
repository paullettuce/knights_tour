from pyglet.shapes import Line

from constants import *
from model.AbsolutePosition import AbsolutePosition


class ShapesPainter:
    def __init__(self):
        self._shapes = []

    def draw_all(self):
        for shape in self._shapes:
            shape.draw()

    def add_line(self, old_position, new_position):
        start_pos = self._calculate_center_of_square(old_position)
        end_pos = self._calculate_center_of_square(new_position)
        line = Line(start_pos.x, start_pos.y, end_pos.x, end_pos.y, width=LINE_WIDTH, color=LINE_COLOR)
        self._shapes.append(line)

    def remove_last_line(self):
        self._shapes.pop()

    def _calculate_center_of_square(self, position) -> AbsolutePosition:
        x = int(position.h_index * SQUARE_SIZE + SQUARE_SIZE / 2)
        y = int(position.v_index * SQUARE_SIZE + SQUARE_SIZE / 2)
        return AbsolutePosition(x, y)
