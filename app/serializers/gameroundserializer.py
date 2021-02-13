from rest_framework import serializers
from app.models import GameRound


class GameRoundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GameRound
        fields = ['url', 'name']
