import pyglet
from pyglet import clock
from pyglet.shapes import Line

from constants import *
from model.ChessBoardPosition import ChessBoardPosition
from view.BoardPainter import BoardPainter
from view.ChessmanPainter import ChessmanPainter
from view.ShapesPainter import ShapesPainter


class ChessBoardWindow(pyglet.window.Window):

    def __init__(self, board, on_knight_locked, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.on_knight_locked = on_knight_locked

        self._chessman_painter = ChessmanPainter(on_knight_locked)
        self._board_painter = BoardPainter(board)
        self._shapes_painter = ShapesPainter()

        self.additional_shapes = []
        self.knight_tour = []

    def on_draw(self):
        self.clear()
        self._board_painter.draw_board()
        self._chessman_painter.draw_all()
        self._shapes_painter.draw_all()

    def on_mouse_press(self, x, y, button, modifiers):
        position = ChessBoardPosition.from_absolute_position(x, y)

        if not self._chessman_painter.is_knight_locked():
            self.lock_knight(position)
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
            self.move_knight(ChessBoardPosition(step.x, step.y))

    def lock_knight(self, position):
        self._board_painter.mark_square_as_visited(position)
        self._chessman_painter.lock_knight(position)

    def move_knight(self, new_position):
        self._board_painter.mark_square_as_visited(new_position)
        old_position = self._chessman_painter.knight_position()
        self._shapes_painter.add_line(old_position, new_position)
        self._chessman_painter.move_knight(new_position)

