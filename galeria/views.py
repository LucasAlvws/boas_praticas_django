from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth, messages
from django.http import HttpResponse
from .models import Fotografia




def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para conseguir acessar ao Home")
        return redirect('login')
    querry_set = Fotografia.objects.order_by("-data_foto").filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards' : querry_set})


def imagem(request, id):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para conseguir acessar ao Item")
        return redirect('login')
    foto = get_object_or_404(Fotografia, pk=id, publicada=True)
    return render(request, 'galeria/imagem.html', {'fotografia':foto})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para conseguir acessar ao Home")
        return redirect('login')
    querry_set = Fotografia.objects.order_by("-data_foto").filter(publicada=True)

    if "buscar" in request.GET:
        nome_buscar = request.GET['buscar']
        if nome_buscar:
            querry_set = querry_set.filter(nome__icontains = nome_buscar)
    return render(request, 'galeria/buscar.html', {'cards' : querry_set})