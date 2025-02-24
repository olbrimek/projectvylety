from rest_framework import serializers
from .models import Vylet
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    """Serializer pro uživatele."""
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class VyletSerializer(serializers.ModelSerializer):
    """Serializer pro výlety."""
    user = UserSerializer(read_only=True)  # Zobrazíme info o uživateli

    class Meta:
        model = Vylet
        fields = ['id', 'name', 'date', 'description', 'user']
