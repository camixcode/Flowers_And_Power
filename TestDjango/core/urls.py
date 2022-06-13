from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core.Carrito import Carrito
#from TestDjango.core.models import Producto



from .views import Arbusto, agregar_producto, eliminar_producto, home, Contacto, Categoria1, F_Crear_Cuenta,form_mod_usuario,Nosotros,HistoricoCompra,index_home,InicioSesion1, limpiar_carrito,listado_producto, Paypal,PerfilProducto,Producto1,Seguimiento,Tierra, Macetero,index_homeOG, form_usuario,restar_producto,usuario, form_producto, Carrito
# ,NavBar


urlpatterns = [
    path('home1',home , name="Home"),
    path('', index_home, name="index_home"),
    path('Arbusto/', Arbusto, name="Arbusto"),
    path('home/',index_homeOG , name="home"),
    path('Contacto/', Contacto, name="Contacto"),
    path('Categoria1/', Categoria1, name="Categoria1"),
    path('F_Crear_Cuenta/', F_Crear_Cuenta, name="F_Crear_Cuenta"),
    path('form_mod_usuario/', form_mod_usuario, name="form_mod_usuario"),
    path('form_usuario/', form_usuario, name="form_usuario"),
    path('form_producto/', form_producto, name="form_producto"),
    path('login',usuario),
    path('login',Carrito),
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
    path('agregar/<int:producto_id>/', agregar_producto, name="add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="del"),
    path('restar/<int:producto_id>/', restar_producto, name="sub"),
    path('limpiar/', limpiar_carrito, name="cls"),
]


urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
##urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
