from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Komentar

class KomentareModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")

    def test_vytvoreni_komentare(self):
        komentar = Komentar.objects.create(uzivatel=self.user, text="Toto je testovací komentář.")
        self.assertEqual(komentar.text, "Toto je testovací komentář")
        self.assertEqual(str(komentar), f'Komentář od {self.user.username}')

class KomentareViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_komentare_page(self):
        response = self.client.get("/komentare/")
        self.assertEqual(response.status_code, 200)
from django.test import TestCase

# Create your tests here.
