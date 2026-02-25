# =============================================================================
# EJEMPLOS COMPLETOS DE PLATYPUS — ReportLab
# Genera un único PDF con un ejemplo de cada característica de Platypus
# No requiere archivos externos (imágenes ni base de datos)
# =============================================================================

from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Table, TableStyle,
    Spacer, Image, Flowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen.canvas import Color

from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart, HorizontalBarChart
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.charts.piecharts import Pie, Pie3d
from reportlab.graphics.charts.legends import Legend, LineLegend
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.widgets.markers import makeMarker


# =============================================================================
# DATOS DE EJEMPLO (reutilizados en todo el archivo)
# =============================================================================

PRODUCTOS   = ["Memoria RAM", "Portátil Dell", "Monitor HP", "Torre Macintosh", "Ratón LG"]
UNIDADES    = [81, 71, 51, 27, 25]
FACTURACION = [324.08, 3648.39, 429.39, 3239.76, 632.67]

MESES      = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
MAXIMAS    = [15, 16, 20, 25, 27, 31, 35, 38, 30, 25, 20, 18]
MINIMAS    = [-3, -4, -1,  4,  6,  9, 12, 15, 16, 10,  2, -2]

CLIENTES   = ["Ana García", "Luis Pérez", "Marta López", "Carlos Ruiz", "Elena Vidal"]
FACTURAS_N = [12, 9, 7, 6, 4]
TOTAL_CLI  = [5800.0, 4200.0, 3100.0, 2700.0, 1500.0]


# =============================================================================
# SECCIÓN 1 — PÁRRAFOS Y ESTILOS
# =============================================================================

def seccion_parrafos(hoja):
    """Muestra todos los estilos de párrafo y cómo modificarlos."""
    elementos = []

    # --- Título de sección ---
    elementos.append(Paragraph("1. PÁRRAFOS Y ESTILOS", hoja["Heading1"]))
    elementos.append(Spacer(0, 10))

    # Estilos predefinidos
    elementos.append(Paragraph("Estilo Title",    hoja["Title"]))
    elementos.append(Paragraph("Estilo Heading1", hoja["Heading1"]))
    elementos.append(Paragraph("Estilo Heading2", hoja["Heading2"]))
    elementos.append(Paragraph("Estilo Heading3", hoja["Heading3"]))
    elementos.append(Paragraph("Estilo Heading4", hoja["Heading4"]))
    elementos.append(Paragraph("Estilo BodyText — " + "texto de cuerpo " * 10, hoja["BodyText"]))
    elementos.append(Paragraph("Estilo Normal",   hoja["Normal"]))
    elementos.append(Spacer(0, 10))

    # Estilo con propiedades modificadas
    est_custom = hoja["Heading2"]
    est_custom.fontSize       = 14
    est_custom.fontName       = "Helvetica-BoldOblique"
    est_custom.textColor      = colors.darkblue
    est_custom.alignment      = 1          # 0=izq, 1=centro, 2=dcha
    est_custom.pageBreakBefore = 0
    est_custom.keepWithNext    = 0
    elementos.append(Paragraph("Heading2 personalizado: centrado, azul oscuro, cursiva", est_custom))
    elementos.append(Spacer(0, 5))

    # Estilo con fondo
    est_fondo = hoja["BodyText"]
    est_fondo.backColor  = colors.lightcyan
    est_fondo.fontSize   = 11
    est_fondo.textColor  = colors.darkgreen
    est_fondo.alignment  = 0
    elementos.append(Paragraph("BodyText con backColor=lightcyan y textColor=darkgreen", est_fondo))
    elementos.append(Spacer(0, 20))

    return elementos


# =============================================================================
# SECCIÓN 2 — SPACER
# =============================================================================

def seccion_spacer(hoja):
    elementos = []
    elementos.append(Paragraph("2. SPACER", hoja["Heading1"]))
    elementos.append(Paragraph("↕ Spacer(0, 10) ↕", hoja["BodyText"]))
    elementos.append(Spacer(0, 10))
    elementos.append(Paragraph("↕ Spacer(0, 40) ↕", hoja["BodyText"]))
    elementos.append(Spacer(0, 40))
    elementos.append(Paragraph("Fin del bloque de spacers.", hoja["BodyText"]))
    elementos.append(Spacer(0, 20))
    return elementos


# =============================================================================
# SECCIÓN 3 — TABLA BÁSICA CON TODOS LOS COMANDOS DE ESTILO
# =============================================================================

def seccion_tabla_basica(hoja):
    elementos = []
    elementos.append(Paragraph("3. TABLA BÁSICA — COMANDOS DE ESTILO", hoja["Heading1"]))
    elementos.append(Spacer(0, 8))

    datos = [
        ["Posición", "Producto",          "Uds. Vendidas", "Facturación"],
        ["1",        "Memoria RAM DDR",   "81",            "324.08€"],
        ["2",        "Portátil Dell",     "71",           "3648.39€"],
        ["3",        "Monitor HP 24\"",   "51",            "429.39€"],
        ["4",        "Torre Macintosh",   "27",           "3239.76€"],
        ["5",        "Ratón LG",          "25",            "632.67€"],
    ]

    estilo = [
        # Fondo y texto de cabecera
        ("BACKGROUND", (0, 0), (-1, 0),  colors.darkblue),
        ("TEXTCOLOR",  (0, 0), (-1, 0),  colors.white),
        # Fuente cabecera
        ("FONT",       (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",   (0, 0), (-1, 0),  10),
        # Rejilla completa
        ("GRID",       (0, 0), (-1, -1), 1,   colors.black),
        # Alineación general centrada
        ("ALIGN",      (0, 0), (-1, -1), "CENTER"),
        # Columna "Producto" a la izquierda
        ("ALIGN",      (1, 1), (1, -1),  "LEFT"),
        # Columna "Facturación" a la derecha
        ("ALIGN",      (-1, 1), (-1, -1), "RIGHT"),
        # Alineación vertical centrada
        ("VALIGN",     (0, 0), (-1, -1), "MIDDLE"),
        # Padding
        ("LEFTPADDING",  (1, 1), (1, -1), 6),
        ("RIGHTPADDING", (-1, 1), (-1, -1), 6),
    ]

    tabla = Table(datos, colWidths=[55, 160, 90, 80])
    tabla.setStyle(estilo)
    elementos.append(tabla)
    elementos.append(Spacer(0, 20))
    return elementos


# =============================================================================
# SECCIÓN 4 — TABLA CON FILAS ALTERNAS (BUCLE DINÁMICO)
# =============================================================================

def seccion_tabla_alternas(hoja):
    elementos = []
    elementos.append(Paragraph("4. TABLA — FILAS ALTERNAS CON BUCLE", hoja["Heading1"]))
    elementos.append(Spacer(0, 8))

    datos = [["Posición", "Producto", "Uds.", "Facturación"]]
    for i in range(len(PRODUCTOS)):
        datos.append([i + 1, PRODUCTOS[i], UNIDADES[i], "%0.2f€" % FACTURACION[i]])

    estilo = [
        ("BACKGROUND", (0, 0), (-1, 0),  colors.brown),
        ("TEXTCOLOR",  (0, 0), (-1, 0),  colors.white),
        ("GRID",       (0, 0), (-1, -1), 1, colors.black),
        ("ALIGN",      (0, 0), (-1, -1), "CENTER"),
        ("ALIGN",      (1, 1), (1, -1),  "LEFT"),
    ]

    # Filas pares (índice 2, 4, 6...) en gris claro
    for i in range(2, len(datos), 2):
        estilo.append(("BACKGROUND", (0, i), (-1, i), colors.lightgrey))

    tabla = Table(datos, colWidths=[55, 175, 80, 80])
    tabla.setStyle(estilo)
    elementos.append(tabla)
    elementos.append(Spacer(0, 20))
    return elementos


# =============================================================================
# SECCIÓN 5 — TABLA CON ESTILOS CONDICIONALES POR VALOR
# =============================================================================

def seccion_tabla_condicional(hoja):
    elementos = []
    elementos.append(Paragraph("5. TABLA — ESTILOS CONDICIONALES POR VALOR", hoja["Heading1"]))
    elementos.append(Spacer(0, 8))

    temperaturas = [
        ["",         "Ene", "Feb", "Mar", "Abr", "May", "Jun",
                     "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
        ["Máximas",  15, 16, 20, 25, 27, 31, 35, 38, 30, 25, 20, 18],
        ["Mínimas",  -3, -4, -1,  4,  6,  9, 12, 15, 16, 10,  2, -2],
    ]

    estilo = [
        ("TEXTCOLOR",  (0, 0), (-1, 0),  colors.grey),
        ("TEXTCOLOR",  (0, 1), (0, -1),  colors.grey),
        ("BOX",        (1, 1), (-1, -1), 1.5, colors.grey),
        ("INNERGRID",  (1, 1), (-1, -1), 0.5, colors.white),
    ]

    for i, fila in enumerate(temperaturas):
        for j, valor in enumerate(fila):
            if type(valor) == int:
                estilo.append(("TEXTCOLOR", (j, i), (j, i), colors.black))
                if valor > 30:
                    estilo.append(("BACKGROUND", (j, i), (j, i), colors.red))
                elif 20 < valor <= 30:
                    estilo.append(("BACKGROUND", (j, i), (j, i), colors.orange))
                elif 10 < valor <= 20:
                    estilo.append(("BACKGROUND", (j, i), (j, i), colors.lightpink))
                elif 0 < valor <= 10:
                    estilo.append(("BACKGROUND", (j, i), (j, i), colors.lightblue))
                else:
                    estilo.append(("TEXTCOLOR",  (j, i), (j, i), colors.blue))
                    estilo.append(("BACKGROUND", (j, i), (j, i), colors.lightgrey))

    tabla = Table(data=temperaturas)
    tabla.setStyle(estilo)
    elementos.append(tabla)
    elementos.append(Spacer(0, 20))
    return elementos


# =============================================================================
# SECCIÓN 6 — TABLA CON CELDAS COMBINADAS (SPAN)
# =============================================================================

def seccion_tabla_span(hoja):
    elementos = []
    elementos.append(Paragraph("6. TABLA — CELDAS COMBINADAS (SPAN)", hoja["Heading1"]))
    elementos.append(Spacer(0, 8))

    datos = [
        # Las celdas del área del SPAN deben estar en blanco ""
        ["TÍTULO COMBINADO (0,0)→(1,0)", "",      "Col 2", "Col 3"],
        ["Fila 1 A", "Fila 1 B",                  "Fila 1 C", "Fila 1 D"],
        ["Fila 2 A", "Fila 2 B", "COMBINADO\nDer", ""       ],
        ["Fila 3 A", "Fila 3 B",                  "",        ""       ],
    ]

    estilo = [
        ("GRID",       (0, 0), (-1, -1), 1,    colors.grey),
        # SPAN fila 0: columnas 0 y 1 fusionadas
        ("SPAN",       (0, 0), (1, 0)),
        ("BACKGROUND", (0, 0), (1, 0),         colors.lavender),
        ("ALIGN",      (0, 0), (1, 0),         "CENTER"),
        # SPAN esquina inferior derecha: cols 2-3, filas 2-3
        ("SPAN",       (2, 2), (3, 3)),
        ("BACKGROUND", (2, 2), (3, 3),         colors.lightblue),
        ("ALIGN",      (2, 2), (3, 3),         "CENTER"),
        ("VALIGN",     (2, 2), (3, 3),         "MIDDLE"),
    ]

    tabla = Table(data=datos, colWidths=[130, 100, 100, 70])
    tabla.setStyle(estilo)
    elementos.append(tabla)
    elementos.append(Spacer(0, 20))
    return elementos


# =============================================================================
# SECCIÓN 7 — TABLAS ANIDADAS (TABLA DENTRO DE TABLA)
# =============================================================================

def seccion_tabla_anidada(hoja):
    elementos = []
    elementos.append(Paragraph("7. TABLAS ANIDADAS", hoja["Heading1"]))
    elementos.append(Spacer(0, 8))

    # Tabla interior izquierda: método de pago
    tab_izq = Table([["Método de pago:", ""], ["", ""]])
    tab_izq.setStyle([
        ("BOX",          (0, 0), (1, 1),  0.5, colors.black),
        ("FONTSIZE",     (0, 0), (0, 0),  8),
        ("RIGHTPADDING", (0, 0), (0, 1),  50),
        ("BOTTOMPADDING",(0, 0), (1, 1),  10),
    ])

    # Tabla interior derecha: totales
    tab_der = Table([
        ["Importe neto",      ""],
        ["+ IVA (21%)",       ""],
        ["- IRPF (15%)",      ""],
        ["TOTAL",             "385 €"],
    ], hAlign="LEFT")
    tab_der.setStyle([
        ("INNERGRID",  (0, 0), (1, 3),  0.5, colors.black),
        ("LINEABOVE",  (0, 3), (1, 3),  1.5, colors.black),
        ("BOX",        (0, 0), (1, 3),  0.5, colors.black),
        ("BACKGROUND", (0, 3), (1, 3),      colors.lightgrey),
        ("FONT",       (0, 3), (1, 3),  "Helvetica-Bold"),
        ("RIGHTPADDING",(1, 3), (1, 3), 20),
    ])

    # Tabla contenedora: pone las dos tablas en la misma fila
    tabla_contenedora = Table([[tab_izq, tab_der], ["", ""]])
    tabla_contenedora.setStyle([
        ("VALIGN",       (0, 0), (0, 0), "TOP"),
        ("BOTTOMPADDING",(0, 0), (-1,-1), 2),
    ])

    elementos.append(tabla_contenedora)
    elementos.append(Spacer(0, 20))
    return elementos


# =============================================================================
# SECCIÓN 8 — TABLA CON FLOWABLES EN CELDAS (Paragraph dentro de celda)
# =============================================================================

def seccion_tabla_flowables(hoja):
    elementos = []
    elementos.append(Paragraph("8. TABLA — FLOWABLES EN CELDAS", hoja["Heading1"]))
    elementos.append(Spacer(0, 8))

    est_verde = hoja["BodyText"]
    est_verde.textColor = colors.darkgreen

    est_rojo = hoja["Heading3"]
    est_rojo.textColor = colors.red
    est_rojo.fontSize  = 10

    p1 = Paragraph("Empresa Optare", est_verde)
    p2 = Paragraph("PSA Group",      est_rojo)

    # Una celda puede contener una LISTA de flowables: se apilan verticalmente
    datos = [
        ["Empresa",          "Candidato 1", "Candidato 2", "Proyecto"],
        ["Ayco",             "Marcos",      "Rubén",       "Web con PHP"],
        ["Iterat",           "Borja",       "Juan",        "OpenCV IA"],
        [[p1, p2],           "Lidier",      "Lucas",       "Apps Telco"],
    ]

    estilo = [
        ("TEXTCOLOR",  (0, 0), (0, -1),  colors.blue),
        ("TEXTCOLOR",  (1, 0), (-1, 0),  colors.blueviolet),
        ("TEXTCOLOR",  (1, 1), (-1, -1), colors.grey),
        ("BOX",        (1, 1), (-1, -1), 1.25, colors.grey),
        ("INNERGRID",  (1, 1), (-1, -1), 1.25, colors.lightgrey),
        ("VALIGN",     (0, 0), (-1, -1), "MIDDLE"),
    ]

    tabla = Table(data=datos)
    tabla.setStyle(estilo)
    elementos.append(tabla)
    elementos.append(Spacer(0, 20))
    return elementos


# =============================================================================
# SECCIÓN 9 — GRÁFICO DE BARRAS VERTICALES (1 serie)
# =============================================================================

def seccion_barras_verticales_1serie(hoja):
    elementos = []
    elementos.append(Paragraph("9. GRÁFICO DE BARRAS VERTICALES — 1 SERIE", hoja["Heading1"]))
    elementos.append(Spacer(0, 8))

    dibujo = Drawing(430, 180)

    grafico = VerticalBarChart()
    grafico.x      = 60
    grafico.y      = 50
    grafico.height = 110
    grafico.width  = 320

    # data SIEMPRE es lista de listas
    grafico.data = [UNIDADES]

    grafico.categoryAxis.categoryNames     = PRODUCTOS
    grafico.categoryAxis.labels.boxAnchor  = "ne"
    grafico.categoryAxis.labels.dx         = -8
    grafico.categoryAxis.labels.dy         = -10
    grafico.categoryAxis.labels.angle      = 30

    grafico.valueAxis.valueMin  = 0
    grafico.valueAxis.valueMax  = 90
    grafico.valueAxis.valueStep = 10

    grafico.strokeColor  = colors.black
    grafico.groupSpacing = 10
    grafico.barSpacing   = 2

    dibujo.add(grafico)
    elementos.append(dibujo)
    elementos.append(Spacer(0, 20))
    return elementos


# =============================================================================
# SECCIÓN 10 — GRÁFICO DE BARRAS VERTICALES (2 series agrupadas)
# =============================================================================

def seccion_barras_verticales_2series(hoja):
    elementos = []
    elementos.append(Paragraph("10. GRÁFICO DE BARRAS VERTICALES — 2 SERIES", hoja["Heading1"]))
    elementos.append(Spacer(0, 8))

    dibujo = Drawing(450, 200)

    grafico = VerticalBarChart()
    grafico.x      = 60
    grafico.y      = 50
    grafico.height = 120
    grafico.width  = 330

    # 2 series: Máximas y Mínimas por mes
    grafico.data = [MAXIMAS, MINIMAS]

    grafico.categoryAxis.categoryNames     = MESES
    grafico.categoryAxis.labels.boxAnchor  = "ne"
    grafico.categoryAxis.labels.dx         = 8
    grafico.categoryAxis.labels.dy         = -10
    grafico.categoryAxis.labels.angle      = 30

    grafico.valueAxis.valueMin  = -10
    grafico.valueAxis.valueMax  = 45
    grafico.valueAxis.valueStep = 5

    grafico.strokeColor  = colors.black
    grafico.groupSpacing = 10
    grafico.barSpacing   = 2

    dibujo.add(grafico)
    elementos.append(dibujo)
    elementos.append(Spacer(0, 20))
    return elementos


# =============================================================================
# SECCIÓN 11 — GRÁFICO DE BARRAS HORIZONTALES
# =============================================================================

def seccion_barras_horizontales(hoja):
    elementos = []
    elementos.append(Paragraph("11. GRÁFICO DE BARRAS HORIZONTALES", hoja["Heading1"]))
    elementos.append(Spacer(0, 8))

    dibujo = Drawing(450, 200)

    grafico = HorizontalBarChart()
    grafico.x      = 100
    grafico.y      = 20
    grafico.height = 140
    grafico.width  = 300

    grafico.data = [UNIDADES]

    grafico.categoryAxis.categoryNames     = PRODUCTOS
    grafico.categoryAxis.labels.boxAnchor  = "ne"

    grafico.valueAxis.valueMin  = 0
    grafico.valueAxis.valueMax  = 90
    grafico.valueAxis.valueStep = 10

    grafico.strokeColor  = colors.black
    grafico.groupSpacing = 10
    grafico.barSpacing   = 2

    dibujo.add(grafico)
    elementos.append(dibujo)
    elementos.append(Spacer(0, 20))
    return elementos


# =============================================================================
# SECCIÓN 12 — GRÁFICO DE LÍNEAS CON MARCADORES Y LEYENDA
# =============================================================================

def seccion_lineas(hoja):
    elementos = []
    elementos.append(Paragraph("12. GRÁFICO DE LÍNEAS + LEYENDA", hoja["Heading1"]))
    elementos.append(Spacer(0, 8))

    dibujo = Drawing(450, 200)

    gl = HorizontalLineChart()
    gl.x      = 50
    gl.y      = 50
    gl.height = 120
    gl.width  = 330

    gl.data = [MAXIMAS, MINIMAS]

    gl.categoryAxis.categoryNames     = MESES
    gl.categoryAxis.labels.boxAnchor  = "ne"
    gl.categoryAxis.labels.angle      = 30
    gl.categoryAxis.labels.dx         = 10
    gl.categoryAxis.labels.dy         = -20

    gl.valueAxis.valueMin  = -10
    gl.valueAxis.valueMax  = 45
    gl.valueAxis.valueStep = 10

    # Personalización de cada línea
    gl.lines[0].strokeWidth = 2
    gl.lines[0].symbol      = makeMarker("FilledCircle")    # marcador circular

    gl.lines[1].strokeWidth = 2
    gl.lines[1].symbol      = makeMarker("FilledTriangle")  # marcador triángulo

    # Leyenda
    leyenda = LineLegend()
    leyenda.fontSize      = 8
    leyenda.fontName      = "Helvetica"
    leyenda.alignment     = "right"
    leyenda.x             = 0
    leyenda.y             = -10
    leyenda.columnMaximum = 2
    leyenda.colorNamePairs = [
        (gl.lines[0].strokeColor, "Máximas"),
        (gl.lines[1].strokeColor, "Mínimas"),
    ]

    dibujo.add(gl)
    dibujo.add(leyenda)
    elementos.append(dibujo)
    elementos.append(Spacer(0, 20))
    return elementos


# =============================================================================
# SECCIÓN 13 — GRÁFICO DE TARTA (PIE 2D) CON LEYENDA
# =============================================================================

def seccion_tarta_2d(hoja):
    elementos = []
    elementos.append(Paragraph("13. GRÁFICO DE TARTA (PIE 2D) + LEYENDA", hoja["Heading1"]))
    elementos.append(Spacer(0, 8))

    ancho, alto = 450, 220
    dibujo = Drawing(ancho, alto)

    tarta = Pie()
    tarta.x      = ancho // 2 - 100
    tarta.y      = alto  // 2 - 80
    tarta.width  = 180
    tarta.height = 180
    tarta.data   = TOTAL_CLI
    tarta.labels = CLIENTES

    tarta.slices.strokeWidth = 0.5
    tarta.sideLabels         = 1

    # Resaltar el primer sector
    tarta.slices[0].popout       = 10
    tarta.slices[0].strokeWidth  = 2

    # Sector con etiqueta especial
    tarta.slices[2].strokeDashArray = [5, 2]
    tarta.slices[2].fontColor       = colors.blue

    # Colores personalizados
    lista_colores = [colors.blue, colors.darkgreen, colors.pink, colors.red, colors.peru]
    for i, color in enumerate(lista_colores):
        tarta.slices[i].fillColor = color

    # Leyenda
    leyenda = Legend()
    leyenda.x             = 350
    leyenda.y             = 180
    leyenda.fontSize      = 7
    leyenda.fontName      = "Helvetica"
    leyenda.boxAnchor     = "n"
    leyenda.columnMaximum = 5
    leyenda.strokeWidth   = 0.5
    leyenda.strokeColor   = colors.grey
    leyenda.deltax        = 20
    leyenda.deltay        = 10
    leyenda.dxTextSpace   = 5
    leyenda.alignment     = "right"
    leyenda.colorNamePairs = [
        (lista_colores[i], CLIENTES[i]) for i in range(len(CLIENTES))
    ]

    dibujo.add(tarta)
    dibujo.add(leyenda)
    elementos.append(dibujo)
    elementos.append(Spacer(0, 20))
    return elementos


# =============================================================================
# SECCIÓN 14 — GRÁFICO DE TARTA 3D (PIE3D)
# =============================================================================

def seccion_tarta_3d(hoja):
    elementos = []
    elementos.append(Paragraph("14. GRÁFICO DE TARTA 3D", hoja["Heading1"]))
    elementos.append(Spacer(0, 8))

    dibujo = Drawing(350, 200)

    tarta3d = Pie3d()
    tarta3d.x      = 65
    tarta3d.y      = 20
    tarta3d.width  = 170
    tarta3d.height = 170
    tarta3d.data   = [10, 5, 20, 25, 40]
    tarta3d.labels = ["Edge", "Brave", "Firefox", "Safari", "Chrome"]

    tarta3d.slices.strokeWidth = 0.5
    tarta3d.slices[3].popout           = 10
    tarta3d.slices[3].strokeWidth      = 2
    tarta3d.slices[3].strokeDashArray  = [2, 2]
    tarta3d.slices[3].fontColor        = colors.blue
    tarta3d.sideLabels = 1

    colores_nav = [colors.red, colors.green, colors.blue, colors.yellow, colors.pink]
    for i, c in enumerate(colores_nav):
        tarta3d.slices[i].fillColor = c

    dibujo.add(tarta3d)
    elementos.append(dibujo)
    elementos.append(Spacer(0, 20))
    return elementos


# =============================================================================
# SECCIÓN 15 — LABEL EN DRAWING (ETIQUETA DE TÍTULO EN GRÁFICO)
# =============================================================================

def seccion_label(hoja):
    elementos = []
    elementos.append(Paragraph("15. LABEL — TÍTULOS DENTRO DE UN DRAWING", hoja["Heading1"]))
    elementos.append(Spacer(0, 8))

    dibujo = Drawing(430, 180)

    # Título del gráfico
    titulo = Label()
    titulo.setOrigin(215, 170)   # posición dentro del Drawing
    titulo.setText("Unidades vendidas por producto")

    # Etiqueta lateral (eje Y)
    etiqueta_y = Label()
    etiqueta_y.setOrigin(10, 90)
    etiqueta_y.angle = 90        # texto vertical
    etiqueta_y.setText("Unidades")

    grafico = VerticalBarChart()
    grafico.x      = 50
    grafico.y      = 30
    grafico.height = 110
    grafico.width  = 320
    grafico.data   = [UNIDADES]
    grafico.categoryAxis.categoryNames    = PRODUCTOS
    grafico.categoryAxis.labels.angle     = 30
    grafico.categoryAxis.labels.dy        = -10
    grafico.categoryAxis.labels.boxAnchor = "ne"
    grafico.valueAxis.valueMin  = 0
    grafico.valueAxis.valueMax  = 90
    grafico.valueAxis.valueStep = 15
    grafico.strokeColor = colors.black

    dibujo.add(titulo)
    dibujo.add(etiqueta_y)
    dibujo.add(grafico)
    elementos.append(dibujo)
    elementos.append(Spacer(0, 20))
    return elementos


# =============================================================================
# SECCIÓN 16 — FLOWABLE PERSONALIZADO (elemento fuera del flujo normal)
# =============================================================================

class BarraLateral(Flowable):
    """
    Dibuja una barra decorativa vertical en el margen izquierdo.
    Al ser un Flowable personalizado puede insertarse en el guion
    como cualquier otro elemento.
    """
    def __init__(self, tabla, x_offset=-55, y_offset=-400):
        Flowable.__init__(self)
        self.tabla    = tabla
        self.x_offset = x_offset
        self.y_offset = y_offset

    def draw(self):
        self.canv.saveState()
        self.canv.translate(self.x_offset, self.y_offset)
        self.tabla.wrapOn(self.canv, 0, 0)
        self.tabla.drawOn(self.canv, 0, 0)
        self.canv.restoreState()


def seccion_flowable_custom(hoja):
    elementos = []
    elementos.append(Paragraph("16. FLOWABLE PERSONALIZADO", hoja["Heading1"]))
    elementos.append(Spacer(0, 8))
    elementos.append(Paragraph(
        "Un Flowable personalizado hereda de Flowable y sobreescribe draw(). "
        "Se usa para posicionar elementos fuera del flujo normal, como una barra lateral decorativa.",
        hoja["BodyText"]
    ))
    elementos.append(Spacer(0, 8))

    # Tabla estrecha que actúa de barra lateral
    barra_tabla = Table(
        [[""], [""], [""], [""]],
        colWidths=[15],
        rowHeights=[40, 200, 5, 100],
    )
    barra_tabla.setStyle([
        ("BACKGROUND", (0, 0), (0, 0), colors.darkgreen),
        ("BACKGROUND", (0, 1), (0, 1), colors.lightgreen),
        ("BACKGROUND", (0, 2), (0, 2), colors.white),
        ("BACKGROUND", (0, 3), (0, 3), colors.lightgreen),
    ])

    barra = BarraLateral(barra_tabla, x_offset=-55, y_offset=-380)
    elementos.append(barra)

    # Contenido de demostración
    for i in range(4):
        elementos.append(Paragraph(f"Línea de contenido {i+1} junto a la barra lateral.", hoja["BodyText"]))
        elementos.append(Spacer(0, 15))

    elementos.append(Spacer(0, 20))
    return elementos


# =============================================================================
# SECCIÓN 17 — TABLA COMPLETA TIPO FACTURA (combinando técnicas)
# =============================================================================

def seccion_factura(hoja):
    elementos = []
    elementos.append(Paragraph("17. TABLA TIPO FACTURA", hoja["Heading1"]))
    elementos.append(Spacer(0, 8))

    # Cabecera: título + empresa
    est_cab = hoja["Heading1"]
    est_cab.textColor   = colors.darkolivegreen
    est_cab.alignment   = 2       # derecha
    est_cab.fontSize    = 14
    elementos.append(Paragraph("FACTURA SIMPLIFICADA", est_cab))
    elementos.append(Spacer(0, 8))

    # Tabla datos empresa / factura
    datos_emp = [
        ["Dirección",      "", "", "Fecha Emisión",       "25/02/2026"],
        ["Ciudad y País",  "", "", "Número de Factura",   "A0001"],
        ["CIF/NIF",        "", "", "", ""],
        ["Teléfono",       "", "", "", ""],
    ]
    tab_emp = Table(datos_emp, colWidths=[100, 100, 80, 110, 100])
    tab_emp.setStyle([
        ("FONT",      (0, 0), (0, -1), "Helvetica-BoldOblique"),
        ("FONT",      (3, 0), (3, -1), "Helvetica-Bold"),
        ("TEXTCOLOR", (0, 0), (-1, -1), colors.darkgreen),
        ("ALIGN",     (3, 0), (3, -1), "RIGHT"),
    ])
    elementos.append(tab_emp)
    elementos.append(Spacer(0, 10))

    # Tabla productos
    productos_fac = [
        ["Descripción",  "Importe", "Cantidad", "Total"],
        ["Memoria RAM",  "3,99",    "10",        "39,90"],
        ["Portátil Dell","1215,00", "1",        "1215,00"],
        ["Monitor HP",   "84,23",   "2",         "168,46"],
        ["Ratón LG",     "25,00",   "3",          "75,00"],
    ]
    tab_prod = Table(productos_fac, colWidths=[190, 100, 100, 100])
    tab_prod.setStyle([
        ("FONT",       (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BACKGROUND", (0, 0), (-1, 0), colors.darkgreen),
        ("TEXTCOLOR",  (0, 0), (-1, 0), colors.white),
        ("BACKGROUND", (0, 1), (-1, -1), colors.lightgreen),
        ("TEXTCOLOR",  (0, 1), (-1, -1), colors.black),
        ("ALIGN",      (0, 0), (-1, -1), "CENTER"),
        ("GRID",       (0, 0), (-1, -1), 1, colors.white),
    ])
    elementos.append(tab_prod)
    elementos.append(Spacer(0, 5))

    # Tabla total
    tab_total = Table([["", "", "TOTAL", "1498,36 €"]],
                      colWidths=[190, 100, 100, 100], rowHeights=25)
    tab_total.setStyle([
        ("FONT",       (2, 0), (3, 0), "Helvetica-Bold"),
        ("BACKGROUND", (2, 0), (3, 0), colors.darkgreen),
        ("TEXTCOLOR",  (2, 0), (3, 0), colors.white),
        ("ALIGN",      (2, 0), (3, 0), "CENTER"),
        ("VALIGN",     (2, 0), (3, 0), "MIDDLE"),
        ("FONTSIZE",   (2, 0), (3, 0), 11),
    ])
    elementos.append(tab_total)
    elementos.append(Spacer(0, 15))

    # Línea de separación
    linea = Table([["", "", "", ""]], colWidths=[190, 100, 100, 100])
    linea.setStyle([("LINEBELOW", (0, 0), (-1, -1), 1, colors.black)])
    elementos.append(linea)
    elementos.append(Spacer(0, 10))

    # Pie de página
    est_pie = hoja["BodyText"]
    est_pie.textColor = colors.darkgreen
    est_pie.alignment = 1
    elementos.append(Paragraph("GRACIAS POR SU CONFIANZA", est_pie))
    elementos.append(Spacer(0, 20))
    return elementos


# =============================================================================
# SECCIÓN 18 — TEXTO DE ANÁLISIS (patrón de informe con BD)
# =============================================================================

def seccion_texto_analisis(hoja):
    elementos = []
    elementos.append(Paragraph("18. TEXTO DE ANÁLISIS (PATRÓN INFORME)", hoja["Heading1"]))
    elementos.append(Spacer(0, 8))

    # Cálculos sobre los datos
    total_uds  = sum(UNIDADES)
    total_fac  = sum(FACTURACION)
    mejor      = PRODUCTOS[0]
    mejor_uds  = UNIDADES[0]
    n          = len(PRODUCTOS)

    texto = (
        "O produto máis vendido é <b>%s</b> con <b>%i unidades</b>. "
        "No total, os <b>%i</b> produtos máis vendidos representan "
        "<b>%i unidades</b> vendidas e unha facturación de <b>%0.2f€</b>."
        % (mejor, mejor_uds, n, total_uds, total_fac)
    )

    # Paragraph admite etiquetas HTML básicas: <b>, <i>, <u>, <br/>
    elementos.append(Paragraph(texto, hoja["BodyText"]))
    elementos.append(Spacer(0, 8))

    # Ejemplo con texto multilínea y etiquetas
    texto2 = """
    El análisis muestra que:<br/>
    &bull; Producto más vendido: <b>%s</b><br/>
    &bull; Total unidades: <b>%i</b><br/>
    &bull; Total facturación: <b>%0.2f€</b>
    """ % (mejor, total_uds, total_fac)

    elementos.append(Paragraph(texto2, hoja["BodyText"]))
    elementos.append(Spacer(0, 20))
    return elementos


# =============================================================================
# MAIN — construir el PDF con todos los ejemplos
# =============================================================================

if __name__ == "__main__":
    hoja    = getSampleStyleSheet()
    guion   = []

    # Portada
    guion.append(Spacer(0, 60))
    guion.append(Paragraph("EJEMPLOS COMPLETOS DE PLATYPUS", hoja["Title"]))
    guion.append(Spacer(0, 10))
    guion.append(Paragraph("Guía práctica de ReportLab — 2DAM Diseño de Interfaces", hoja["Heading2"]))
    guion.append(Spacer(0, 30))
    guion.append(Paragraph(
        "Este archivo contiene un ejemplo funcional de cada característica de Platypus: "
        "párrafos, tablas básicas, estilos condicionales, filas alternas, celdas combinadas, "
        "tablas anidadas, gráficos de barras, líneas, tartas, leyendas, labels, "
        "flowables personalizados y plantilla de factura.",
        hoja["BodyText"]
    ))
    guion.append(Spacer(0, 40))

    # Añadir todas las secciones
    guion += seccion_parrafos(hoja)
    guion += seccion_spacer(hoja)
    guion += seccion_tabla_basica(hoja)
    guion += seccion_tabla_alternas(hoja)
    guion += seccion_tabla_condicional(hoja)
    guion += seccion_tabla_span(hoja)
    guion += seccion_tabla_anidada(hoja)
    guion += seccion_tabla_flowables(hoja)
    guion += seccion_barras_verticales_1serie(hoja)
    guion += seccion_barras_verticales_2series(hoja)
    guion += seccion_barras_horizontales(hoja)
    guion += seccion_lineas(hoja)
    guion += seccion_tarta_2d(hoja)
    guion += seccion_tarta_3d(hoja)
    guion += seccion_label(hoja)
    guion += seccion_flowable_custom(hoja)
    guion += seccion_factura(hoja)
    guion += seccion_texto_analisis(hoja)

    # Generar PDF
    doc = SimpleDocTemplate("ejemplos_platypus.pdf", pagesize=A4)
    doc.build(guion)
    print("PDF generado: ejemplos_platypus.pdf")
