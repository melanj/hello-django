from rest_framework import viewsets, permissions

from app.models import TeamStat
from app.serializers import TeamStatSerializer
from app.utils.auth import IsCoach


class TeamStatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Team stats to be viewed or edited.
    """
    queryset = TeamStat.objects.all().order_by('-id')
    serializer_class = TeamStatSerializer
    permission_classes = [IsCoach | permissions.IsAdminUser]
