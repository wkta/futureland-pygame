import sys

import pygame

import coremon_main
import glvars
from coremon_main.runners import VanillaGameCtrl
from datamodel.Camera import Camera
from datamodel.Player import Player
from game_gui.Avatar import Avatar
from game_gui.GameKeybControls import GameKeybControls
from game_gui.WorldView import WorldView

"""
Soon we are gonna use some tools:
- gameobjects.SpriteSheet to load a tileset
- matricks.IntegerMatrix and BoolMatrix to store level data (static structures)
"""


print('------------------------------------')
print('~Futureland: the game~')
print('this is python {}'.format(sys.version))
print('pygame version is {}'.format(pygame.ver))
print()
print('CONTROLS:')
print('* use arrows to move')
print('------------------------------------')
print()

coremon_main.init(glvars.SCR_SIZE, glvars.SOFTWARE_LBL)

# - creating a data model
player = Player()
cam = Camera()

# - what user will see and do...
v = WorldView(player, cam)
vp = Avatar(player, cam)

pcontrols = GameKeybControls(player, cam)
game_ctrl = VanillaGameCtrl(max_fps=110)


# - run the game

# -- activating game components
v.turn_on()
vp.turn_on()

pcontrols.turn_on()
game_ctrl.turn_on()

# -- game loop
game_ctrl.loop()

# -- clean exit
coremon_main.cleanup()
print('game ended. See ya!')
