from django.db import models
from django.urls import reverse
from .team import Team
from .gameround import GameRound


class Game(models.Model):
    host = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='host')
    guest = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='guest')
    winner = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='winner')
    date = models.DateField(verbose_name='game date')
    round = models.ForeignKey(GameRound, on_delete=models.CASCADE, related_name='round')

    def __str__(self):
        return 'Game : %s' % self.id

    def get_absolute_url(self):
        return reverse('game', args=[str(self.id)])
