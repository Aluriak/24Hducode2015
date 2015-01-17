"""
define some easy access to schedule data.
Work mainly with definitions of schedule take from json data.
"""


import datetime


def next_car(schedule, travel_time):
    """return date of next car, according to given schedule.
    
    Schedule is considered as a list of date (HH:MM:SS), that represent 
    when a car (or tram) arrives to a stop.

    travel_time input must be as 
        2015-03-18 04:44:00
    returned time is the same
    """

    travel_time = datetime.datetime.strptime(datetime.datetime.strptime(travel_time, '%Y-%m-%d %H:%M:%S').strftime('%H:%M:%S'), '%H:%M:%S')
    next_time = None

    for index, time in enumerate(schedule):
        time = datetime.datetime.strptime(time, '%H:%M:%S')
        # total_seconds is negative if travel_time is upper than time in schedule
        # if its possible to get car when arrived at the same time it go to next stop
        # just use >= instead of >
        if (time - travel_time).total_seconds() > 0:
            #print('SÉÉ:', time.__class__, time)
            #print('SÉÉ:', travel_time.__class__, travel_time)
            #print(time - travel_time)
            #print('AUI:', travel_time - time, (travel_time - time).total_seconds())
            #print('RET:', time)
            next_time = index
            break

    return 0 if next_time is None else next_time
    


if __name__ == '__main__':
    print(next_car(['00:15:00', '10:30:00', '10:32:00', '10:33:00', '23:34:00'], '2015-03-18 04:44:00'))
    print(next_car(['00:15:00', '10:30:00', '10:32:00', '10:33:00', '23:34:00'], '2015-03-18 10:31:00'))
    print(next_car(['10:30:00', '10:32:00', '10:33:00', '23:34:00'],             '2015-03-18 10:32:00'))
    print(next_car(['10:30:00', '10:32:00', '10:33:00', '23:34:00'],             '2015-03-18 23:34:00'))
    pass




