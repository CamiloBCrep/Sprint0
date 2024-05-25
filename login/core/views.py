from django.shortcuts import render

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
    return render(request, 'core/login.html',data)
def recovery(request):
    title = "Recuperación de contraseña"
    data = {
        "title":title,
    }
    return render(request, 'core/recovery.html', data)
# Create your views here.