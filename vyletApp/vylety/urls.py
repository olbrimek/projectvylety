from django.urls import path, include

from . import views




urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add_vylet/', views.add_vylet, name='add_vylet'),
    path('delete_vylet/<int:id>/', views.delete_vylet, name='delete_vylet'),
    path('komentare/', include('komentare.urls')),
]
