from typing import Any

import pyglet
from pyglet import clock
from pyglet.window import key

from model.ChessBoardPosition import ChessBoardPosition
from view.KnightsControllerInterface import KnightsControllerInterface
from view.drawing_helpers.BoardPainter import BoardPainter
from view.drawing_helpers.ChessmanPainter import ChessmanPainter
from view.drawing_helpers.KnightsTourDrawingHelper import KnightsTourDrawingHelper
from view.drawing_helpers.ShapesPainter import ShapesPainter


class ChessBoardWindow(pyglet.window.Window, KnightsControllerInterface):

    def __init__(self, board, on_knight_locked, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.on_knight_locked = on_knight_locked

        self._chessman_painter = ChessmanPainter(on_knight_locked)
        self._board_painter = BoardPainter(board)
        self._shapes_painter = ShapesPainter()
        self._tour_drawing_helper = KnightsTourDrawingHelper(self)

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
            self._show_control_buttons()

    def on_mouse_enter(self, x, y):
        self._chessman_painter.create_floating_sprite(x, y)

    def on_mouse_leave(self, x, y):
        self._chessman_painter.delete_floating_sprite()

    def on_mouse_motion(self, x, y, dx, dy):
        self._chessman_painter.update_floating_sprite(x, y)

    def on_key_press(self, symbol, modifiers):
        if symbol is key.RIGHT:
            self._tour_drawing_helper.manually_draw_next_step()
            return
        if symbol is key.LEFT:
            self._tour_drawing_helper.undo_last_step()
            return
        if symbol is key.SPACE:
            self._tour_drawing_helper.schedule_auto_drawing()
            return

    def move_knight(self, new_position: ChessBoardPosition):
        old_position = self._chessman_painter.knight_position()
        self._board_painter.visit_square(new_position)
        self._shapes_painter.add_line(old_position, new_position)
        self._chessman_painter.move_knight(new_position)

    def move_knight_back(self, to_position: ChessBoardPosition):
        old_position = self._chessman_painter.knight_position()
        self._board_painter.unvisit_square(old_position)
        self._shapes_painter.remove_last_line()
        self._chessman_painter.move_knight(to_position)

    def add_route_info(self, route):
        self._tour_drawing_helper.add_route(route)

    def tour_not_found(self):
        # add label and reset
        pass

    def lock_knight(self, position: ChessBoardPosition):
        self._board_painter.visit_square(position)
        self._chessman_painter.lock_knight(position)

    def _show_control_buttons(self):
        # show info about control buttons
        pass
