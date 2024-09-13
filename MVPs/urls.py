# MVPs/urls.py
from django.urls import path
from . import views
from .views import lista_projetos

urlpatterns = [
    path('', views.index, name='index'),  # Rota para a função 'index' na página inicial
    path('lista_projetos/', views.lista_projetos, name='lista_projetos'),
    path('lista_alunos/', views.index, name='lista_alunos'),  # Adicione ou verifique esta linha
]