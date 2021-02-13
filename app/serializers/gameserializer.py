from rest_framework import serializers
from app.models import Game


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ['url', 'host', 'guest', 'winner', 'date', 'round']
