from django.contrib import admin

from api.models import GameUser
from api.models import UserStats
from api.models import UserWeaponStats

class CustomModelAdmin(admin.ModelAdmin):
    """
    Custom subclass to display all fields of a model
    """

    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(CustomModelAdmin, self).__init__(model, admin_site)

class GameUserAdmin(CustomModelAdmin):
    pass

admin.site.register(GameUser, GameUserAdmin)
admin.site.register(UserStats)
admin.site.register(UserWeaponStats)
