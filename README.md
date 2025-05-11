# HSC - Evaluación Final Transversal (PGY3221)

Proyecto web desarrollado como parte de la **Evaluación Final Transversal** del curso **Programación Web (PGY3221)**. Esta aplicación integra las experiencias previas, incorpora seguridad, API propia, consumo de servicios externos, y fue desplegada exitosamente en Heroku.

---

## 🌐 Enlace a la aplicación desplegada
👉 [https://hsc-etf-demo-bc86b4cdeae4.herokuapp.com/](https://hsc-etf-demo-bc86b4cdeae4.herokuapp.com/)

---

## 🎥 Enlace al video de presentación
👉 [Video en Google Drive](https://drive.google.com/drive/folder/XXXXXXXXXX)  
*(Reemplazar con el enlace real compartido desde tu cuenta institucional)*

---

## 🛠️ Tecnologías utilizadas

- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Backend**: Django 4.2, Django REST Framework
- **Base de Datos**: Oracle (conexión mediante `oracledb`)
- **APIs externas**:  
  - [OpenWeather API](https://openweathermap.org/api) para clima.  
  - [Mindicador.cl](https://mindicador.cl) para el valor del dólar.

---

## ✅ Funcionalidades implementadas

- Carrito de compras con persistencia en sesión
- Seguridad: autenticación por token y control de roles
- Gestión de productos, categorías y ventas
- Panel de administración (Django admin)
- API propia RESTful:  
  - `/api/productos/`  
  - `/api/ventas/<usuario>/`  
  - `/api/categorias/`
- Consumo de 2 servicios externos (clima + dólar)
- Interfaz adaptable a 3 tamaños de pantalla

---

## 📂 Estructura del proyecto

- `/Inicio/` — App principal con vistas, templates y contexto dinámico.
- `/api_hsc/` — App que contiene la API REST propia.
- `/media/` — Archivos multimedia (no incluidos en el repositorio).
- `ScriptFinal.sql` — Script de creación e inserción para la base de datos en Oracle.

---

## 🧪 Instrucciones para ejecución local

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Chiripio/eft_hsc_heroku.git
   cd eft_hsc_heroku


	Crea y activa un entorno virtual:


python3 -m venv venv
source venv/bin/activate

	Instala las dependencias:

 
pip install -r requirements.txt

Configura las variables necesarias (por ejemplo, acceso Oracle si es necesario).


	Ejecuta el servidor:

 python manage.py runserver

Exclusiones importantes
	•	No se incluyen archivos pesados como wallet/, .env, archivos .mp4, ni .sqlite3.
	•	.gitignore correctamente configurado para mantener el repositorio liviano.

 
