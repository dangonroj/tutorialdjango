from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from datetime import date

# Create your views here.

def index(request):
    imagenes = Imagen.objects.all()
    numero_imagenes = imagenes.count()
    
    return render(request, 'index.html',{'numero_imagenes': numero_imagenes})

def subir_imagen(request):
    if request.method == 'GET':
        return render(request, 'subir_imagen.html')
    elif request.method == 'POST':
        form = ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = Imagen(  imagen = form.cleaned_data["imagen"],
                                nombre = form.cleaned_data["nombre"]
                                )
            new_image.save()
            return HttpResponseRedirect('/galeria/galeria_imagenes/')
        
        
def galeria_imagenes(request):
    imagenes = Imagen.objects.all().order_by('-id')
    print(imagenes)
    return render(request, 'galeria_imagenes.html', {'imagenes': imagenes})
