from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import GameUser

class UserJoined(APIView):

    def post(self, request, **kwargs):
        
        user = GameUser.objects.get_or_create(user_id=kwargs['user_id'])[0]
            
        return Response({
            'user_id': user.user_id,
            'first_joined_game': user.first_joined_game
            })