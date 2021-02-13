from rest_framework import serializers
from app.models import SiteStat


class SiteStatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SiteStat
        fields = ['url', 'user', 'login_time', 'logout_time']
