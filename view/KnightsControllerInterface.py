import abc

from model.ChessBoardPosition import ChessBoardPosition


class KnightsControllerInterface:
    @abc.abstractmethod
    def move_knight(self, position: ChessBoardPosition):
        pass

    @abc.abstractmethod
    def move_knight_back(self, to_position: ChessBoardPosition):
        pass
