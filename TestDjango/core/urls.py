from django.urls import path

#from TestDjango.core.models import Producto



from .views import Arbusto, home, Contacto



from .views import  home,Arbusto

urlpatterns = [
    path('', home, name="home"),
    path('Arbusto/', Arbusto, name="Arbusto"),
    path('Contacto/', Contacto, name="Contacto"),



]

