"""
Views do app do dashboard.
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@login_required
def home_view(request):
    """
    View principal do dashboard futurista.
    """
    context = {
        'user': request.user,
        'page_title': 'NEXUS Dashboard',
    }
    return render(request, 'dashboard/home.html', context)


@login_required
def profile_view(request):
    """
    View do perfil do usuário.
    """
    context = {
        'user': request.user,
        'page_title': 'Perfil do Usuário',
    }
    return render(request, 'dashboard/profile.html', context)


@login_required
@csrf_exempt
def api_stats(request):
    """
    API para estatísticas do dashboard.
    """
    if request.method == 'GET':
        stats = {
            'users_online': 1247,
            'system_uptime': '99.8%',
            'data_processed': '2.4TB',
            'active_sessions': 156,
            'security_level': 'HIGH',
            'server_status': 'ONLINE',
        }
        return JsonResponse(stats)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)
