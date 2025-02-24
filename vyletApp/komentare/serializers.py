from rest_framework import serializers
from .models import Komentar

class KomentarSerializer(serializers.ModelSerializer):
    """Serializer pro komentáře."""
    class Meta:
        model = Komentar
        fields = ['id', 'uzivatel', 'vylet', 'text', 'datum']
