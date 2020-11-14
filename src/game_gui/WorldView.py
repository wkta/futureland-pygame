import coremon_main as enjin
from coremon_main import EventReceiver, EngineEvTypes
import pygame


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


class WorldView(EventReceiver):

    BG_COLOR = (85, 33, 55)

    def __init__(self, player, cam):
        super().__init__()
        self._player_mod = player
        self._cam = cam
        self._ft = pygame.font.Font(None, 38)

    def _drawlarge_sq_screen(self, wlandmarks):
        scr_landmark = list()
        for lan in wlandmarks:
            scr_landmark.append(self._cam.to_screen_coords(*lan))
        pygame.draw.polygon(enjin.screen, (5, 88, 5), scr_landmark, 2)

    def proc_event(self, ev, source):
        if ev.type == EngineEvTypes.PAINT:
            enjin.screen.fill(self.BG_COLOR)

            # (this code is rly dirty, but this is meant to be a temporary thing)
            # it shows four large squares, so the user can get a sense of camera+player movements
            for world_landmarks in possib_wlandmarks:
                self._drawlarge_sq_screen(world_landmarks)

            # -- Even more DIRTY DEBUG infos ---
            pl_pos_txt = 'player '+str(self._player_mod.get_pos())
            cam_pos_txt = 'camera '+str(self._cam.get_pos())
            labels = [
                self._ft.render(pl_pos_txt, False, (180, 180, 100)),
                self._ft.render(cam_pos_txt, False, (180, 180, 100))
            ]
            enjin.screen.blit(labels[0], (0, 0))
            enjin.screen.blit(labels[1], (0, 96))
