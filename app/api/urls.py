from django.urls import path
from api.views import UserJoined, ShowUserStats

urlpatterns = [
    path('user_joined/<int:user_id>', UserJoined.as_view()),
    path('user_stats/<int:user_id>', ShowUserStats.as_view()),
    # path('user_stats/<int:user_id>/<int:kills>', UserJoined.as_view()),
]