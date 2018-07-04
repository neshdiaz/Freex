from django.shortcuts import render

app_name = 'core'


def index(request):
    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about.html')


def catalogo(request):
    return render(request, 'core/catalogo.html')


def soporte(request):
    return render(request, 'core/soporte.html')


def login(request):
    return render(request, 'core/login.html')
