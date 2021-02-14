from rest_framework import serializers
from app.models import Team


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ['url', 'name']
        read_only_fields = ['name']
