from django.test import TestCase
import requests
import pprint

def get_stats():
    response = requests.get('http://127.0.0.1:8000/v1/user_stats/123')
    # response = requests.patch('http://127.0.0.1:8000/v1/user_stats/123/add_weapon_kills/AR-11/2')
    pprint.pprint(response.json())

get_stats()