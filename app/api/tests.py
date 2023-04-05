
# SIMULATES BOT MAKING REQUESTS TO THE SERVER

from django.test import TestCase
import requests
import pprint

def get_xp():
    response = requests.get('http://127.0.0.1:8000/v1/user_xp/573280920')
    pprint.pprint(response.json())
    
def joined():
    response = requests.post('http://127.0.0.1:8000/v1/user_joined/21311')
    pprint.pprint(response.json())
    
def update_xp():
    response = requests.patch('http://127.0.0.1:8000/v1/user_xp/573280920/add_xp/25')
    pprint.pprint(response.json())

def asd():
    response = requests.get('http://127.0.0.1:8000/v1/test/')

asd()