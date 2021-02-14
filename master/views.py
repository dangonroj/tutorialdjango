from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from master.models import *

# Create your views here.
def index(request):
    asignaturas = Asignatura.objects.all()
    profesores = Profesor.objects.all()
    alumnos = Alumno.objects.all()
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