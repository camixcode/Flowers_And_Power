from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, ParseError
from django.views.decorators.csrf import csrf_exempt
#from yaml import serialize
from core.models import Producto
from .serializers import ProductoSerializer
@csrf_exempt
@api_view(['GET', 'POST'])

def lista_Producto(request):
    """
    LISTA DE TODOS LOS Productos 
    """
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':        
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
