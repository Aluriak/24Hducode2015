"""
Access by dictionnary to all data in json.
"""
import json
import graph.schedule_manager
import os
from collections import defaultdict
from horaire import Horaire

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



def creat_weight():
    """ HEAVY generation of main dictionnary

    returned dict link a track, a stop and a date to a date.
    value is the date when bot will arrived to given stop, if 
    follow given track since given date.

    date must be in format provided (not expected in move query)
    by the server
    """
    from schedule_manager import all_next_cars
    data = {}
    return data




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
