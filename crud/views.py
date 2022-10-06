from multiprocessing import context
from django.shortcuts import render
from .models import persona 

def inicio(request):
    return render(request, 'inicio.html')

def lista_personas(request):
    p=persona.objects.all()
    context ={'p':p}
    return render(request, 'persona.html', context)