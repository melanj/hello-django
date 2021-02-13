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

run runserver command to run the development server
```bash
python3 manage.py runserver
```

## how to run unit and integration tests

```bash
 python3 manage.py test
```
