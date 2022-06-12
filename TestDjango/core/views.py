from re import U
from sqlite3 import DateFromTicks
from xml.dom.minidom import Document
from xml.parsers.expat import model
from django.shortcuts import render

from .forms import RegistrarProducto, RegistrarUsuario
from . models import Producto
from .models import Usuario


# Create your views here.
def home(request):
    productos = Producto.objects.all()
    datos = {
        'productos': productos,
        "nombre": "diego araya"
    }  
    return render(request, 'core/home.html', datos)


def usuario(request):
    if request.method == 'post':
        usuario= request.post['nombreUsuario']
        contrasena= request.post['contrasena']
        usu=Usuario.objects.get(nombreUsuario=usuario)
        if usu: 
            #cont=usu.filter(contrasena=contrasena)
            if str(usu.contrasena) == str(contrasena):
                return render(request, 'core/home.html', usu)        
            else:
                datos = {
                    'error': 'usuario',
                    "mensaje": "error contrasena incorrecta"
                }  
           
            return render(request, 'core/F_Crear_Cuenta.html',datos) 

        else:
            datos = {
                    'error': 'usuario',
                    "mensaje": "error usuario no valido"
                }  
            return render(request, 'core/F_Crear_Cuenta.html',datos) 




def Arbusto(request):
    return render(request, 'core/Arbusto.html')

def Contacto(request):
    return render(request, 'core/Contacto.html')

def Categoria1(request):
    return render(request, 'core/Categoria1.html')

def F_Crear_Cuenta(request):
    datos ={
            'form': RegistrarUsuario()
    }
    if request.method =='POST':
        formulario = RegistrarUsuario(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"

    return render(request, 'core/F_Crear_Cuenta.html',datos)

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

def form_usuario(request):
    datos ={
            'form': RegistrarUsuario()
    }
    if request.method =='POST':
        formulario = RegistrarUsuario(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"

    return render(request, 'core/form_usuario.html',datos)

def form_producto(request):
    datos ={
            'form': RegistrarProducto()
    }
    if request.method =='POST':
        formulario = RegistrarProducto(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"

    return render(request, 'core/form_producto.html',datos)
                     

#def NavBar(request):
 #   return render(request, 'core/NavBar.html')  
     