# main code

import pyglet

from constants import SQUARE_SIZE, BOARD_HEIGHT, BOARD_WIDTH, LABEL_HEIGHT
from knights_tour.KnightsTour import KnightsTour
from model.board import *
from view.ChessBoardWindow import ChessBoardWindow


def on_knight_locked(h_index, v_index):
    knightsTour.start(h_index, v_index, on_tour_found=window.add_route_info, on_tour_not_found=window.tour_not_found)


board = Board(BOARD_WIDTH, BOARD_HEIGHT)
knightsTour = KnightsTour(board)

window = ChessBoardWindow(board,
                          on_knight_locked,
                          BOARD_WIDTH * SQUARE_SIZE, BOARD_HEIGHT * SQUARE_SIZE + LABEL_HEIGHT,
                          "Knight's Tour")

pyglet.app.run()
