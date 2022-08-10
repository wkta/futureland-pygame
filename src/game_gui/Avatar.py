import katagames_engine as kengi
from defs import MyEvTypes
EngineEvTypes = kengi.event.EngineEvTypes
pygame = kengi.pygame
Receiver = kengi.event.EventReceiver


class Avatar(Receiver):

    def __init__(self, player, camera_model):
        super().__init__()
        self._pl = player
        self._cam = camera_model

        # where to draw?
        self.wtd_x, self.wtd_y = self._cam.to_screen_coords(*player.get_pos())

    def _refresh_player_screenpos(self):
        step = 60  # px
        a, b = self._pl.get_pos()
        a *= step
        b *= step
        self.wtd_x, self.wtd_y = self._cam.to_screen_coords(a, b)

    def proc_event(self, ev, source):
        if ev.type in (MyEvTypes.PlayerMoves, MyEvTypes.CameraMoves):
            self._refresh_player_screenpos()

        elif ev.type == EngineEvTypes.PAINT:
            pygame.draw.rect(kengi.get_surface(), (33, 25, 150), (self.wtd_x, self.wtd_y, 25, 25))
