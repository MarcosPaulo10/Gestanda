from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cadastro.views import cadastros_home

def signin_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "As senhas não coincidem.")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Usuário já existe.")
            return redirect("signup")

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("cadastros_home")

    return render(request, "signin.html")


def login_view(request):
    if request.user.is_authenticated:
        return redirect(cadastros_home)

    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect(cadastros_home)
        else:
            return HttpResponse('Usuário ou Senha inválidos!')


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")