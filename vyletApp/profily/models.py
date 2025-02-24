from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):
    """
    Model reprezentující uživatelský profil.

    Atributy:
        uzivatel (User): Uživatel, ke kterému profil patří.
        bio (str, optional): Krátký popis uživatele.
        avatar (ImageField, optional): Profilový obrázek uživatele.
    """
    uzivatel = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profil",
                                    help_text="Uživatel, ke kterému tento profil patří")
    bio = models.TextField(blank=True, help_text="Krátký popis uživatele")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, help_text="Profilový obrázek uživatele")

    def __str__(self):
        return f'Profil {self.uzivatel.username}'
