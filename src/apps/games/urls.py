"""
URLs do app de jogos.
"""

from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.game_list_view, name='list'),
    path('<slug:slug>/', views.game_detail_view, name='detail'),
    path('space-invaders/', views.space_invaders_view, name='space_invaders'),
    path('cyber-puzzle/', views.cyber_puzzle_view, name='cyber_puzzle'),
    path('neon-runner/', views.neon_runner_view, name='neon_runner'),
]
