from django.db.models.signals import post_save
from django.dispatch import receiver

from api.models import GameUser
from api.models import UserStats

from constants import POSSIBLE_MODES

@receiver(post_save, sender=GameUser)
def my_callback(sender, instance, created, **kwargs):
    if created:
        for mode in POSSIBLE_MODES:
            UserStats.objects.create(
                user=instance,
                mode=mode
            )
