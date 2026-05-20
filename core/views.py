from django.shortcuts import render, redirect, get_object_or_404
from core.forms import LoginForm, CadastroLink
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

def login(request):
    if request.user.id is not None:
        return redirect("home")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            auth_login(request, form.user)
            return redirect("home")
        context = {'acesso_negado': True}
        return render(request, 'login.html', {'form':form})
    return render(request, 'login.html', {'form':LoginForm()})




        
def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return render(request, 'logout.html')
    return redirect("home")



def cadastrar_link(request):
    if request.method == "POST":
        print('O cadastrar link foi chamado')
        form = CadastroLink(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CadastroLink()
    return render(request, 'forms.html', {'form': form, 'titulo_pagina': 'Cadastrar link'})


@login_required
def home(request):
    context = {}
    return render(request, 'index.html', context)


