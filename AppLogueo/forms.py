from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts={ k:''for k in fields}


class UserEditForm(forms.Form):
    username=forms.CharField(label='nombre de usuario')
    email= forms.EmailField(label='modificar email')
    first_name=forms.CharField(label='nombre')
    last_name=forms.CharField(label='apellido')    

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
        help_texts={ k:''for k in fields}

class AvatarFormulario(forms.ModelForm):

    class Meta:
        model= Avatar
        fields='__all__'
        exclude=['user']

#Listo (-