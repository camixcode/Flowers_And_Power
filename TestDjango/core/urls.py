from django.urls import path

#from TestDjango.core.models import Producto



from .views import Arbusto, home, Contacto, Categoria1, F_Crear_Cuenta,form_mod_usuario,Nosotros,HistoricoCompra,index_home,InicioSesion1,listado_producto ,Paypal,PerfilProducto,Producto1,Seguimiento,Tierra, Macetero,index_homeOG


urlpatterns = [
    path('', index_homeOG, name="home"),
    path('Home2', index_home, name="home"),
    path('Arbusto/', Arbusto, name="Arbusto"),
    path('Home/', home, name="Home"),
    path('Contacto/', Contacto, name="Contacto"),
    path('Categoria1/', Categoria1, name="Categoria1"),
    path('Crear Cuenta/', F_Crear_Cuenta, name="Crear Cuenta"),
    path('Formulario Usuario/', form_mod_usuario, name="Formulario Usuario"),
    path('Historico de Compras/', HistoricoCompra, name="Historico de Compras"),
    path('Home/', index_home, name="Home"),
    path('Inicio de Sesion/', InicioSesion1, name="Inicio de Sesion"),
    path('Lista de productos/', listado_producto, name="Lista de productos"),
    path('Producto de Macetero/', Macetero, name="Producto de Macetero"),
    path('Nosotros/', Nosotros, name="Nosotros"),
    path('Paypal/', Paypal, name="Paypal"),
    path('Perfil de Producto/', PerfilProducto, name="Perfil de Producto"),
    path('Producto/', Producto1, name="Producto"),
    path('Seguimiento de Compra/', Seguimiento, name="Seguimiento de Compra"),
    path('Producto de Tierra/', Tierra, name="Tierra"),

]

