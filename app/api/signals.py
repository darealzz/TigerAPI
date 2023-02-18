from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.cache import cache

from api.models import GameUser
from api.models import UserStats
from api.models import UserWeaponStats

from constants import POSSIBLE_MODES, POSSIBLE_WEAPONS, RANK_XP_BINDS, GROUP_ID


@receiver(post_save, sender=GameUser)
def callback(sender, instance, created, **kwargs):
    if created:
        for mode in POSSIBLE_MODES:
            UserStats.objects.create(
                user=instance,
                mode=mode
            )
        
        for weapon in POSSIBLE_WEAPONS:
            UserWeaponStats.objects.create(
                user=instance,
                weapon=weapon
            )
    
    else:
        last_key = 0
        for key, value in RANK_XP_BINDS.items():
            if value > instance.xp:
                break
            last_key = key
        
        Client = cache.get('Client')
        Client.change_rank(GROUP_ID, instance.user_id, last_key)
