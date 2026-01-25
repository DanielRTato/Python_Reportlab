# Guía de Referencia Rápida: ReportLab (Examen DI)

Esta guía resume los patrones de código, importaciones y trucos utilizados en los ejercicios (`Ejercicios_Informes`) para generar PDFs con Python y ReportLab.

## 1. Estructura Básica (Boilerplate)

Casi todos los scripts comienzan así. Copia y pega esto para empezar.

```python
from reportlab.platypus import (SimpleDocTemplate, PageBreak, Image, Spacer, 
                                Paragraph, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

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

# Crear y añadir
p = Paragraph("Hola Mundo", estilo)
elementos.append(p)
elementos.append(Spacer(1, 20)) # Espacio vertical de 20pt
```

## 3. Tablas (Lo más importante)

Las tablas se usan para datos y para **maquetar** (alinear cosas).

### Sistema de Coordenadas (Celdas)
Para aplicar estilos, ReportLab usa el sistema `(columna, fila)`. **¡Ojo! Empieza en 0.**

| Columna 0 | Columna 1 | Columna 2 |
| :--- | :--- | :--- |
| (0, 0) | (1, 0) | (2, 0) | <- Fila 0
| (0, 1) | (1, 1) | (2, 1) | <- Fila 1
| (0, 2) | (1, 2) | (2, 2) | <- Fila 2
| (0, -1) | (1, -1) | (-1, -1) | <- -1 es "el último"

**Ejemplos de selección:**
```python
# Una sola celda (la (1,1) es columna 2, fila 2):
('BACKGROUND', (1, 1), (1, 1), colors.red)

# Una fila entera (fila 0):
('BACKGROUND', (0, 0), (-1, 0), colors.blue)

# Una columna entera (columna 0):
('BACKGROUND', (0, 0), (0, -1), colors.yellow)

# Toda la tabla:
('GRID', (0, 0), (-1, -1), 1, colors.black)
```

### Comandos de Estilo Comunes
Aquí tienes los más usados y sus valores:

*   **Alineación Horizontal (`ALIGN`):** `'LEFT'`, `'CENTER'`, `'RIGHT'`.
*   **Alineación Vertical (`VALIGN`):** `'TOP'`, `'MIDDLE'`, `'BOTTOM'`.
*   **Fuentes (`FONTNAME` y `FONTSIZE`):** `'Helvetica'`, `'Helvetica-Bold'`, etc.
*   **Bordes:**
    *   `'GRID'`: Rejilla completa (interior y exterior).
    *   `'BOX'` o `'OUTLINE'`: Solo el borde exterior.
    *   `'INNERGRID'`: Solo las líneas de dentro.
    *   `'LINEBELOW'`, `'LINEABOVE'`, `'LINEBEFORE'`, `'LINEAFTER'`: Líneas individuales.

```python
estilo_avanzado = [
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),        # Todo centrado horizontalmente
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),       # Todo centrado verticalmente
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'), # Cabecera en negrita
    ('FONTSIZE', (0,0), (-1,-1), 10),           # Tamaño de letra general
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),       # Margen inferior de celda
    ('TOPPADDING', (0,0), (-1,-1), 5),          # Margen superior de celda
    ('LINEBELOW', (0,0), (-1,0), 2, colors.black), # Línea gorda bajo cabecera
]
```

### Creación y Estilo Básico
```python
datos = [
    ["Cabecera 1", "Cabecera 2"],
    ["Dato 1", "Dato 2"],
    ["Dato 3", "Dato 4"]
]

tabla = Table(datos, colWidths=[100, 200]) # Anchos opcionales

estilo_tabla = [
    # Sintaxis: ('COMANDO', (col_ini, fila_ini), (col_fin, fila_fin), VALOR)
    # (-1, -1) significa el final.
    
    ('BACKGROUND', (0,0), (-1,0), colors.blue),      # Fondo cabecera
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),      # Texto cabecera blanco
    ('BOX', (0,0), (-1,-1), 1, colors.black),        # Borde exterior
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.grey), # Rejilla interna
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),            # Alineación vertical
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),             # Alineación horizontal
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

### Formato Condicional (Colores según valor)
Si te piden cambiar el color si un número es negativo o mayor a X (visto en `ejemplo_Tabla2.py`).

```python
estilo = [] # Lista vacía inicial

for i, fila in enumerate(datos):
    for j, valor in enumerate(fila):
        # Suponiendo que son números
        if type(valor) == int:
            if valor < 0:
                # Fondo azul para negativos en esa celda específica (j, i)
                estilo.append(('BACKGROUND', (j, i), (j, i), colors.blue))
            elif valor > 30:
                # Fondo rojo para altos
                estilo.append(('BACKGROUND', (j, i), (j, i), colors.red))

tabla.setStyle(TableStyle(estilo))
```

### Anidar Elementos en Celdas
Puedes meter imágenes o párrafos DENTRO de una celda.
```python
img = Image("check.png", 20, 20)
parrafo = Paragraph("Texto", hojaEstilo['Normal'])

# La celda es una LISTA de flowables
datos = [
    ["Fila simple", "Texto"],
    [[parrafo, img], "Celda compleja"] 
]
```

## 4. Gráficos (Drawing & Charts)

Necesitas importar clases específicas. ¡Ojo con las rutas!

### Imports Correctos (Visto en correcciones)
```python
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart, HorizontalBarChart
from reportlab.graphics.charts.piecharts import Pie, Pie3d
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.charts.lineplots import ScatterPlot # Ojo ruta
from reportlab.graphics.charts.spider import SpiderChart
from reportlab.graphics.legends import Legend
```

### Plantilla Genérica de Gráfico
```python
dibujo = Drawing(400, 200) # Ancho, Alto del área de dibujo

# Ejemplo: Barras Verticales
grafico = VerticalBarChart()
grafico.x = 50
grafico.y = 50
grafico.height = 125
grafico.width = 300
grafico.data = [[10, 20, 30], [15, 25, 35]] # Lista de listas (series)
grafico.categoryAxis.categoryNames = ['Ene', 'Feb', 'Mar']

# Configuración Ejes
grafico.valueAxis.valueMin = 0
grafico.valueAxis.valueMax = 40
grafico.valueAxis.valueStep = 10

dibujo.add(grafico)
elementos.append(dibujo)
```

### Gráfico de Tarta (Pie)
```python
tarta = Pie()
tarta.x = 100
tarta.y = 100
tarta.data = [10, 20, 70]
tarta.labels = ['A', 'B', 'C']
tarta.slices[0].fillColor = colors.red # Color sector 0
tarta.slices[1].popout = 10            # Sacar sector hacia fuera
dibujo.add(tarta)
```

## 5. Diseño de Facturas (Layout)

Evita usar posicionamiento absoluto (`PositionedTable`) si es posible. Usa la técnica de **"Tabla Maestra"**:

1. Crea una tabla grande invisible (sin bordes).
2. Divide la tabla en columnas (ej: Izquierda para barra lateral, Derecha para contenido).
3. Mete otras tablas dentro de esa tabla maestra.

```python
# Ejemplo Layout Factura
contenido_izquierda = Table([[""], [""]], colWidths=[20]) # Barra verde
contenido_derecha = [] # Lista con cabecera, tabla productos, totales...

# Creamos la tabla maestra
tabla_maestra = Table(
    [[contenido_izquierda, contenido_derecha]], 
    colWidths=[30, 480]
)

# Estilo invisible para la maestra
tabla_maestra.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'), # Todo alineado arriba
    ('LEFTPADDING', (0,0), (-1,-1), 0),
]))

elementos.append(tabla_maestra)
```

## 6. Colores Útiles
```python
colors.red, colors.blue, colors.green, colors.white, colors.black, colors.grey
colors.lightgrey, colors.darkgreen, colors.orange
# Transparente o custom
Color(1, 0, 0, 0.5) # Rojo 50% transparente
```
