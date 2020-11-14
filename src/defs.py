from coremon_main import enum_for_custom_event_types, CgmEvent
from coremon_main.util import enum_starting_from_zero

GameStates = enum_starting_from_zero('Default')
MyEvTypes = enum_for_custom_event_types(
    'PlayerMoves',  # contains: newx, newy
    'CameraMoves',  # contains: newx, newy
    'NewLevel'
)
CgmEvent.inject_custom_names(MyEvTypes)
