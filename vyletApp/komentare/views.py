from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Komentar






def komentare_index(request):
    return render(request, 'komentare/index.html')

