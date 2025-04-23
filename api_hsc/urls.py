from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet
from .views import noticias

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='categorias')

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    path('noticias/', noticias, name='noticias'),
]