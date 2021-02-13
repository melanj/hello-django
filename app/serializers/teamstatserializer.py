from rest_framework import serializers
from app.models import TeamStat


class TeamStatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamStat
        fields = ['url', 'team', 'game', 'score']
