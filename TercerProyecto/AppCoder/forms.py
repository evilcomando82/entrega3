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
        
        
        
   