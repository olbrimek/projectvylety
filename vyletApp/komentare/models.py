from django.db import models
from django.contrib.auth.models import User

class Komentar(models.Model):
    uzivatel = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    datum = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Komentář od {self.uzivatel.username}'
from django.db import models

# Create your models here.
