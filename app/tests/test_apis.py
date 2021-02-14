import base64
import json

from django.contrib.auth.models import Group, User
from django.test import Client
from django.test import TestCase

from app.models import GameRound

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

        first_round = GameRound(name='First Round')
        first_round.save()
        quarter_final = GameRound(name='Quarter Final')
        quarter_final.save()
        semi_final = GameRound(name='Semi Final')
        semi_final.save()
        final = GameRound(name='Final')
        final.save()

    def test_list_all_user(self):
        # get users response
        resp = client.get('/users/', **auth_headers)
        # self.assertTrue(resp. > 0)
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
        # self.assertEqual(User.objects.count(), 3)
        self.assertEqual(resp.status_code, 200)
