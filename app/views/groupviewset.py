from django.contrib.auth.models import Group
from rest_framework import permissions, viewsets

from app.serializers import GroupSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed.
    """
    queryset = Group.objects.all().order_by('-id')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]
