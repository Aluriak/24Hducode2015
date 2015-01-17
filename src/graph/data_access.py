"""
Access by dictionnary to all data in json.
"""
import json
import os
from collections import defaultdict

PATH = '../../data/'
data, graph = {}, defaultdict(list)

for file_name in ['11_A', '11_R', ]:
    with open(PATH+file_name+'.json', 'r') as fl:
        data[file_name] = json.loads(fl.read())

    # id of previous 
    prev_id = None
    for stop in data[file_name]['stops']:
        if prev_id is not None:
            graph[prev_id].append(stop['id'])
        prev_id = stop['id']

print(dir(data['11_A']))
print(data['11_A'].keys())
print(graph)



