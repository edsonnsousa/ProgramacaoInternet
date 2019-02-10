from django.http import HttpResponse
from django.shortcuts import render
from pools.models import Questoes
# Create your views here.
def index(request):
    return render(request, 'index.html')
def exibir(request,questoes_id):
    questoes = Questoes()
    if questoes_id=='1':
        questoes=Questoes('Qual seu nome?','17/05/2009')
    if questoes_id=='7':
        questoes=Questoes('Sua idade','17/03/2004')

    return render(request, 'questoes.html', {"questoes" : questoes})