"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView
from holaMundo import views
urlpatterns = [
    #path('', RedirectView.as_view(url='/galeria/', permanent=True)), #para tener todas las app en una pagina
    path('admin/', admin.site.urls),
    path(r'^$', views.index),
    path('galeria/', include('galeria.urls')),
    url('tutorial/', views.index, name='index_tutorial'),
    url('calendario/', views.calendario, name='reloj'),
    url('calculadora/(?P<a>\d+)/(?P<b>\d+)', views.calculadora, name='calculadora'),
    url('holaMundo2/', views.holaMundo2),
    url('holaMundo/', include('holaMundo.urls'))
]

#para imagenes
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

