from pyglet import image
from pyglet.sprite import Sprite

from constants import SQUARE_SIZE, CHESS_PIECE_SCALING
from model.ChessBoardPosition import ChessBoardPosition


class PygletKnightPiece:
    def __init__(self, position: ChessBoardPosition, sprite):
        self._position = position
        self._sprite = sprite

    def draw(self):
        self._sprite.draw()

    def update(self, position):
        self._position = position
        x = self._calculate_sprite_x()
        y = self._calculate_sprite_y()
        self._sprite.update(x, y)

    def position(self) -> ChessBoardPosition:
        return self._position

    def _calculate_sprite_x(self):
        sprite_width = self._sprite.sprite.width
        return self._calculate_center(self._position.h_index, sprite_width)

    def _calculate_sprite_y(self):
        sprite_height = self._sprite.sprite.height
        return self._calculate_center(self._position.v_index, sprite_height)

    def _calculate_center(self, axis_index, image_size):
        return int(axis_index * SQUARE_SIZE + SQUARE_SIZE / 2 - image_size / 2)


class PygletSprite:
    def __init__(self, x, y, resource_name='knight_w.png'):
        self.x = x
        self.y = y

        self.sprite = self._create_and_scale_sprite(resource_name)

    def draw(self):
        self.sprite.draw()

    def update(self, x, y):
        image_width = self.sprite.width
        image_height = self.sprite.height
        self.x = self._calculate_center_of_square(x, image_width)
        self.y = self._calculate_center_of_square(y, image_height)
        self.sprite.update(self.x, self.y)

    def _create_and_scale_sprite(self, resource_name):
        knight_image = image.load(resource_name)

        sprite_scaling = self._calculate_scaling_for_sprite(knight_image.width, SQUARE_SIZE * CHESS_PIECE_SCALING)
        sprite = Sprite(knight_image, self.x, self.y)
        sprite.update(self.x, self.y, scale=sprite_scaling)
        sprite.anchor_x = sprite.width // 2
        sprite.anchor_y = sprite.height // 2
        return sprite

    def _calculate_scaling_for_sprite(self, current_image_size, target_size) -> float:
        return target_size / current_image_size

    def _calculate_center_of_square(self, coordinate, image_size):
        index = int(coordinate / SQUARE_SIZE)
        return int(index * SQUARE_SIZE + SQUARE_SIZE / 2 - image_size / 2)

