from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Vylet
from django.contrib import messages
from rest_framework import generics, permissions
from .serializers import VyletSerializer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from komentare.models import Komentar

def is_admin(user):
    return user.is_staff or user.is_superuser

# Zobrazení výletů
def index(request):
    vylety = Vylet.objects.all()
    users = User.objects.all()
    return render(request, "vylety/index.html", {"vylety": vylety, "users": users})

# Registrace uživatele
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'vylety/register.html', {'form': form})

# Přihlášení uživatele
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Špatné uživatelské jméno nebo heslo!")
    return render(request, 'vylety/login.html')

# Odhlášení uživatele
def user_logout(request):
    logout(request)
    return redirect('/')

# API: Přidání výletu (pouze pro přihlášené uživatele)
@csrf_exempt
@login_required
def add_vylet(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Vylet.objects.create(
            name=data['name'],
            date=data['date'],
            description=data['description'],
            user=request.user
        )
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error", "message": "Neplatná metoda!"}, status=400)

# API: Smazání výletu (uživatel může smazat svůj, admin může smazat jakýkoliv)
@csrf_exempt
@login_required
def delete_vylet(request, id):
    if request.method == "DELETE":
        vylet = get_object_or_404(Vylet, id=id)
        if request.user == vylet.user or is_admin(request.user):
            vylet.delete()
            return JsonResponse({"status": "success"})
        else:
            return JsonResponse({"status": "error", "message": "Nemáte oprávnění!"}, status=403)
    return JsonResponse({"status": "error", "message": "Neplatná metoda!"}, status=400)

# Admin: Editace uživatele (pouze admin)
@user_passes_test(is_admin)
def edit_user(request, id):
    user = get_object_or_404(User, id=id)
    # Zde přidejte logiku pro editaci uživatele (např. formulář)
    return render(request, 'vylety/edit_user.html', {'user': user})

# Výpis uživatelů (pouze admin)
@user_passes_test(is_admin)
def seznam_uzivatelu(request):
    users = User.objects.all()
    return render(request, 'vylety/seznam_uzivatelu.html', {'users': users})

def index(request):
    vylety = Vylet.objects.all()
    users = User.objects.all()
    komentare = Komentar.objects.all()
    return render(request, "vylety/index.html", {
        "vylety": vylety,
        "users": users,
        "komentare": komentare
    })