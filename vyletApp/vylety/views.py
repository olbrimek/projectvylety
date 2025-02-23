from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Vylet
from django.contrib import messages

# Zobrazení výletů
def index(request):
    vylety = Vylet.objects.all()

    return render(request, "vylety/index.html", {"vylety": vylety})

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
def add_vylet(request):
    if request.method == "POST" and request.user.is_authenticated:
        data = json.loads(request.body)
        Vylet.objects.create(name=data['name'], date=data['date'], description=data['description'], user=request.user)
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error", "message": "Nejste přihlášen!"}, status=401)

# API: Smazání výletu
@csrf_exempt
def delete_vylet(request, id):
    if request.method == "DELETE" and request.user.is_authenticated:
        Vylet.objects.filter(id=id, user=request.user).delete()
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error", "message": "Nejste přihlášen!"}, status=401)
from django.shortcuts import render

# Create your views here.
