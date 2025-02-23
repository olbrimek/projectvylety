from django.db import models

class Obrázek(models.Model):
    nazev = models.CharField(max_length=100)
    obrazek = models.ImageField(upload_to='galerie/')
    popis = models.TextField(blank=True)
    datum = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nazev
from django.db import models

# Create your models here.
