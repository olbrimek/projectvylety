from django.urls import path

from . import views



urlpatterns = [
    path('', views.komentare_index, name='komentare_index'),
    path('pridat_komentar/<int:vylet_id>/', views.pridat_komentar, name='pridat_komentar'),
]
