from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, 'home.html')

def sobre(request):

    return render(request, 'sobre.html')


def equipe(request):

    return render(request, 'equipe.html')


def parcerias(request):

    return render(request, 'parcerias.html')


def sindicatos(request):

    return render(request, 'sindicatos.html')