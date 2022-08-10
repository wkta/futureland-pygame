import katagames_engine as kengi

MyEvTypes = kengi.event.enum_ev_types(
    'PlayerMoves',  # contains: newx, newy
    'CameraMoves',  # contains: newx, newy
    'NewLevel'
)
