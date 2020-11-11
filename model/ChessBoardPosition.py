from constants import SQUARE_SIZE


class ChessBoardPosition:
    def __init__(self, horizontal_index, vertical_index):
        self.h_index = horizontal_index
        self.v_index = vertical_index

    def __eq__(self, other):
        return self.h_index == other.h_index and self.v_index == other.v_index

    def to_string(self):
        return "(" + str(self.h_index) + "," + str(self.v_index) + ")"

    @staticmethod
    def from_absolute_position(x, y):
        return ChessBoardPosition(ChessBoardPosition.calculate_index(x), ChessBoardPosition.calculate_index(y))

    @staticmethod
    def calculate_index(coordinate):
        return int(coordinate / SQUARE_SIZE)
