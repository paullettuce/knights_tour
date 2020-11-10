import pyglet
from pyglet import clock
from pyglet.shapes import Line

from constants import *
from view.BoardSquare import BoardSquare
from view.ChessmanPainter import ChessmanPainter
from view.PygletKnightPiece import PygletKnightPiece
from view.BoardPainter import BoardPainter

class ChessBoardWindow(pyglet.window.Window):

    def __init__(self, board, on_knight_locked, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.on_knight_locked = on_knight_locked

        self._chessman_painter = ChessmanPainter(on_knight_locked)
        self._board_painter = BoardPainter(board)

        self.additional_shapes = []
        self.knight_tour = []

    def on_draw(self):
        self.clear()
        self._board_painter.draw_board()
        self._chessman_painter.draw_all()

        for shape in self.additional_shapes:
            shape.draw_board()

    def on_mouse_press(self, x, y, button, modifiers):
        h_index = int(x / SQUARE_SIZE)
        v_index = int(y / SQUARE_SIZE)

        if not self._chessman_painter.is_knight_locked():
            self.lock_knight(h_index, v_index)
        else:
            clock.unschedule(self._draw_next_step)
            clock.schedule_interval(self._draw_next_step, 1)

    def on_mouse_enter(self, x, y):
        self._chessman_painter.create_floating_sprite(x, y)

    def on_mouse_leave(self, x, y):
        self._chessman_painter.delete_floating_sprite()

    def on_mouse_motion(self, x, y, dx, dy):
        self._chessman_painter.update_floating_sprite(x, y)

    def add_route_info(self, route):
        for step in route:
            self.knight_tour.append(step)

    def _draw_next_step(self, _):
        if self.knight_tour:
            step = self.knight_tour.pop(0)
            self.move_knight(step.x, step.y)

    def lock_knight(self, h_index, v_index):
        self.mark_square_as_visited(h_index, v_index)
        self._chessman_painter.lock_knight(h_index, v_index)

    def move_knight(self, h_index, v_index):
        self._board_painter.mark_square_as_visited(h_index, v_index)

        old_h_index = self.knight_piece.h_index
        old_v_index = self.knight_piece.v_index
        self.draw_line(old_h_index, old_v_index, h_index, v_index)

        self._chessman_painter.move_knight(h_index, v_index)

    def mark_square_as_visited(self, h_index, v_index):
        self._board_painter.mark_square_as_visited(h_index, v_index)

    def draw_line(self, from_h_index, from_v_index, to_h_index, to_v_index):
        from_x = self._calculate_center_of_square_for_index(from_h_index)
        from_y = self._calculate_center_of_square_for_index(from_v_index)
        to_x = self._calculate_center_of_square_for_index(to_h_index)
        to_y = self._calculate_center_of_square_for_index(to_v_index)
        line = Line(from_x, from_y, to_x, to_y, width=LINE_WIDTH, color=LINE_COLOR)
        self.additional_shapes.append(line)
        line.draw()

    def _calculate_center_of_square_for_index(self, axis_index):
        return int(axis_index * SQUARE_SIZE + SQUARE_SIZE / 2)
