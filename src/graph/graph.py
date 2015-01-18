# -*- encoding: utf-8 -*-
import heapq
import pickle
from graph.data_access import compute_weight
from collections import defaultdict
from horaire import Horaire
"""
Graph representation:
dict graph node:next
dict weights node-next:weight
"""

# weight of a edge
DISTANCE_BETWEEN_TWO_NODES = 1



def simplify_dijkstra(func):
    def wrap(*argv, **kwargs):
        path = func(*argv, **kwargs)
        new_path = []
        track_current, track_first_stop = path[0]
        previous_track, previous_stop   = path[0]
        for track, stop in path:
            if track is not track_current:
                # add only end of each
                new_path.append((previous_track, previous_stop))
                previous_track, previous_stop = track, stop

        print('POY:', new_path)
        return new_path
    return wrap



#@simplify_dijkstra
def dijkstra(next_stop, schedules, linkings, stop_start, stop_target, initial_time):
    """
    next_stop (structure), schedules, weights and linkings are dictionnary created since 
    data_access module.
    stop_start and stop_target are stop_id where bot start and where bot must go.

    return list of (track_id, stop_id, time) needed for reach target from start.
    track_id is the track that is taked from stop_id. time is object
    that is the time that can be send to server, and tell when we leave stop_id.
    """
    def pop_min_dist_nodes():
        """Return stop_id of the nearer stop_id from source that is in unwalked
        Remove the thing from unwalked"""
        unwalked.sort(key=lambda x:dist[x[1]], reverse=True)
        #unwalked.sort(key=lambda x:dist[x[1]])
        return unwalked.pop()[1]



    INFINITY = 999999999
    # def of a graph node :
    dist = defaultdict(lambda: INFINITY , {stop_start:0}) 
    prev = defaultdict(lambda: None     , {stop_start:(None, None)}) # value is (track, stop)
    time = {stop_start:Horaire(0, 0)}
    # all are unwalked, except stop_start
    unwalked = [(dist[stop_start], stop_start)]
    # get ordered list of nodes, by priority queue
    unwalked.extend(((INFINITY, stop) for stop in linkings.keys() if stop is not stop_start))
    #for node in linkings.keys():
        #heapq.heappush(unwalked, (INFINITY, node))
    

    # walk on all nodes
    while len(unwalked) > 0:
        #print('HPQ:', unwalked)
        stop = pop_min_dist_nodes()
        #print('PRV:', stop, prev, prev[stop])
        # for each neighbor of node
        for track, node in ((track, next_stop[track, stop]) for track in linkings[stop]):
            tested_track = prev[stop]
            tested_track = tested_track[0] if tested_track is not None else tested_track
            weight, leave_horaire = compute_weight(
                tested_track,  # we use this track
                track,          # we try this one
                stop,           # from here
                node,           # to here
                initial_time,   # we start to play at this time
                time[stop],     # at this moment 
                next_stop,      # to this stop
                schedules       # with these schedules
            )
            alt = dist[stop] + weight
            #print('DST:', dist, weight, alt, dist[node])
            if alt < dist[node]: # shorter path to node found
                dist[node] = alt
                prev[node] = (track, stop)
                #assert(next_stop[track, stop] == node)
                time[node] = leave_horaire

    
    # path reconstruction
    path = []
    #print(prev)
    previous = prev[stop_target]
    #print('CLE:', previous)
    while previous != (None, None):
        path = [(previous[0], next_stop[previous])] + path
        #path = [(previous[0], previous[1], time[previous[1]])] + path
        previous = prev[previous[1]]
    #print('BPH:', path)
    return path








