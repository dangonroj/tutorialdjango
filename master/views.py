from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect

from master.models import *
from master.forms import *

# Create your views here.
def index(request):
    asignaturas = Asignatura.objects.all()
    profesores = Profesor.objects.all()
    alumnos = Alumno.objects.all().order_by('nombre')
    return render(request, 'indexMaster.html', {'asignaturas': asignaturas,'profesores': profesores,'alumnos': alumnos})

def ver_asignatura(request, id):
    asignatura = get_object_or_404(Asignatura, id=id)
    return render(request,'ver_asignatura.html', {'asignatura':asignatura})

def ver_prof(request, id):
    prof = get_object_or_404(Profesor, id=id)
    asignaturas = prof.asignatura_set.all()
    return render(request,'ver_prof.html', {'prof':prof, 'asignaturas':asignaturas})

def ver_alum(request, id):
    alum = get_object_or_404(Alumno, id=id)
    matriculas = Matricula.objects.filter(alumno=alum)
    return render(request,'ver_alum.html', {'alum':alum, 'matriculas':matriculas})

def crear_alum(request):
   if request.method == 'GET':
      return render(request, 'crear_alum.html')
   elif request.method == 'POST':
       form = AlumnoForm(request.POST)
       if form.is_valid():
           nuevo_alum = Alumno(nombre=form.cleaned_data["nombre"],
                             apellidos=form.cleaned_data["apellidos"],
                               email=form.cleaned_data["email"]
                             )
           nuevo_alum .save()
           id = nuevo_alum.id
           return HttpResponseRedirect('/master/alum/'+str(id))
       else:
           return HttpResponseRedirect('/master/crear_alum/')

def buscar_alum(request):
   if request.method == 'GET':
      return render(request, 'buscar_alum.html')
   elif request.method == 'POST':
       form = BuscarAlumForm(request.POST)
       if form.is_valid():
           texto = form.cleaned_data["q"]
           alumnos = Alumno.objects.filter(apellidos__icontains=texto)
           return render(request,'listado_alum.html', {'alumnos':alumnos})
       else:
           return HttpResponseRedirect('/master/buscar_alum/')