from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from .team import Team


class Player(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    height = models.IntegerField()

    def __str__(self):
        return 'Name : %s ' % self.user.first_name

    def get_absolute_url(self):
        return reverse('player', args=[str(self.id)])


