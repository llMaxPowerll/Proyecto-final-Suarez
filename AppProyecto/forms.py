from django import forms

class BibliotecasFormulario(forms.Form):
    nombre=forms.CharField()
    direccion=forms.CharField()
    email=forms.EmailField()
   # =forms.BooleanField(required=False)

class LibrosFormulario(forms.Form):
    titulo= forms.CharField()
    editorial=forms.CharField()
    paginas= forms.IntegerField()
    #= forms.BooleanField(required=False)

class AutoresFormulario(forms.Form):
    nombre= forms.CharField()
    apellido=forms.CharField()
    edad= forms.IntegerField()
    #= forms.BooleanField(required=False)