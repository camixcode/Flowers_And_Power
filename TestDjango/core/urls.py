from django.urls import path

#from TestDjango.core.models import Producto


from .views import home


urlpatterns = [
    path('', home, name="home"),


]

