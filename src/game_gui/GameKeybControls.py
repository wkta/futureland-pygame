import pygame

from coremon_main import EventReceiver, PygameBridge, EngineEvTypes
from datamodel.Camera import Camera
from datamodel.Player import Player


class GameKeybControls(EventReceiver):

    def __init__(self, ref_player, ref_camera):
        super().__init__()
        self._player_mod = ref_player
        self._cam = ref_camera
        self._camera_mode = False

    def proc_event(self, ev, source):
        if ev.type == PygameBridge.KEYDOWN:

            if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                self._camera_mode = True

            if self._camera_mode:
                target = self._cam
            else:
                target = self._player_mod

            if ev.key == PygameBridge.K_RIGHT:
                target.move(Player.DIR_EAST)

            elif ev.key == PygameBridge.K_UP:
                target.move(Player.DIR_NORTH)

            if ev.key == PygameBridge.K_LEFT:
                target.move(Player.DIR_WEST)

            elif ev.key == PygameBridge.K_DOWN:
                target.move(Player.DIR_SOUTH)

        elif ev.type == PygameBridge.KEYUP:
            if not (pygame.key.get_mods() & pygame.KMOD_SHIFT):
                self._camera_mode = False

        elif ev.type == EngineEvTypes.LOGICUPDATE:  # scrolling continu camera
            tmp = pygame.key.get_pressed()
            if self._camera_mode and tmp[PygameBridge.K_RIGHT]:
                self._cam.move(Camera.DIR_EAST)
            elif self._camera_mode and tmp[PygameBridge.K_UP]:
                self._cam.move(Camera.DIR_NORTH)
            elif self._camera_mode and tmp[PygameBridge.K_LEFT]:
                self._cam.move(Camera.DIR_WEST)
            elif self._camera_mode and tmp[PygameBridge.K_DOWN]:
                self._cam.move(Camera.DIR_SOUTH)
