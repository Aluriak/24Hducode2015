# -*- coding: utf-8 -*-
#########################
#       SERVER_REQUEST            
#########################


#########################
# IMPORTS               #
#########################
import json
import requests
import datetime
import locale
from secret import jacky_secret_key, jacky_token




#########################
# PRE-DECLARATIONS      #
#########################
def ask_server(url, json_data):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    return requests.post(url, data=json.dumps(json_data), headers=headers)


def timin2timout(timin):
    """
    return given time format (returned by server):
        2015-03-18T04:44:00+00:00
    in this time format (expected by server for move):
        2015-03-18 04:44:00
    """
    d = datetime.datetime.strptime(timin, '%Y-%m-%dT%H:%M:%S+00:00')
    d = datetime.datetime.strftime(d, '%d %a %H:%M:%S %Y')
    print(d)
    return d




#########################
# CLASS                 #
#########################
class Game():
    TRAINING = 'training'
    ARENA = 'arena'
    URL_START = 'http://24hc15.haum.org/api/connect/'
    URL_ROOT  = 'http://24hc15.haum.org'

# CONSTRUCTOR #################################################################
    def __init__(self, mode, token=jacky_token, secret_key=jacky_secret_key):
        if not mode in [Game.TRAINING, Game.ARENA]:
            mode = Game.TRAINING
            print('WARNING: invalid given mode. Used one is TRAINING')
        self.mode = mode
        self.token = token
        self.secret_key = secret_key

# PUBLIC METHODS ##############################################################
    def start(self):
        """Ask to start a game, and return game url, or None if error."""
        data = {
            'secret': self.secret_key,
            'mode': self.mode 
        }
        response = json.loads(ask_server(Game.URL_START + self.token, json_data=data).text)
        if not response['success']:
            print('ERROR:Game:start: something go wrong, start request returned False.')
            return None
        else:
            print('GAME ASKED:', end='')
        self.game_url = Game.URL_ROOT + response['url']
        print('game_url:', self.game_url)
        return self.game_url


    def game_have_begin(self):
        """return (True, game_state) iff game have begin, else (False, self.last_game_state)"""
        data = {'secret_token': self.secret_key}
        self.last_game_state = json.loads(ask_server(self.game_url, json_data=data).text)
        #print(self.last_game_state)
        game_started = self.last_game_state['success'] is True and self.last_game_state['status'] == 'game_started'
        if game_started:
            self.move_url = Game.URL_ROOT + self.last_game_state['url']
        return game_started


    def game_state(self):
        """"""
        data = {'secret_token': self.secret_key}
        self.last_game_state = json.loads(ask_server(self.game_url, json_data=data).text)
        return self.last_game_state

        
    def send_move(self, stop_id, track_number, datetime_str):
        """Send received move to server
        
        datetime_str need to be formatted as '13 Sep 13:20:00 2015'
        """
        data = {
            "secret_token": self.secret_key,
            "track": track_number, # 11_A, by example
            "connection": datetime_str, # forme : 13 Sep 13:20:00 2015
            "to_stop": stop_id,
            "type": "move"
        }
        #print(json.dumps(data))
        #exit(0)
        r = ask_server(self.move_url, json_data=data)
        self.last_move_state = json.loads(r.text)
        print('MOVE', self.last_move_state)
        return self.last_move_state


# PRIVATE METHODS #############################################################
# PREDICATS ###################################################################
# ACCESSORS ###################################################################
# CONVERSION ##################################################################
# OPERATORS ###################################################################




#########################
# FUNCTIONS             #
#########################





