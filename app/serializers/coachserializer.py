from rest_framework import serializers
from app.models import Coach


class CoachSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coach
        fields = ['url', 'user', 'team']
