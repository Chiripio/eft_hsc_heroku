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

📂 Estructura clave del proyecto:

Hsc/
├── api_hsc/
│   ├── views.py         # API y consumo de servicio externo
│   ├── serializers.py   # Serialización de modelos
│   ├── urls.py          # Rutas de API y Web
├── templates/
│   └── api_hsc/noticias.html
├── settings.py          # Configuración base + REST + Token
└── .gitignore           # Ignora archivos mayores a 100MB









