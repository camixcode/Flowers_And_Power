from django.urls import path

#from TestDjango.core.models import Producto


from .views import  home,Arbusto
urlpatterns = [
    path('', home, name="home"),
    path('', Arbusto, name="Arbusto"),



]

