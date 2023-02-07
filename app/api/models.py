from django.db import models


class GameUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    first_joined_game = models.DateTimeField(auto_now=False, auto_now_add=True) # Track when object is created, don't overide when saved

    class Meta:
        verbose_name = "Game User"
        

class UserStats(models.Model):
    user = models.ForeignKey(GameUser, on_delete=models.CASCADE)
    mode = models.CharField(max_length=20)
    wins = models.IntegerField(default=0)
    kills = models.IntegerField(default=0)
    topfrags = models.IntegerField(default=0)

    class Meta:
        verbose_name = "User Stat"