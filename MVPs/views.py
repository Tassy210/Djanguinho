from django.shortcuts import render
from .models import Alunos, Professores, Projetos

def index(request):
    alunos = Alunos.objects.all().order_by('nome')
    return render(request, 'MVPs/lista_alunos.html', {'alunos': alunos})


def lista_projetos(request):
    projetos = Projetos.objects.all()
    return render(request, 'MVPs/lista_projetos.html', {'projetos': projetos})