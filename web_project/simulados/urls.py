from django.urls import path
from simulados import views
app_name = "simulados"
urlpatterns = [
    #mostra os simulados
    path('', views.index, name = "home"),
    #mostra as questoes
    path('simulado/<int:simulado_id>', views.questao, name = "questao"),
    #mostra as respostas
    path('resposta/<int:questao_id>', views.resposta, name = "resposta")
]