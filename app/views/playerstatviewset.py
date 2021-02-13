from rest_framework import viewsets

from app.models import PlayerStat
from app.serializers import PlayerStatSerializer
from app.utils.auth import IsCoach


class PlayerStatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Player stats to be viewed or edited.
    """
    queryset = PlayerStat.objects.all().order_by('-id')
    serializer_class = PlayerStatSerializer
    permission_classes = [IsCoach]
