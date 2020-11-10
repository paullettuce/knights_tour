from constants import VISITED_SQUARE_COLOR
from view.BoardSquare import BoardSquare


class BoardPainter:
    def __init__(self, board):
        self.board_squares = self._create_board(board.size_horizontal, board.size_vertical)

    def draw_board(self):
        # print("BoardPainter: draw_board")
        for square in self.board_squares:
            square.draw()

    def _create_board(self, size_horizontal, size_vertical):
        squares = []
        for i in range(size_horizontal):
            for j in range(size_vertical):
                squares.append(BoardSquare(i, j))
        return squares

    def mark_square_as_visited(self, h_index, v_index):
        dummy_square = BoardSquare(h_index, v_index)
        i = self.board_squares.index(dummy_square)
        drawn_square = self.board_squares[i]
        drawn_square.set_color(VISITED_SQUARE_COLOR)