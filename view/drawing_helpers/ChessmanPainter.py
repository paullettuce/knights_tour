from model.ChessBoardPosition import ChessBoardPosition
from view.PygletKnightPiece import PygletSprite, PygletKnightPiece


class ChessmanPainter:
    def __init__(self):
        self._floating_sprite = None
        self._knight = None

    def draw_all(self):
        self._draw_floating_sprite()
        self._draw_knight()

    def create_floating_sprite(self, x, y):
        if not self.is_knight_locked():
            self._floating_sprite = PygletSprite(x, y)

    def delete_floating_sprite(self):
        self._floating_sprite = None

    def update_floating_sprite(self, x, y):
        if self.is_knight_locked():
            return
        if not self._floating_sprite:
            self.create_floating_sprite(x, y)
        self._floating_sprite.update(x, y)

    def is_knight_locked(self) -> bool:
        return self._knight

    def lock_knight(self, position: ChessBoardPosition):
        self._knight = PygletKnightPiece(position, self._floating_sprite)
        self.delete_floating_sprite()

    def unlock_knight(self) -> ChessBoardPosition:
        position = self._knight.position()
        self._knight = None
        return position

    def move_knight(self, position: ChessBoardPosition):
        self._knight.update(position)

    def knight_position(self) -> ChessBoardPosition:
        return self._knight.position()

    def _draw_knight(self):
        if self.is_knight_locked():
            self._knight.draw()

    def _draw_floating_sprite(self):
        if not self.is_knight_locked() and self._is_floating_sprite_created():
            self._floating_sprite.draw()

    def _is_floating_sprite_created(self):
        return self._floating_sprite
