# -*- coding: utf-8 -*-
#########################
#       MAIN            
#########################


#########################
# IMPORTS               #
#########################
from server_request import Game, timin2timout




#########################
# PRE-DECLARATIONS      #
#########################



#########################
# CLASS                 #
#########################
# CONSTRUCTOR #################################################################
# PUBLIC METHODS ##############################################################
# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################
if __name__ == '__main__':
    g = Game(Game.TRAINING)
    g.start()
    while not g.game_have_begin():
        pass
    g.send_move('1123', '11_A', timin2timout(g.last_game_state['dtstart']))
    print(timin2timout(d))


