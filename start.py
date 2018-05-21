from ex45.engine import Engine
from ex45.map import Map

#import sys
#print(sys.path)

start_room = 'central_corridor'

##################################################################################
# START
##################################################################################

a_map = Map(start_room)
a_game = Engine(a_map)
a_game.play()