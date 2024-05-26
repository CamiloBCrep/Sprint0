from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def home(request):
    title = "inicio"
    data={
        "title":title
    }
    return render(request, 'core/home.html', data)

def login(request):
    title = "Inicio de sesión"

    data = {
        "title":title,
    }
    return render(request, 'registration/login.html',data)

def recovery(request):
    title = "Recuperación de contraseña"
    data = {
        "title":title,
    }
    return render(request, 'core/recovery.html', data)

def exit(request):
    logout(request)
    return redirect('home')