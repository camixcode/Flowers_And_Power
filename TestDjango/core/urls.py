from django.urls import path

from TestDjango.core.models import Producto
from .views import Arbusto, Categoria, Contacto, F_Crear_Cuenta, HistoricoCompra, InicioSesion1, Macetero, Nosotros, Paypal, PerfilProducto, Seguimiento, Tierra, home, index_home

urlpatterns = [
    path('', home, name="home"),
    path('', Arbusto, name="Arbusto"),
    path('', Categoria, name="Categoria"),
    path('', Contacto, name="Contacto"),
    path('', F_Crear_Cuenta, name="F_crear_Cuenta"),
    path('', HistoricoCompra, name="HistoricoCompra"),
    path('', InicioSesion1, name="InicioSesion1"),
    path('', Macetero, name="Macetero"),
    path('', Nosotros, name="Nosotros"),
    path('', Paypal, name="Paypal"),
    path('', PerfilProducto, name="PerfilProducto"),
    path('', Producto, name="Producto"),
    path('', Seguimiento, name="Seguimiento"),
    path('', Tierra, name="Tierra"),
    path('', index_home, name="index_home"),

]