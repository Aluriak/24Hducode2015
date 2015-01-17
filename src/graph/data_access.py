"""
Access by dictionnary to all data in json.
"""
import json
import os
from collections import defaultdict

PATH = '../../data/'
data, graph = {}, defaultdict(list)


def generationGraph :
    for file_name in ['11_A', '11_R', '12_A', '12_R', '16_A', '16_R', '17_A', '17_R', '18_A', '18_R', '19_A', '19_R',
                       '20_A', '20_R', '21_A', '21_R', '22_A', '22_R', '23_A', '23_R', '24_A', '24_R', '25_A', '25_R',
                       '26_A', '26_R', '27_A', '27_R', '2_A', '2_R', '3_A', '3_R', '4_A', '4_R', '5_A','5_R', '6_A', '6_R',
                       '8_A', '8_R', '9_A', '9_R', 'T1_A', 'T1_R', 'T2_A', 'T2_R']:
        with open(PATH+file_name+'.json', 'r') as fl:
            data[file_name] = json.loads(fl.read())

        # id of previous
        prev_id = None
        #for stop in data[file_name]['stops']:
            #if prev_id is not None:
                #graph[prev_id].append(stop['id'])
                #        prev_id = stop['id']
        for stop in data[file_name]['stops']:
            if prev_id is not None:
                for i in data[file_name]['n_stop']-prev_id['position']:
                    graph[prev_id].append(['id'])
            prev_id = stop['id']

    #print(dir(data['11_A']))
    #print(data['11_A'].keys())
    print(graph)


def generationHoraire :
    for file_name in ['11_A', '11_R', '12_A', '12_R', '16_A', '16_R', '17_A', '17_R', '18_A', '18_R', '19_A', '19_R',
                       '20_A', '20_R', '21_A', '21_R', '22_A', '22_R', '23_A', '23_R', '24_A', '24_R', '25_A', '25_R',
                       '26_A', '26_R', '27_A', '27_R', '2_A', '2_R', '3_A', '3_R', '4_A', '4_R', '5_A','5_R', '6_A', '6_R',
                       '8_A', '8_R', '9_A', '9_R', 'T1_A', 'T1_R', 'T2_A', 'T2_R']:
        with open(PATH+file_name+'.json', 'r') as fl:
            data[file_name] = json.loads(fl.read())

        id_tmp = None
        for stop in data[file_name]:
            if id_none is not None:
                for horaire in date[file_name]['schedule'][stop['track_id']][abbrev_du_jour]:
                    horaires[stop['track_id'][abbrev_du_jour].append(horaire)
