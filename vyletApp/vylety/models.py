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
        oblibene (User): Uživatelé, kteří si výlet přidali do oblíbených.
    """
    name = models.CharField(max_length=200, help_text="Zadejte název výletu")
    date = models.DateField(help_text="Datum konání výletu")
    description = models.TextField(help_text="Krátký popis výletu")
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Vlastník výletu")
    oblibene = models.ManyToManyField(User, related_name="oblibene_vylety", blank=True,
                                      help_text="Uživatelé, kteří si výlet přidali do oblíbených")

    def __str__(self):
        return self.name
