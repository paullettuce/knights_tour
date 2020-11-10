# main code

import pyglet

from constants import SQUARE_SIZE
from knights_tour.KnightsTour import KnightsTour
from model.board import *
from view.ChessBoardWindow import ChessBoardWindow


def on_knight_locked(h_index, v_index):
    knightsTour.start(h_index, v_index, on_tour_found=window.add_route_info, on_tour_not_found=window.tour_not_found)


board_width = 5
board_height = 5

board = Board(board_width, board_height)
knightsTour = KnightsTour(board)

window = ChessBoardWindow(board,
                          on_knight_locked,
                          board_width * SQUARE_SIZE, board_height * SQUARE_SIZE,
                          "Knight's Tour")

pyglet.app.run()
