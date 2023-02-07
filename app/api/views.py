from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import GameUser

class UserJoined(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def post(self, request, **kwargs):
        user = GameUser.objects.filter(user_id=kwargs['user_id'])
        
        if not user:
            user = GameUser.objects.create(user_id=kwargs['user_id'])
            user.save()

        return Response(user)   