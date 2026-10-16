# Trabajo Final - Landing Page Funcional

**Sistema:** Landing Page "Identidad Digital - Control de Acceso"
**Módulo:** 3 - Desarrollo al lado del cliente y servidor web

## 1. Descripción

Landing Page funcional que presenta un servicio de control de acceso e identidad digital. Supera el nivel informativo al incorporar interacción con el usuario, procesamiento del lado del servidor, gestión de información en base de datos y comunicación cliente-servidor mediante AJAX/Fetch.

## 2. Tecnologías

| Capa | Tecnología |
|---|---|
| Presentación (cliente) | HTML5, CSS3, JavaScript ES6 (Fetch API) |
| Lógica (servidor) | PHP 8.3 (clases núcleo Database, Request, Router) |
| Datos | SQLite (archivo `data/landing.db`) mediante PDO |

## 3. Funcionalidades

- Diseño responsive (escritorio y móvil).
- Menú de navegación con toggle en móvil.
- Secciones: hero, solución, características, casos de uso y contacto.
- Formulario de contacto con validación en cliente y en servidor.
- API REST: `POST /api/leads.php` (crear), `GET /api/leads.php` (listar últimos 100).
- Persistencia y consulta de leads en SQLite.
- Comunicación asíncrona cliente-servidor con respuestas JSON.

## 4. Comunicación cliente-servidor

1. El usuario completa el formulario de contacto.
2. JavaScript valida los campos y envía los datos como JSON mediante `fetch()`.
3. `api/leads.php` recibe la petición, valida en servidor, inserta el registro en SQLite y responde en JSON.
4. El cliente muestra el mensaje de éxito o error sin recargar la página.

```
Navegador (JS/Fetch)  --JSON-->  api/leads.php (PHP 8.3)  --PDO-->  SQLite (data/landing.db)
        ^                                 |
        |______________ JSON _____________|
```

## 5. Estructura del proyecto

```text
TRABAJO_FINAL_LANDING_PAGE/
├── public/                 # Document root
│   ├── index.html          # Landing Page
│   ├── .htaccess           # Reescritura (Apache)
│   ├── assets/
│   │   ├── style.css       # Estilos (responsive)
│   │   └── app.js          # Interacción + Fetch (AJAX)
│   ├── api/leads.php       # Endpoint REST
│   └── core/               # Database.php, Request.php, Router.php
├── src/
│   ├── core/               # Clases núcleo
│   └── api/leads.php       # Código fuente del endpoint
├── data/                   # landing.db (creado automáticamente)
├── docs/                   # Documentación
├── capturas/               # Evidencia de funcionamiento
└── generar_pdf_final.py    # Generación del PDF entregable
```

## 6. Ejecución

```bash
cd TRABAJO_FINAL_LANDING_PAGE
php -S 127.0.0.1:8000 -t public
```

Abrir en el navegador: `http://127.0.0.1:8000`

> Requisito: extensión `pdo_sqlite` habilitada en PHP.

## 7. API

| Método | Ruta | Descripción |
|---|---|---|
| POST | `/api/leads.php` | Crea un lead. Body JSON: `{nombre, email, telefono, interes, mensaje}`. Devuelve `{"success":true,"id":"N"}`. |
| GET | `/api/leads.php` | Lista los últimos 100 leads en JSON. |

## 7.1. Esquema de la base de datos

```sql
CREATE TABLE leads (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre     TEXT NOT NULL,
  email      TEXT NOT NULL,
  telefono   TEXT,
  interes    TEXT,
  mensaje    TEXT,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
```

## 7. Ejemplo de uso del API

```bash
curl -X POST http://127.0.0.1:8000/api/leads.php \
  -H "Content-Type: application/json" \
  -d '{"nombre":"Demo","email":"demo@test.com"}'
# -> {"success":true,"id":"1"}
```

## 8. Evidencia de funcionamiento

Capturas reales en `capturas/`:

- `real_desktop.png` - Landing en escritorio.
- `real_mobile.png` - Landing en móvil (responsive).
- `real_api.png` - Respuesta JSON del API.
- `01_estructura.png` - Estructura del proyecto.

## 9. Repositorio

https://github.com/jeferzonfloresb-cyber/Trabajo-Final
