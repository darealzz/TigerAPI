from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import GameUser
from api.models import UserStats

class UserJoined(APIView):

    def post(self, request, **kwargs):
        
        user = GameUser.objects.get_or_create(user_id=kwargs['user_id'])[0]
            
        return Response({
            'user_id': user.user_id,
            'first_joined_game': user.first_joined_game
            })
        
class ShowUserStats(APIView):

    def get(self, request, **kwargs):
        
        try:
            user = GameUser.objects.get(user_id=kwargs['user_id'])
        except GameUser.DoesNotExist:
            return Response({'detail': 'user id does not exist'}, status=404)
        
        return_object = {}
        user_stats = UserStats.objects.filter(user=user)
        
        for stat in user_stats:
            return_object[str(stat.mode)] = {
                'wins': stat.wins,
                'kills': stat.kills,
                'topfrags': stat.topfrags
                }
            
        return Response(return_object)