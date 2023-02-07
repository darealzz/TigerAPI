from django.urls import path
from api.views import UserJoined

urlpatterns = [
    path('user_joined/<int:user_id>', UserJoined.as_view())
]