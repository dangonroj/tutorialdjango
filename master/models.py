from django.db import models

# Create your models here.

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellidos)

class Alumno (models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellidos)

class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    creditos = models.IntegerField()
    profesores = models.ManyToManyField(Profesor)
    curso = models.IntegerField()

    def __str__(self):
        return '%s' % (self.nombre)

class Matricula(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    nota = models.FloatField()
    presentado = models.BooleanField(default=False)
    fecha = models.DateField()

    def __str__(self):
        return '%s %s - %s' % (self.alumno.nombre, self.alumno.apellidos, self.asignatura.nombre)
