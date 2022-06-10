from django.urls import path

#from TestDjango.core.models import Producto



from .views import Arbusto, home, Contacto, Categoria1, F_Crear_Cuenta,form_mod_usuario,Nosotros,HistoricoCompra,index_home,InicioSesion1,listado_producto ,Paypal,PerfilProducto,Producto1,Seguimiento,Tierra, Macetero,index_homeOG, form_usuario
# ,NavBar


urlpatterns = [
    path('',home , name="Home"),
    path('index_home', index_home, name="index_home"),
    path('Arbusto/', Arbusto, name="Arbusto"),
    path('home/',index_homeOG , name="home"),
    path('Contacto/', Contacto, name="Contacto"),
    path('Categoria1/', Categoria1, name="Categoria1"),
    path('F_Crear_Cuenta/', F_Crear_Cuenta, name="F_Crear_Cuenta"),
    path('form_mod_usuario/', form_mod_usuario, name="form_mod_usuario"),
    path('form_usuario/', form_usuario, name="form_usuario"),

    path('HistoricoCompra/', HistoricoCompra, name="HistoricoCompra"),
    #path('Home/', index_home, name="Home"),
    path('InicioSesion1/', InicioSesion1, name="InicioSesion1"),
    path('listado_producto/', listado_producto, name="listado_producto"),
    path('Macetero/', Macetero, name="Macetero"),
    path('Nosotros/', Nosotros, name="Nosotros"),
    path('Paypal/', Paypal, name="Paypal"),
    path('PerfilProducto/', PerfilProducto, name="PerfilProducto"),
    path('Producto/', Producto1, name="Producto"),
    path('Seguimiento/', Seguimiento, name="Seguimiento"),
    path('Tierra/', Tierra, name="Tierra"),
    #path('Nav/', NavBar, name="Nav"),

]

