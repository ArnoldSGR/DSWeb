from django.shortcuts import render, get_object_or_404 as geto
from .models import Simulado, Questao, Resposta
# Create your views here.

def index(request):
    lista_simulados = Simulado.objects.all()
    context = {
        'lista_simulados' : lista_simulados
    }
    return render(request,'simulados/home.html', context)

def questao(request, simulado_id):
    lista_questoes = Questao.objects.filter(simulado  = simulado_id)
    context = {
        'questoes' : lista_questoes
    }
    return render(request, 'simulados/questao.html', context)

def resposta(request, questao_id):
    lista_respostas = Resposta.objects.filter(questao = questao_id)
    context = {
        'respostas' : lista_respostas
    }
    return render(request,'simulados/resposta.html', context)