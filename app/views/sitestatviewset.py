from rest_framework import permissions, viewsets

from app.models import SiteStat
from app.serializers import SiteStatSerializer


class SiteStatViewSet(viewsets.ReadOnlyModelViewSet):
    """
        API endpoint that allows site stats to be viewed.
        """
    queryset = SiteStat.objects.all().order_by('-id')
    serializer_class = SiteStatSerializer
    permission_classes = [permissions.IsAdminUser]
