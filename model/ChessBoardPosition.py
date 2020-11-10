from constants import SQUARE_SIZE


class ChessBoardPosition:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.horizontal_index = self._calculate_index(x)
        self.vertical_index = self._calculate_index(y)

    def _calculate_index(self, coordinate):
        return int(coordinate / SQUARE_SIZE)

