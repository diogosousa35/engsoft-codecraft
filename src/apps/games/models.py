"""
Modelos do app de jogos.
"""

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Game(models.Model):
    """
    Modelo para representar um jogo.
    """
    DIFFICULTY_CHOICES = [
        ('easy', 'Fácil'),
        ('medium', 'Médio'),
        ('hard', 'Difícil'),
    ]
    
    name = models.CharField(max_length=100, verbose_name='Nome')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    description = models.TextField(verbose_name='Descrição')
    icon = models.CharField(max_length=50, verbose_name='Ícone')
    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES,
        default='medium',
        verbose_name='Dificuldade'
    )
    max_players = models.PositiveIntegerField(default=1, verbose_name='Máximo de Jogadores')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    
    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class GameScore(models.Model):
    """
    Modelo para pontuações dos jogos.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Jogo')
    score = models.PositiveIntegerField(verbose_name='Pontuação')
    level_reached = models.PositiveIntegerField(default=1, verbose_name='Nível Alcançado')
    time_played = models.DurationField(verbose_name='Tempo Jogado')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    
    class Meta:
        verbose_name = 'Pontuação'
        verbose_name_plural = 'Pontuações'
        ordering = ['-score', '-created_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.game.name}: {self.score}"
