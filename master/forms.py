from django import forms
from .models import *

class AlumnoForm(forms.ModelForm):
   class Meta:
      model = Alumno
      fields = ['nombre','apellidos','email']

class BuscarAlumForm(forms.Form):
   q = forms.CharField()