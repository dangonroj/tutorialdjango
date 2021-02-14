from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'master'
urlpatterns = [
    path('', views.index, name='index'),
    url('asignatura/(?P<id>\d+)/', views.ver_asignatura),
    url('prof/(?P<id>\d+)/', views.ver_prof),
    url('alum/(?P<id>\d+)/', views.ver_alum)
]