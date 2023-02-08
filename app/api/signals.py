from django.db.models.signals import post_save
from django.dispatch import receiver

from api.models import GameUser
from api.models import UserStats
from api.models import UserWeaponStats

from constants import POSSIBLE_MODES, POSSIBLE_WEAPONS

@receiver(post_save, sender=GameUser)
def my_callback(sender, instance, created, **kwargs):
    if created:
        for mode in POSSIBLE_MODES:
            UserStats.objects.create(
                user=instance,
                mode=mode
            )
        
        for weapon in POSSIBLE_WEAPONS:
            UserWeaponStats.objects.create(
                user=instance,
                weapon=weapon,
            )

