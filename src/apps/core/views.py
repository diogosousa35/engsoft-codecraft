"""
Views do app core.
"""

from django.shortcuts import render
from django.http import JsonResponse


def handler404(request, exception):
    """
    Handler customizado para erro 404.
    """
    return render(request, 'errors/404.html', status=404)


def handler500(request):
    """
    Handler customizado para erro 500.
    """
    return render(request, 'errors/500.html', status=500)


def api_health_check(request):
    """
    Endpoint de health check da API.
    """
    return JsonResponse({
        'status': 'healthy',
        'version': '1.0.0',
        'timestamp': '2024-01-01T00:00:00Z'
    })
