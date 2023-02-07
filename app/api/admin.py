from django.contrib import admin
from api.models import GameUser, UserStats

# Register your models here.

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
