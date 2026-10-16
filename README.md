# Trabajo Final - Landing Page Funcional

**Sistema:** Landing Page "Identidad Digital - Control de Acceso"

Trabajo Final del Módulo 3 (Desarrollo al lado del cliente y servidor web).

## Descripción

Landing Page funcional que presenta un servicio de control de acceso e identidad digital.
Supera el nivel informativo al incorporar interacción con el usuario, procesamiento del
lado del servidor, gestión de información en base de datos y comunicación cliente-servidor
mediante AJAX/Fetch.

## Tecnologías

- **Cliente:** HTML5, CSS3, JavaScript ES6 (Fetch API)
- **Servidor:** PHP 8.3 (clases núcleo Database, Request, Router)
- **Datos:** SQLite (PDO)

## Funcionalidades

- Diseño responsive (escritorio y móvil).
- Menú de navegación con toggle en móvil.
- Secciones: hero, solución, características, casos de uso y contacto.
- Formulario con validación en cliente y servidor.
- API REST: `POST /api/leads.php` (crear) y `GET /api/leads.php` (listar).
- Persistencia y consulta de leads en SQLite.
- Comunicación asíncrona con respuestas JSON.

## Ejecución

```bash
cd public
php -S 127.0.0.1:8000
# Abrir http://127.0.0.1:8000
```

## Documentación

Ver [`docs/README.md`](docs/README.md).

## Evidencia

Capturas reales del funcionamiento en [`capturas/`](capturas/):
`real_desktop.png`, `real_mobile.png`, `real_api.png`.

## Entregable PDF

[`TRABAJO_FINAL_ENTREGABLE.pdf`](TRABAJO_FINAL_ENTREGABLE.pdf)
