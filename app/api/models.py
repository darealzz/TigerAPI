from django.db import models


class GameUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    first_joined_game = models.DateTimeField(auto_now=False, auto_now_add=True) # Track when object is created, don't overide when saved
    xp = models.IntegerField(default=0)
    events_attended = models.IntegerField(default=0)
    events_hosted = models.IntegerField(default=0)
    heals_given = models.IntegerField(default=0)
            
    class Meta:
        verbose_name = "Game User"
        

class UserStats(models.Model):
    user = models.ForeignKey(GameUser, on_delete=models.CASCADE)
    mode = models.CharField(max_length=20)
    wins = models.IntegerField(default=0)
    kills = models.IntegerField(default=0)
    topfrags = models.IntegerField(default=0)

    class Meta:
        verbose_name = "UserStat"


class UserWeaponStats(models.Model):
    user = models.ForeignKey(GameUser, on_delete=models.CASCADE)
    weapon = models.CharField(max_length=20)
    kills = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'User Weapon Stat'


class UserMedals(models.Model):
    user = models.ForeignKey(GameUser, on_delete=models.CASCADE)
    medal_name = models.CharField(max_length=50)
    tier = models.IntegerField(default=1)
    
    class Meta:
        verbose_name = 'User Medal'