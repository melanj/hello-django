from rest_framework import viewsets

from app.models import GameRound
from app.serializers import GameRoundSerializer
from app.utils.auth import IsCoach


class GameRoundViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Game rounds to be viewed.
    """
    queryset = GameRound.objects.all().order_by('-id')
    serializer_class = GameRoundSerializer
    permission_classes = [IsCoach]
