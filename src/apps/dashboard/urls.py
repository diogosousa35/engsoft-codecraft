"""
URLs do app do dashboard.
"""

from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
