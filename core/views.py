from django.shortcuts import render
from .models import Prestador

app_name = 'core'


def index(request):
    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about.html')


def catalogo(request):
    prestadores = Prestador.objects.all()[:5]
    return render(request, 'core/catalogo.html', {'prestadores': prestadores})


def soporte(request):
    return render(request, 'core/soporte.html')


def login(request):
    return render(request, 'core/login.html')
