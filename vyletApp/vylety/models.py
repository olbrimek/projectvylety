from django.db import models
from django.contrib.auth.models import User

class Vylet(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Každý výlet patří uživateli

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
