from django.contrib.auth.models import Group, User
from django.core.management.base import BaseCommand

from app.models import GameRound


class Command(BaseCommand):
    help = 'Install groups'

    def handle(self, *args, **options):
        admin = Group(name='Admin')
        admin.save()
        self.stdout.write(self.style.SUCCESS('Admin group created'))
        coach = Group(name='Coach')
        coach.save()
        self.stdout.write(self.style.SUCCESS('Coach group created'))
        player = Group(name='Player')
        player.save()
        self.stdout.write(self.style.SUCCESS('Player group created'))
        User.objects.create_user(username='admin', email='norely@localhost.org', is_staff=True, password='adminadmin')
        self.stdout.write(self.style.SUCCESS('Admin user created'))
        quarter_final = GameRound(name='Quarter Final')
        quarter_final.save()
        self.stdout.write(self.style.SUCCESS('Quarter final round created'))
        semi_final = GameRound(name='Semi Final')
        semi_final.save()
        self.stdout.write(self.style.SUCCESS('Semi final round created'))
        final = GameRound(name='Final')
        final.save()
        self.stdout.write(self.style.SUCCESS('Final round created'))
