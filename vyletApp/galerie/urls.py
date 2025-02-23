from django.urls import path
from . import views

urlpatterns = [
    path('', views.galerie_index, name='galerie_index'),
]
