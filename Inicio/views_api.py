from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Producto
from .serializers import ProductoSerializer, VentaSerializer
from .models import Venta, Usuario
from django.contrib.auth.models import User

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def listar_productos(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def ventas_por_usuario(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=404)

    try:
        usuario = Usuario.objects.get(username=user.username)
    except Usuario.DoesNotExist:
        return Response({'error': 'No existe un usuario asociado al username'}, status=404)

    ventas = Venta.objects.filter(usuario=usuario)
    serializer = VentaSerializer(ventas, many=True)
    return Response(serializer.data)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='/iniciarsesion/')
def ventas_api_html(request):
    return render(request, 'Inicio/ventas_api.html')