import json
from django.db import models

# Create your models here.

class GameUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    first_joined_game = models.DateTimeField(auto_now=False, auto_now_add=True) # Track when object is created, don't overide when saved
    user_stats = models.JSONField(default={
        'tdm': {
            'wins': 0,
            'kills': 0,
            'Topfrags': 0
        },
        'juggernaut': {
            'wins': 0,
            'kills': 0,
            'Topfrags': 0
        },
        'hardpoint': {
            'wins': 0,
            'kills': 0,
            'Topfrags': 0
        },
        'Domination': {
            'wins': 0,
            'kills': 0,
            'Topfrags': 0
        },
        'ctf': {
            'wins': 0,
            'kills': 0,
            'Topfrags': 0
        },
        'ffa': {
            'wins': 0,
            'kills': 0,
            'Topfrags': 0
        },
        'koth': {
            'wins': 0,
            'kills': 0,
            'Topfrags': 0
        },
    })
    