from dataclasses import field
from django import forms
from .models import Usuario

class formLog(forms.ModelForm):
    class Meta:
        Model = Usuario
        fields = ['nombreUsuario','Contrasena']