from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth, messages
from django.http import HttpResponse
from .models import Fotografia
from .forms import FotografiaForms




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
    return render(request, 'galeria/index.html', {'cards' : querry_set})

def nova_img(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para conseguir acessar ao Item")
        return redirect('login')
    
    form = FotografiaForms()

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.instance.usuario = request.user
            form.save()
            messages.success(request, "Foto adicionada a galeria com sucesso.")
            return redirect('index')
    return render(request, 'galeria/nova_img.html',{ "form" : form})



def editar_img(request, id):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para conseguir acessar ao Item")
        return redirect('login')
    foto = Fotografia.objects.get(pk=id)
    form = FotografiaForms(instance=foto)

    if request.method == "POST":
        form = FotografiaForms(request.POST, request.FILES, instance=foto)
        if form.is_valid():
            form.instance.usuario = request.user
            form.save()
            messages.success(request, "Foto Editada sucesso.")
            return redirect('imagem', foto.pk)

    return render(request, 'galeria/editar_img.html',{ "form" : form, "fotografia": foto})


def deletar_img(request, id):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para conseguir acessar ao Item")
        return redirect('login')
    foto = Fotografia.objects.get(pk=id)
    foto.delete()
    messages.success(request, "Foto Deletada sucesso.")
    return redirect('index')

def filtro(request, tag):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para conseguir acessar ao Item")
        return redirect('login')
    fotos = Fotografia.objects.filter(categoria=tag)
    return render(request, 'galeria/index.html', {'cards' : fotos})
