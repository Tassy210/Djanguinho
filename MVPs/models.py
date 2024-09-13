from django.db import models
from django.utils import timezone

class Alunos(models.Model): 
    nome = models.CharField(max_length=200)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome
    
class Professores(models.Model): 
    nome_professor = models.CharField(max_length=200)
    curso = models.CharField(max_length=200) 
    contato = models.IntegerField()  # Corrigido para IntegerField sem max_length

    def __str__(self):
        return self.nome_professor

     
class Projetos(models.Model): 
    nome_projeto = models.CharField(max_length=300)
    date_added = models.DateTimeField(default=timezone.now)
    professor_responsavel = models.ForeignKey(Professores, null=True, blank=True, on_delete=models.SET_NULL, related_name='projetos')

    def __str__(self):
        return self.nome_projeto

     

