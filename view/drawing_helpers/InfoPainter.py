from pyglet import text

from constants import LABEL_HEIGHT, BOARD_WIDTH, SQUARE_SIZE, BOARD_HEIGHT, LABEL_PADDING
from view.drawing_helpers.ProgressPainter import ProgressPainter


class InfoPainter:
    def __init__(self):
        self._board_width = SQUARE_SIZE * BOARD_WIDTH
        self._board_height = SQUARE_SIZE * BOARD_HEIGHT
        self._label = None
        self._progress_painter = ProgressPainter()
        self._should_show_progress = False
        self.show_initial_info()

    def draw_current_info(self):
        if self._label:
            self._label.draw()

        if self._should_show_progress:
            self._progress_painter.show()
        else:
            self._progress_painter.hide()

    def show_initial_info(self):
        msg = "Pick a Square to start finding Knight's Tour from"
        self._create_label(msg)

    def show_finding_tour_info(self):
        msg = "Looking for possible Tours... It may take up to few minutes"
        self._create_label(msg)
        self._show_progress()

    def show_tour_ready_info(self):
        msg = "Knight's Tour is ready! Use Left and Right arrows to navigate or simply use Space for autoplay."
        self._create_label(msg)
        self._hide_progress()

    def show_tour_not_found_info(self):
        msg = "It's impossible for Knight to travel whole board starting at this Square. Please pick another start point"
        self._create_label(msg)
        self._hide_progress()

    def _create_label(self, msg):
        self._label = text.Label(msg,
                                 font_name='Times New Roman',
                                 font_size=14,
                                 x=self._board_width // 2, y=self._board_height + LABEL_HEIGHT - LABEL_HEIGHT // 2,
                                 width=self._board_width - LABEL_PADDING,
                                 align='center',
                                 anchor_x='center', anchor_y='center',
                                 multiline=True)

    def _show_progress(self):
        self._should_show_progress = True

    def _hide_progress(self):
        self._should_show_progress = False
