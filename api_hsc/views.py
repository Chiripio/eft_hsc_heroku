from rest_framework import viewsets
from .serializers import CategoriaSerializer
from Inicio.models import Categoria

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

import requests
from django.shortcuts import render

def noticias(request):
    url = 'https://hn.algolia.com/api/v1/search?query=technology'
    noticias = []
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # lanza excepción si el código no es 200
        noticias_data = response.json()
        noticias = noticias_data.get('hits', [])
    except requests.RequestException as e:
        print(f"⚠️ Error al conectar con la API de noticias: {e}")
        # Aquí puedes incluso mostrar un mensaje en pantalla si lo deseas

    return render(request, 'api_hsc/noticias.html', {'noticias': noticias})