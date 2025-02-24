from django.db import models
from django.contrib.auth.models import User
from vylety.models import Vylet  # Import modelu Vylet


class Komentar(models.Model):
    """
    Model reprezentující komentář uživatele k výletu.

    Atributy:
        uzivatel (User): Uživatel, který napsal komentář.
        vylet (Vylet): Výlet, ke kterému komentář patří.
        text (str): Obsah komentáře.
        datum (datetime): Datum a čas vytvoření komentáře.
    """
    uzivatel = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Uživatel, který napsal komentář")
    vylet = models.ForeignKey(Vylet, on_delete=models.CASCADE, related_name="komentare",
                              help_text="Výlet, ke kterému komentář patří")
    text = models.TextField(help_text="Obsah komentáře")
    datum = models.DateTimeField(auto_now_add=True, help_text="Datum vytvoření komentáře")

    def __str__(self):
        return f'Komentář od {self.uzivatel.username} k výletu {self.vylet.name}'
