from pyglet import text

from constants import LABEL_HEIGHT, BOARD_WIDTH, SQUARE_SIZE, BOARD_HEIGHT, LABEL_PADDING


class InfoPainter:
    def __init__(self):
        self._board_width = SQUARE_SIZE * BOARD_WIDTH
        self._board_height = SQUARE_SIZE * BOARD_HEIGHT

        self._label = None
        self.msg = ""
        self.show_initial_info()

    def draw_current_info(self):
        self._create_label()
        self._label.draw()

    def show_initial_info(self):
        self.msg = "Pick a Square to start finding Knight's Tour from"

    def show_finding_tour_info(self):
        self.msg = "Looking for possible Tours... It may take up to few minutes"

    def show_tour_ready_info(self):
        self.msg = "Knight's Tour is ready! Use Left and Right arrows to navigate or simply use Space for autoplay."

    def show_tour_not_found_info(self):
        self.msg = "It's impossible for Knight to travel whole board starting at this Square. Please pick another start point"

    def _create_label(self):
        self._label = text.Label(self.msg,
                                 font_name='Times New Roman',
                                 font_size=14,
                                 x=self._board_width // 2, y=self._board_height + LABEL_HEIGHT - LABEL_HEIGHT // 2,
                                 width=self._board_width - LABEL_PADDING,
                                 align='center',
                                 anchor_x='center', anchor_y='center',
                                 multiline=True)
