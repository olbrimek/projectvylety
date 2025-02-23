from django.urls import path
from . import views

urlpatterns = [
    path('', views.komentare_index, name='komentare_index'),
]
