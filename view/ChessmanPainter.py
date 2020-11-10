from view.PygletKnightPiece import PygletSprite, PygletKnightPiece


class ChessmanPainter:
    def __init__(self, on_knight_locked):
        self._on_knight_locked = on_knight_locked
        self._floating_sprite = None
        self._knight = None

    def draw_all(self):
        self._draw_floating_sprite()
        self._draw_knight()

    def create_floating_sprite(self, x, y):
        if not self.is_knight_locked():
            self._floating_sprite = PygletSprite(x, y, 0.9)

    def delete_floating_sprite(self):
        self._floating_sprite = None

    def update_floating_sprite(self, x, y):
        if self._floating_sprite:
            self._floating_sprite.update(x, y, True)

    def is_knight_locked(self) -> bool:
        return self._knight

    def lock_knight(self, h_index, v_index):
        self._knight = PygletKnightPiece(h_index, v_index, self._floating_sprite)
        self._knight.draw()
        self.delete_floating_sprite()
        self._on_knight_locked(h_index, v_index)

    def move_knight(self, h_index, v_index):
        self._knight.update(h_index, v_index)

    def _draw_knight(self):
        if self.is_knight_locked():
            self._knight.draw()

    def _draw_floating_sprite(self):
        if not self.is_knight_locked() and self._is_floating_sprite_created():
            self._floating_sprite.draw()

    def _is_floating_sprite_created(self):
        return self._floating_sprite
