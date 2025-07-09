"""
Views do app de jogos.
"""

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Game, GameScore


@login_required
def game_list_view(request):
    """
    Lista todos os jogos disponíveis.
    """
    games = Game.objects.filter(is_active=True)
    context = {
        'games': games,
        'page_title': 'Centro de Jogos',
    }
    return render(request, 'games/list.html', context)


@login_required
def game_detail_view(request, slug):
    """
    Exibe detalhes de um jogo específico.
    """
    game = get_object_or_404(Game, slug=slug, is_active=True)
    user_scores = GameScore.objects.filter(
        user=request.user,
        game=game
    ).order_by('-score')[:5]
    
    context = {
        'game': game,
        'user_scores': user_scores,
        'page_title': f'Jogo: {game.name}',
    }
    return render(request, 'games/detail.html', context)


@login_required
def space_invaders_view(request):
    """
    View do jogo Space Invaders.
    """
    game = get_object_or_404(Game, slug='space-invaders')
    context = {
        'game': game,
        'page_title': 'Space Invaders',
    }
    return render(request, 'games/space_invaders.html', context)


@login_required
def cyber_puzzle_view(request):
    """
    View do jogo Cyber Puzzle.
    """
    game = get_object_or_404(Game, slug='cyber-puzzle')
    context = {
        'game': game,
        'page_title': 'Cyber Puzzle',
    }
    return render(request, 'games/cyber_puzzle.html', context)


@login_required
def neon_runner_view(request):
    """
    View do jogo Neon Runner.
    """
    game = get_object_or_404(Game, slug='neon-runner')
    context = {
        'game': game,
        'page_title': 'Neon Runner',
    }
    return render(request, 'games/neon_runner.html', context)
