from model.available_moves import KnightsAvailableMoves


class ChessPiece:
    def __init__(self, board, position, moves, color):
        self.board = board
        self.position = position
        self.color = color
        self.moves = moves

    def possible_positions(self):
        self.moves.find_available_moves(
            self.position[0],
            self.position[1],
            self.board.size_horizontal,
            self.board.size_vertical)

    def move_to_square(self, square):
        self.position = square


class Knight(ChessPiece):
    def __init__(self, board, position, color):
        super().__init__(board, position, KnightsAvailableMoves(), color)
