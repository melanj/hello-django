from rest_framework import viewsets, permissions

from app.models import Player
from app.serializers import PlayerSerializer
from app.utils.auth import IsCoach, IsPlayer


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows players to be viewed or edited.
    """
    queryset = Player.objects.all().order_by('-id')
    serializer_class = PlayerSerializer
    permission_classes = [IsCoach | IsPlayer | permissions.IsAdminUser]
