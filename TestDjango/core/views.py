from ast import Try
from itertools import product
from re import U
from sqlite3 import DateFromTicks
from tokenize import Triple
from urllib import request
from warnings import catch_warnings
from xml.dom.minidom import Document
from xml.parsers.expat import model
from django.shortcuts import redirect, render
from core.forms import RegistrarProducto, RegistrarUsuario

from core.Carrito import Carrito


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




def Producto1(request):
    productos = Producto.objects.all()
    datos = {
        'productos': productos
    } 
    return render(request, 'core/Producto1.html', datos)  

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.agregar_producto(producto)
    return redirect("Producto")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.eliminar(producto)
    return redirect("Producto")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_id)
    carrito.restar(producto)
    return redirect("Producto") 

def limpiar_carrito(request):
    carrito = Carrito(request)   
    carrito.limpiar()
    return redirect("Producto") 


def usuario(request):
    print("Detecto request()", request)
    print("Detecto request()", request.method)
    if request.method == 'POST':
        print("Detecto llamda post")
        print(request.POST)
        usuario= request.POST['nombreUsuario']
        print(usuario)
        contrasena= request.POST['contrasena']
        print(contrasena)
        try: 
            usu=Usuario.objects.get(nombreUsuario=usuario)
        except:
            datos = {
                    'error': 'usuario',
                    "mensaje": "error usuario no valido"
                }  
            return render(request, 'core/InicioSesion1.html',datos)  
        if usu: 
            print("Detecto")
            #cont=usu.filter(contrasena=contrasena)
            if str(usu.contrasena) == str(contrasena):
                datos = {

                    'NombreUsuario' : usu.nombreUsuario
                }
                return render(request, 'core/index_home.html',datos)       
            else:
                datos = {
                    'error': 'usuario',
                    "mensaje": "error contrasena incorrecta"
                }            
            return render(request, 'core/InicioSesion1.html',datos) 
        else:
            datos = {
                    'error': 'usuario',
                    "mensaje": "error usuario no valido"
                }  
            return redirect("index_home")  




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
    dict={}
    if request.method == 'POST':
        username= request.POST["nomUsuario"]
        password = request.POST["contrasenaUsuario"]
        dict = {
            "nombre": username
        }
    return render(request, 'core/InicioSesion1.html',dict)             

def listado_producto(request):
    productos =Producto.objects.all()
    datos={
         'productos':productos}
    
    return render(request, 'core/listado_producto.html',datos)   

def Macetero(request):
    return render(request, 'core/Macetero.html')    

def Nosotros(request):
    return render(request, 'core/Nosotros.html')                

def Paypal(request):
    return render(request, 'core/Paypal.html')   

def PerfilProducto(request):
    return render(request, 'core/PerfilProducto.html')      

  

def Seguimiento(request):
    return render(request, 'core/Seguimiento.html')      

def Tierra(request):
    return render(request, 'core/Tierra.html')     

def form_usuario(request):
    datos = {
        'form': RegistrarUsuario()
    }

    if request.method == 'POST':
        formmulario = RegistrarUsuario(request.POST)
        if formmulario.is_valid:
            formmulario.save()
            datos['mensaje'] = "Guardados Correctamente"

    return render(request, 'core/form_usuario.html',datos)          

def form_producto(request):
    datos = {
        'form': RegistrarProducto()
    }

    if request.method == 'POST':

        formmulario = RegistrarProducto(request.POST)

        if formmulario.is_valid:
            formmulario.save()
            datos['mensaje'] = "Guardados Correctamente"
    return render(request, 'core/form_producto.html',datos)     

def form_mod_producto(request):
    return render(request, 'core/form_producto.html')                      


def F_Crear_Cuenta(request):
    datos = {
        'form': RegistrarUsuario()
    }

    if request.method == 'POST':

        formmulario = RegistrarUsuario(request.POST)

        if formmulario.is_valid:
            formmulario.save()
            datos['mensaje'] = "Guardados Correctamente"

    return render(request, 'core/F_Crear_Cuenta.html',datos)

def form_mod_usuario(request):
    return render(request, 'core/form_mod_usuario.html')

def form_mod_producto(request,id):
    producto =Producto.objects.get(idProducto = id)
    datos={
        'form': RegistrarProducto(instance=producto)
    }
    if request.method == 'POST':
        formulario = RegistrarProducto(data=request.POST, instance= producto)
        if formulario.is_valid:
            formulario.save()

    return render(request, 'core/form_mod_producto.html',datos)



#def NavBar(request):
 #   return render(request, 'core/NavBar.html')  
     