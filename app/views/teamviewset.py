from django.db.models import Avg
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from app.models import Team, Player, PlayerStat
from app.serializers import TeamSerializer, PlayerSerializer
from app.utils.auth import IsCoach


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed or edited.
    """
    queryset = Team.objects.all().order_by('-id')
    serializer_class = TeamSerializer
    permission_classes = [IsCoach | permissions.IsAdminUser]

    @action(detail=True, methods=['get'], name='Get players whose average score is in the 90 percentile')
    def best_players(self, request, pk=None):
        serializer_context = {
            'request': request,
        }
        team = self.get_object()
        players_in_team = Player.objects.filter(team=team).all()
        players = PlayerStat.objects.filter(player__in=players_in_team).values('player').annotate(
            avg=Avg('score')).filter(avg__gte=0.9).all()
        best_players = []
        for player in players.iterator():
            player_obj = players_in_team.filter(pk=player['player']).first()
            player_data = PlayerSerializer(player_obj, context=serializer_context).data
            player_data["average"] = player['avg']
            best_players.append(player_data)

        return Response(best_players)
