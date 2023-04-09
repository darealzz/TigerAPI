from rest_framework.response import Response
from rest_framework.views import APIView

from django.utils import timezone

from api.models import GameUser
from api.models import UserStats
from api.models import UserWeaponStats
from api.models import UserMedals

from dateutil.relativedelta import relativedelta

from constants import RANK_XP_BINDS


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
            return Response({'detail': 'Provided "User ID" does not exist.'}, status=404)
        
        return_object = {}
        user_stats = UserStats.objects.filter(user=user)
        weapon_stats = UserWeaponStats.objects.filter(user=user)

        for stat in user_stats:
            return_object[str(stat.mode)] = {
                'wins': stat.wins,
                'total_kills': stat.kills,
                'topfrags': stat.topfrags
                }

        return_object['weapon_kills'] = {}

        for weapon_stat in weapon_stats:
            return_object['weapon_kills'][str(weapon_stat.weapon)] = weapon_stat.kills

        return Response(return_object)

class ModifyWeaponKills(APIView):

    def patch(self, request, **kwargs):

        try:
            user = GameUser.objects.get(user_id=kwargs['user_id'])
            weapon_stats = UserWeaponStats.objects.filter(user=user, weapon=kwargs['weapon_name'].upper())[0]
        except GameUser.DoesNotExist:
            return Response({'detail': 'Provided "User ID" does not exist.'}, status=404)
        except IndexError:
            return Response({'detail': 'Provided "Weapon Name" does not exist.'}, status=404)

        weapon_stats.kills = weapon_stats.kills + kwargs['add_kills']
        weapon_stats.save()

        return Response({
            'user_id': user.user_id,
            'weapon_name': weapon_stats.weapon,
            'kills': weapon_stats.kills
        })

class ModifyXP(APIView):

    def patch(self, request, **kwargs):

        try:
            user = GameUser.objects.get(user_id=kwargs['user_id'])
        except GameUser.DoesNotExist:
            return Response({'detail': 'Provided "User ID" does not exist.'}, status=404)

        user.xp = user.xp + kwargs['add_xp']
        user.save()

        return Response({
            'user_id': user.user_id,
            'total_xp': user.xp,
        })

class ShowXP(APIView):
    
    def get(self, request, **kwargs):

        try:
            user = GameUser.objects.get(user_id=kwargs['user_id'])
        except GameUser.DoesNotExist:
            return Response({'detail': 'Provided "User ID" does not exist.'}, status=404)

        return Response({
            'user_id': user.user_id,
            'total_xp': user.xp,
            'bounds': RANK_XP_BINDS
        })


class asd(APIView):
    
    def get(self, request, **kwargs):

        now = timezone.now()

        three_months_ago = now - relativedelta(months=3)
        six_months_ago = now - relativedelta(months=6)
        one_year_ago = now - relativedelta(years=1)
        two_years_ago = now - relativedelta(years=2)

        medals_three_months = UserMedals.objects.filter(medal_name='Soldier of Radia', tier__lt=2, user__first_joined_game__gte=three_months_ago)
        medals_six_months = UserMedals.objects.filter(medal_name='Soldier of Radia', tier__lt=3, user__first_joined_game__gte=six_months_ago, user__first_joined_game__lt=three_months_ago)
        medals_one_year = UserMedals.objects.filter(medal_name='Soldier of Radia', tier__lt=4, user__first_joined_game__gte=one_year_ago, user__first_joined_game__lt=six_months_ago)
        medals_two_years = UserMedals.objects.filter(medal_name='Soldier of Radia', tier__lt=5, user__first_joined_game__lt=two_years_ago)

        # print(medals_three_months[0].user.first_joined_game)
        print(medals_three_months, medals_six_months, medals_one_year, medals_two_years)
        
        return Response({
            'user_id': '123'
        })
