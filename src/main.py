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



def jouer():
    init()
    dijkstra()
	move() = moves.pop
    while not arrived
        send_move(move)
        move = moves.pop()
		
		
		if response['success']:
			if response['status'] == "moved":
		        send_move(move)
    		    move = moves.pop()
			elif response['status'] == "rerouted":
				init(response.target)
		elif not response['success']:
			print(response['status'])


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
    start()
	jouer()
