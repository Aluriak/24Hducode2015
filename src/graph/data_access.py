"""
Access by dictionnary to all data in json.
"""
import json
import graph.schedule_manager
import os
from collections import defaultdict
from horaire import Horaire
from graph.schedule_manager import next_car


CURRENT_DATE = 0
PENALTY_TRACK_CHANGE = 70
PENALTY_CONNECTION_DATE_NOT_VALID = 30
PENALTY_UNKNOWN_CONNECTION = 20
PENALTY_PASTED_CONNECTION = 0
PENALTY_BAD_TRACK = 30
PENALTY_BAD_STOP = 0
PENALTY_UNKNOWN_TRACK = 30
PATH = '../data/'
TRACKS =  ['11_A', '11_R', '12_A', '12_R', '16_A', '16_R', '17_A', '17_R', '18_A', '18_R', '19_A', '19_R',
           '20_A', '20_R', '21_A', '21_R', '22_A', '22_R', '23_A', '23_R', '24_A', '24_R', '25_A', '25_R',
           '26_A', '26_R', '27_A', '27_R', '2_A', '2_R', '3_A', '3_R', '4_A', '4_R', '5_A','5_R', '6_A', '6_R',
           '8_A', '8_R', '9_A', '9_R', 'T1_A', 'T1_R', 'T2_A', 'T2_R']


def next_stop(structure, track_id, stop_id):
    """ SHORTCUT for structure dict

    Return unique id of stop after given stop_id in track of id track_id, 
    or None if no next stop.
    stop_id and track_id must be the unique id.
    """
    return structure[track_id, stop_id]


def creat_tracknames():
    data = {}
    for file_name in TRACKS:
        with open(PATH+file_name+'.json', 'r') as fl:
            data[json.loads(fl.read())['track_id']] = file_name
    return data




def creat_structure():
    """ HEAVY creation of main dictionnary

    Creation of structure dictionnary, that link (track_id, stop_id) to stop_id,
    where value is id of the stop in track of track_id that is just next received stop_id.
    structure[track, stop] : next_stop
    """
    data = {}
    for file_name in TRACKS:
        with open(PATH+file_name+'.json', 'r') as fl:
            brute_data = json.loads(fl.read())
            previous_stop = None
            for stop in brute_data['stops']:
                if previous_stop is not None:
                    data[brute_data['track_id'], previous_stop] = stop['id']
                previous_stop = stop['id']

    return data



def creat_schedules():
    """ HEAVY creation of main dictionnary

    Creation of schedule dictionnary, that link a track and a stop (by their id) 
    to a schedule object.
    This construction assume that all days have the same schedule.

    """
    data = {}

    for file_name in TRACKS:
        with open(PATH+file_name+'.json', 'r') as fl:
            brute_data = json.loads(fl.read())
            for stop in brute_data['stops']:
                # get schedule of stop the monday (or any other day)
                # and put it in data dict
                sched = brute_data['schedule'][str(stop['id'])]['lu']
                # translate in Horaire object all values of schedules
                data[brute_data['track_id'], stop['id']] = \
                    [Horaire.from_schedules_dialect(_) for _ in sched]

    return data



def compute_weight(current_track, tested_track, current_stop, tested_stop, initial_time, time, structure, schedules):
    """
    Returned weight of path between current_stop and tested_stop, by passing 
    through tested_track. The last taked track is current_track, the initial_time game time is initial_time,
    time is current time, structure the heavy dictionnary creat with creat_structure(), and schedules the heavy dictionnary 
    create with creat_schedules().
    Returne also the time to leave the current_node
    format : 
        weight, time
    """

    #assert(isinstance(time, Horaire))
    next_car_index  = next_car(schedules[tested_track, current_stop], time)
    new_date        = schedules[tested_track, tested_stop][next_car_index]
    new_time        = new_date.as_minutes()
    start_date      = initial_time.as_minutes()
    #assert(new_time > start_date)

    return (new_time - start_date) + (PENALTY_TRACK_CHANGE if current_track is not tested_track else 0), schedules[tested_track, current_stop][next_car_index]


def creat_linkings(structure):
    """ HEAVY generation of main dictionnary

    Link a stop_id to tracks that pass over this stop_id.
    return dict have stop_id as key and a set of track_id as value
    
    Take a structure dictionnary (see creat_structure function)
    as parameter
    """
    # a set can't have doublons
    # so values can't have doublons
    linking = defaultdict(set)
    for track_id, stop_id in structure.keys():
        linking[stop_id].add(track_id)
    return linking





if __name__ == '__main__':
    next_stop = creat_structure()
    schedules = creat_schedules()
    linkings  = creat_linkings (next_stop)
    track = 36
    stop  = 1334 
    print(next_stop[track, stop])
    print(schedules[track, stop])
