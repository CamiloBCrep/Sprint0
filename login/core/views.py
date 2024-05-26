from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
#from django.core.mail import send_mail
#from django.conf import settings


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


def exit(request):
    logout(request)
    return redirect('home')