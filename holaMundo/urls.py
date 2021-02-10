from django.urls import path
from . import views
app_name = 'holaMundo'
urlpatterns = [
    path('', views.holaMundo, name='holaMundo'),
]