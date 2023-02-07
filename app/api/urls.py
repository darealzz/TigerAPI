from django.urls import path
from api.views import get_users

urlpatterns = [
    path('', get_users)
]