from rest_framework import serializers
from app.models import PlayerStat


class PlayerStatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayerStat
        fields = ['url', 'player', 'game', 'score']
