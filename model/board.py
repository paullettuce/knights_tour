from model.Color import *


class Board:

    def __init__(self, size_horizontal, size_vertical):
        self.size_horizontal = size_horizontal
        self.size_vertical = size_vertical
        self.squares = []
        self._add_squares()

    def fields_count(self):
        return self.size_vertical * self.size_horizontal

    def _add_squares(self):
        for i in range(self.size_horizontal):
            for j in range(self.size_vertical):
                self.squares.append(self._create_square(i, j))

    def _create_square(self, x, y):
        if (x + y) % 2 == 0:
            color = (255, 255, 255)
        else:
            color = (0, 0, 0)

        return Square(x, y, color)


class Square:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def positionString(self):
        return str(self.x + "," + self.y)

