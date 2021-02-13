from django.db import models
from django.urls import reverse
from .game import Game
from .player import Player


class PlayerStat(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return str(self.score)

    def get_absolute_url(self):
        return reverse('player_stat', args=[str(self.id)])
