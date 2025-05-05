# HSC - Proyecto Semana 8 (PGY3221 - Programación Web)

Este es el proyecto final correspondiente a la **Semana 8** del ramo **Programación Web** del estudiante **Eduardo Guerrero Soto**.

## 📌 Descripción

El sitio web HSC permite a usuarios navegar productos tecnológicos (mouse, teclados, RAM, GPU, etc.), agregar al carrito, ver perfil, y como novedad de esta semana:

- Se ha implementado una **API REST protegida con token**.
- Se consume un **servicio web externo (OpenWeatherMap)** para mostrar el clima en tiempo real.
- El frontend está completamente funcional, conectado a Oracle y animado con estilos personalizados.

## 🛠️ Instalación y uso

1. Clonar el repositorio:

```bash
git clone https://github.com/Chiripio/Hsc_Semana8.git
cd Hsc_Semana8



	2.	Crear entorno virtual y activar:

python3 -m venv venv
source venv/bin/activate

	3.	Instalar dependencias:

pip install -r requirements.txt


	4.	Configurar la conexión a Oracle (usando wallet).
	5.	Correr el servidor:

python manage.py runserver


 Acceso al panel de administración
	•	Usuario: admin
	•	Contraseña: DUoc2025

Entrar en http://127.0.0.1:8000/admin

🧩 API REST (Django REST Framework)

Endpoints disponibles:
	•	GET /api/productos/ → Lista de productos
	•	GET /api/ventas/<usuario>/ → Ventas por usuario
	•	GET /api/clima/ → Clima en tiempo real por IP (OpenWeather)

Token de autenticación
	•	Token generado por usuario registrado (ver en admin).
	•	Agregar a Postman como Header:


Authorization: Token <tu_token>


GET http://127.0.0.1:8000/api/productos/
Authorization: Token TU_TOKEN



Clima animado

El clima se muestra dinámicamente en:
	•	Parte superior derecha del index.html
	•	Página /clima/ con animaciones y fondo que cambia según el tiempo actual detectado por IP.

🧪 Revisión completa

✔️ Conexión Oracle funcionando
✔️ API protegida por Token
✔️ Consumo de API externa (OpenWeather)
✔️ Vistas enlazadas desde el frontend
✔️ Proyecto completo subido a GitHub



📌 Instrucciones del Proyecto HSC

⚙️ Requisitos del sistema

- Python 3.10+
- Oracle Instant Client y `oracledb`
- Django 4.2+
- Bootstrap 5
- Cuenta Oracle con esquema cargado (`ScriptFinal.sql` ejecutado)

🚀 Cómo ejecutar el proyecto

1. Clona este repositorio o descarga el proyecto:
   git clone https://github.com/Chiripio/Hsc_Semana8.git

2. Crea y activa un entorno virtual:
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate

3. Instala las dependencias:
   pip install -r requirements.txt

4. Asegúrate de tener el archivo `wallet` de Oracle si estás usando autenticación con wallet. Colócalo en `/oracle_wallet/` y configura `settings.py` correctamente.

5. Ejecuta el servidor:
   python manage.py runserver

🔑 Credenciales de ejemplo

- Usuario administrador Django:
  - Usuario: admin
  - Contraseña: DUoc2025

- Usuario registrado (app):
  - Usuario: usuario1
  - Contraseña: 123

🔗 Endpoints principales

- Inicio: /
- Carrito: /carrito/usuario/
- API Clima: /api/clima/
- API Ventas: /api/ventas/<usuario>/
- API Productos: /api/productos/

🗂️ Notas adicionales

- Al iniciar sesión, se redirige según el tipo de usuario.
- Si el usuario no está autenticado, se registra como `anonimo` en el carrito.
- El botón "Comprar" simula un pago y limpia el carrito.
- El clima y el dólar se cargan automáticamente usando APIs públicas.


