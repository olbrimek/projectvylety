from django.test import TestCase, Client
from .models import Clanek

class BlogModelTest(TestCase):
    def test_vytvoreni_clanku(self):
        clanek = Clanek.objects.create(titulek="Testovací článek", obsah="Toto je obsah článku.")
        self.assertEqual(clanek.titulek, "Testovací článek")
        self.assertEqual(str(clanek), "Testovací článek")

class BlogViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_blog_page(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)
