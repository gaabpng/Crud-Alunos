from django.db import models

class Alunos(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    matricula = models.CharField(max_length=9)
    nota_p1 = models.FloatField()
    nota_p2 = models.FloatField()
    nota_trabalho = models.FloatField()
    media = models.FloatField()
    
    def __str__(self):
        return self.title