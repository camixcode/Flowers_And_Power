from django.shortcuts import render
from . models import Producto
# Create your views here.

def home(request):
    return render(request,'core/home.html')

def home(request):
    contexto={"nombre": "diego araya"}
    return render(request,'core/home.html', contexto)

def home (request):
    productos = Producto.objects.all()

    datos ={
        'productos': productos
    }
    return render(request,'core/home.html', datos)