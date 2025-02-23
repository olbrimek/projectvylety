from django.urls import path
from . import views

urlpatterns = [
    path('', views.profil_index, name='profil_index'),
]
