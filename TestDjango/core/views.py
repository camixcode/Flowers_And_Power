from sqlite3 import DateFromTicks
from django.shortcuts import render
from . models import Producto



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

def Arbusto(request):
    return render(request, 'core/Arbusto.html')


def Contacto(request):
    return render(request, 'core/Contacto.html')



def Categoria1(request):
    return render(request, 'core/Categoria1.html')

def F_Crear_Cuenta(request):
    return render(request, 'core/F_Crear_Cuenta.html')

def form_mod_usuario(request):
    return render(request, 'core/form_mod_usuario.html')

def HistoricoCompra(request):
    return render(request, 'core/HistoricoCompra.html')

def index_home(request):
    return render(request, 'core/index_home.html')    

def index_homeOG(request):
    return render(request, 'core/index_homeOG.html')    

def InicioSesion1(request):
    return render(request, 'core/InicioSesion1.html')        

def listado_producto(request):
    return render(request, 'core/listado_producto.html')    

def Macetero(request):
    return render(request, 'core/Macetero.html')    

def Nosotros(request):
    return render(request, 'core/Nosotros.html')                

def Paypal(request):
    return render(request, 'core/Paypal.html')   

def PerfilProducto(request):
    return render(request, 'core/PerfilProducto.html')      

def Producto1(request):
    return render(request, 'core/Producto1.html')      

def Seguimiento(request):
    return render(request, 'core/Seguimiento.html')      

def Tierra(request):
    return render(request, 'core/Tierra.html')                          