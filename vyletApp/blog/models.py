from django.db import models

class Clanek(models.Model):
    titulek = models.CharField(max_length=200)
    obsah = models.TextField()
    datum = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulek
from django.db import models

# Create your models here.
