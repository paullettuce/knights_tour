import abc


class AvailableMoves:
    @abc.abstractmethod
    def find_available_moves(self, x, y, board_width, board_height):
        pass

    @staticmethod
    def is_move_valid(x, y, board_width, board_height):
        return board_width > x >= 0 and board_height > y >= 0


class KnightsAvailableMoves(AvailableMoves):
    def find_available_moves(self, x, y, board_width, board_height):
        moves = []
        for x, y in [(x - 1, y - 2),
                     (x - 1, y + 2),
                     (x + 1, y - 2),
                     (x + 1, y + 2),
                     (x - 2, y - 1),
                     (x + 2, y - 1),
                     (x - 2, y + 1),
                     (x + 2, y + 1)]:
            if self.is_move_valid(x, y, board_width, board_height):
                moves.append((x, y))
        return moves
