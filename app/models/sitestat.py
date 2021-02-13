from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone


class SiteStat(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    login_time = models.DateTimeField(default=timezone.now)
    logout_time = models.DateTimeField(default='1970-01-01 00:00:00')

    def __str__(self):
        return str(self.user.name)

    def get_absolute_url(self):
        return reverse('user_stat_detail', args=[str(self.id)])
