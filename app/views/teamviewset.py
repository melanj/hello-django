from rest_framework import viewsets

from app.models import Team
from app.serializers import TeamSerializer
from app.utils.auth import IsCoach


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed or edited.
    """
    queryset = Team.objects.all().order_by('-id')
    serializer_class = TeamSerializer
    permission_classes = [IsCoach]
