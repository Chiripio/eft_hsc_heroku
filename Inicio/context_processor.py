import requests
from .models import Usuario

def total_carrito(request):
    total = 0
    if "carrito" in request.session:
        for key, value in request.session["carrito"].items():
            try:
                total += int(value.get("acumulado", 0))
            except:
                pass
    return {"total_carrito": total}

## clima + dolar + usuario (global)
def clima_y_dolar(request):
    usuario = None
    if 'usuario' in request.session:
        try:
            usuario = Usuario.objects.get(username=request.session['usuario'])
        except Usuario.DoesNotExist:
            usuario = None

    contexto = {'clima': None, 'dolar': None, 'usuario': usuario}

    try:
        # Obtener IP pública (evita IP localhost)
        ip = request.META.get('REMOTE_ADDR', '')
        if ip == '127.0.0.1' or ip.startswith('192.168') or ip == '':
            ip = requests.get("https://api64.ipify.org").text

        # Ciudad desde IP
        ciudad = requests.get(f'https://ipapi.co/{ip}/json/', timeout=5).json().get('city', 'Santiago')

        # Datos clima
        api_key = '3aa40bf58c891102b7f62742923f8b68'
        clima_data = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es',
            timeout=5).json()

        contexto['clima'] = {
            'ciudad': ciudad,
            'temperatura': round(clima_data['main']['temp']),
            'descripcion': clima_data['weather'][0]['description']
        }

        # Datos dólar
        dolar_data = requests.get("https://mindicador.cl/api", timeout=5).json()
        contexto['dolar'] = round(dolar_data['dolar']['valor'])

    except Exception as e:
        print(f"[ERROR contexto clima_y_dolar]: {e}")
        contexto['clima'] = {
            'ciudad': 'Santiago',
            'temperatura': 'N/D',
            'descripcion': 'No disponible'
        }
        contexto['dolar'] = 'N/D'

    return contexto