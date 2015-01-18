# -*- encoding: utf-8 -*-
from queue import Queue
import pickle
"""
Graph representation:
dict graph node:next
dict weights node-next:weight
"""

# weight of a edge
DISTANCE_BETWEEN_TWO_NODES = 1



def simplify_dijkstra(func):
    def wrap(*argv, **kwargs):
        path = dijkstra(*argv, **kwargs)
        new_path = [path[0]]
        track_current, track_first_stop = path[0]
        previous_track, previous_stop   = path[0]
        for track, stop in path:
            if track is not track_current:
                # add only end of each
                new_path.append(previous_track, previous_stop)
            previous_track, previous_stop = track, stop
        # if the last is not pushed
        if path[-1] != new_path[-1]:
            new_path.append(path[0])

        return new_path
    return wrap



@simplify_dijkstra
def dijkstra(next_stop, schedules, linkings, stop_start, stop_target):
    """
    next_stop (structure), schedules, weights and linkings are dictionnary created since 
    data_access module.
    stop_start and stop_target are stop_id where bot start and where bot must go.

    return list of (track_id, stop_id) needed for reach target from start
    track_id is the track that is taked for reach stop_id.
    """
    import heapq
    INFINITY = 999999999
    # def of a graph node :
    dist = defaultdict(lambda: None, {stop_start:0}) 
    prev = defaultdict(lambda: None, {stop_start:(None, None)}) # value is (track, stop)
    time = defaultdict(lambda: None, {stop_start:Horaire(0, 0)})
    # all are unwalked, except stop_start
    unwalked = [_ for _ in linkings.keys() if _ is not stop_start]
    # get ordered list of nodes, by priority queue
    for node in linkings.keys():
        heapq.heappush(unwalked, (INFINITY, node))
    

    # walk on all nodes
    while len(unwalked) > 0:
        dist, stop = heapq.heappop(unwalked)
        # for each neighbor of node
        for track, node in (track, next_stop[track, stop] for track in linkings[stop]):
            weight, arrived_horaire = compute_weight(
                prev[stop][0],  # we are here
                track,          # we try this one
                stop,           # from here
                node,           # to here
                time[stop_start], # at this moment 
                next_stop,      # in this structure
                schedules       # with these schedules
            )
            alt = dist[stop] + weight
            if alt < dist[node]: # shorter path to node found
                dist[node] = alt
                prev[node] = (track, stop)

    
    # path reconstruction
    path = []
    cur_node = stop_target
    while cur_node is not None: # while first is not reach
        track, stop = prev[cur_node]
        path = path + [track, stop]
        cur_node = stop
    return  path
#function Dijkstra(Graph, source):


   #for each vertex v in Graph:  // Initialization
#if v ≠ source            // Where v has not yet been removed from Q (unvisited nodes)
     #dist[v] ← infinity             // Unknown distance function from source to v
        #prev[v] ← undefined            // Previous node in optimal path from source
     #end if 
     #add v to Q                     // All nodes initially in Q (unvisited nodes)
 #end for
 
 #while Q is not empty:
         #u ← vertex in Q with min dist[u]  // Source node in first case
         #remove u from Q 
         
         #for each neighbor v of u:           // where v has not yet been removed from Q.
             #alt ← dist[u] + length(u, v)
             #if alt < dist[v]:               // A shorter path to v has been found
                 #dist[v] ← alt 
                 #prev[v] ← u 
             #end if
         #end for
     #end while

     #return dist[], prev[]

                 #29  end function





