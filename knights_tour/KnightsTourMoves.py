from model.available_moves import AvailableMoves


class KnightsTourMoves:
    def find_available_moves(self, x, y, board_width, board_height, stack):
        moves = []
        for x, y in [(x - 1, y - 2),
                     (x - 1, y + 2),
                     (x + 1, y - 2),
                     (x + 1, y + 2),
                     (x - 2, y - 1),
                     (x + 2, y - 1),
                     (x - 2, y + 1),
                     (x + 2, y + 1)]:
            if AvailableMoves.is_move_valid(x, y, board_width, board_height):
                move = TourNode(x, y)
                if move not in stack:
                    moves.append(move)
        return moves


class TourNode:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_string(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
