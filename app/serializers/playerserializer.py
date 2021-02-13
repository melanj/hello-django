from rest_framework import serializers
from app.models import Player


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['url', 'user', 'team', 'height']
