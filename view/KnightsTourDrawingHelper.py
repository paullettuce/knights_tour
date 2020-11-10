from pyglet import clock


class KnightsTourDrawingHelper:

    def __init__(self, window):
        self.window = window

    def draw_route(self, route):
        self.execute_all_moves(route)

    def execute_all_moves(self, route):
        self.window.draw_knight_tour(route)
