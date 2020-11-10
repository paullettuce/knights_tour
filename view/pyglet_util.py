import pyglet


def create_pyglet_square(x, y, size, color, border_color):
    return pyglet.shapes.BorderedRectangle(x, y, size, size, color=color, border_color=border_color)

