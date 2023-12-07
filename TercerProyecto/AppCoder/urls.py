
from django.urls import path

#from AppCoder.views import buscar_personas_view, crear_personas_view, padre_view, listar_personas_view, crear_paises_view, buscar_paises_view, listar_paises_view, crear_cursos_view, buscar_cursos_view, listar_cursos_view
from . import views

urlpatterns = [
    
    path("crear_personas/", views.crear_personas_view, name="crear_personas"),
    path("buscar_personas/", views.buscar_personas_view, name="buscar_personas"),
    
    path("listar_personas/", views.listar_personas_view, name="listar_personas"),
    
    path("crear_paises/", views.crear_paises_view, name="crear_paises"),
    path("buscar_paises/", views.buscar_paises_view, name="buscar_paises"),
    path("listar_paises/", views.listar_paises_view, name="listar_paises"),

    path("crear_cursos/", views.crear_cursos_view, name="crear_cursos"),
    path("buscar_cursos/", views.buscar_cursos_view, name="buscar_cursos"),
    path("listar_cursos/", views.listar_cursos_view, name="listar_cursos"),

    
    
    
    
    
    path("", views.padre_view, name="index"),
    
]
