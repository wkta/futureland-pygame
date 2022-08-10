import katagames_engine as kengi
import glvars
pygame = kengi.pygame
EngineEvTypes = kengi.event.EngineEvTypes

k = 180
possib_wlandmarks = [
    [(0, 0), (0, -k), (-k, -k), (-k, 0)],  # carré allant de Org vers NW
    [(k, 0), (k, -k), (0, -k), (0, 0)],  # de Est vers Nord
    [(k, k), (k, 0), (0, 0), (0, k)],  # de SE vers Org
    [(0, k), (0, 0), (-k, 0), (-k, k)],  # de S vers W

    [ (0, -2*k), (-2*k, -2*k), (-2*k, 0)],  # carré allant de Org vers NW
    [(2*k, 0), (2*k, -2*k), (0, -2*k)],  # de Est vers Nord
    [(2*k, 2*k), (2*k, 0), (0, 2*k)],  # de SE vers Org
    [(0, 2*k), (-2*k, 0), (-2*k, 2*k)],  # de S vers W
]

Receiver = kengi.event.EventReceiver


class WorldView(Receiver):

    BG_COLOR = (85, 33, 55)

    def __init__(self, player, cam, etm_obj):
        super().__init__()
        self._player_mod = player
        self._cam = cam
        self._ft = pygame.font.Font(None, 38)
        self._etm_obj = etm_obj

    def _drawlarge_sq_screen(self, wlandmarks):
        scr_landmark = list()
        for lan in wlandmarks:
            scr_landmark.append(self._cam.to_screen_coords(*lan))
        pygame.draw.polygon(kengi.get_surface(), (5, 88, 5), scr_landmark, 2)

    @staticmethod
    def colorcode_to_rgb(cc):
        # exemple: cc peut être 3748067
        ch = bin(cc)[2:]

        # normalise longueur seq bits -> 24
        if len(ch) <= 3*8:
            x = ch.zfill(3*8)
        elif cc > 16777215:  # soit 24 digits 1 en binaire...
            x = bin(16777215)[2:]

        # decoupage & conversion vers int
        bi_r = x[16:]
        bi_g = x[8:16]
        bi_b = x[:8]

        # t = list(bi_b)
        # t[6] = '0'
        # t[7] = '0'
        # bi_b = ''.join(t)

        r, g, b = int(bi_r, 2)//2, int(bi_g, 2), int(bi_b, 2)
        if b > g:
            tmp = g
            g = b
            b = tmp

        # contrast reduction
        r /= 1.25
        g /= 1.33
        b /= 1.5

        return int(r), int(g), int(b)

    def draw_tile(self, ij_coords, colorcode):
        tsize = 59  # px

        xscr, yscr = self._cam.to_screen_coords(ij_coords[0]*60, ij_coords[1]*60)
        pygame.draw.rect(
            kengi.get_surface(),
            WorldView.colorcode_to_rgb(colorcode),
            (xscr, yscr, tsize, tsize),
            0
        )

    def proc_event(self, ev, source):
        if ev.type == EngineEvTypes.PAINT:
            kengi.get_surface().fill(self.BG_COLOR)

            # (this code is rly dirty, but this is meant to be a temporary thing)
            # it shows four large squares, so the user can get a sense of camera+player movements
            for world_landmarks in possib_wlandmarks:
                self._drawlarge_sq_screen(world_landmarks)

            # affiche couleurs (tuiles) par-dessus large squares
            mw, mh = self._etm_obj.get_size()
            i, j = self._player_mod.get_pos()
            for w in range(mw):
                for h in range(mh):
                    self.draw_tile((w, h), self._etm_obj[(w, h)])

            # -- Even more DIRTY DEBUG infos in overlay... ---
            pl_pos_txt = 'player '+str(self._player_mod.get_pos())
            cam_pos_txt = 'camera '+str(self._cam.get_pos())
            labels = [
                self._ft.render(pl_pos_txt, False, (180, 180, 100)),
                self._ft.render(cam_pos_txt, False, (180, 180, 100))
            ]
            scr = kengi.get_surface()
            scr.blit(labels[0], (0, 0))
            scr.blit(labels[1], (0, 96))
