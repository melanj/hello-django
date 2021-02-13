from rest_framework import viewsets

from app.models import Game
from app.serializers import GameSerializer
from app.utils.auth import IsCoach


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Games to be viewed or edited.
    """
    queryset = Game.objects.all().order_by('-id')
    serializer_class = GameSerializer
    permission_classes = [IsCoach]
