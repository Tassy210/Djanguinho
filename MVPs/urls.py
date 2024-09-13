# MVPs/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Rota para a função 'index' na página inicial
]
