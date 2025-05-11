from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Usuario,Direccion,Comuna,Region,TipoUsuario, Producto, Marca,Categoria,TipoProd,Marca
from django.contrib import messages
from .Carrito import Carrito
import requests
from django.http import JsonResponse



# Create your views here.
def inicio(request):
    try:
        ip = request.META.get('REMOTE_ADDR', '')
        if ip == '127.0.0.1' or ip.startswith('192.168') or ip == '':
            ip = requests.get("https://api64.ipify.org").text

        location_url = f'https://ipapi.co/{ip}/json/'
        location_response = requests.get(location_url, timeout=5).json()
        ciudad = location_response.get('city', 'Santiago')

        api_key = '3aa40bf58c891102b7f62742923f8b68'
        clima_url = f'https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es'
        clima_response = requests.get(clima_url, timeout=5).json()

        descripcion = clima_response['weather'][0]['description']
        temperatura = clima_response['main']['temp']
        icono = clima_response['weather'][0]['icon']

        clima = {
            'ciudad': ciudad,
            'descripcion': descripcion,
            'temperatura': round(temperatura),
            'icono': icono
        }

        # Obtener valor del dólar desde mindicador.cl
        dolar = None
        try:
            response = requests.get("https://mindicador.cl/api", timeout=5)
            data = response.json()
            dolar = round(data['dolar']['valor'])
        except:
            dolar = None

        usuario = None
        if 'usuario' in request.session:
            try:
                usuario = Usuario.objects.get(username=request.session['usuario'])
            except Usuario.DoesNotExist:
                usuario = None

        return render(request, 'Inicio/index.html', {
            'clima': clima,
            'usuario': usuario,
            'dolar': dolar,
            'ver_clima_url': reverse('ver_clima')
        })

    except Exception as e:
        return render(request, 'Inicio/index.html', {
            'clima': None,
            'error': str(e),
            'usuario': None,
            'dolar': None
        })



def inicioadmin(request):

    return render(request,'Inicio/index_admin.html') 
def vistamod(request):
    
    return render(request,'Inicio/modificar_producto.html')


def addprod (request):
    tipoProd = TipoProd.objects.all()
    marca = Marca.objects.all()
    contexto = {"tipoProd":tipoProd,"Marca":marca}

    return render (request,'Inicio/agregar_producto.html',contexto)   

def iniciar(request):

    return render(request,'Inicio/inicio_sesion.html')

def menuadmin(request):

    return render(request,'Inicio/dashboard-admin.html')

def carrito(request, id):
    usuario = None
    if 'usuario' in request.session:
        try:
            usuario = Usuario.objects.get(username=request.session['usuario'])
        except Usuario.DoesNotExist:
            usuario = None

    # Obtener valor del dólar desde la API del Mindicador
    valor_dolar = None
    try:
        response = requests.get("https://mindicador.cl/api", timeout=5)
        data = response.json()
        valor_dolar = data['dolar']['valor']
    except Exception as e:
        valor_dolar = None

    contexto = {
        "usuario": usuario,
        "valor_dolar": valor_dolar,
    }
    return render(request, 'Inicio/carrito.html', contexto)

def perfilusuario(request,id):
    usuario = Usuario.objects.get(username=id)
    contexto = {"usuario":usuario}
    
    return render(request,'Inicio/perfil-user.html',contexto)



def mostrarperfil(request,id):
    usuario = Usuario.objects.get(username=id)
    direccion = Direccion.objects.get(usuario=id)
    region = Region.objects.all()
    comuna = Comuna.objects.all()
    contexto = {"usuario":usuario, "direccion" : direccion,"region" : region,"comuna" : comuna}
    return render(request, 'Inicio/perfil_usuario.html',contexto)    

def modificarPerfil(request,id):
    usuario = Usuario.objects.get(username=id)
    contexto = {"usuario":usuario}
    usuario.username= request.POST.get('username')
    usuario.nombre = request.POST.get('nomusu')
    usuario.apellido = request.POST.get('apepusu')
    usuario.email = request.POST.get('mailusu')
    usuario.save()
    messages.success(request, '¡Perfil modificado correctamente!')
    return render (request,'Inicio/perfil-user.html',contexto)







# -------------------- PRODUCTOS --------------------

# ----- Vistas para productos ANÓNIMO -----
def mostrarMicAnonimo(request):
    micros = Producto.objects.filter(tipoprod=1)
    return render(request, "Inicio/microfonos.html", {"mic": micros})

def mostrarTecladoAnonimo(request):
    teclados = Producto.objects.filter(tipoprod=2)
    return render(request, "Inicio/teclados.html", {"teclado": teclados})

def mostrarMouseAnonimo(request):
    mouses = Producto.objects.filter(tipoprod=5)
    return render(request, "Inicio/mouses.html", {"mouse": mouses})

def mostrarGraficaAnonimo(request):
    graficas = Producto.objects.filter(tipoprod=3)
    return render(request, "Inicio/graficas.html", {"grafica": graficas})

def mostrarRamAnonimo(request):
    rams = Producto.objects.filter(tipoprod=4)
    return render(request, "Inicio/rams.html", {"ram": rams})

def mostrarProcesadorAnonimo(request):
    procesadores = Producto.objects.filter(tipoprod=6)
    return render(request, "Inicio/procesadores.html", {"procesador": procesadores})
# MICROFONOS
def mostrarMic(request,id):
    micros = Producto.objects.filter(tipoprod=1)
    usuario = None
    if id != "anonimo":
        try:
            usuario = Usuario.objects.get(username=id)
        except Usuario.DoesNotExist:
            usuario = None
    contexto = {"mic": micros,"usuario":usuario}
    return render(request, "Inicio/microfonos.html",contexto)

def micadmin (request,id):
    micros = Producto.objects.filter(tipoprod=1)
    usuario = None
    if id != "anonimo":
        try:
            usuario = Usuario.objects.get(username=id)
        except Usuario.DoesNotExist:
            usuario = None
    contexto = {"mic": micros,"usuario":usuario}
    return render (request,'Inicio/micadmin.html',contexto) 
  
def micro(request,idmic,usuario):
    productos = Producto.objects.get(idProducto = idmic)
    try:
        username = Usuario.objects.get(username=usuario)
    except Usuario.DoesNotExist:
        username = None
    contexto ={"prod": productos,"usuario":username} 
    return render(request, "Inicio/mic1.html",contexto)    



# TECLADOS
def mostrarTeclado(request, id):
    teclados = Producto.objects.filter(tipoprod=2)
    usuario = None
    if id != "anonimo":
        try:
            usuario = Usuario.objects.get(username=id)
        except Usuario.DoesNotExist:
            usuario = None
    contexto= {"teclado": teclados,"usuario":usuario}
    return render(request, "Inicio/teclados.html",contexto)

def tecladoadmin (request,id):
    teclados = Producto.objects.filter(tipoprod=2)
    usuario = None
    if id != "anonimo":
        try:
            usuario = Usuario.objects.get(username=id)
        except Usuario.DoesNotExist:
            usuario = None
    contexto = {"teclado": teclados,"usuario":usuario}
    return render (request,'Inicio/tecladoadmin.html',contexto) 

def teclado(request,idk, usuario):
    productos = Producto.objects.get(idProducto = idk)
    try:
        username = Usuario.objects.get(username=usuario)
    except Usuario.DoesNotExist:
        username = None
    contexto = {"prod": productos,"usuario":username}
    return render(request, "Inicio/mic1.html",contexto)

# MOUSES
def mostrarMouse(request,id):
    mouses = Producto.objects.filter(tipoprod=5)
    usuario = None
    if id != "anonimo":
        try:
            usuario = Usuario.objects.get(username=id)
        except Usuario.DoesNotExist:
            usuario = None
    contexto = {"mouse": mouses,"usuario":usuario}
    return render(request, "Inicio/mouses.html",contexto)

def mouseAdmin (request,id):
    mouses= Producto.objects.filter(tipoprod=5)
    usuario = None
    if id != "anonimo":
        try:
            usuario = Usuario.objects.get(username=id)
        except Usuario.DoesNotExist:
            usuario = None
    contexto = {"mouse": mouses,"usuario":usuario}
    return render (request,'Inicio/mouseAdmin.html',contexto) 
    
def mouse(request,idm,usuario):
    try:
        usuario = Usuario.objects.get(username=usuario)
    except Usuario.DoesNotExist:
        usuario = None
    productos = Producto.objects.get(idProducto = idm)
    contexto = {"prod": productos,"usuario":usuario}
    return render(request, "Inicio/mic1.html",contexto)    

# GRAFICAS
def mostrarGrafica(request,id):
    graficas = Producto.objects.filter(tipoprod=3)
    usuario = None
    if id != "anonimo":
        try:
            usuario = Usuario.objects.get(username=id)
        except Usuario.DoesNotExist:
            usuario = None
    contexto = {"grafica": graficas,"usuario":usuario}
    return render(request, "Inicio/graficas.html",contexto)

def graficaAdmin (request,id):
    graficas= Producto.objects.filter(tipoprod=3)
    usuario = None
    if id != "anonimo":
        try:
            usuario = Usuario.objects.get(username=id)
        except Usuario.DoesNotExist:
            usuario = None
    contexto ={"grafica": graficas,"usuario":usuario}
    return render (request,'Inicio/graficaAdmin.html',contexto) 
    
def grafica(request,idg,usuario):
    productos = Producto.objects.get(idProducto = idg)
    try:
        usuario = Usuario.objects.get(username=usuario)
    except Usuario.DoesNotExist:
        usuario = None
    contexto = {"prod": productos,"usuario":usuario}
    return render(request, "Inicio/mic1.html",contexto)    

# PROCESADORES
def mostrarProcesador(request,id):
    procesadores = Producto.objects.filter(tipoprod=6)
    usuario = None
    if id != "anonimo":
        try:
            usuario = Usuario.objects.get(username=id)
        except Usuario.DoesNotExist:
            usuario = None
    contexto = {"procesador": procesadores,"usuario":usuario}
    return render(request, "Inicio/procesadores.html",contexto)

def procesadorAdmin (request,id):
    procesadores= Producto.objects.filter(tipoprod=6)
    usuario = None
    if id != "anonimo":
        try:
            usuario = Usuario.objects.get(username=id)
        except Usuario.DoesNotExist:
            usuario = None
    contexto = {"procesador": procesadores,"usuario":usuario}
    return render (request,'Inicio/procesadorAdmin.html',contexto) 
    
def procesador(request,idp,usuario):
    productos = Producto.objects.get(idProducto = idp)
    try:
        usuario = Usuario.objects.get(username=usuario)
    except Usuario.DoesNotExist:
        usuario = None
    contexto = {"prod": productos,"usuario":usuario}
    return render(request, "Inicio/mic1.html",contexto)  

# RAMS
def mostrarRam(request,id):
    rams = Producto.objects.filter(tipoprod=4)
    usuario = None
    if id != "anonimo":
        try:
            usuario = Usuario.objects.get(username=id)
        except Usuario.DoesNotExist:
            usuario = None
    contexto = {"ram": rams,"usuario":usuario}
    return render(request, "Inicio/rams.html",contexto)

def ramAdmin (request,id):
    rams= Producto.objects.filter(tipoprod=4)
    usuario = None
    if id != "anonimo":
        try:
            usuario = Usuario.objects.get(username=id)
        except Usuario.DoesNotExist:
            usuario = None
    contexto = {"ram": rams,"usuario":usuario}
    return render (request,'Inicio/ramAdmin.html',contexto) 
    
def ram(request,idr,usuario):
    productos = Producto.objects.get(idProducto = idr)
    try:
        usuario = Usuario.objects.get(username=usuario)
    except Usuario.DoesNotExist:
        usuario = None
    contexto = {"prod": productos,"usuario":usuario}
    return render(request, "Inicio/mic1.html",contexto )    











def registrarse(request):
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    contexto = {"comunas_m": comunas,"regiones_m": regiones}
    return render(request,"Inicio/registrarse.html",contexto)

def registrar_m (request):
    user = request.POST['usuario']
    contra = request.POST['contra']
    correo = request.POST['email']
    region = request.POST['region']
    direccion = request.POST['direccion']
    comuna = request.POST['comuna']
    nombree = request.POST['nombre']
    apellido = request.POST['apellido']
    
    comuna2 = Comuna.objects.get(idComuna = comuna)
    region2 = Region.objects.get(idRegion = region)
    tipousuario2 = TipoUsuario.objects.get(idTipoUsuario = 2)
    existe = None
    try:
        existe = Usuario.objects.get(username=user)
        messages.error(request,'El usuario ya existe')
        return redirect ('registrarse')
    except:
        Usuario.objects.create(username = user , contrasennia = contra, nombre = nombree, apellido = apellido, email = correo,tipousuario = tipousuario2)
        x = Usuario.objects.get(username = user)
        # Check if user already has a Direccion before creating
        if Direccion.objects.filter(usuario=x).exists():
            messages.error(request, 'El usuario ya tiene una dirección asociada.')
            return redirect('registrarse')
        Direccion.objects.create(descripcionDir = direccion, usuario = x,region = region2)
        return redirect ('iniciar')

        
def iniciar_sesion(request):
    if request.method == 'POST':
        usuario1 = request.POST.get('usuario')
        contra1 = request.POST.get('contra')
        if usuario1 and contra1:
            try:
                usuario2 = Usuario.objects.get(username=usuario1, contrasennia=contra1)
                if usuario2.tipousuario.idTipoUsuario == 1:
                    return redirect('menu_admin')
                else:
                    request.session['usuario'] = usuario2.username
                    return redirect('inicio')
            except Usuario.DoesNotExist:
                messages.error(request, 'El usuario o la contraseña son incorrectos')
                return render(request, 'Inicio/inicio_sesion.html')
        else:
            messages.error(request, 'Debe ingresar usuario y contraseña')
            return render(request, 'Inicio/inicio_sesion.html')
    else:
        return render(request, 'Inicio/inicio_sesion.html')
    
 






    
def newProd(request):
    nombre = request.POST['nomprod']
    tipoProd = request.POST['tipoprod']
    marca = request.POST['marcaprod']
    stock = request.POST['stockprod']
    imagen = request.FILES['imgprod']
    desc = request.POST['descprod']
    precio = request.POST['precio']
    
    idProd2 = TipoProd.objects.get(idTiporod = tipoProd)
    marca2 = Marca.objects.get(idMarca = marca)
    existe = None
    try:
        existe = Producto.objects.get(nombreProducto = nombre)
        messages.error(request,'El producto ya existe')
        return redirect ('addprod')
    except:
        Producto.objects.create(nombreProducto = nombre,precioProducto = precio,especificacionProd = desc,stockProd =stock,imagenProd = imagen,tipoprod = idProd2,marca = marca2)
        return redirect ('menu_admin')
    

def eliminarProducto(request, idProducto):
    producto= Producto.objects.get(idProducto=idProducto)
    producto.delete()

    messages.success(request, '¡Producto Eliminado!')

    return redirect('indexadmin')


 
def edicionProducto(request, idProducto):
    tipoProd = TipoProd.objects.all()
    marca = Marca.objects.all()
    producto = Producto.objects.get(idProducto=idProducto)

    return render(request,'Inicio/edicionProducto.html', {"producto": producto, "tipoProd":tipoProd,"Marca":marca})

def editarProducto(request,idProducto):
    producto = Producto.objects.get(idProducto=idProducto)
    tiprod1 =request.POST['tipoprod'] 
    tipoprod2 = TipoProd.objects.get(idTiporod =tiprod1)
    marca1 = request.POST['marcaprod']
    marca2 = Marca.objects.get(idMarca = marca1)
    if (request.FILES.get("imgprod")):
        fotoprod =  request.FILES['imgprod']
        producto.imagenProd = fotoprod
    producto.nombreProducto = request.POST.get('nomprod')
    producto.tipoprod = tipoprod2
    producto.marca = marca2
    producto.stockProd = request.POST.get('stockprod')
    producto.precioProducto = request.POST.get('precio')
    producto.especificacionProd = request.POST.get('descprod')
    producto.save()
    messages.success(request, '¡Producto Modificado!')
    return redirect('indexadmin')
    




def agregar_producto(request, idProducto):
    carrito = Carrito(request)
    if 'usuario' not in request.session or request.session['usuario'] == 'anonimo':
        if request.user.is_authenticated:
            request.session['usuario'] = request.user.username
        else:
            request.session['usuario'] = 'anonimo'
    producto = Producto.objects.get(idProducto=idProducto)
    carrito.agregar(producto)
    usuario = request.session.get('usuario', 'anonimo')
    return redirect('carrito', id=usuario)

def eliminar_producto(request, idProducto):
    carrito = Carrito(request)
    if 'usuario' not in request.session or request.session['usuario'] == 'anonimo':
        if request.user.is_authenticated:
            request.session['usuario'] = request.user.username
        else:
            request.session['usuario'] = 'anonimo'
    producto = Producto.objects.get(idProducto=idProducto)
    carrito.eliminar(producto)
    usuario = request.session.get('usuario', 'anonimo')
    return redirect('carrito', id=usuario)

def restar_producto(request, idProducto):
    carrito = Carrito(request)
    if 'usuario' not in request.session or request.session['usuario'] == 'anonimo':
        if request.user.is_authenticated:
            request.session['usuario'] = request.user.username
        else:
            request.session['usuario'] = 'anonimo'
    producto = Producto.objects.get(idProducto=idProducto)
    carrito.restar(producto)
    usuario = request.session.get('usuario', 'anonimo')
    return redirect('carrito', id=usuario)

def limpiar_producto(request):
    carrito = Carrito(request)
    if 'usuario' not in request.session or request.session['usuario'] == 'anonimo':
        if request.user.is_authenticated:
            request.session['usuario'] = request.user.username
        else:
            request.session['usuario'] = 'anonimo'
    carrito.limpiar()
    usuario = request.session.get('usuario', 'anonimo')
    return redirect('carrito', id=usuario)




def clima_actual(request):
    ciudad = "Santiago"
    api_key = "3aa40bf58c891102b7f62742923f8b68"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&lang=es&units=metric"

    try:
        respuesta = requests.get(url)
        datos = respuesta.json()

        clima = {
            'city': ciudad,
            'country': datos['sys']['country'],
            'temperature': datos['main']['temp'],
            'weather': datos['weather'][0]['description']
        }
        return JsonResponse(clima)
    except Exception as e:
        return JsonResponse({'error': 'No se pudo obtener el clima', 'detalle': str(e)}, status=500)




def ver_clima(request):
    usuario = None
    if 'usuario' in request.session:
        try:
            usuario = Usuario.objects.get(username=request.session['usuario'])
        except Usuario.DoesNotExist:
            usuario = None

    # Obtener clima y dólar desde el context processor directamente
    from .context_processor import clima_y_dolar
    contexto = clima_y_dolar(request)
    contexto["usuario"] = usuario

    # Obtener pronóstico extendido para 5 días (filtrado por 12:00 cada día)
    api_key = "3aa40bf58c891102b7f62742923f8b68"
    clima_data = contexto.get("clima")
    ciudad = clima_data.get("ciudad", "Santiago") if clima_data else "Santiago"
    url_forecast = f"https://api.openweathermap.org/data/2.5/forecast?q={ciudad}&appid={api_key}&units=metric&lang=es"

    try:
        respuesta_forecast = requests.get(url_forecast, timeout=5)
        data_forecast = respuesta_forecast.json()
        pronostico_raw = data_forecast.get('list', [])

        pronostico_filtrado = []
        fechas_agregadas = set()

        for item in pronostico_raw:
            fecha_hora = item['dt_txt']
            if "12:00:00" in fecha_hora:
                fecha = fecha_hora.split(" ")[0]
                if fecha not in fechas_agregadas:
                    dia = {
                        'fecha': fecha,
                        'temperatura': round(item['main']['temp']),
                        'descripcion': item['weather'][0]['description'],
                        'icon': item['weather'][0]['icon']
                    }
                    pronostico_filtrado.append(dia)
                    fechas_agregadas.add(fecha)
                    if len(pronostico_filtrado) >= 5:
                        break

        contexto["pronostico"] = pronostico_filtrado
    except Exception as e:
        print(f"[ERROR al obtener pronóstico]: {e}")
        contexto["pronostico"] = []

    return render(request, 'Inicio/clima.html', contexto)


from django.contrib import messages

def confirmar_pago(request):
    if 'usuario' not in request.session or request.session['usuario'] == 'anonimo':
        messages.error(request, "Debes iniciar sesión para finalizar la compra.")
        return redirect('iniciar')

    carrito = request.session.get('carrito', {})
    if not carrito:
        messages.warning(request, "Tu carrito está vacío. Agrega productos antes de pagar.")
        return redirect('carrito', id=request.session.get('usuario', 'anonimo'))

    total = sum(item['acumulado'] for item in carrito.values())

    # Simulación de compra
    messages.success(request, f"¡Gracias por tu compra! Total pagado: ${total}")

    # Vaciar carrito
    request.session['carrito'] = {}

    return render(request, 'Inicio/confirmar_pago.html', {'total_pagado': total})


# -------------------- CERRAR SESION --------------------
def cerrar_sesion(request):
    request.session.flush()  # Borra toda la sesión, incluyendo 'usuario' y 'carrito'
    return redirect('inicio')
