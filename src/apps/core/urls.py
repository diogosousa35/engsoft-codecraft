"""
URLs do app core.
"""

from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('health/', views.api_health_check, name='health_check'),
]
