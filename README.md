Hello django
=========================
:construction: This is my first Django project. This is a backend implementation of a basketball management system. I am using sqlite as database backend and HTTP Basic Auth as authentication method   

:traffic_light: All commands listed here are Linux commands. If you're working on a windows, macOS or etc, please use relevant alternative commands

## Prerequisites

- [x] python3
- [x] pip3
- [x] virtualenv (optional)

## how to run this application

clone this repository 

```bash
git clone git@github.com:melanj/hello-django.git
```

:sunrise: if you wish to you virtualenv, create a new virtual environment and active the environment

```bash
virtualenv -p python3 venv
source venv/bin/activate
```

install the project dependencies listed in requirements.txt
```bash
pip3 install -r requirements.txt
```

run init command to create admin account and other requited groups (user types), etc. admin username is 'admin' and password is 'adminadmin'
```bash
python3 manage.py init
```

:sunrise: if you wish use following command to populate dummy data set, all users account generated with this having password 'demodemo123' 
```bash
python3 manage.py dummy_data_setup
```

run runserver command to run the development server
```bash
python3 manage.py runserver
```

## how to run unit and integration tests

```bash
 python3 manage.py test
```

## API Details

list available APIs

```bash
 curl http://0.0.0.0:8000/ 2>/dev/null | jq
 ```

result:

```json
{
  "users": "http://0.0.0.0:8000/users/",
  "groups": "http://0.0.0.0:8000/groups/",
  "teams": "http://0.0.0.0:8000/teams/",
  "players": "http://0.0.0.0:8000/players/",
  "stats": "http://0.0.0.0:8000/stats/",
  "coaches": "http://0.0.0.0:8000/coaches/",
  "rounds": "http://0.0.0.0:8000/rounds/",
  "games": "http://0.0.0.0:8000/games/",
  "player-stats": "http://0.0.0.0:8000/player-stats/",
  "team-stats": "http://0.0.0.0:8000/team-stats/"
}
 ```

**API details**

| Prefix       | Description  | Create             | Read               | Update             | Delete             |
|--------------|--------------|--------------------|--------------------|--------------------|--------------------|
| users        | Manage users        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| groups       | View types of users in the system       | :x:                | :heavy_check_mark: | :x:                | :x:                |
| teams        | Manage teams        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| players      | Manage players      | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| stats        | View the statistics of the site’s usage        | :x:                | :heavy_check_mark: | :x:                | :x:                |
| coaches      | Manage coaches      | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| rounds       | View rounds       | :x:                | :heavy_check_mark: | :x:                | :x:                |
| games        | Manage games        | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| player-stats | Manage player statistics | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| team-stats   | Manage team statistics   | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |


teams API has an additional feature to view list of players having average score more than 90% across the team
/teams/<team_id>/best_players/

eg.

```bash
curl -u jasmine77:demodemo123 http://127.0.0.1:8000/teams/9/best_players/ 2>/dev/null | jq
 ```

result:
```json
[
  {
    "url": "http://127.0.0.1:8000/players/81/",
    "user": "http://127.0.0.1:8000/users/90/",
    "team": "http://127.0.0.1:8000/teams/9/",
    "height": 180,
    "average": 1
  },
  {
    "url": "http://127.0.0.1:8000/players/82/",
    "user": "http://127.0.0.1:8000/users/91/",
    "team": "http://127.0.0.1:8000/teams/9/",
    "height": 190,
    "average": 2
  },
  {
    "url": "http://127.0.0.1:8000/players/83/",
    "user": "http://127.0.0.1:8000/users/92/",
    "team": "http://127.0.0.1:8000/teams/9/",
    "height": 188,
    "average": 1.5
  },
  {
    "url": "http://127.0.0.1:8000/players/85/",
    "user": "http://127.0.0.1:8000/users/94/",
    "team": "http://127.0.0.1:8000/teams/9/",
    "height": 186,
    "average": 1.25
  }
]
 ```