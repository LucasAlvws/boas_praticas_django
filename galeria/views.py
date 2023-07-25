from django.shortcuts import render
from django.http import HttpResponse
from .models import Fotografia




def index(request):
    querry_set = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {'cards' : querry_set})


def imagem(request):
    return render(request, 'galeria/imagem.html')