from ast import Try
from itertools import product
from math import prod
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
from core.usuario import Usuario as PU


# Create your views here.
def home(request):
    productos = Producto.objects.all()
    
    datos = {
        'productos': productos,
        "nombre": "diego araya"
    }  
    return render(request, 'core/home.html', datos)




def Producto1(request):
    productos =Producto.objects.all()
    for key, value in request.session ["usuario"].items():
        datos = {
            'idUsuario' : value["idUsuario"],
            'NombreUsuario' : value["nombreUsuario"],
            'productos':productos
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
            print(usu)
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
                permenencia = PU(request)
                permenencia.agregar(usu)
                print(request.session["usuario"].items())
                for key, value in request.session ["usuario"].items():
                    datos = {
                        'idUsuario' : value["idUsuario"],
                        'NombreUsuario' : value["nombreUsuario"]
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
            return redirect("index_home",)  




def Arbusto(request):
    for key, value in request.session ["usuario"].items():
        datos = {
            'idUsuario' : value["idUsuario"],
            'NombreUsuario' : value["nombreUsuario"]
        }
    return render(request, 'core/Arbusto.html',datos)

def Contacto(request):
    for key, value in request.session ["usuario"].items():
        datos = {
            'idUsuario' : value["idUsuario"],
            'NombreUsuario' : value["nombreUsuario"]
        }
    return render(request, 'core/Contacto.html',datos)

def Categoria1(request):
    for key, value in request.session ["usuario"].items():
        datos = {
            'idUsuario' : value["idUsuario"],
            'NombreUsuario' : value["nombreUsuario"]
        }
    return render(request, 'core/Categoria1.html',datos)

def F_Crear_Cuenta(request):
    for key, value in request.session ["usuario"].items():
        datos = {
            'idUsuario' : value["idUsuario"],
            'NombreUsuario' : value["nombreUsuario"]
        }
    return render(request, 'core/F_Crear_Cuenta.html',datos)

def form_mod_usuario(request):
    for key, value in request.session ["usuario"].items():
        datos = {
            'idUsuario' : value["idUsuario"],
            'NombreUsuario' : value["nombreUsuario"]
        }
    return render(request, 'core/form_mod_usuario.html',datos)

def form_borrar_producto(request,id):
    producto = Producto.objects.get(idProducto=id)
    producto.delete()
    productos =Producto.objects.all()
    
    datos = {
        'productos':productos
    }
    return render(request, 'core/listado_producto.html',datos)

def form_borrar_usuario(request,id):
    usuario = Usuario.objects.get(idUsuario=id)
    usuario.delete()
    usuarios =Usuario.objects.all()
    
    datos = {
        'usuarios':usuarios
    }
    return render(request, 'core/listado_usuario.html',datos)

def HistoricoCompra(request):
    for key, value in request.session ["usuario"].items():
        datos = {
            'idUsuario' : value["idUsuario"],
            'NombreUsuario' : value["nombreUsuario"]
        }
    return render(request, 'core/HistoricoCompra.html',datos)

def index_home(request):
    for key, value in request.session ["usuario"].items():
        datos = {
            'idUsuario' : value["idUsuario"],
            'NombreUsuario' : value["nombreUsuario"]
        }
        print(datos)
    return render(request, 'core/index_home.html',datos)    

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
    for key, value in request.session ["usuario"].items():
        datos = {
            'idUsuario' : value["idUsuario"],
            'NombreUsuario' : value["nombreUsuario"],
            'productos':productos
        }
    return render(request, 'core/listado_producto.html',datos) 

def listado_usuario(request):
    usuarios =Usuario.objects.all()
    for key, value in request.session ["usuario"].items():
        datos = {
            'idUsuario' : value["idUsuario"],
            'NombreUsuario' : value["nombreUsuario"],
            'usuarios': usuarios
        }
    return render(request, 'core/listado_usuario.html',datos)   

def Macetero(request):
    for key, value in request.session ["usuario"].items():
        datos = {
            'idUsuario' : value["idUsuario"],
            'NombreUsuario' : value["nombreUsuario"]
        }
    
    return render(request, 'core/Macetero.html',datos)    

def Nosotros(request):
    for key, value in request.session ["usuario"].items():
        datos = {
            'idUsuario' : value["idUsuario"],
            'NombreUsuario' : value["nombreUsuario"]
        }
    return render(request, 'core/Nosotros.html',datos)                

def Paypal(request):
    return render(request, 'core/Paypal.html')   

def PerfilProducto(request):
    for key, value in request.session ["usuario"].items():
        datos = {
            'idUsuario' : value["idUsuario"],
            'NombreUsuario' : value["nombreUsuario"]
        }
    return render(request, 'core/PerfilProducto.html',datos)      

  

def Seguimiento(request):
    for key, value in request.session ["usuario"].items():
        datos = {
            'idUsuario' : value["idUsuario"],
            'NombreUsuario' : value["nombreUsuario"]
        }
    return render(request, 'core/Seguimiento.html',datos)      

def Tierra(request):
    for key, value in request.session ["usuario"].items():
        datos = {
            'idUsuario' : value["idUsuario"],
            'NombreUsuario' : value["nombreUsuario"]
        }
    return render(request, 'core/Tierra.html',datos)     

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
    for key, value in request.session ["usuario"].items():
        datos = {
            'idUsuario' : value["idUsuario"],
            'NombreUsuario' : value["nombreUsuario"],
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

def form_mod_usuario(request,id):
    usuario =Usuario.objects.get(idUsuario = id)
    datos={
        'form': RegistrarUsuario(instance=usuario)
    }
    if request.method == 'POST':
        formulario = RegistrarUsuario(data=request.POST, instance= usuario)
        if formulario.is_valid:
            formulario.save()

    return render(request, 'core/form_mod_usuario.html',datos)

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
     