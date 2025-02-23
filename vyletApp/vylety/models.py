from django.db import models
from django.contrib.auth.models import User

class Vylet(models.Model):
    """
       Model reprezentující výlet vytvořený uživatelem.

       Atributy:
           name (str): Název výletu.
           date (date): Datum konání výletu.
           description (str): Stručný popis výletu.
           user (User): Uživatel, který výlet vytvořil.
       """

    name = models.CharField(max_length=200, help_text="Zadejte název výletu")
    date = models.DateField(help_text="Datum konání výletu")
    description = models.TextField(help_text="Krátký popis výletu")
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Vlastník výletu")  # Každý výlet patří uživateli

    def __str__(self):
        """Vrací název výletu jako reprezentaci objektu."""
        return self.name
from django.db import models

# Create your models here.
