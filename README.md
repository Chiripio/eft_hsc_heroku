# 🖥️ HSC - Semana 7: API REST + Servicio Web + Token Auth

Repositorio oficial del proyecto correspondiente a la Semana 7 de Programación Web, cuyo objetivo es compartir información mediante una API REST y consumir un servicio web externo, utilizando Django REST Framework.

## ✅ Funcionalidades desarrolladas

### 1. API REST protegida por token
- Endpoint: `/api/categorias/`
- Método: `GET`, `POST`, `PUT`, `DELETE` (según permisos)
- Requiere autenticación por token.

### 2. Autenticación por Token
- Endpoint para generar token: `/api/token/`
- Método: `POST`
- Formato:
  ```json
  {
    "username": "admin",
    "password": "admin123"
  }




3. Servicio Web Externo
	•	Consumo de noticias desde Hacker News con query=technology.
	•	URL: /api/noticias/
	•	Formato amigable en noticias.html, integrando diseño coherente con el resto del sitio.


Prueba de autenticación protegida


# Obtener token

curl -X POST http://127.0.0.1:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{"username": "admin", "password": "admin123"}'

# Usar token para consultar datos
curl -H "Authorization: Token TU_TOKEN_AQUI" http://127.0.0.1:8000/api/categorias/


Tecnologías utilizadas
	•	Python 3 + Django
	•	Django REST Framework
	•	Oracle Database (via oracledb)
	•	Bootstrap para diseño visual
	•	GitHub + Terminal para colaboración

# 🖥️ HSC - Proyecto Semana 8 PGY3221

Este proyecto corresponde al desarrollo de la Semana 8 del curso **Programación Web (PGY3221)** de Duoc UC.

## ✅ Objetivos cumplidos

- ✔️ API REST con Django Rest Framework
- ✔️ Conexión a base de datos Oracle
- ✔️ Autenticación por Token
- ✔️ Consumo de servicio web externo (clima) con visualización en el frontend
- ✔️ Integración completa con Django (modelos, views, templates, URLs)
- ✔️ Subida a GitHub en repositorio exclusivo

## 🌐 Endpoints importantes

- `http://127.0.0.1:8000/api/productos/` → Protegido por Token
- `http://127.0.0.1:8000/api/ventas/<usuario>/` → Protegido por Token
- `http://127.0.0.1:8000/api/clima/` → Servicio de clima (API)
- `http://127.0.0.1:8000/clima/` → Vista visual del clima con animación

## 🔒 Autenticación por Token

Para acceder a los endpoints protegidos, se debe incluir el header:

Puedes obtener el token desde el Django admin o utilizando la API de login.

## 🧪 Pruebas realizadas

- Pruebas de endpoints en Postman
- Verificación visual de interfaz de clima
- Login, carrito, y consumo de datos desde Oracle

## 📁 Estructura relevante

Hsc/
├── Inicio/
│   ├── views.py
│   ├── views_api.py
│   ├── serializers.py
│   ├── templates/
│   │   └── Inicio/
│   │       ├── index.html
│   │       ├── clima.html
│   │       └── ventas_api.html
│   ├── static/
│   │   └── Inicio/img/clima/
│   │       ├── soleado.jpg
│   │       ├── lluvia.jpg
│   │       ├── nublado.jpg
│   │       └── tormenta.jpg
├── manage.py
├── db.sqlite3 (ignorado)
├── wallet/ (ignorado)
└── README.md


## 👨‍💻 Autor

Eduardo Guerrero Soto - Duoc UC  
Curso: PGY3221 – Programación Web  
Semana: 8

---

> Repositorio oficial: [github.com/Chiripio/Hsc_Semana8](https://github.com/Chiripio/Hsc_Semana8)

