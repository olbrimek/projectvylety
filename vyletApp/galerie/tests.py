from django.test import TestCase, Client
from .models import Obrázek

class GalerieModelTest(TestCase):
    def test_vytvoreni_obrazku(self):
        obrazek = Obrázek.objects.create(nazev="Testovací obrázek")
        self.assertEqual(obrazek.nazev, "Testovací obrázek")
        self.assertEqual(str(obrazek), "Testovací obrázek")

class GalerieViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_galerie_page(self):
        response = self.client.get("/galerie/")
        self.assertEqual(response.status_code, 200)
from django.test import TestCase

# Create your tests here.
