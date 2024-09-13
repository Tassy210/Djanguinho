from django.shortcuts import render
from .models import Alunos

def index(request):
    alunos = Alunos.objects.all().order_by('nome')
    return render(request, 'MVPs/lista_alunos.html', {'alunos': alunos})