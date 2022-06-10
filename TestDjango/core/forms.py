
from django import forms
from django.forms import ModelForm
from .models import Usuario

class RegistrarUsuario(ModelForm):

    class Meta:
        model = Usuario
        fields =['idUsuario','nombres','apellidos','nombreUsuario','contrasena']