 
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
