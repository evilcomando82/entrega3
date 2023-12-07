ALUMNO: SEBASTIÁN NAVARRO VEAS

## Configuración inicial del proyecto
Crear carpeta para nuestro repositorio, "proyecto3"
1.	Crear archivo README.md
2.	Instalar `django`:  pip install django
3.	Crear proyecto:  django-admin startproject TercerProyecto  (Este comando dejará creada una nueva carpeta `TercerProyecto`)
4.	Dentro de la carpeta `proyecto3/TercerProyecto` o botón derecho sobre manage.py y abrir en terminal integrado
5.	python manage.py startapp AppCoder  (anterior creamos el proyecto, ahora la APP)
6.	Registrar la aplicación en TercerProyecto/settings.py
```python
 

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'AppCoder',  #aca se agrega
]

```
7.	Servidor Web
python manage.py runserver
## Configurar Rutas
Registrar rutas `ProyectoCoder/urls.py`
```python
from django.urls import path, include #agregar include
path("AppCoder/", include("AppCoder.urls")),

```

Copiar archivo TercerProyecto/urls.py en AppCoder
Crear ruta dentro de urls.py AppCoder 


```python


from django.urls import path
from AppCoder.views import personas_view

urlpatterns = [
    path("", personas_view),
    
]

```

Crear una función de prueba en views.py en AppCoder, se debe ingresar en la ruta AppCoder/ del navegador, esto es para prueba, estamos realizando “el esqueleto de como queremos que funcione nuestro sitio”
```python
Ejemplo:
def buscar_personas_view (request):
    return HttpResponse ("Buscar personas")

```
Finalmente creamos las rutas definitivas:
```python

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


```

8. Creando templates y herencia
Crear un directorio llamado `templates` dentro del directorio `AppCoder`, luego crear otro directorio dentro de `templates` llamado `AppCoder y dentro padre.html.
 
```python
path("padre/", padre_view),
```
```python

def padre_view(request):
    return render(request, 'AppCoder/padre.html')
```

```python
Agregamos en `cursos.html`
    ```html
    {% extends "AppCoder/padre.html" %}
    ```
 Agregamos en `padre.html`
    ```html
    {% block contenidoQueCambia %}
    {% endblock %}
    ```
    y en `cursos.html`

    ```html
    {% block contenidoQueCambia %}
    Este es el contenido de cursos.html!
    {% endblock %}
```
Renderizamos la vista 

```python
def cursos_view(request):
   # return HttpResponse("cursos")
    return render(request, "AppCoder/padre.html")
```

Crear una carpeta llamada `static` en nuestra app: `AppCoder/static/AppCoder`
Le agregamos 1 línea y modificamos otra:
{% load static %}
<!-- Core theme CSS (includes Bootstrap)-->
<link href="{% static 'AppCoder/css/styles.css'  %}" rel="stylesheet" />


8. Creamos los modelos:
```python


from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
    
class Curso(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    pais_origen =models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)
    curso_origen =models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

```

Registramos los modelos en archive /admin.py  
```python

from django.contrib import admin
from . import models

admin.site.register(models.Pais)
admin.site.register(models.Curso)
admin.site.register(models.Persona)

# Register your models here.

```

9. Creamos las tablas en base de datos:
python manage.py makemigrations
python manage.py migrate

Creamos el admin y password 123, para crear la administración de nuestro sitio
python manage.py createsuperuser

Creamos archive forms.py en AppCoder
```python

from django import forms
 
from . import models

class PersonaForm(forms.ModelForm):
    class Meta:
        model = models.Persona
        fields =["nombre", "apellido", "pais_origen", "curso_origen"]
    
        widgets = { 
            "nombre" : forms.TextInput(attrs={'class':'form-control'}),
            "apellido" : forms.TextInput(attrs={'class':'form-control'}),
            "pais_origen" :forms.Select(attrs={'class':'form-control'}),
            "curso_origen" : forms.Select(attrs={'class':'form-control'})

   
        }

class PaisForm(forms.ModelForm):
    class Meta:
        model = models.Pais
        fields =["nombre"]
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

class CursoForm(forms.ModelForm):
    class Meta:
        model = models.Curso
        fields =["nombre"]
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        
        
        
   
```


En las páginas .html se de crear*** se debe agregar el siguiente código por ejemplo: (se debe crear con antelación la carpeta templates  (/AppCoder/Templates/AppCoder/xxx.html
```python
{% extends "AppCoder/padre.html" %}

{% block title %}
<h2>Crear Paises</h2>
{% endblock %}

{% block context %}
<div class="container">
 
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="mb-5 btn btn-success">guardar</button>
</form>
</div>
 
{% endblock %}
```

En listar*** html por ejemplo
```python
{% extends "AppCoder/padre.html" %}

{% block title %}
<h2>Listar Paises</h2>
{% endblock %}

{% block context %}

<div class="container">
  <table class="table table-bordered table-dark ">
    <thead>
      <tr>
        <th scope="col">id</th>
        <th scope="col">Nombre</th>
         
         
      </tr>
    </thead>
    <tbody>
        {% for pais in paises  %}
      <tr>
         
        <td>{{pais.id}}</td>
        <td>{{pais.nombre}}</td>
       
         
      </tr>
      {% endfor %}
     
    </tbody>
  </table>
</div>

{% endblock %}
     
    </tbody>
  </table>
</div>

{% endblock %}
```
En buscar*** html por ejemplo
```python
{% extends "AppCoder/padre.html" %}

{% block title %}
<h2>Buscar Paises por nombre</h2>
{% endblock %}

{% block context %}

    <form  method="POST" action="{% url 'buscar_paises' %}" >
        {% csrf_token %}
        <input type="text" name="nombre" id="nombre"/>

        <input type="submit" value="Buscar" class="mb-5"/>
    </form>
    
    {% if pais.count > 0 %}
    <div class="container">
    <table class="table table-bordered table-dark  ">
        <thead class="thead-dark">
          <tr>
            <th scope="col">id</th>
            <th scope="col">Nombre</th>
           </tr>
        </thead>
        <tbody>
            {% for pa in pais  %}
          <tr>
             
            <td>{{pa.id}}</td>
            <td>{{pa.nombre}}</td>
           
             
          </tr>
          {% endfor %}
         
        </tbody>
      </table>  
    </div>    
    {% endif %}

    {% if pais.count == 0 %}
    <div class="alert alert-danger" role="alert">
        {{mensaje}} 
    </div>
    {% endif %}
    
    
{% endblock %}

```
Creamos las nuevas vistas:
```python
 
from django.shortcuts import get_object_or_404, redirect, render
from . import forms
from . import models


def crear_personas_view (request):
 
    if request.method == 'POST':
        form = forms.PersonaForm(request.POST)
        if form.is_valid():
            formulario =form.save()
            msg=f"registro guardado conforme con el id={formulario.id} y su nombre: {formulario.nombre}" 
            #return redirect ("index", {'msg':msg})
            return render(request, "AppCoder/padre.html", {'msg': msg})
    else:
        formulario = forms.PersonaForm()
    return render(request, "AppCoder/crear_personas.html", {'form': formulario})
   


def buscar_personas_view (request):
    
    if request.method == 'POST':
        persona = models.Persona.objects.filter(nombre = request.POST['nombre'])   
        mensaje = '' if len(persona) > 0 else 'Sin registros'
        return render(request, 'AppCoder/buscar_personas.html',{'persona':persona,'mensaje':mensaje}) 
    else:
        return render(request, 'AppCoder/buscar_personas.html')       
    

def listar_personas_view (request):
    personas = models.Persona.objects.all() 
    context = {"personas": personas} #vemos el contecto    
    return render(request, 'AppCoder/listar_personas.html', context) #se agrega como parámetro context


def crear_paises_view (request):
 
    if request.method == 'POST':
        form = forms.PaisForm(request.POST)
        if form.is_valid():
            formulario =form.save()
            
            msg=f"registro guardado conforme con el id={formulario.id} y su nombre: {formulario.nombre}" 
            #return redirect ("index", {'msg':msg})
            return render(request, "AppCoder/padre.html", {'msg': msg})
    else:
        formulario = forms.PaisForm()
    return render(request, "AppCoder/crear_paises.html", {'form': formulario})

def buscar_paises_view (request):
    if request.method == 'POST':
        pais = models.Pais.objects.filter(nombre = request.POST['nombre'])   
        mensaje = '' if len(pais) > 0 else 'Sin registros'
        return render(request, 'AppCoder/buscar_paises.html',{'pais':pais,'mensaje':mensaje}) 
    else:
        return render(request, 'AppCoder/buscar_paises.html')       

def listar_paises_view (request):
    paises = models.Pais.objects.all()  #en la función se agrega    
    context = {"paises": paises} #vemos el contecto
    return render(request, 'AppCoder/listar_paises.html', context) #se agrega como parámetro context

def crear_cursos_view (request):
    if request.method == 'POST':
        form = forms.CursoForm(request.POST)
        if form.is_valid():
            formulario =form.save()
            
            msg=f"registro guardado conforme con el id={formulario.id} y su nombre: {formulario.nombre}" 
            #return redirect ("index", {'msg':msg})
            return render(request, "AppCoder/padre.html", {'msg': msg})
    else:
        formulario = forms.CursoForm()
    return render(request, "AppCoder/crear_cursos.html", {'form': formulario})

def buscar_cursos_view (request):
    if request.method == 'POST':
        curso = models.Curso.objects.filter(nombre = request.POST['nombre'])   
        mensaje = '' if len(curso) > 0 else 'Sin registros'
        return render(request, 'AppCoder/buscar_cursos.html',{'curso':curso,'mensaje':mensaje}) 
    else:
        return render(request, 'AppCoder/buscar_cursos.html')     

def listar_cursos_view (request):
    cursos = models.Curso.objects.all()  #en la función se agrega    
    context = {"cursos": cursos} #vemos el contecto
    return render(request, 'AppCoder/listar_cursos.html', context) #se agrega como parámetro context


def padre_view(request):
    return render(request, 'AppCoder/padre.html')


```



