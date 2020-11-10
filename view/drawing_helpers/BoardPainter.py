from constants import VISITED_SQUARE_COLOR
from model.ChessBoardPosition import ChessBoardPosition
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

    def visit_square(self, position: ChessBoardPosition):
        square = self._find_square(position)
        square.set_color(VISITED_SQUARE_COLOR)

    def unvisit_square(self, position: ChessBoardPosition):
        square = self._find_square(position)
        square.reset_color()

    def _find_square(self, position: ChessBoardPosition) -> BoardSquare:
        dummy_square = BoardSquare(position.h_index, position.v_index)
        i = self.board_squares.index(dummy_square)
        return self.board_squares[i]
