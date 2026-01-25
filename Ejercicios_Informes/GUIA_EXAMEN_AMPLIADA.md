# Guía de Referencia Rápida: ReportLab (Examen DI)

Esta guía resume los patrones de código, importaciones y trucos utilizados en los ejercicios (`Ejercicios_Informes`) para generar PDFs con Python y ReportLab.

## 1. Estructura Básica (Boilerplate)

Casi todos los scripts comienzan así. Copia y pega esto para empezar.

```python
from reportlab.platypus import (SimpleDocTemplate, PageBreak, Image, Spacer, 
                                Paragraph, Table, TableStyle, Flowable)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
# Importaciones para gráficos
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.legends import Legend
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.widgets.markers import makeMarker

# 1. Configuración del documento
doc = SimpleDocTemplate("nombre_archivo.pdf", pagesize=A4)

# 2. Hoja de estilos
hojaEstilo = getSampleStyleSheet()
elementos = [] # Lista de flowables

# ... AQUI VA TU LÓGICA ...

# 3. Generar PDF
doc.build(elementos)
```

## 2. Textos y Párrafos

Cómo añadir títulos y texto normal cambiando colores o alineación.

```python
# Estilos comunes: 'Normal', 'BodyText', 'Heading1', 'Heading2', 'Title'
estilo = hojaEstilo["BodyText"]

# Modificaciones al vuelo
estilo.textColor = colors.darkgreen  # Color
estilo.alignment = 1                 # 0=Izq, 1=Centro, 2=Der
estilo.fontSize = 12                 # Tamaño
estilo.fontName = 'Helvetica-Bold'   # Fuente

# Crear y añadir
p = Paragraph("Hola Mundo", estilo)
elementos.append(p)
elementos.append(Spacer(1, 20)) # Espacio vertical de 20pt
```

## 3. Tablas (Lo más importante)

Las tablas se usan para datos y para **maquetar** (alinear cosas).

### Sistema de Coordenadas (Celdas)
Para aplicar estilos, ReportLab usa el sistema `(columna, fila)`. **¡Ojo! Empieza en 0.**
Recuerda: `(0,0)` es la esquina superior izquierda. Los índices negativos cuentan desde el final (`-1` es el último).

**Ejemplo Visual: Tabla 4 Columnas x 5 Filas**

| | Col 0 | Col 1 | Col 2 | Col 3 |
| :--- | :---: | :---: | :---: | :---: |
| **Fila 0** | (0,0) | (1,0) | (2,0) | (3,0) |
| **Fila 1** | (0,1) | (1,1) | (2,1) | (3,1) |
| **Fila 2** | (0,2) | (1,2) | (2,2) | (3,2) |
| **Fila 3** | (0,3) | (1,3) | (2,3) | (3,3) |
| **Fila 4** | (0,4) | (1,4) | (2,4) | (3,4) |

**Cómo seleccionar rangos (Sintaxis `start`, `end`):**
La sintaxis es `(col_inicio, fila_inicio), (col_fin, fila_fin)`.

1.  **Celda única (ej: (1,1)):** `(1,1), (1,1)`
2.  **Primera Fila (Cabecera):** `(0,0), (-1,0)` -> Desde primera col, fila 0 HASTA última col (-1), fila 0.
3.  **Primera Columna (Lateral):** `(0,0), (0,-1)` -> Desde col 0, primera fila HASTA col 0, última fila (-1).
4.  **Bloque central (2x2):** `(1,1), (2,2)` -> Selecciona (1,1), (2,1), (1,2) y (2,2).
5.  **Última Fila:** `(0,-1), (-1,-1)` -> Desde col 0, última fila HASTA última col, última fila.
6.  **Todo menos la cabecera:** `(0,1), (-1,-1)` -> Desde col 0, fila 1 HASTA el final de la tabla.

### Comandos de Estilo Comunes
*   **Alineación:** `ALIGN` (LEFT, CENTER, RIGHT), `VALIGN` (TOP, MIDDLE, BOTTOM).
*   **Fuentes:** `FONT` o `FONTNAME` (ej. 'Helvetica-Bold'), `FONTSIZE`.
*   **Bordes:** `GRID` (todo), `BOX` (borde ext), `INNERGRID` (rejilla int), `LINEBELOW` (subrayado).
*   **Padding:** `LEFTPADDING`, `RIGHTPADDING`, `TOPPADDING`, `BOTTOMPADDING`.
*   **Colores:** `BACKGROUND`, `TEXTCOLOR`.

```python
datos = [
    ["Cabecera 1", "Cabecera 2"],
    ["Dato 1", "Dato 2"],
    ["Total", "100€"]
]

tabla = Table(datos, colWidths=[100, 200], rowHeights=[30, 20, 20])

estilo_tabla = [
    # Sintaxis: ('COMANDO', (col_ini, fila_ini), (col_fin, fila_fin), VALOR)
    
    ('BACKGROUND', (0,0), (-1,0), colors.blue),      # Fondo cabecera
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),      # Texto cabecera blanco
    ('FONT', (0,0), (-1,0), 'Helvetica-Bold'),       # Fuente cabecera
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),             # Alineación horizontal
    ('valign', (0,0), (-1,-1), 'MIDDLE'),            # Alineación vertical
    ('BOX', (0,0), (-1,-1), 1, colors.black),        # Borde exterior
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.grey), # Rejilla interna
    
    # Ejemplo fila específica (Total)
    ('FONT', (0,-1), (-1,-1), 'Helvetica-BoldOblique'), 
]

tabla.setStyle(TableStyle(estilo_tabla))
elementos.append(tabla)
```

### Fusionar Celdas (SPAN)
Útil para títulos o logos en facturas.
```python
estilo = [
    # Fusionar desde columna 0, fila 0 HASTA columna 1, fila 0
    ('SPAN', (0,0), (1,0)) 
]
```

### Anidar Elementos en Celdas
Puedes meter imágenes o párrafos DENTRO de una celda.
```python
img = Image("check.png", 20, 20)
parrafo = Paragraph("Texto", hojaEstilo['Normal'])
datos = [ ["Fila simple", "Texto"], [[parrafo, img], "Celda compleja"] ]
```

## 4. Gráficos (Avanzado)

### Labels (Títulos dentro del gráfico)
```python
dibujo = Drawing(400, 200)
titulo = Label()
titulo.setOrigin(200, 180) # Posición X, Y
titulo.setText("Mi Gráfico")
titulo.fontSize = 12
dibujo.add(titulo)
```

### Barras Verticales (`VerticalBarChart`)
```python
grafico = VerticalBarChart()
grafico.x = 50; grafico.y = 50; grafico.height = 125; grafico.width = 300
grafico.data = [[10, 20, 30], [15, 25, 35]] 
grafico.categoryAxis.categoryNames = ['Ene', 'Feb', 'Mar']
grafico.valueAxis.valueMin = 0
grafico.valueAxis.valueMax = 40
grafico.groupSpacing = 10  # Espacio entre grupos de barras (Ene vs Feb)
grafico.barSpacing = 2     # Espacio entre barras del mismo grupo
dibujo.add(grafico)
```

### Líneas (`HorizontalLineChart`) con Marcadores
```python
lineas = HorizontalLineChart()
# ... configuración x, y, data ...
lineas.lines[0].strokeWidth = 2
lineas.lines[0].symbol = makeMarker('FilledCircle') # Puntos rellenos
lineas.lines[1].symbol = makeMarker('FilledTriangle') # Triángulos
dibujo.add(lineas)
```

### Tartas (`Pie`)
```python
tarta = Pie()
tarta.data = [10, 20, 70]
tarta.labels = ['A', 'B', 'C']
tarta.slices[1].popout = 10            # Sacar sector hacia fuera
tarta.sideLabels = 1                   # Líneas indicativas laterales
tarta.slices[0].fillColor = colors.red
dibujo.add(tarta)
```

### Leyendas (`Legend`) - ¡Truco Examen!
El truco es usar `colorNamePairs` con un bucle para enlazar colores y nombres automáticamente.

```python
leyenda = Legend()
leyenda.x = 350; leyenda.y = 150
leyenda.boxAnchor = 'ne' # Anclado al noreste
leyenda.columnMaximum = 1 

# Truco para auto-generar pares (Color, Texto) desde el gráfico
# Asume que 'grafico' es tu tarta o gráfico de barras
leyenda.colorNamePairs = [
    (grafico.slices[i].fillColor, grafico.labels[i]) 
    for i in range(len(grafico.data))
]
# O manual: [(colors.red, "Serie A"), (colors.blue, "Serie B")]

dibujo.add(leyenda)
```

## 5. Diseño Avanzado (Facturas y Elementos Flotantes)

### Técnica de la Tabla Maestra
Para maquetar la factura entera, usa una tabla invisible contenedora.
```python
# Izquierda (barra), Derecha (contenido)
tabla_maestra = Table([[barra_lateral, contenido_principal]], colWidths=[30, 480])
tabla_maestra.setStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]) # Alinear arriba
```

### Elementos "Fuera de Flujo" (Sidebar Decorativo)
Si te piden una barra lateral que va de arriba a abajo y se sale de los márgenes normales (visto en `Modelo_Factura1.py`), usa esta clase `PositionedTable`.

```python
class PositionedTable(Flowable):
    def __init__(self, table, x, y):
        Flowable.__init__(self)
        self.table = table
        self.x = x
        self.y = y
    def draw(self):
        self.canv.saveState()
        self.canv.translate(self.x, self.y) # Mover origen
        self.table.wrapOn(self.canv, 0, 0)
        self.table.drawOn(self.canv, 0, 0)
        self.canv.restoreState()

# Uso: coordenadas negativas relativas al margen
borde = PositionedTable(mi_tabla_borde, -60, -450)
elementos.append(borde)
```

## 6. Colores Útiles
```python
colors.red, colors.blue, colors.green, colors.white, colors.black, colors.grey
colors.lightgrey, colors.darkgreen, colors.orange, colors.darkolivegreen
Color(1, 0, 0, 0.5) # Rojo semi-transparente
```
