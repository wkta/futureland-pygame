from math import cos, sin, pi

from matricks.IntegerMatrix import IntegerMatrix


class ElasticTilemap:
    """
    l'idée c'est d'avoir un tilemap qui va perdre des éléments & en gagner,
    au fur et à mesure du déplacement de l'avatar
    """

    DIAM = 17  # le diametre autour de l'avatar

    def __init__(self, anchor_coords):
        # the magic (terrain-gen) is done by this function
        self.height_func = lambda x: -1*100 + (228 + 128 * cos(0.0002 * x) + 32 * sin(0.01 * x) + 64 * sin(pi / 800 * x) + 16 * abs(
            sin(0.02 * x + (pi / 2))))
        c = 1+2*self.DIAM
        self._matrix_repr = IntegerMatrix((c, c))
        self.preload_tiles(anchor_coords)
        self._prev_anchor = None

    def get_size(self):
        return self._matrix_repr.get_size()

    def __getitem__(self, item):
        return self._matrix_repr.get_val(*item)

    def preload_tiles(self, anchcoords):
        x, y = anchcoords
        for j in range(y-self.DIAM, y+self.DIAM+1):
            for i in range(x-self.DIAM, x+self.DIAM+1):
                p = self.height_func(i)**2
                p *= self.height_func(j)*11
                self._matrix_repr.set_val(i, j, round(p / (2 ** 4)))
        self._prev_anchor = anchcoords

    def input_new_anchor(self, anchcoords):
        # todo décalage valeurs ds la matrice, recalcul du nécessaire
        self.preload_tiles(anchcoords)  # vraiment pas opti!

    def __str__(self):
        return str(self._matrix_repr)
