# main code
import concurrent.futures
import logging
import threading

import pyglet

from constants import SQUARE_SIZE, BOARD_HEIGHT, BOARD_WIDTH, LABEL_HEIGHT
from knights_tour.KnightsTour import KnightsTour
from model.board import *
from view.ChessBoardWindow import ChessBoardWindow


def on_knight_locked(h_index, v_index):
    x = threading.Thread(target=start_looking_for_tour, args=(h_index, v_index))
    x.start()


def start_looking_for_tour(h_index, v_index):
    logging.info("main, start_looking_for_tour")
    knightsTour.start(h_index, v_index, on_tour_found=window.add_route_info, on_tour_not_found=window.tour_not_found)


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
