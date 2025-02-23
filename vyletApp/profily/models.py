from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    uzivatel = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f'Profil {self.uzivatel.username}'
from django.db import models

# Create your models here.
