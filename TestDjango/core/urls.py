from django.urls import path

from TestDjango.core.models import Producto

from .views import Arbusto
from .views import Categoria
from .views import Contacto
from .views import F_Crear_Cuenta
from .views import HistoricoCompra
from .views import InicioSesion1
from .views import Macetero
from .views import Nosotros
from .views import Paypal
from .views import PerfilProducto
from .views import Seguimiento
from .views import Tierra
from .views import home
from .views import index_home

urlpatterns = [
    path('', home, name="home"),


]

urlpatterns = [
    path('', Arbusto, name="Arbusto"),

]
urlpatterns = [
    path('', Categoria, name="Categoria"),

]
urlpatterns = [
    path('', Contacto, name="Contacto"),

]
urlpatterns = [
    path('', F_Crear_Cuenta, name="F_crear_Cuenta"),

]
urlpatterns = [
    path('', HistoricoCompra, name="HistoricoCompra"),

]
urlpatterns = [
    path('', InicioSesion1, name="InicioSesion1"),

]
urlpatterns = [
    path('', Macetero, name="Macetero"),

]
urlpatterns = [
    path('', Nosotros, name="Nosotros"),

]
urlpatterns = [
    path('', Paypal, name="Paypal"),

]

urlpatterns = [
   path('', PerfilProducto, name="PerfilProducto"),

]
urlpatterns = [
    path('', Producto, name="Producto"),

]
urlpatterns = [
    path('', Seguimiento, name="Seguimiento"),

]
urlpatterns = [
        path('', Tierra, name="Tierra"),

]
urlpatterns = [
    path('', index_home, name="index_home"),

]