from django.urls import path

from api.views import UserJoined
from api.views import ShowUserStats
from api.views import ModifyWeaponKills
from api.views import ModifyXP, ShowXP, asd

urlpatterns = [
    path('user_joined/<int:user_id>', UserJoined.as_view()),
    
    path('user_stats/<int:user_id>', ShowUserStats.as_view()),
    path('user_stats/<int:user_id>/add_weapon_kills/<str:weapon_name>/<int:add_kills>', ModifyWeaponKills.as_view()),
    # TODO: add stats modification for modes
    
    path('user_xp/<int:user_id>', ShowXP.as_view()),
    path('user_xp/<int:user_id>/add_xp/<int:add_xp>', ModifyXP.as_view()),
    
    path('test/', asd.as_view())
]