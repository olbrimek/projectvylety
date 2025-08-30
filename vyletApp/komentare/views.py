from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Komentar








from django.shortcuts import redirect, get_object_or_404
from .models import Komentar
from vylety.models import Vylet

def komentare_index(request):
    komentare = Komentar.objects.all()
    return render(request, 'komentare/index.html', {'komentare': komentare})

def pridat_komentar(request, vylet_id):
    if request.method == "POST" and request.user.is_authenticated:
        vylet = get_object_or_404(Vylet, id=vylet_id)
        text = request.POST.get("text")
        Komentar.objects.create(vylet=vylet, uzivatel=request.user, text=text)
    return redirect('/')
