# -*- coding: utf-8 -*-
#########################
#       MAIN            
#########################


#########################
# IMPORTS               #
#########################
from server_request import Game, timin2timout
from server_request import Game
from graph.schedule_manager import *
from graph.data_access import *
from graph.graph import *




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



def times_creator(path, schedules, initial_time, server_initial_time):
    """
    wait for path as list of (track, stop), schedules dictionnary and initial_time in Horaire format
    """
    current_time = initial_time
    time_path = []
    for track, stop in path:
        current_time = schedules[track, stop][next_car(schedules[track, stop], current_time)]
        time_path.append((track, stop, current_time.to_server_dialect(day=server_initial_time.day, year=server_initial_time.year, month=server_initial_time.month)))
    return time_path


def jouer():
    print('CREATION OF RESSOURCES')
    next_stop = creat_structure()
    schedules = creat_schedules()
    linkings  = creat_linkings (next_stop)
    tracknames= creat_tracknames()
    print('END ! ')
    game = Game(mode=Game.TRAINING)
    #game = Game(mode=Game.ARENA)
    game.start()
    while not game.game_have_begin(): pass
    print('NOW, START PLAY !')
    stop_start, stop_target = game.main_stops()
    initial_time = game.begin_time()
    print('START  IS', stop_start)
    print('TARGET IS', stop_target)
    print('TIME   IS', initial_time)
    print('RUNNING…')
    path = dijkstra(next_stop, schedules, linkings, stop_start, stop_target, Horaire(4, 0))
    print(path)
    print('OK !')
    for track, stop, time in times_creator(path, schedules, initial_time, game.server_initial_time()):
        print(next_stop[track, stop], track, time)
        game.send_move(next_stop[track, stop], tracknames[track], time)
        #game.send_move(stop, tracknames[track], time)


    #while not response['status'] == "arrived":
        #if response['success']:
            #if response['status'] == "moved":
                #send_move(move)
                #move = moves.pop()
            #elif response['status'] == "rerouted":
                #init(response.target)
        #elif not response['success']:
            #print(response['status'])












if __name__ == '__main__':
    jouer()
    exit(0)
    #print('CREATION OF RESSOURCES')
    #next_stop = creat_structure()
    #schedules = creat_schedules()
    #linkings  = creat_linkings (next_stop)
    #print('END ! ')
    #print('NOW, START PLAY !')
    #stop_start, stop_target = 1334, 1291
    #initial_time = Horaire(5, 34)
    ##import random
    ##stop_target = random.choice(tuple(linkings.keys()))
    #print('START  IS', stop_start)
    #print('TARGET IS', stop_target)
    #print('TIME   IS', initial_time)
    #print('RUNNING…')
    #path = dijkstra(next_stop, schedules, linkings, stop_start, stop_target, Horaire(4, 0))
    #print('OK !')
    #for data in times_creator(path, schedules, initial_time):
        #print(data)
    
    #def tracks_list():
        #t = []
        #for v in linkings.values():
            #t.extend(list(v))
        #return t

    #for track, stop in dijkstra(next_stop, schedules, linkings, stop_start, stop_target, Horaire(4, 0)):
        #assert(stop in linkings.keys())
        #assert(track in tracks_list())
        #print(stop, ',', track, ':', next_stop[track, stop] if (track, stop) in next_stop else None)
    #print(next_car(['00:15:00', '10:30:00', '10:32:00', '10:33:00', '23:34:00'], '2015-03-18 04:44:00'))
    #next_stop = creat_structure()
    #schedules = creat_schedules()
    #linkings  = creat_linkings (next_stop)
    #track = 36
    #stop  = 1334 
    #print(next_stop[track, stop])
    #print(schedules[track, stop])
    #g = Game(Game.TRAINING)
    #g.start()
    #while not g.game_have_begin():
        #pass
    #g.send_move('1123', '11_A', timin2timout(g.last_game_state['dtstart']))
    #print(timin2timout(d))







    #init_graph()
    #start()
    #jouer()
