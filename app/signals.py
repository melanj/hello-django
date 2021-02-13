from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.utils import timezone

from app.models import SiteStat


def login_handler(sender, user, request, **kwargs):
    stat, created = SiteStat.objects.get_or_create(user=user)
    SiteStat.objects.filter(pk=stat.pk).update(login_time=timezone.now(),
                                               logout_time='1970-01-01 00:00:00')


def logout_handler(sender, user, request, **kwargs):
    stat, created = SiteStat.objects.get_or_create(user=user)
    SiteStat.objects.filter(pk=stat.pk).update(logout_time=timezone.now())


user_logged_in.connect(login_handler)
user_logged_out.connect(logout_handler)
