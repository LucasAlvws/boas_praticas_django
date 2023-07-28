from django.shortcuts import render, redirect
from .forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.urls import reverse
from urllib.parse import urlencode

# Create your views here.


def login(request):
    form = LoginForms()

    if request.method == "POST":
        form = LoginForms(request.POST)
        if form.is_valid():
            nome = form['name_login'].value()
            senha = form['senha'].value()
            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, "Usuário logado com sucesso")
                return redirect('index')
            else:
                messages.error(request, "Usuário ou senha incorreto")
                return redirect('login')
    return render(request, 'usuarios/login.html', {"form":form})




def cadastro(request):
    form = CadastroForms()

    if request.method == "POST":
        form = CadastroForms(request.POST)
        if form.is_valid():
            nome = form["name_cadastro"].value()
            email = form['email_cadastro'].value()
            senha = form['senha_1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request,"Usuário já existe")
                return redirect('login')
            print(nome)
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request,"Usuário cadastrado, efetue o login.")
            return redirect('login')
    return render(request, 'usuarios/cadastro.html', {"form":form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect('login')