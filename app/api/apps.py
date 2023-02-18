from django.apps import AppConfig
from django.core.cache import cache

from roblox import client
from constants import CLIENT_COOKIE


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        import api.signals

        cache.set('Client', client.Client(CLIENT_COOKIE))
