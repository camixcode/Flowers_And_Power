from django.urls import path
from rest_producto.views import lista_Producto
#from rest_producto.viewsLogin import login

urlpatterns = [
    path('lista_Producto', lista_Producto, name="lista_Producto"),
    #path('login', login, name="login"),
]