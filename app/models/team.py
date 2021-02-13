from django.db import models
from django.urls import reverse


class Team(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('team', args=[str(self.id)])


