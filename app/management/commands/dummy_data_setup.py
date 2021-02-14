from dateutil import tz
from django.contrib.auth.models import Group, User
from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from app.models import GameRound, Team, Player, Coach, Game, PlayerStat, TeamStat, SiteStat


def play(self, fake, current_round, teams):
    for r in range(0, len(teams), 2):
        if r + 1 < len(teams):
            host = teams[r]
            guest = teams[r + 1]
            self.stdout.write(
                self.style.SUCCESS('%s : Creating game between %s and %s' % (current_round, host, guest)))
            # temporally set host as winner
            game = Game(host=host, guest=guest, round=current_round, winner=host,
                        date=fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None))
            game.save()

            host_score = players_scoring(self, fake, host, game)
            host_team_stat = TeamStat(game=game, team=host, score=host_score)
            host_team_stat.save()

            guest_score = players_scoring(self, fake, guest, game)
            guest_team_stat = TeamStat(game=game, team=guest, score=guest_score)
            guest_team_stat.save()

            # not handled the tie scenario
            if guest_score > host_score:
                game.winner = guest
            else:
                game.winner = host
            game.save()
            self.stdout.write(self.style.SUCCESS('%s scored %s' % (game.host.name, host_score)))
            self.stdout.write(self.style.SUCCESS('%s scored %s' % (game.guest.name, guest_score)))
            self.stdout.write(self.style.SUCCESS('%s won the game' % game.winner))
            self.stdout.write('\n')


def players_scoring(self, fake, team, game):
    team_score = 0
    players = Player.objects.filter(team=team).all()
    for j in range(len(players)):
        score = fake.random_int(min=0, max=2, step=1)
        team_score = team_score + score
        stat = PlayerStat(game=game, player=players[j], score=score)
        stat.save()
        if score > 0:
            self.stdout.write(self.style.SUCCESS('%s scored %s' % (stat.player.user.first_name, score)))
    return team_score


def get_unique_username(fake):
    name = fake.user_name()
    username = User.objects.filter(username=name).first()
    if username is not None:
        name = get_unique_username(fake)
    return name


class Command(BaseCommand):
    help = 'populate dummy data'

    def handle(self, *args, **options):
        fake = Faker()
        admin_group = Group.objects.filter(name='Admin').first()
        if admin_group is None:
            raise CommandError('Please run "python3 manage.py init" first!')
        coach_group = Group.objects.filter(name='Coach').first()
        player_group = Group.objects.filter(name='Player').first()

        first_round = GameRound.objects.filter(name='First Round').first()
        quarter_final = GameRound.objects.filter(name='Quarter Final').first()
        semi_final = GameRound.objects.filter(name='Semi Final').first()
        final = GameRound.objects.filter(name='Final').first()

        # create teams and members
        for r in range(16):
            team = Team(name=fake.slug())
            team.save()
            self.stdout.write(self.style.SUCCESS('Successfully created Team : %s' % team.name))
            self.stdout.write(self.style.SUCCESS('Adding members.....'))
            for i in range(10):
                username_player = get_unique_username(fake)
                password = 'demodemo123'
                player_user = User.objects.create_user(username=username_player, email=fake.safe_email(),
                                                       password=password, first_name=fake.first_name(),
                                                       last_name=fake.last_name())
                player_group.user_set.add(player_user)
                player = Player(user=player_user, team=team, height=fake.random_int(min=172, max=190, step=1))
                player.save()
                self.stdout.write(self.style.SUCCESS(
                    '%s %s joined' % (player_user.first_name, player_user.last_name)))
            username_coach = get_unique_username(fake)
            password = 'demodemo123'
            coach_user = User.objects.create_user(username=username_coach, email=fake.safe_email(), password=password,
                                                  first_name=fake.first_name(), last_name=fake.last_name())
            coach_group.user_set.add(coach_user)
            coach = Coach(user=coach_user, team=team)
            coach.save()
            self.stdout.write(self.style.SUCCESS(
                '%s %s joined as the coach' % (coach_user.first_name, coach_user.last_name)))
            self.stdout.write('\n')

        # create 1st round games
        first_round_teams = Team.objects.all()
        play(self, fake, first_round, first_round_teams)

        # create quarter final games
        first_round_winner_ids = Game.objects.filter(round=first_round).values_list('winner_id', flat=True).all()
        quarter_final_teams = Team.objects.filter(pk__in=set(first_round_winner_ids))
        play(self, fake, quarter_final, quarter_final_teams)

        # create semi final games
        quarter_final_winner_ids = Game.objects.filter(round=quarter_final).values_list('winner_id', flat=True).all()
        semi_final_teams = Team.objects.filter(pk__in=set(quarter_final_winner_ids))
        play(self, fake, semi_final, semi_final_teams)

        # create semi final games
        semi_final_winner_ids = Game.objects.filter(round=semi_final).values_list('winner_id', flat=True).all()
        final_teams = Team.objects.filter(pk__in=set(semi_final_winner_ids))
        play(self, fake, final, final_teams)

        # create site stats
        users = User.objects.all()
        for user in users:
            for i in range(fake.random_int(min=5, max=8, step=1)):
                stat = SiteStat(user=user,
                                login_time=fake.date_time_this_month(before_now=True, after_now=False,
                                                                     tzinfo=tz.gettz('Asia/Colombo')),
                                logout_time=fake.date_time_this_month(before_now=False, after_now=True,
                                                                      tzinfo=tz.gettz('Asia/Colombo')))
                stat.save()
            self.stdout.write(self.style.SUCCESS('Stat created for user  %s %s' % (user.first_name, user.last_name)))
        self.stdout.write(self.style.SUCCESS('*** Done ***'))
