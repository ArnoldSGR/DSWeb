from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

class Simulado(models.Model):
    titulo = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.titulo}'

class Questao(models.Model):
    title = models.CharField(max_length=200, default='')
    comando = models.CharField(max_length=500)
    pontuacao = models.CharField(max_length=5)
    simulado = models.ForeignKey(Simulado, on_delete = CASCADE)

    def __str__(self):
        return f'{self.comando}'

    class Meta:
        verbose_name_plural = "Questões"


class Resposta(models.Model):
    descricao = models.CharField(max_length=200)
    eh_correta = models.BooleanField(default=False)
    questao = models.ForeignKey(Questao, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.descricao}'

