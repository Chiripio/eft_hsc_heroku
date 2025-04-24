from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, noticias
from rest_framework.authtoken.views import obtain_auth_token

# Router para las vistas basadas en viewsets
router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='categorias')

# URLs combinadas
urlpatterns = [
    path('', include(router.urls)),                  # Endpoint para categorias
    path('noticias/', noticias, name='noticias'),    # Endpoint para noticias externas
    path('token/', obtain_auth_token, name='api_token_auth'),  # Endpoint para autenticación por token
]