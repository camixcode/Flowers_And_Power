
from django import forms
from django.forms import ModelForm
from .models import Producto, Usuario

class RegistrarUsuario(ModelForm):
    class Meta:
        model = Usuario
        fields =['idUsuario','nombres','apellidos','nombreUsuario','contrasena']

class RegistrarProducto(ModelForm):

    class Meta:
        model = Producto
        fields =['idProducto','nombreProducto','descripcionProducto','precioProducto','imagen','categoria',]