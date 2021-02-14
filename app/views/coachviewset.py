from rest_framework import viewsets, permissions

from app.models import Coach
from app.serializers import CoachSerializer
from app.utils.auth import IsCoach


class CoachViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows coaches to be viewed or edited.
    """
    queryset = Coach.objects.all().order_by('-id')
    serializer_class = CoachSerializer
    permission_classes = [IsCoach | permissions.IsAdminUser]
