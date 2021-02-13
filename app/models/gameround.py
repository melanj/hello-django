from django.db import models
from django.urls import reverse


class GameRound(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('game', args=[str(self.id)])
