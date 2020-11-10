from pyglet import clock

from model.ChessBoardPosition import ChessBoardPosition
from view.KnightsControllerInterface import KnightsControllerInterface


class KnightsTourDrawingHelper:
    def __init__(self, knights_controller: KnightsControllerInterface):
        self._route = []
        self._current_index = 0
        self._knights_controller = knights_controller

    def add_route(self, route):
        self._current_index = 0
        self._route = route.copy()

    def manually_draw_next_step(self):
        self._unschedule_auto_drawing()
        self._draw_next_step(None)

    def undo_last_step(self):
        self._unschedule_auto_drawing()
        step = self._previous_step()
        if step:
            self._knights_controller.move_knight_back(ChessBoardPosition(step.x, step.y))

    def schedule_auto_drawing(self):
        self._unschedule_auto_drawing()
        clock.schedule_interval(self._draw_next_step, 1)

    def _unschedule_auto_drawing(self):
        clock.unschedule(self._draw_next_step)

    def _draw_next_step(self, _):
        step = self._next_step()
        if step:
            self._knights_controller.move_knight(ChessBoardPosition(step.x, step.y))

    def _next_step(self):
        new_index = self._current_index + 1
        if new_index >= len(self._route):
            return None
        else:
            self._current_index = new_index
            return self._current_step()

    def _previous_step(self):
        new_index = self._current_index - 1
        if new_index < 0:
            return None
        else:
            self._current_index = new_index
            return self._current_step()

    def _current_step(self):
        return self._route[self._current_index]


