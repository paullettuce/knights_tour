import logging
import time

from knights_tour.KnightsTourMoves import KnightsTourMoves, TourNode
from model.stack import Stack


class KnightsTour:

    def __init__(self, board):
        self.board = board
        self.moves = KnightsTourMoves()
        self.tour_steps_stack = Stack(max_size=board.size_horizontal * board.size_vertical)
        self.tries = 0
        self.start_time = time.time()

    def start(self, x, y, on_tour_found, on_tour_not_found):
        self._log_start(x, y)
        self._add_first_node(x, y, self.tour_steps_stack)
        self._depth_first_search(self.tour_steps_stack)
        self._print_result()

        if self.tour_steps_stack.is_full():
            on_tour_found(self.tour_steps_stack.as_list())
        else:
            on_tour_not_found()
            self.tour_steps_stack.clear()

    def _add_first_node(self, x, y, stack):
        root = TourNode(x, y)
        stack.push(root)

    def _depth_first_search(self, stack):
        self._log_tries()

        # proceed
        top = stack.top()
        moves = self.moves.find_available_moves(top.x, top.y, self.board.size_horizontal, self.board.size_vertical,
                                                stack)

        # loop through possible move options from current node,
        # recurrently checking every each one of them
        while moves.__len__() > 0:
            next_node = moves.pop(0)
            if stack.size() < stack.max_size:
                stack.push(next_node)
                self._depth_first_search(stack)

        # if no more moves in this node, remove it from tour stack,
        # and go back to check other possible moves from previous node
        if moves.__len__() == 0 and 1 < stack.size() < stack.max_size:
            stack.pop()

    def _print_result(self):
        print("Knights Tour: ")
        print("[", end="")
        for i in range(self.tour_steps_stack.size()):
            print(self.tour_steps_stack.get(i).to_string(), end="; ")
        print("]")
        self._print_tries()

    def _log_tries(self):
        self.tries += 1
        if self.tries % 150000 == 0:
            self._print_tries()
        if self.tries % 1000000 == 0:
            self._print_result()

    def _print_tries(self):
        logging.info("Try no " + str(self.tries) +
                     ", time passed: " + self._solving_time() +
                     ". Stack size is " + str(self.tour_steps_stack.size()))

    def _solving_time(self) -> str:
        seconds_passed = time.time() - self.start_time
        return str(int(seconds_passed)) + " sec"

    def _log_start(self, x, y):
        logging.info("Finding Knight's Tour in progress, beginning at " + str(x) + "," + str(y))
