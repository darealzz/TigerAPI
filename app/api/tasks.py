from django.db import models

from datetime import timedelta
from django.db.models.functions import Now

from models import GameUser
from models import UserStats
from models import UserWeaponStats
from models import UserMedals

def award_medals():
    x = GameUser.objects.filter(Created_at__lte=Now() - timedelta(months=3))
    print(x)

award_medals()