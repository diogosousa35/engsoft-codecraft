"""
Modelos do app de autenticação.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Modelo de usuário customizado para o NEXUS.
    """
    avatar = models.ImageField(
        upload_to='avatars/',
        null=True,
        blank=True,
        verbose_name='Avatar'
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
        verbose_name='Biografia'
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Data de Nascimento'
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Telefone'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em'
    )
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.username
    
    @property
    def full_name(self):
        """Retorna o nome completo do usuário."""
        return f"{self.first_name} {self.last_name}".strip() or self.username
