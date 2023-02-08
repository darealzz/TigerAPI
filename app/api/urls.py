from django.urls import path

from api.views import UserJoined
from api.views import ShowUserStats
from api.views import ModifyWeaponKills

urlpatterns = [
    path('user_joined/<int:user_id>', UserJoined.as_view()),
    path('user_stats/<int:user_id>', ShowUserStats.as_view()),
    path('user_stats/<int:user_id>/add_weapon_kills/<str:weapon_name>/<int:add_kills>', ModifyWeaponKills.as_view()),
]