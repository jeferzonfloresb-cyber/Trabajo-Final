from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from PIL import Image as PILImage

styles = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=styles['Heading1'], fontSize=14, spaceBefore=10, spaceAfter=6, alignment=TA_CENTER)
H2 = ParagraphStyle('H2', parent=styles['Heading2'], fontSize=11, spaceBefore=8, spaceAfter=4)
BODY = ParagraphStyle('BODY', parent=styles['BodyText'], fontSize=9, leading=12, alignment=TA_JUSTIFY)


def P(t, s=BODY):
    return Paragraph(str(t), s)


def fit(path, maxw=16.0, maxh=21.0):
    w, h = PILImage.open(path).size
    ratio = w / h
    tw = maxw
    th = tw / ratio
    if th > maxh:
        th = maxh
        tw = th * ratio
    return Image(path, width=tw * cm, height=th * cm)


story = []
story.append(P('MAESTRÍA EN INGENIERÍA DE SOFTWARE Y SISTEMAS INFORMÁTICOS', H1))
story.append(P('MÓDULO 3 - DESARROLLO AL LADO DEL CLIENTE Y SERVIDOR WEB', H2))
story.append(Spacer(1, 1.2 * cm))
story.append(P('TRABAJO FINAL', H1))
story.append(P('DESARROLLO DE UNA LANDING PAGE FUNCIONAL', H1))
story.append(Spacer(1, 0.8 * cm))
story.append(P('Sistema: Landing Page "Identidad Digital - Control de Acceso"', H2))
story.append(P('Caso: Control de acceso e identidad digital (emprendimiento/servicio tecnológico)', BODY))
story.append(Spacer(1, 1.0 * cm))
story.append(P('Estudiante: ________________________', BODY))
story.append(P('Fecha: ____ / ____ / 2026', BODY))
story.append(PageBreak())

story.append(P('1. Introducción', H1))
story.append(P('Se desarrolló una Landing Page funcional para presentar un servicio de control de acceso e identidad digital. '
               'El sitio supera el nivel meramente informativo: incorpora interacción con el usuario, procesamiento del lado '
               'del servidor, gestión/consulta de información en una base de datos y comunicación cliente-servidor mediante '
               'peticiones asincrónicas.', BODY))
story.append(Spacer(1, 4))

story.append(P('2. Cumplimiento de requisitos', H1))
req = [
    ['Requisito', 'Cumplimiento'],
    ['Funcional', 'Sí - inicia y opera con PHP 8.3 en 127.0.0.1'],
    ['Diseño claro y coherente', 'Sí - tema oscuro consistente, tipografía y paleta definidas'],
    ['Adaptable a dispositivos', 'Sí - diseño responsive (escritorio y móvil)'],
    ['Comunica su propósito', 'Sí - hero, solución, características y casos de uso'],
    ['Interacción con el usuario', 'Sí - menú móvil y validación de formulario'],
    ['Procesamiento del lado del servidor', 'Sí - PHP 8.3 (endpoint REST)'],
    ['Gestiona/consulta información', 'Sí - SQLite (tabla leads), POST y GET'],
    ['Comunicación cliente-servidor', 'Sí - Fetch + JSON (AJAX)'],
]
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
data = [[Paragraph('<b>Requisito</b>', BODY), Paragraph('<b>Cumplimiento</b>', BODY)]] + \
       [[Paragraph(r[0], BODY), Paragraph(r[1], BODY)] for r in req[1:]]
t = Table(data, colWidths=[5.5 * cm, 11.5 * cm])
t.setStyle(TableStyle([
    ('GRID', (0, 0), (-1, -1), 0.4, colors.grey),
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#dbe4ff')),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('LEFTPADDING', (0, 0), (-1, -1), 4),
    ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ('TOPPADDING', (0, 0), (-1, -1), 3),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
]))
story.append(t)
story.append(PageBreak())

story.append(P('3. Arquitectura y comunicación cliente-servidor', H1))
story.append(P('La aplicación sigue una arquitectura cliente-servidor de tres capas:', BODY))
story.append(P('- Capa de presentación (cliente): HTML5, CSS3 y JavaScript (Fetch API).', BODY))
story.append(P('- Capa de lógica (servidor): PHP 8.3 con clases núcleo Database, Request y Router.', BODY))
story.append(P('- Capa de datos: base de datos SQLite (archivo data/landing.db) gestionada con PDO.', BODY))
story.append(Spacer(1, 4))
story.append(P('Flujo: el usuario completa el formulario; JavaScript valida y envía JSON vía Fetch a api/leads.php; '
               'PHP valida, persiste en SQLite y responde JSON; el cliente muestra el resultado sin recargar la página.', BODY))
story.append(Spacer(1, 6))

story.append(P('4. Estructura del proyecto', H1))
story.append(fit('capturas/01_estructura.png', 16.0, 10.0))
story.append(PageBreak())

story.append(P('5. Demostración de funcionamiento - Escritorio', H1))
story.append(fit('capturas/real_desktop.png', 16.0, 21.0))
story.append(PageBreak())

story.append(P('6. Demostración de funcionamiento - Móvil (responsive)', H1))
story.append(fit('capturas/real_mobile.png', 12.0, 21.0))
story.append(PageBreak())

story.append(P('7. Comunicación cliente-servidor - Respuesta del API', H1))
story.append(P('Evidencia de la respuesta real del endpoint api/leads.php (petición GET), que devuelve en formato JSON '
               'los registros almacenados en la base de datos SQLite.', BODY))
story.append(Spacer(1, 6))
story.append(fit('capturas/real_api.png', 16.0, 10.0))
story.append(Spacer(1, 6))
story.append(P('Petición POST: {"nombre":"Demo","email":"demo@test.com",...} -> {"success":true,"id":"1"}', BODY))
story.append(PageBreak())

story.append(P('8. Código fuente y repositorio', H1))
story.append(P('El código fuente completo se encuentra en el repositorio GitHub:', BODY))
story.append(P('https://github.com/darkpro/MAESTRIA_EN_INGENIERIA_DE_SOFTWARE_Y_SISTEMAS_INFORMATICO', BODY))
story.append(P('Ruta: MODULO_3_DESARROLLO_AL_LADO_DEL_CLIENTE_Y_SERVIDOR_WEB/TRABAJO_FINAL_LANDING_PAGE', BODY))
story.append(Spacer(1, 4))
story.append(P('Archivos principales: public/index.html, public/assets/style.css, public/assets/app.js, '
               'public/api/leads.php, src/core/Database.php, src/core/Request.php, src/core/Router.php, docs/README.md.', BODY))
story.append(Spacer(1, 6))

story.append(P('9. Conclusión', H1))
story.append(P('La Landing Page cumple todos los requisitos del trabajo final: es funcional, responsive, comunica su '
               'propósito, incorpora interacción con el usuario, procesamiento del lado del servidor, gestión de '
               'información en base de datos y comunicación cliente-servidor mediante AJAX/Fetch con respuestas JSON.', BODY))

doc = SimpleDocTemplate('TRABAJO_FINAL_ENTREGABLE.pdf', pagesize=A4,
                        rightMargin=1.5 * cm, leftMargin=1.5 * cm, topMargin=1.5 * cm, bottomMargin=1.5 * cm)
doc.build(story)
print('ok')
