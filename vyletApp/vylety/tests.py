from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Vylet

class VyletModelTest(TestCase):
    def test_vytvoreni_vyletu(self):
        vylet = Vylet.objects.create(
            name="Testovací výlet",
            date="2024-06-01",
            description="Toto je testovací popis.",
            user=User.objects.create(username="testuser")
        )
        self.assertEqual(vylet.name, "Testovací výlet")
        self.assertEqual(str(vylet), "Testovací výlet")

class VyletViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.vylet = Vylet.objects.create(
            name="Testovací výlet",
            date="2024-06-01",
            description="Toto je testovací popis.",
            user=self.user
        )

    def test_index_page(self):
        """Test, zda hlavní stránka odpovídá 200 OK"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_blog_page(self):
        """Test, zda stránka Blog odpovídá 200 OK"""
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    def test_prihlaseni(self):
        """Test přihlášení uživatele"""
        response = self.client.post("/login/", {"username": "testuser", "password": "testpass"})
        self.assertEqual(response.status_code, 200)

    def test_pridani_vyletu(self):
        """Test, zda přihlášený uživatel může přidat výlet"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.post("/add_vylet/", {
            "name": "Nový výlet",
            "date": "2024-06-10",
            "description": "Nový testovací výlet"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Vylet.objects.count(), 2)
from django.test import TestCase

# Create your tests here.
