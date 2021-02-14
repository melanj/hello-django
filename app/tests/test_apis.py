import base64
import json

from django.contrib.auth.models import Group, User
from django.test import Client
from django.test import TestCase

from app.models import GameRound, Team

client = Client()
auth_headers = {
    'HTTP_AUTHORIZATION': 'Basic ' + base64.b64encode('admin:adminadmin'.encode()).decode(),
}


class TestAllApis(TestCase):
    """ Test module for GET test all API """

    def setUp(self):
        admin = Group(name='Admin')
        admin.save()
        coach = Group(name='Coach')
        coach.save()
        player = Group(name='Player')
        player.save()
        admin_user = User.objects.create_user(username='admin', email='norely@localhost.org', is_staff=True,
                                              password='adminadmin')
        admin.user_set.add(admin_user)

        self.colombo_fc_user1 = User.objects.create_user(username='colombo_fc_user1', email='norely@localhost.org',
                                                         password='adminadmin')
        player.user_set.add(self.colombo_fc_user1)
        self.colombo_fc_user2 = User.objects.create_user(username='colombo_fc_user2', email='norely@localhost.org',
                                                         password='adminadmin')
        player.user_set.add(self.colombo_fc_user2)
        self.navy_sc_user1 = User.objects.create_user(username='navy_sc_user1', email='norely@localhost.org',
                                                      password='adminadmin')
        admin.user_set.add(self.navy_sc_user1)
        self.navy_sc_user2 = User.objects.create_user(username='navy_sc_user2', email='norely@localhost.org',
                                                      password='adminadmin')
        admin.user_set.add(self.navy_sc_user2)

        first_round = GameRound(name='First Round')
        first_round.save()
        quarter_final = GameRound(name='Quarter Final')
        quarter_final.save()
        semi_final = GameRound(name='Semi Final')
        semi_final.save()
        final = GameRound(name='Final')
        final.save()
        colombo_fc = Team(name='Colombo FC')
        colombo_fc.save()
        navy_sc = Team(name='Navy SC')
        navy_sc.save()

    def test_list_all_user(self):
        # get users response
        resp = client.get('/users/', **auth_headers)
        self.assertEqual(resp.status_code, 200)

    def test_create_user(self):
        # create a user
        create_user_payload = {
            "username": "melan",
            "first_name": "Melan",
            "last_name": "Jayasinghage",
            "email": "melannj86@gmail.com",
            "groups": [
                "http://127.0.0.1:8000/groups/2/"
            ]
        }
        resp = client.post('/users/', json.dumps(create_user_payload),
                           content_type='application/json', **auth_headers)
        self.assertEqual(resp.status_code, 201)

    def test_list_all_groups(self):
        # get API response
        resp = client.get('/groups/', **auth_headers)
        self.assertEqual(resp.status_code, 200)

    def test_list_all_teams(self):
        resp = client.get('/teams/', **auth_headers)
        self.assertEqual(resp.status_code, 200)

    def test_create_team(self):
        create_team_payload = {
            "name": "Oakland Raiders"
        }
        resp = client.post('/teams/', json.dumps(create_team_payload),
                           content_type='application/json', **auth_headers)
        self.assertEqual(resp.status_code, 201)

    def test_create_game(self):
        create_game_payload = {
            "host": "http://127.0.0.1:8000/teams/1/",
            "guest": "http://127.0.0.1:8000/teams/2/",
            "winner": "http://127.0.0.1:8000/teams/2/",
            "date": "2020-12-23",
            "round": "http://127.0.0.1:8000/rounds/4/"
        }
        resp = client.post('/games/', json.dumps(create_game_payload),
                           content_type='application/json', **auth_headers)
        self.assertEqual(resp.status_code, 201)

    def test_create_player(self):
        create_player_payload = {
            "user": "http://127.0.0.1:8000/users/2/",
            "team": "http://127.0.0.1:8000/teams/1/",
            "height": 187
        }
        resp = client.post('/players/', json.dumps(create_player_payload),
                           content_type='application/json', **auth_headers)
        self.assertEqual(resp.status_code, 201)

    def test_create_coach(self):
        create_coach_payload = {
            "user": "http://127.0.0.1:8000/users/3/",
            "team": "http://127.0.0.1:8000/teams/1/",
            "height": 187
        }
        resp = client.post('/coaches/', json.dumps(create_coach_payload),
                           content_type='application/json', **auth_headers)
        self.assertEqual(resp.status_code, 201)
