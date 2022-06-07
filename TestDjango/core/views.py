from django.shortcuts import render
from . models import Producto
from . models import Arbusto
from . models import Categoria
from . models import Contacto
from . models import F_crear_Cuenta
from . models import HistoricoCompra
from . models import InicioSesion1
from . models import Macetero
from . models import Nosotros
from . models import Paypal
from . models import PerfilProducto
from . models import Seguimiento
from . models import Tierra
from . models import index_home

# Create your views here.


def home(request):
    return render(request, 'core/home.html')


def home(request):
    contexto = {"nombre": "diego araya"}
    return render(request, 'core/home.html', contexto)


def home(request):
    productos = Producto.objects.all()

    datos = {
        'productos': productos
    }
    return render(request, 'core/home.html', datos)


def Categoria(request):
    return render(request, 'core/Categoria.html')


def Contacto(request):
    return render(request, 'core/Contacto.html')


def Arbusto(request):
    return render(request, 'core/Arbusto.html')


def F_Crear_Cuenta(request):
    return render(request, 'core/F_Crear_Cuenta.html')


def HistoricoCompra(request):
    return render(request, 'core/HistoricoCompra.html')


def index_home(request):
    return render(request, 'core/index_home.html')


def Macetero(request):
    return render(request, 'core/Macetero.html')

def Nosotros(request):
    return render(request, 'core/Nosotros.html')

def Paypal(request):
    return render(request, 'core/Paypal.html')

def PerfilProducto(request):
    return render(request, 'core/PerfilProducto.html')  

def Producto(request):
    return render(request, 'core/Producto.html')

def Seguimiento(request):
    return render(request, 'core/Seguimiento.html')  

def Tierra(request):
    return render(request, 'core/Tierra.html')

def InicioSesion1(request):
    return render(request, 'core/InicioSesion1.html')
    