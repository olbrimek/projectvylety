from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Komentar
from .serializers import KomentarSerializer





def komentare_index(request):
    return render(request, 'komentare/index.html')

