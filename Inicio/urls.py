from django.urls import path
from .views import (
    iniciar, iniciar_sesion, inicio, inicioadmin, registrar_m, registrarse, newProd, addprod,
    vistamod, eliminarProducto, menuadmin, micadmin, tecladoadmin, mouseAdmin, ramAdmin,
    graficaAdmin, procesadorAdmin, mostrarTeclado, teclado, mostrarMic, micro,
    mostrarMouse, mouse, mostrarGrafica, grafica, mostrarRam, ram, mostrarProcesador,
    procesador, carrito, perfilusuario, edicionProducto, editarProducto, mostrarperfil,
    modificarPerfil, agregar_producto, eliminar_producto, restar_producto, limpiar_producto,
    mostrarMicAnonimo, mostrarTecladoAnonimo, mostrarMouseAnonimo, mostrarGraficaAnonimo,
    mostrarRamAnonimo, mostrarProcesadorAnonimo, clima_actual, ver_clima, confirmar_pago
)
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from . import views_api
from . import views
from Inicio import views

urlpatterns = [
    path('clima/', views.ver_clima, name='ver_clima'),
    path('iniciar/', iniciar, name="iniciar"),
    path('iniciarsesion/', iniciar_sesion, name="iniciarsesion"),
    
    path('', inicio, name="inicio"),
    path('indexadmin', inicioadmin, name="indexadmin"),
    path('registrar/', registrar_m, name="registrar"),
    path('registrarse/', registrarse, name="registrarse"),

    # Productos (Agregar/Modificar)
    path('agregar2/', newProd, name="addProd"),
    path('agregar/', addprod, name="agregarprod"),
    path('modificar/', vistamod, name="modificar"),
    path('eliminarProducto/<idProducto>', eliminarProducto, name="eliminarProducto"),

    # Menú admin
    path('menuadmin/', menuadmin, name="menu_admin"),
    path('micadmin/<id>', micadmin, name="micadmin"),
    path('tecladoadmin/<id>', tecladoadmin, name="tecladoadmin"),
    path('mouseAdmin/<id>', mouseAdmin, name="mouseAdmin"),
    path('graficaAdmin/<id>', graficaAdmin, name="graficaAdmin"),
    path('procesadorAdmin/<id>', procesadorAdmin, name="procesadorAdmin"),

    # Mostrar productos (usuario identificado)
    path('teclados/<id>', mostrarTeclado, name="teclados"),
    path('teclados/<idk>/<usuario>', teclado, name="teclado"),
    path('microfonos/<id>', mostrarMic, name="mostrarMic"),
    path('microfono/<idmic>/<usuario>', micro, name="micro"),
    path('mouses/<id>', mostrarMouse, name="mostrarMouse"),
    path('mouses/<idm>/<usuario>', mouse, name="mouse"),
    path('graficas/<id>', mostrarGrafica, name="mostrarGrafica"),
    path('graficas/<idg>/<usuario>', grafica, name="grafica"),
    path('rams/<id>', mostrarRam, name="mostrarRam"),
    path('rams/<idr>/<usuario>', ram, name="ram"),
    path('procesadores/<id>', mostrarProcesador, name="mostrarProcesador"),
    path('procesadores/<idp>/<usuario>', procesador, name="procesador"),

    # Mostrar productos (anónimo)
    path('teclados/', mostrarTecladoAnonimo, name="tecladosAnonimo"),
    path('microfonos/', mostrarMicAnonimo, name="mostrarMicAnonimo"),
    path('mouses/', mostrarMouseAnonimo, name="mostrarMouseAnonimo"),
    path('graficas/', mostrarGraficaAnonimo, name="mostrarGraficaAnonimo"),
    path('rams/', mostrarRamAnonimo, name="mostrarRamAnonimo"),
    path('procesadores/', mostrarProcesadorAnonimo, name="mostrarProcesadorAnonimo"),

    # Carrito
    path('carrito/<str:id>/', views.carrito, name='carrito'),
    path('agregar3/<int:idProducto>/', agregar_producto, name="Add"),
    path('eliminar/<int:idProducto>/', eliminar_producto, name="Del"),
    path('restar/<int:idProducto>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_producto, name="CLS"),

    # Usuario
    path('miperfil/<id>', perfilusuario, name="miperfil"),
    path('mostrarperfil/<id>', mostrarperfil, name="mostrarperfil"),
    path('modificarPerfil/<id>', modificarPerfil, name="modificarPerfil"),
    path('edicionProducto/<idProducto>', edicionProducto, name="edicionProducto"),
    path('editarProducto/<idProducto>', editarProducto, name="editarProducto"),

    # API
    path('api/productos/', views_api.listar_productos, name='api_productos'),
    path('api/ventas/<str:username>/', views_api.ventas_por_usuario, name='api_ventas_usuario'),
    path('ventas-api/', views_api.ventas_api_html, name="ventas_api"),
    path('api/clima/', clima_actual, name="api_clima"),
    path('confirmar_pago/', confirmar_pago, name='confirmar_pago'),

    # cerrar sesion 
    path('cerrarsesion/', views.cerrar_sesion, name='cerrar_sesion'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)