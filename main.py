# main code
import logging
import threading

import pyglet

from constants import SQUARE_SIZE, BOARD_HEIGHT, BOARD_WIDTH, LABEL_HEIGHT
from knights_tour.KnightsTour import KnightsTour
from model.ChessBoardPosition import ChessBoardPosition
from model.board import *
from view.ChessBoardWindow import ChessBoardWindow

# NOTE FOR ME
# before moving on with this project
# - refactor KnightsTour class, think of faster way to find route


def on_knight_locked(position: ChessBoardPosition):
    x = threading.Thread(target=start_looking_for_tour, args=(position,))
    x.start()


def start_looking_for_tour(position: ChessBoardPosition):
    logging.info("main, start_looking_for_tour")
    knightsTour.start(position, on_tour_found=window.add_route_info, on_tour_not_found=window.tour_not_found)


format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")

board = Board(BOARD_WIDTH, BOARD_HEIGHT)
knightsTour = KnightsTour(board)

window = ChessBoardWindow(board,
                          on_knight_locked,
                          BOARD_WIDTH * SQUARE_SIZE, BOARD_HEIGHT * SQUARE_SIZE + LABEL_HEIGHT,
                          "Knight's Tour")

pyglet.app.run()
