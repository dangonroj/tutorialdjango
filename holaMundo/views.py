from django.shortcuts import render
from django.http import HttpResponse
from datetime import date


# Create your views here.
def index(request):
    # básico
    return render(request, 'inicio.html')

def holaMundo(request):
    # básico
    return HttpResponse("Hola mundo")


def holaMundo2(request):

    return render(request, 'holaMundo2.html')


def calendario(request):
    #enviando datos
    hoy = date.today()
    return render(request, 'calendario.html', {'fecha': hoy})

def calculadora(request,a,b):
    numA = int(a)
    numB = int(b)
    suma = numA + numB
    resta = numA - numB

    return render(request, 'calculadora.html',{'numA':numA, 'numB':numB, 'suma': suma, 'resta':resta})
