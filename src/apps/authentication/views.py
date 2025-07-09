"""
Views do app de autenticação.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.http import JsonResponse
import json


@csrf_protect
@never_cache
def login_view(request):
    """
    View de login com interface futurista.
    """
    if request.user.is_authenticated:
        return redirect('dashboard:home')
    
    if request.method == 'POST':
        if request.content_type == 'application/json':
            # Handle AJAX request
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
        else:
            # Handle form request
            username = request.POST.get('username')
            password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if request.content_type == 'application/json':
                return JsonResponse({
                    'success': True,
                    'message': 'Login realizado com sucesso!',
                    'redirect_url': '/dashboard/'
                })
            return redirect('dashboard:home')
        else:
            error_message = 'Credenciais inválidas. Tente novamente.'
            if request.content_type == 'application/json':
                return JsonResponse({
                    'success': False,
                    'message': error_message
                })
            messages.error(request, error_message)
    
    return render(request, 'authentication/login.html')


@login_required
def logout_view(request):
    """
    View de logout.
    """
    logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('authentication:login')


@csrf_protect
def register_view(request):
    """
    View de registro de usuário.
    """
    if request.user.is_authenticated:
        return redirect('dashboard:home')
    
    if request.method == 'POST':
        # Implementar lógica de registro aqui
        pass
    
    return render(request, 'authentication/register.html')


@csrf_protect
def forgot_password_view(request):
    """
    View de recuperação de senha.
    """
    if request.user.is_authenticated:
        return redirect('dashboard:home')
    
    if request.method == 'POST':
        # Implementar lógica de recuperação de senha aqui
        pass
    
    return render(request, 'authentication/forgot_password.html')
