# GUÍA COMPLETA REPORTLAB — 2DAM Diseño de Interfaces
> Basada en todo el contenido del proyecto de clase

---

## ÍNDICE
1. [Dos formas de generar PDFs](#1-dos-formas-de-generar-pdfs)
2. [Canvas — control total manual](#2-canvas--control-total-manual)
3. [Platypus — documentos con flujo](#3-platypus--documentos-con-flujo)
4. [Párrafos y estilos de texto](#4-párrafos-y-estilos-de-texto)
5. [Imágenes](#5-imágenes)
6. [Tablas](#6-tablas)
7. [Celdas combinadas SPAN](#7-celdas-combinadas-span)
8. [Tablas anidadas](#8-tablas-anidadas)
9. [Gráfico de barras verticales](#9-gráfico-de-barras-verticales)
10. [Gráfico de barras horizontales](#10-gráfico-de-barras-horizontales)
11. [Gráfico de líneas](#11-gráfico-de-líneas)
12. [Gráfico de tarta / sectores](#12-gráfico-de-tarta--sectores)
13. [Leyenda (Legend)](#13-leyenda-legend)
14. [Label — título en un Drawing](#14-label--título-en-un-drawing)
15. [Drawing — transformaciones](#15-drawing--transformaciones)
16. [Consulta SQLite](#16-consulta-sqlite)
17. [Flowable personalizado](#17-flowable-personalizado)
18. [Propiedades de estilo — referencia rápida](#18-propiedades-de-estilo--referencia-rápida)
19. [Colores útiles](#19-colores-útiles)
20. [Fuentes disponibles](#20-fuentes-disponibles)
21. [Esqueleto de informe completo](#21-esqueleto-de-informe-completo)
22. [Errores comunes](#22-errores-comunes)
23. [Imports de referencia rápida](#23-imports-de-referencia-rápida)

---

## 1. DOS FORMAS DE GENERAR PDFs

| | Canvas | Platypus (SimpleDocTemplate) |
|---|---|---|
| Control | Manual, coordenadas absolutas | Automático, flujo de elementos |
| Uso | Facturas muy personalizadas, gráficos puros | Informes, documentos con texto, tablas y gráficos |
| Salto de página | Manual (`showPage()`) | Automático |
| Clave | `canvas.Canvas(...)` | `SimpleDocTemplate(...).build(guion)` |

---

## 2. CANVAS — CONTROL TOTAL MANUAL

### Básico
```python
from reportlab.pdfgen import canvas

hoja = canvas.Canvas("documento.pdf")

# Texto directo (origen: esquina INFERIOR IZQUIERDA)
hoja.drawString(50, 100, "Texto en posición (50,100)")

# Imagen
hoja.drawImage("imagen.png", 250, 300, width=100, height=100)

# Cambiar fuente activa del canvas
hoja.setFont("Helvetica", 16)

hoja.showPage()   # fin de página
hoja.save()       # guardar el PDF
```

### Objeto de texto (TextObject)
Permite formatear bloques de texto con múltiples estilos antes de pintarlos.

```python
objTexto = hoja.beginText()
objTexto.setTextOrigin(100, 500)   # posición inicial del cursor
objTexto.setFont("Courier", 16)

# textLine() → escribe una línea y baja el cursor
objTexto.textLine("Primera línea")
objTexto.textLine("Segunda línea")

# textLines() → procesa un string con saltos de línea \n
objTexto.textLines("Línea 1\nLínea 2\nLínea 3")

# textOut() → escribe sin bajar de línea
objTexto.textOut("texto en la misma línea")

# moveCursor(dx, dy) → mueve el cursor de forma relativa
objTexto.moveCursor(20, 15)

# Colores de relleno
objTexto.setFillGray(0.5)          # gris (0=negro, 1=blanco)
objTexto.setFillColor(colors.pink) # color por nombre
objTexto.setFillColor("Green")     # color por string
objTexto.setFillColor(colors.Color(0.2, 0, 0.6))  # RGB 0.0-1.0

# Espaciado entre caracteres
objTexto.setCharSpace(3)

# Espaciado entre palabras
objTexto.setWordSpace(5)

hoja.drawText(objTexto)  # pintar en el canvas
```

### Fuentes disponibles en Canvas
```python
for fuente in hoja.getAvailableFonts():
    print(fuente)
# Courier, Courier-Bold, Helvetica, Helvetica-Bold,
# Helvetica-Oblique, Helvetica-BoldOblique,
# Times-Roman, Times-Bold, Symbol, ZapfDingbats...
```

### renderPDF — guardar Drawing como PDF
```python
from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import A4

dibujo = Drawing(A4[0], A4[1])
# ... añadir elementos ...
renderPDF.drawToFile(dibujo, "salida.pdf")
```

---

## 3. PLATYPUS — DOCUMENTOS CON FLUJO

### Patrón base
```python
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4

guion = []  # lista de flowables (elementos del documento)

# ... añadir elementos a guion ...

doc = SimpleDocTemplate("salida.pdf", pagesize=A4)
doc.build(guion)
```

### Opciones de SimpleDocTemplate
```python
doc = SimpleDocTemplate(
    "salida.pdf",
    pagesize=A4,        # también: A5, letter...
    showBoundary=1,     # mostrar bordes de caja (para depurar)
    showBoundary=0,     # sin bordes
)
```

### Tamaños de página
```python
from reportlab.lib.pagesizes import A4, A5
# A4 = (595.28, 841.89) puntos
# A5 = (419.53, 595.28) puntos
print(A4)   # (595.2755905511812, 841.8897637795277)
```

---

## 4. PÁRRAFOS Y ESTILOS DE TEXTO

### Estilos predefinidos
```python
from reportlab.lib.styles import getSampleStyleSheet

hoja = getSampleStyleSheet()

# Estilos disponibles:
hoja["Title"]     # Título grande, centrado
hoja["Heading1"]  # Encabezado nivel 1
hoja["Heading2"]  # Encabezado nivel 2
hoja["Heading3"]  # Encabezado nivel 3
hoja["Heading4"]  # Encabezado nivel 4
hoja["BodyText"]  # Texto de cuerpo
hoja["Normal"]    # Texto normal
```

### Crear párrafos
```python
from reportlab.platypus import Paragraph

p = Paragraph("Texto del párrafo", hoja["Title"])
guion.append(p)
```

### Modificar propiedades del estilo
```python
estilo = hoja["Heading1"]
estilo.fontSize = 18
estilo.fontName = "Helvetica-Bold"        # o "Helvetica", "Helvetica-Oblique"
estilo.alignment = 0                      # 0=izq, 1=centro, 2=dcha
estilo.textColor = colors.darkgreen
estilo.backColor = colors.lightcyan       # fondo del párrafo
estilo.pageBreakBefore = 0               # 0=no forzar salto de página antes
estilo.keepWithNext = 0                   # no forzar unión con el siguiente
```

### Spacer — espacio en blanco vertical
```python
from reportlab.platypus import Spacer

guion.append(Spacer(0, 30))   # 30 puntos de espacio vertical
guion.append(Spacer(1, 60))   # equivalente
```

---

## 5. IMÁGENES

### Imagen en Platypus (flowable)
```python
from reportlab.platypus import Image

imagen = Image("ruta/imagen.jpg", width=400, height=300)
guion.append(imagen)
```

### Imagen en Canvas
```python
hoja.drawImage("ruta/imagen.jpg", x=100, y=200, width=50, height=50)
```

### Imagen en Drawing (gráficos)
```python
from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF

imagen = Image(0, 0, 100, 100, "check.png")  # x, y, w, h, ruta
dibujo = Drawing()
dibujo.add(imagen)
```

### Transformaciones en Drawing
```python
dibujo = Drawing()
dibujo.add(imagen)
dibujo.translate(100, 50)   # desplazar
dibujo.rotate(45)            # rotar en grados
dibujo.scale(0.5, 0.5)      # escalar (x, y)
```

---

## 6. TABLAS

### Crear tabla básica
```python
from reportlab.platypus import Table, TableStyle

datos = [
    ["Cabecera 1", "Cabecera 2", "Cabecera 3"],
    ["fila1_col1",  "fila1_col2",  "fila1_col3"],
    ["fila2_col1",  "fila2_col2",  "fila2_col3"],
]

tabla = Table(datos)
# Con anchos de columna:
tabla = Table(datos, colWidths=[60, 200, 100])
# Con alineación horizontal de la tabla:
tabla = Table(datos, hAlign='CENTER')   # LEFT, CENTER, RIGHT
# Con altura de filas:
tabla = Table(datos, rowHeights=30)
```

### Referencia de coordenadas — MUY IMPORTANTE
```
(col, fila)  →  empieza en (0, 0) = esquina SUPERIOR IZQUIERDA
(-1, -1)     →  última columna, última fila
(0, 0), (-1, 0)    →  toda la fila 0 (cabecera)
(0, 0), (-1, -1)   →  toda la tabla
(0, 1), (0, -1)    →  toda la columna 0 excepto cabecera
```

### Todas las propiedades de estilo

```python
estilo = [
    # --- FONDOS ---
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),   # fondo cabecera
    ('BACKGROUND', (0, 1), (-1, -1), colors.lightgreen), # fondo cuerpo
    ('BACKGROUND', (0, 2), (-1, 2), colors.lightgrey),   # fila específica

    # --- TEXTO ---
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),    # color texto
    ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),      # fuente
    ('FONT', (0, 0), (0, -1), 'Helvetica-BoldOblique'),
    ('FONTSIZE', (0, 0), (-1, 0), 12),               # tamaño de fuente

    # --- BORDES ---
    ('GRID', (0, 0), (-1, -1), 1, colors.black),      # rejilla completa
    ('BOX', (0, 0), (-1, -1), 1, colors.black),       # solo borde exterior
    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black), # solo interior
    ('LINEABOVE', (0, 3), (-1, 3), 1.5, colors.black), # línea encima fila
    ('LINEBELOW', (0, 0), (-1, 0), 2, colors.green),  # línea debajo fila

    # --- ALINEACIÓN ---
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),   # CENTER, LEFT, RIGHT
    ('ALIGN', (1, 0), (1, -1), 'LEFT'),      # columna 1 a la izquierda
    ('ALIGN', (-1, 1), (-1, -1), 'RIGHT'),   # última col a la derecha
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # TOP, MIDDLE, BOTTOM

    # --- PADDING ---
    ('RIGHTPADDING', (0, 0), (0, -1), 35),
    ('LEFTPADDING', (1, 0), (1, -1), 35),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
]

tabla.setStyle(estilo)
guion.append(tabla)
```

### Tabla con estilos condicionales (por valor)
```python
# Ejemplo: tabla de temperaturas con colores según rango
for i, fila in enumerate(datos):
    for j, valor in enumerate(fila):
        if type(valor) == int:
            if valor > 30:
                estilo.append(('BACKGROUND', (j, i), (j, i), colors.red))
            elif 20 < valor <= 30:
                estilo.append(('BACKGROUND', (j, i), (j, i), colors.orange))
            elif 10 < valor <= 20:
                estilo.append(('BACKGROUND', (j, i), (j, i), colors.lightpink))
            elif 0 < valor <= 10:
                estilo.append(('BACKGROUND', (j, i), (j, i), colors.lightblue))
            else:
                estilo.append(('BACKGROUND', (j, i), (j, i), colors.lightgrey))
```

### Filas alternas con bucle (patrón de examen)
```python
for i in range(2, len(datos), 2):   # filas 2, 4, 6...
    estilo.append(('BACKGROUND', (0, i), (-1, i), colors.lightgrey))
```

### Tabla desde BD (patrón de examen)
```python
cabecera = ['Pos.', 'Nombre', 'Uds.', 'Facturación']
tabla_datos = [cabecera]

for i, dato in enumerate(resultados):
    fila = [i + 1, dato[0], dato[1], '%0.2f€' % (dato[2],)]
    tabla_datos.append(fila)

tab = Table(tabla_datos)
tab.setStyle(estilo)
guion.append(tab)
```

### Celdas con múltiples elementos (Paragraph + Image)
```python
parrafo = Paragraph("Texto", estilo_texto)
imagen  = Image("check.png", 20, 20)

datos = [
    ["Cabecera 1", "Cabecera 2"],
    [[parrafo, imagen], "Otro texto"],  # lista de flowables en una celda
]
```

---

## 7. CELDAS COMBINADAS SPAN

```python
datos = [
    ["Título grande", "",   "col2",  "col3"],  # fila 0
    ["",              "",   "...",   "..."],    # fila 1 (parte del SPAN)
    ["dato",          "dato", "dato", "dato"],
]

estilo = [
    ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    # Fusionar (col0,fila0) hasta (col1,fila1) — 2x2
    ('BACKGROUND', (0, 0), (1, 1), colors.lavender),
    ('SPAN', (0, 0), (1, 1)),
    # Fusionar las 2 últimas columnas en las 2 últimas filas
    ('SPAN', (-2, -2), (-1, -1)),
    # Fusionar toda la fila 0
    ('SPAN', (0, 0), (-1, 0)),
    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
]
```

---

## 8. TABLAS ANIDADAS

Se puede insertar una tabla como celda de otra tabla:

```python
# Tabla A y Tabla B se colocan en la misma fila
tabla_contenedora = Table([[tablaA, tablaB], ['', '']])
tabla_contenedora.setStyle([
    ('VALIGN', (0, 0), (0, 0), 'TOP'),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
])
guion.append(tabla_contenedora)
```

---

## 9. GRÁFICO DE BARRAS VERTICALES

```python
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.lib import colors

# Datos — SIEMPRE lista de listas
nombres = ["Ene", "Feb", "Mar", "Abr", "May"]
serie1  = [15, 16, 20, 25, 27]
serie2  = [-3, -4, -1, 4, 6]

dibujo = Drawing(450, 200)   # ancho, alto del lienzo

grafico = VerticalBarChart()

# Posición del gráfico dentro del lienzo
grafico.x = 50
grafico.y = 50

# Tamaño del área de barras
grafico.height = 125
grafico.width  = 300

# Datos: lista de listas (una lista = una serie de barras)
grafico.data = [serie1]          # 1 serie
grafico.data = [serie1, serie2]  # 2 series (barras agrupadas)
grafico.data = temperaturas[1:]  # desde lista más grande

# Eje de valores (Y)
grafico.valueAxis.valueMin  = -5
grafico.valueAxis.valueMax  = 40
grafico.valueAxis.valueStep = 5

# Eje de categorías (X)
grafico.categoryAxis.categoryNames      = nombres
grafico.categoryAxis.labels.boxAnchor  = 'ne'  # anclaje: ne, n, nw, e, w...
grafico.categoryAxis.labels.dx         = 8     # desplazamiento horizontal
grafico.categoryAxis.labels.dy         = -15   # desplazamiento vertical
grafico.categoryAxis.labels.angle      = 30    # rotación de etiquetas

# Apariencia
grafico.strokeColor  = colors.black  # borde de las barras
grafico.groupSpacing = 10            # espacio entre grupos
grafico.barSpacing   = 2             # espacio entre barras del mismo grupo

dibujo.add(grafico)
guion.append(dibujo)
```

---

## 10. GRÁFICO DE BARRAS HORIZONTALES

Exactamente igual que el vertical, cambiando solo la clase:

```python
from reportlab.graphics.charts.barcharts import HorizontalBarChart

grafico = HorizontalBarChart()
# Resto de propiedades idénticas a VerticalBarChart
```

---

## 11. GRÁFICO DE LÍNEAS

```python
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.widgets.markers import makeMarker

dibujo = Drawing(400, 200)

gl = HorizontalLineChart()
gl.x = 50
gl.y = 50
gl.height = 125
gl.width  = 300

gl.data = temperaturas[1:]             # lista de listas
gl.categoryAxis.categoryNames = temperaturas[0]
gl.categoryAxis.labels.boxAnchor = 'ne'
gl.categoryAxis.labels.angle     = 30
gl.categoryAxis.labels.dx        = 10
gl.categoryAxis.labels.dy        = -20

gl.valueAxis.valueMin  = 0
gl.valueAxis.valueMax  = 40
gl.valueAxis.valueStep = 10

# Personalización de líneas (por índice de serie)
gl.lines[0].strokeWidth = 1
gl.lines[0].symbol      = makeMarker('FilledCircle')   # marcador circular
gl.lines[1].strokeWidth = 5
gl.lines[1].symbol      = makeMarker('FilledTriangle') # marcador triángulo

dibujo.add(gl)
guion.append(dibujo)
```

### Marcadores disponibles
```python
makeMarker('FilledCircle')    # círculo relleno
makeMarker('FilledTriangle')  # triángulo relleno
makeMarker('FilledSquare')    # cuadrado relleno
makeMarker('FilledDiamond')   # rombo relleno
```

---

## 12. GRÁFICO DE TARTA / SECTORES

### Pie (2D)
```python
from reportlab.graphics.charts.piecharts import Pie

dibujo = Drawing(300, 200)

tarta = Pie()
tarta.x      = 65      # posición dentro del Drawing
tarta.y      = 15
tarta.width  = 170     # tamaño de la tarta
tarta.height = 170

tarta.data   = [10, 20, 30, 40, 50]                    # valores
tarta.labels = ['Oppo', 'Pixel', 'Galaxy', 'Iphone', 'Xiaomi']  # etiquetas

tarta.slices.strokeWidth = 0.5   # borde de los sectores
tarta.sideLabels = 1             # etiquetas a los lados con línea

# Resaltar un sector específico
tarta.slices[3].popout = 10              # sacar el sector hacia fuera
tarta.slices[3].strokeDashArray = [5, 2] # borde discontinuo
tarta.slices[3].labelRadius = 3          # distancia de la etiqueta al centro
tarta.slices[3].fontColor = colors.red   # color del texto de la etiqueta

# Colores de sectores
colores = [colors.blue, colors.red, colors.green, colors.yellow, colors.orange]
for i, color in enumerate(colores):
    tarta.slices[i].fillColor = color

dibujo.add(tarta)
guion.append(dibujo)
```

### Pie3d (3D)
```python
from reportlab.graphics.charts.piecharts import Pie3d

tarta = Pie3d()
tarta.x      = 65
tarta.y      = 15
tarta.data   = [10, 5, 20, 25, 40]
tarta.labels = ['Edge', 'Brave', 'Firefox', 'Safari', 'Chrome']
tarta.slices.strokeWidth = 0.5
tarta.slices[3].popout        = 10
tarta.slices[3].strokeWidth   = 2
tarta.slices[3].strokeDashArray = [2, 2]
tarta.slices[3].fontColor     = colors.blue
tarta.sideLabels = 1
dibujo.add(tarta)
```

### Centrar tarta en el Drawing
```python
ancho, alto = 400, 350
dibujo = Drawing(ancho, alto)
tarta.x      = ancho / 2 - 100   # centrado
tarta.y      = alto / 2 - 50
tarta.width  = 200
tarta.height = 200
```

---

## 13. LEYENDA (Legend)

### Legend (para Pie)
```python
from reportlab.graphics.charts.legends import Legend

leyenda = Legend()

# Posición dentro del Drawing
leyenda.x = 370
leyenda.y = 5

# Tipografía
leyenda.fontName = 'Helvetica'
leyenda.fontSize = 7

# Anclaje de posición
leyenda.boxAnchor = 'n'   # n, s, e, w, ne, nw, se, sw, c

# Máximo de columnas
leyenda.columnMaximum = 3

# Bordes
leyenda.strokeWidth = 1
leyenda.strokeColor = colors.black

# Separación
leyenda.deltax = 20         # horizontal entre elementos
leyenda.deltay = 10         # vertical entre filas
leyenda.autoXPadding = 20   # padding columnas
leyenda.yGap = 0
leyenda.dxTextSpace = 10    # espacio entre cuadro de color y texto

# Alineación del cuadro de color respecto al texto
leyenda.alignment = 'right'

# Líneas divisoras (7 = todas)
leyenda.dividerLines = 7
leyenda.dividerOffsY = 5.5
leyenda.subCols.rpad = 15

# Datos: lista de (color, etiqueta)
leyenda.colorNamePairs = [
    (colors.blue, 'Oppo'),
    (colors.red, 'Pixel'),
]
# O desde el gráfico:
leyenda.colorNamePairs = [
    (tarta.slices[i].fillColor, tarta.labels[i])
    for i in range(len(tarta.data))
]

dibujo.add(leyenda)
```

### LineLegend (para gráfico de líneas)
```python
from reportlab.graphics.charts.legends import LineLegend

leyenda = LineLegend()
leyenda.fontSize      = 8
leyenda.fontName      = "Helvetica"
leyenda.alignment     = "right"
leyenda.x             = 0
leyenda.y             = -15
leyenda.columnMaximum = 2

series = ["Máximas", "Mínimas"]
leyenda.colorNamePairs = [(gl.lines[i].strokeColor, series[i]) for i in range(len(gl.data))]

dibujo.add(leyenda)
```

---

## 14. LABEL — TÍTULO EN UN DRAWING

```python
from reportlab.graphics.charts.textlabels import Label

titulo = Label()
titulo.setOrigin(200, 190)   # posición dentro del Drawing
titulo.setText("Título del gráfico")

etiquetaLateral = Label()
etiquetaLateral.setOrigin(10, 100)
etiquetaLateral.angle = 90   # texto vertical
etiquetaLateral.setText("Porcentaje")

dibujo.add(titulo)
dibujo.add(etiquetaLateral)
```

---

## 15. DRAWING — TRANSFORMACIONES

```python
from reportlab.graphics.shapes import Drawing, Image

dibujo = Drawing()
dibujo.add(imagen)

dibujo.translate(100, 50)  # desplazar (x, y)
dibujo.rotate(45)           # rotar en grados
dibujo.scale(0.5, 0.5)     # escalar (fx, fy)
```

> **Orden importa:** las transformaciones se aplican en orden inverso (la última escrita se aplica primero).

---

## 16. CONSULTA SQLITE

### Patrón básico
```python
import sqlite3

def obtener_datos(path_bd, limite=5):
    conn   = sqlite3.connect(path_bd)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT columna1, columna2, SUM(columna3)
        FROM tabla
        JOIN otra ON tabla.id = otra.id
        GROUP BY columna1
        ORDER BY columna2 DESC
        LIMIT ?
    """, (limite,))
    resultados = cursor.fetchall()
    conn.close()        # SIEMPRE cerrar la conexión
    return resultados   # lista de tuplas
```

### Consulta productos más vendidos (patrón de examen)
```python
cursor.execute("""
    SELECT
        p.nome,
        SUM(lf.cantidade) AS total_vendido,
        SUM(lf.cantidade * lf.prezo_unitario * (1 - lf.desconto/100)) AS facturacion
    FROM linhas_factura lf
        JOIN produtos p ON lf.id_produto = p.id_produto
    GROUP BY p.id_produto, p.nome
    ORDER BY total_vendido DESC
    LIMIT ?
""", (limite,))
```

### Consulta clientes por facturación con IVA
```python
cursor.execute("""
    SELECT c.nome,
           COUNT(DISTINCT f.id_factura) AS num_facturas,
           SUM(lf.cantidade * lf.prezo_unitario
               * (1 - lf.desconto/100)
               * (1 + p.iva/100)) AS facturacion_total
    FROM clientes c
        JOIN facturas f       ON c.id_cliente  = f.id_cliente
        JOIN linhas_factura lf ON f.id_factura  = lf.id_factura
        JOIN produtos p        ON lf.id_produto = p.id_produto
    GROUP BY c.id_cliente, c.nome
    ORDER BY facturacion_total DESC
    LIMIT ?
""", (limite,))
```

### Usar los resultados
```python
# resultado[i] es una tupla: (nombre, unidades, facturacion)
nombres    = [d[0] for d in datos]
valores    = [d[1] for d in datos]
facturas   = [d[2] for d in datos]

total = sum(d[1] for d in datos)
media = sum(d[2] for d in datos) / len(datos)

# Formato dinámico para texto de análisis
texto = ("El producto más vendido es %s con %i uds. "
         "Los %i productos representan %i uds. y %0.2f€."
         % (datos[0][0], datos[0][1], len(datos), total, sum(facturas)))
```

---

## 17. FLOWABLE PERSONALIZADO

Se usa para colocar elementos fuera del flujo normal (ej. barra lateral decorativa):

```python
from reportlab.platypus import Flowable

class TablaPositionada(Flowable):
    def __init__(self, tabla, x, y):
        Flowable.__init__(self)
        self.tabla = tabla
        self.x = x
        self.y = y

    def draw(self):
        self.canv.saveState()
        self.canv.translate(self.x, self.y)
        self.tabla.wrapOn(self.canv, 0, 0)
        self.tabla.drawOn(self.canv, 0, 0)
        self.canv.restoreState()

# Uso:
borde = TablaPositionada(tabla_borde, -60, -445)
guion.append(borde)
```

---

## 18. PROPIEDADES DE ESTILO — REFERENCIA RÁPIDA

### Estilo de Paragraph
| Propiedad | Valores | Descripción |
|---|---|---|
| `fontSize` | número | Tamaño de letra |
| `fontName` | `"Helvetica"`, `"Helvetica-Bold"`, `"Courier"`, `"Times-Roman"` | Fuente |
| `alignment` | `0`, `1`, `2` | Izquierda, Centro, Derecha |
| `textColor` | `colors.X` | Color del texto |
| `backColor` | `colors.X` | Color de fondo del párrafo |
| `pageBreakBefore` | `0` / `1` | Salto de página antes |
| `keepWithNext` | `0` / `1` | No separar del siguiente elemento |

### Comandos de estilo de Tabla
| Comando | Argumentos | Descripción |
|---|---|---|
| `BACKGROUND` | ini, fin, color | Fondo de celdas |
| `TEXTCOLOR` | ini, fin, color | Color de texto |
| `FONT` | ini, fin, nombre_fuente | Tipo de fuente |
| `FONTSIZE` | ini, fin, tamaño | Tamaño de fuente |
| `ALIGN` | ini, fin, dir | Alineación horizontal (CENTER/LEFT/RIGHT) |
| `VALIGN` | ini, fin, dir | Alineación vertical (TOP/MIDDLE/BOTTOM) |
| `GRID` | ini, fin, grosor, color | Rejilla completa |
| `BOX` | ini, fin, grosor, color | Solo borde exterior |
| `INNERGRID` | ini, fin, grosor, color | Solo líneas interiores |
| `LINEABOVE` | ini, fin, grosor, color | Línea encima de la fila |
| `LINEBELOW` | ini, fin, grosor, color | Línea debajo de la fila |
| `SPAN` | ini, fin | Fusionar celdas |
| `RIGHTPADDING` | ini, fin, puntos | Padding derecho |
| `LEFTPADDING` | ini, fin, puntos | Padding izquierdo |
| `BOTTOMPADDING` | ini, fin, puntos | Padding inferior |

---

## 19. COLORES ÚTILES

```python
from reportlab.lib import colors

# Básicos
colors.black       colors.white       colors.grey
colors.red         colors.green       colors.blue
colors.yellow      colors.orange      colors.pink

# Oscuros
colors.darkblue    colors.darkgreen   colors.darkolivegreen

# Claros / pasteles
colors.lightblue   colors.lightgreen  colors.lightgrey
colors.lightcyan   colors.lightpink   colors.lavender
colors.lavenderblush

# Varios
colors.brown       colors.chocolate   colors.peru
colors.blueviolet

# Color personalizado RGB (valores 0.0 a 1.0)
colors.Color(0.2, 0.0, 0.6)

# Desde pdfgen.canvas (valores 0-255 se tratan como > 1.0)
from reportlab.pdfgen.canvas import Color
Color(150, 0, 0, 1)    # rojo saturado
```

---

## 20. FUENTES DISPONIBLES

```
Courier               Courier-Bold
Courier-Oblique       Courier-BoldOblique
Helvetica             Helvetica-Bold
Helvetica-Oblique     Helvetica-BoldOblique
Times-Roman           Times-Bold
Times-Italic          Times-BoldItalic
Symbol                ZapfDingbats
```

---

## 21. ESQUELETO DE INFORME COMPLETO

```python
import sqlite3
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.piecharts import Pie
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


def obtener_datos(limite=5):
    conn = sqlite3.connect("base_de_datos.bd")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.nome,
               SUM(lf.cantidade) AS total,
               SUM(lf.cantidade * lf.prezo_unitario * (1 - lf.desconto/100)) AS facturacion
        FROM linhas_factura lf
            JOIN produtos p ON lf.id_produto = p.id_produto
        GROUP BY p.id_produto
        ORDER BY total DESC
        LIMIT ?
    """, (limite,))
    res = cursor.fetchall()
    conn.close()
    return res


def crear_pdf(limite=5):
    datos = obtener_datos(limite)

    nombres   = [d[0] for d in datos]
    valores   = [d[1] for d in datos]
    facturas  = [d[2] for d in datos]

    # --- Estilos ---
    hoja = getSampleStyleSheet()
    p_titulo   = Paragraph("Título del Informe",       hoja["Title"])
    p_subgraf  = Paragraph("Subtítulo del Gráfico",    hoja["Heading2"])
    p_subtabla = Paragraph("Subtítulo de la Tabla",    hoja["Heading2"])

    # --- Gráfico de barras ---
    dibujo = Drawing(300, 150)
    grafico = VerticalBarChart()
    grafico.x, grafico.y   = 50, 50
    grafico.height, grafico.width = 100, 220
    grafico.data           = [valores]
    grafico.categoryAxis.categoryNames     = nombres
    grafico.categoryAxis.labels.angle      = 30
    grafico.categoryAxis.labels.dy         = -15
    grafico.categoryAxis.labels.boxAnchor  = 'ne'
    grafico.valueAxis.valueMin             = 0
    grafico.valueAxis.valueMax             = max(valores) + 10
    grafico.valueAxis.valueStep            = 10
    grafico.strokeColor    = colors.black
    grafico.groupSpacing   = 10
    grafico.barSpacing     = 2
    dibujo.add(grafico)

    # --- Tabla ---
    filas = [['Pos.', 'Producto', 'Uds.', 'Facturación']]
    for i, d in enumerate(datos):
        filas.append([i + 1, d[0], d[1], '%0.2f€' % (d[2],)])

    estilo = [
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR',  (0, 0), (-1, 0), colors.white),
        ('GRID',       (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN',      (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN',      (1, 0), (1, -1),  'LEFT'),
        ('ALIGN',      (-1, 1), (-1, -1), 'RIGHT'),
    ]
    for i in range(2, len(filas), 2):
        estilo.append(('BACKGROUND', (0, i), (-1, i), colors.lightgrey))

    tabla = Table(filas, colWidths=[40, 180, 80, 90])
    tabla.setStyle(estilo)

    # --- Texto de análisis ---
    texto = ("El producto más vendido es %s con %i uds. "
             "Los %i productos representan %i uds. y %0.2f€ de facturación."
             % (datos[0][0], datos[0][1], len(datos),
                sum(valores), sum(facturas)))
    p_analisis = Paragraph(texto, hoja["BodyText"])

    # --- Montar guion ---
    guion = []
    guion.append(p_titulo)
    guion.append(Spacer(0, 30))
    guion.append(p_subgraf)
    guion.append(dibujo)
    guion.append(Spacer(0, 40))
    guion.append(p_subtabla)
    guion.append(tabla)
    guion.append(Spacer(0, 40))
    guion.append(p_analisis)

    doc = SimpleDocTemplate("informe.pdf", pagesize=A4)
    doc.build(guion)


if __name__ == "__main__":
    crear_pdf(5)
```

---

## 22. ERRORES COMUNES

| Error | Causa | Solución |
|---|---|---|
| `grafico.data = [80, 65, 48]` | Data no es lista de listas | `grafico.data = [[80, 65, 48]]` |
| Tabla muestra datos en columnas cruzadas | Coordenadas `(col, fila)` confundidas con `(fila, col)` | Recordar: siempre `(col, fila)` |
| `def func(self, ...)` fuera de clase | `self` en función suelta | Quitar `self` del parámetro |
| PDF vacío o incompleto | Falta `conn.close()` o `doc.build(guion)` | Siempre cerrar conexión y llamar a `build` |
| `valueMax` demasiado pequeño | Barras se salen del área | Ajustar a `max(datos) + margen` |
| Texto desbordado en tabla | Sin `colWidths` definido | Añadir `colWidths=[...]` con anchos adecuados |
| Leyenda fuera del dibujo | Coordenadas `x, y` de la leyenda incorrectas | Ajustar `x, y` dentro del tamaño del `Drawing` |
| `textLines` vs `textLine` | Confundir singular y plural | `textLine(str)` = 1 línea; `textLines(str_con_\n)` = varias |
| `showPage()` sin `save()` en Canvas | PDF no se guarda | Siempre terminar con `hoja.save()` |
| Error al fusionar celdas | Celdas fusionadas sin datos vacíos `""` en el área | Rellenar con `""` las celdas del área del SPAN |

---

## 23. IMPORTS DE REFERENCIA RÁPIDA

```python
import sqlite3

# Core
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, A5
from reportlab.lib.styles import getSampleStyleSheet

# Canvas (control manual)
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF

# Platypus (flujo de documento)
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Table,
    TableStyle,
    Spacer,
    Image,
    Flowable,
    KeepTogether,
)

# Gráficos — contenedor
from reportlab.graphics.shapes import Drawing, Image as DrawingImage

# Gráficos — tipos
from reportlab.graphics.charts.barcharts  import VerticalBarChart, HorizontalBarChart
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.charts.piecharts  import Pie, Pie3d
from reportlab.graphics.charts.legends    import Legend, LineLegend
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.widgets.markers   import makeMarker
```