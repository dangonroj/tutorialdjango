from django.urls import path
from . import views
app_name = 'galeria'
urlpatterns = [
    path('', views.index, name='index'),
    path('subir_imagen/', views.subir_imagen, name='subir_imagen'),
    path('galeria_imagenes/', views.galeria_imagenes, name='galeria_imagenes')
]