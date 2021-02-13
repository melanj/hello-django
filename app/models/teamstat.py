from django.db import models
from django.urls import reverse
from .game import Game
from .team import Team


class TeamStat(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game')
    score = models.IntegerField()

    def __str__(self):
        return str(self.score)

    def get_absolute_url(self):
        return reverse('team_stat', args=[str(self.id)])


