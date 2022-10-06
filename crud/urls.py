from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name="inicio"),
    
    path('personas/',views.lista_personas, name="listaPersonas"),
]