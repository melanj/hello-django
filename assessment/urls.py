"""
URL Configuration
"""
from django.urls import include, path
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'players', views.PlayerViewSet)
router.register(r'stats', views.SiteStatViewSet)
router.register(r'coaches', views.CoachViewSet)
router.register(r'rounds', views.GameRoundViewSet)
router.register(r'games', views.GameViewSet)
router.register(r'player-stats', views.PlayerStatViewSet)
router.register(r'team-stats', views.TeamStatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
