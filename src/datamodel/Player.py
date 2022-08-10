import katagames_engine as kengi
from defs import MyEvTypes


class Player(kengi.event.CogObj):

    DIR_EAST, DIR_NORTH, DIR_WEST, DIR_SOUTH = range(4)

    def __init__(self):
        super().__init__()
        self._x, self._y = 0, 0

    def get_pos(self):
        return self._x, self._y

    def move(self, direction):
        if direction == self.DIR_EAST:
            self._x += 1
        elif direction == self.DIR_NORTH:
            self._y -= 1
        elif direction == self.DIR_WEST:
            self._x -= 1
        elif direction == self.DIR_SOUTH:
            self._y += 1

        self.pev(MyEvTypes.PlayerMoves, newx=self._x, newy=self._y)
