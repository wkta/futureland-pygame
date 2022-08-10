import sys
import katagames_engine as kengi
kengi.bootstrap_e()

import glvars
from datamodel.Camera import Camera
from datamodel.ElasticTilemap import ElasticTilemap
from datamodel.Player import Player
from game_gui.Avatar import Avatar
from game_gui.GameKeybControls import GameKeybControls
from game_gui.WorldView import WorldView


kengi.init()

# TODO
# - use SpriteSheet tool to load a tileset
# - use matricks.IntegerMatrix and BoolMatrix to store level data (static structures)
pygame = kengi.pygame

print('------------------------------------')
print('~Futureland: the game~')
print('this is python {}'.format(sys.version))
print('pygame version is {}'.format(pygame.ver))
print()
print('CONTROLS:')
print('* use arrows to move')
print('------------------------------------')
print()

# coremon_main.init(glvars.SCR_SIZE, glvars.SOFTWARE_LBL)

# - creating a data model
player = Player()
cam = Camera()
etm_obj = ElasticTilemap(player.get_pos())

# - what user will see and do...
v = WorldView(player, cam, etm_obj)
vp = Avatar(player, cam)

pcontrols = GameKeybControls(player, cam)
#game_ctrl = VanillaGameCtrl(max_fps=110)
game_ctrl = kengi.get_game_ctrl()

# - run the game

# -- activating game components
v.turn_on()
vp.turn_on()

pcontrols.turn_on()
game_ctrl.turn_on()

# -- game loop
game_ctrl.loop()

# -- clean exit
kengi.quit()
print('game ended. See ya!')
