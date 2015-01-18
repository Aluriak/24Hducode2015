# -*- coding: utf-8 -*-
#########################
#       MAIN            
#########################


#########################
# IMPORTS               #
#########################
from server_request import Game, timin2timout
from graph.schedule_manager import *
from graph.data_access import *




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

def init_graph():
    load_graph()




def demander_partie():
    prepare_request()
    send_request()
    wait_request()
    parse_responce()




def jouer():
    init()
    dijkstra()
    while not arrived
        send_step()
        step = next_step()
        if rerooted
            init()
            dijkstra()
    print(score)










if __name__ == '__main__':
    print(next_car(['00:15:00', '10:30:00', '10:32:00', '10:33:00', '23:34:00'], '2015-03-18 04:44:00'))
    next_stop = creat_structure()
    schedules = creat_schedules()
    linkings  = creat_linkings (next_stop)
    track = 36
    stop  = 1334 
    print(next_stop[track, stop])
    print(schedules[track, stop])
    #g = Game(Game.TRAINING)
    #g.start()
    #while not g.game_have_begin():
        #pass
    #g.send_move('1123', '11_A', timin2timout(g.last_game_state['dtstart']))
    #print(timin2timout(d))







    init_graph()
    demande_partie()
    jouer()
