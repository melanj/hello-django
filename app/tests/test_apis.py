import base64
import json
from urllib.parse import urlparse

from django.contrib.auth.models import Group, User
from django.test import Client
from django.test import TestCase

from app.models import GameRound, Team, Player, PlayerStat, TeamStat, Game, SiteStat

client = Client()
auth_headers = {
    'HTTP_AUTHORIZATION': 'Basic ' + base64.b64encode('admin:adminadmin'.encode()).decode(),
}


class TestAllApis(TestCase):
    """ Test module for GET test all API """

    @classmethod
    def setUpTestData(cls):
        admin = Group(name='Admin')
        admin.save()
        coach = Group(name='Coach')
        coach.save()
        player = Group(name='Player')
        player.save()
        admin_user = User.objects.create_user(username='admin', email='norely@localhost.org', is_staff=True,
                                              password='adminadmin')
        admin.user_set.add(admin_user)

        cls.colombo_fc_user1 = User.objects.create_user(username='colombo_fc_user1', email='norely@localhost.org',
                                                        password='adminadmin')
        player.user_set.add(cls.colombo_fc_user1)
        cls.colombo_fc_user2 = User.objects.create_user(username='colombo_fc_user2', email='norely@localhost.org',
                                                        password='adminadmin')
        player.user_set.add(cls.colombo_fc_user2)
        cls.navy_sc_user1 = User.objects.create_user(username='navy_sc_user1', email='norely@localhost.org',
                                                     password='adminadmin')
        player.user_set.add(cls.navy_sc_user1)
        cls.navy_sc_user2 = User.objects.create_user(username='navy_sc_user2', email='norely@localhost.org',
                                                     password='adminadmin')
        player.user_set.add(cls.navy_sc_user2)

        cls.first_round = GameRound(name='First Round')
        cls.first_round.save()
        quarter_final = GameRound(name='Quarter Final')
        quarter_final.save()
        semi_final = GameRound(name='Semi Final')
        semi_final.save()
        final = GameRound(name='Final')
        final.save()
        cls.colombo_fc = Team(name='Colombo FC')
        cls.colombo_fc.save()
        cls.navy_sc = Team(name='Navy SC')
        cls.navy_sc.save()

        cls.game = Game(host=cls.navy_sc, guest=cls.colombo_fc, winner=cls.navy_sc, round=cls.first_round
                        , date='2020-12-23')
        cls.game.save()

        cls.navy_sc_player = Player(user=cls.navy_sc_user1, team=cls.navy_sc, height=179)
        cls.navy_sc_player.save()
        cls.player_stat = PlayerStat(player=cls.navy_sc_player, game=cls.game, score=1)
        cls.player_stat.save()
        cls.team_stat = TeamStat(team=cls.navy_sc, game=cls.game, score=1)
        cls.team_stat.save()

        cls.site_stat = SiteStat(user=cls.navy_sc_user1, login_time='2021-02-15T04:25:37+05:30',
                                 logout_time='2021-02-15T16:59:16+05:30')
        cls.site_stat.save()

    def test_list_all_user(self):
        # get users response
        resp = client.get('/users/', **auth_headers)
        self.assertIsNotNone(resp.content)
        self.assertEqual(resp.status_code, 200)

    def test_list_all_user_unauthorized(self):
        # get users response
        resp = client.get('/users/')
        self.assertIsNotNone(resp.content)
        self.assertEqual(resp.status_code, 401)

    def test_create_update_read_delete_user(self):
        # create a user
        create_user_payload = {
            "username": "foobar",
            "first_name": "Foo",
            "last_name": "Bar",
            "email": "foobar@gmail.com",
            "groups": [
                "http://testserver/groups/2/"
            ]
        }
        resp = client.post('/users/', json.dumps(create_user_payload),
                           content_type='application/json', **auth_headers)
        self.assertEqual(resp.status_code, 201)

        self.assertTrue(resp.has_header('Location'))
        location = resp.get('Location')
        path = urlparse(location).path

        update_user_payload = {
            "url": location,
            "username": "foobar",
            "first_name": "Foo",
            "last_name": "Bar",
            "email": "rename@gmail.com",
            "groups": [
                "http://testserver/groups/2/"
            ]
        }
        resp = client.put(path, json.dumps(update_user_payload),
                          content_type='application/json', **auth_headers)
        self.assertEqual(resp.status_code, 200)

        resp = client.get(path, **auth_headers)
        self.assertIsNotNone(resp.content)
        self.assertEqual(resp.status_code, 200)

        patch_user_payload = {
            "email": "foobar@foobar.com",
        }
        resp = client.patch(path, json.dumps(patch_user_payload),
                            content_type='application/json', **auth_headers)
        self.assertEqual(resp.status_code, 200)

        resp = client.delete(path, **auth_headers)
        self.assertEqual(resp.status_code, 204)

    def test_list_all_groups(self):
        resp = client.get('/groups/', **auth_headers)
        self.assertIsNotNone(resp.content)
        self.assertEqual(resp.status_code, 200)

    def test_list_all_rounds(self):
        resp = client.get('/rounds/', **auth_headers)
        self.assertIsNotNone(resp.content)
        self.assertEqual(resp.status_code, 200)

    def test_list_all_teams(self):
        resp = client.get('/teams/', **auth_headers)
        self.assertIsNotNone(resp.content)
        self.assertEqual(resp.status_code, 200)

    def test_create_update_read_delete_team(self):
        create_team_payload = {
            "name": "Oakland Raiders"
        }
        resp = client.post('/teams/', json.dumps(create_team_payload),
                           content_type='application/json', **auth_headers)
        self.assertEqual(resp.status_code, 201)

        self.assertTrue(resp.has_header('Location'))
        location = resp.get('Location')
        path = urlparse(location).path

        update_team_payload = {
            "url": location,
            "name": "Oakland Raiders 2"
        }
        resp = client.put(path, json.dumps(update_team_payload),
                          content_type='application/json', **auth_headers)
        self.assertEqual(resp.status_code, 200)

        resp = client.get(path, **auth_headers)
        self.assertIsNotNone(resp.content)
        self.assertEqual(resp.status_code, 200)

        patch_team_payload = {
            "name": "Oakland Raiders"
        }
        resp = client.patch(path, json.dumps(patch_team_payload),
                            content_type='application/json', **auth_headers)
        self.assertEqual(resp.status_code, 200)

        resp = client.delete(path, **auth_headers)
        self.assertEqual(resp.status_code, 204)

    def test_team_get_best_players(self):
        path = "/teams/" + str(self.navy_sc.id) + "/best_players/"
        expected_result = [{
            "url": "http://testserver/players/" + str(self.navy_sc_player.id) + "/",
            "user": "http://testserver/users/" + str(self.navy_sc_user1.id) + "/",
            "team": "http://testserver/teams/" + str(self.navy_sc.id) + "/",
            "height": 179,
            "average": 1.0
        }]
        resp = client.get(path, **auth_headers)
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.content)
        self.assertJSONEqual(str(resp.content, encoding='utf8'), expected_result)

    def test_create_update_read_delete_game(self):
        create_game_payload = {
            "host": "http://testserver/teams/1/",
            "guest": "http://testserver/teams/2/",
            "winner": "http://testserver/teams/2/",
            "date": "2020-12-23",
            "round": "http://testserver/rounds/4/"
        }
        resp = client.post('/games/', json.dumps(create_game_payload),
                           content_type='application/json', **auth_headers)
        self.assertEqual(resp.status_code, 201)
        self.assertTrue(resp.has_header('Location'))
        location = resp.get('Location')
        path = urlparse(location).path

        update_game_payload = {
            "url": location,
            "host": "http://testserver/teams/1/",
            "guest": "http://testserver/teams/2/",
            "winner": "http://testserver/teams/2/",
            "date": "2020-12-26",
            "round": "http://testserver/rounds/4/"
        }
        resp = client.put(path, json.dumps(update_game_payload),
                          content_type='application/json', **auth_headers)
        self.assertEqual(resp.status_code, 200)

        resp = client.get(path, **auth_headers)
        self.assertIsNotNone(resp.content)
        self.assertEqual(resp.status_code, 200)

        patch_game_payload = {
            "date": "2020-12-26",
        }
        resp = client.patch(path, json.dumps(patch_game_payload),
                            content_type='application/json', **auth_headers)
        self.assertEqual(resp.status_code, 200)

        resp = client.delete(path, **auth_headers)
        self.assertEqual(resp.status_code, 204)

    def test_create_update_read_delete_player(self):
        create_player_payload = {
            "user": "http://testserver/users/2/",
            "team": "http://testserver/teams/1/",
            "height": 0
        }
        resp = client.post('/players/', json.dumps(create_player_payload),
                           content_type='application/json', **auth_headers)
        self.assertIsNotNone(resp.content)
        self.assertEqual(resp.status_code, 201)
        self.assertTrue(resp.has_header('Location'))
        location = resp.get('Location')
        path = urlparse(location).path

        update_player_payload = {
            "url": location,
            "user": "http://testserver/users/2/",
            "team": "http://testserver/teams/1/",
            "height": 187
        }
        resp = client.put(path, json.dumps(update_player_payload),
                          content_type='application/json', **auth_headers)
        self.assertEqual(resp.status_code, 200)

        resp = client.get(path, **auth_headers)
        self.assertIsNotNone(resp.content)
        self.assertEqual(resp.status_code, 200)

        patch_player_payload = {
            "height": 188
        }
        resp = client.patch(path, json.dumps(patch_player_payload),
                            content_type='application/json', **auth_headers)
        self.assertEqual(resp.status_code, 200)

        resp = client.delete(path, **auth_headers)
        self.assertEqual(resp.status_code, 204)

    def test_create_update_read_delete_coach(self):
        create_coach_payload = {
            "user": "http://testserver/users/3/",
            "team": "http://testserver/teams/1/"
        }
        resp = client.post('/coaches/', json.dumps(create_coach_payload),
                           content_type='application/json', **auth_headers)
        self.assertEqual(resp.status_code, 201)
        self.assertTrue(resp.has_header('Location'))
        location = resp.get('Location')
        path = urlparse(location).path

        update_coach_payload = {
            "url": location,
            "user": "http://testserver/users/3/",
            "team": "http://testserver/teams/2/"
        }
        resp = client.put(path, json.dumps(update_coach_payload),
                          content_type='application/json', **auth_headers)
        self.assertEqual(resp.status_code, 200)

        resp = client.get(path, **auth_headers)
        self.assertIsNotNone(resp.content)
        self.assertEqual(resp.status_code, 200)

        patch_coach_payload = {
            "team": "http://testserver/teams/1/"
        }
        resp = client.patch(path, json.dumps(patch_coach_payload),
                            content_type='application/json', **auth_headers)
        self.assertEqual(resp.status_code, 200)

        resp = client.delete(path, **auth_headers)
        self.assertEqual(resp.status_code, 204)

    def test_create_update_read_delete_player_stat(self):
        players_url = "http://testserver/players/" + str(self.navy_sc_player.id) + "/"
        games_url = "http://testserver/games/" + str(self.game.id) + "/"

        create_player_stat_payload = {
            "player": players_url,
            "game": games_url,
            "score": 1
        }
        resp = client.post('/player-stats/', json.dumps(create_player_stat_payload),
                           content_type='application/json', **auth_headers)
        self.assertEqual(resp.status_code, 201)
        self.assertTrue(resp.has_header('Location'))
        location = resp.get('Location')
        path = urlparse(location).path

        update_player_stat_payload = {
            "url": location,
            "player": players_url,
            "game": games_url,
            "score": 2
        }
        resp = client.put(path, json.dumps(update_player_stat_payload),
                          content_type='application/json', **auth_headers)
        self.assertEqual(resp.status_code, 200)

        resp = client.get(path, **auth_headers)
        self.assertIsNotNone(resp.content)
        self.assertEqual(resp.status_code, 200)

        patch_player_stat_payload = {
            "score": 1
        }
        resp = client.patch(path, json.dumps(patch_player_stat_payload),
                            content_type='application/json', **auth_headers)
        self.assertEqual(resp.status_code, 200)

        resp = client.delete(path, **auth_headers)
        self.assertEqual(resp.status_code, 204)

    def test_create_update_read_delete_team_stat(self):
        team_url = "http://testserver/teams/" + str(self.navy_sc.id) + "/"
        game_url = "http://testserver/games/" + str(self.game.id) + "/"
        create_team_stat_payload = {
            "team": team_url,
            "game": game_url,
            "score": 7
        }
        resp = client.post('/team-stats/', json.dumps(create_team_stat_payload),
                           content_type='application/json', **auth_headers)
        self.assertEqual(resp.status_code, 201)
        self.assertTrue(resp.has_header('Location'))
        location = resp.get('Location')
        path = urlparse(location).path

        update_team_stat_payload = {
            "url": location,
            "team": team_url,
            "game": game_url,
            "score": 10
        }
        resp = client.put(path, json.dumps(update_team_stat_payload),
                          content_type='application/json', **auth_headers)
        self.assertEqual(resp.status_code, 200)

        resp = client.get(path, **auth_headers)
        self.assertIsNotNone(resp.content)
        self.assertEqual(resp.status_code, 200)

        patch_team_stat_payload = {
            "score": 12
        }
        resp = client.patch(path, json.dumps(patch_team_stat_payload),
                            content_type='application/json', **auth_headers)
        self.assertEqual(resp.status_code, 200)

        resp = client.delete(path, **auth_headers)
        self.assertEqual(resp.status_code, 204)

    def test_list_all_stats(self):
        resp = client.get('/stats/', **auth_headers)
        self.assertIsNotNone(resp.content)
        self.assertEqual(resp.status_code, 200)

    def test_list_stats_by_id(self):
        path = '/stats/' + str(self.site_stat.id) + '/'
        expected_result = {
            "url": "http://testserver/stats/" + str(self.site_stat.id) + "/",
            "user": "http://testserver/users/" + str(self.site_stat.user_id) + "/",
            "login_time": "2021-02-15T04:25:37+05:30",
            "logout_time": "2021-02-15T16:59:16+05:30"
        }
        resp = client.get(path, **auth_headers)
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.content)
        self.assertJSONEqual(str(resp.content, encoding='utf8'), expected_result)
