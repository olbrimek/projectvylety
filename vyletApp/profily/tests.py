from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Profil

class ProfilyModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")

    def test_vytvoreni_profilu(self):
        profil = Profil.objects.create(uzivatel=self.user, bio="Toto je bio uživatele.")
        self.assertEqual(profil.bio, "Toto je bio uživatele.")
        self.assertEqual(str(profil), f'Profil {self.user.username}')

class ProfilyViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_profily_page(self):
        response = self.client.get("/profily/")
        self.assertEqual(response.status_code, 200)
from django.test import TestCase

# Create your tests here.
