# GUÍA EXAMEN REPORTLAB — 2DAM Diseño de Interfaces

---

## ESTRUCTURA GENERAL DE UN PDF

Todo informe sigue este patrón:

```python
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

guion = []  # lista de elementos que irán al PDF

# ... añadir elementos a guion ...

doc = SimpleDocTemplate("salida.pdf", pagesize=A4)
doc.build(guion)
```

---

## 1. PÁRRAFOS (Paragraph)

### Estilos disponibles
```python
hojaEstilo = getSampleStyleSheet()

estiloTitulo    = hojaEstilo["Title"]      # Título principal grande
estiloSubtitulo = hojaEstilo["Heading2"]   # Subtítulo (h2)
estiloH3        = hojaEstilo["Heading3"]   # Subtítulo (h3)
estiloTexto     = hojaEstilo["BodyText"]   # Texto normal
```

### Crear párrafos
```python
p_titulo    = Paragraph("Título del informe", estiloTitulo)
p_subtitulo = Paragraph("Subtítulo del gráfico", estiloSubtitulo)
p_texto     = Paragraph("Texto descriptivo del análisis...", estiloTexto)

guion.append(p_titulo)
guion.append(p_subtitulo)
guion.append(p_texto)
```

### Modificar propiedades del estilo
```python
estilo = hojaEstilo["Title"]
estilo.fontSize = 18
estilo.fontName = "Helvetica-Oblique"  # o "Helvetica", "Helvetica-Bold"
estilo.alignment = 1                   # 0=izq, 1=centro, 2=dcha
estilo.pageBreakBefore = 0
```

---

## 2. ESPACIADOR (Spacer)

Inserta espacio en blanco vertical entre elementos.

```python
from reportlab.platypus import Spacer

guion.append(Spacer(0, 30))   # 30 puntos de espacio
guion.append(Spacer(1, 60))   # también válido con 1 como primer arg
```

---

## 3. TABLA (Table + TableStyle)

### Crear datos y tabla
```python
from reportlab.platypus import Table, TableStyle

datos = [
    ["Posición", "Producto",         "Uds. Vendidas", "Facturación"],  # cabecera
    ["1",        "Memoria RAM DDR",  "81",            "324.08€"],
    ["2",        "Portátil DELL",    "71",           "3648.39€"],
    ["3",        "Monitor HP 24\"",  "51",            "429.39€"],
    ["4",        "Torre Macintosh",  "27",           "3239.76€"],
    ["5",        "Rato LG",          "25",            "632.67€"],
]

tabla = Table(datos, colWidths=[60, 200, 100, 90])  # anchos de columna opcionales
```

### Estilos de tabla — referencia de coordenadas
```
(col, fila) — empieza en (0,0) = esquina superior izquierda
(-1, -1)    = última columna, última fila
(0, 0), (-1, 0) = toda la fila 0 (cabecera)
(0, 0), (-1, -1) = toda la tabla
```

### Propiedades de estilo más usadas
```python
estilo = [
    # Fondo cabecera
    ('BACKGROUND', (0, 0), (-1, 0),  colors.brown),     # o darkblue, green...
    # Color texto cabecera
    ('TEXTCOLOR',  (0, 0), (-1, 0),  colors.white),
    # Cuadrícula completa
    ('GRID',       (0, 0), (-1, -1), 1, colors.black),
    # Solo borde exterior
    ('BOX',        (0, 0), (-1, -1), 1, colors.black),
    # Solo líneas interiores
    ('INNERGRID',  (0, 0), (-1, -1), 0.25, colors.black),
    # Alineación: CENTER, LEFT, RIGHT
    ('ALIGN',      (0, 0), (-1, -1), 'CENTER'),
    ('ALIGN',      (1, 0), (1, -1),  'LEFT'),   # columna 1 a la izquierda
    ('ALIGN',      (-1, 1), (-1, -1), 'RIGHT'),  # última columna a la dcha
    # Filas alternas
    ('BACKGROUND', (0, 2), (-1, 2),  colors.lightgrey),
    ('BACKGROUND', (0, 4), (-1, 4),  colors.lightgrey),
]

tabla.setStyle(estilo)
guion.append(tabla)
```

### Filas alternas con bucle (dinámico)
```python
for i in range(2, len(datos), 2):   # filas pares (0-indexadas): 2, 4, 6...
    estilo.append(('BACKGROUND', (0, i), (-1, i), colors.lightgrey))
```

### Construir tabla desde BD (patrón)
```python
fila0 = ['Pos.', 'Nombre', 'Uds.', 'Facturación']
tabla_datos = [fila0]

for i, dato in enumerate(resultados):
    fila = [i + 1, dato[0], dato[1], '%0.2f€' % (dato[2],)]
    tabla_datos.append(fila)

tab = Table(tabla_datos)
tab.setStyle(estilo)
guion.append(tab)
```

---

## 4. GRÁFICO DE BARRAS VERTICAL (VerticalBarChart)

```python
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart

# Datos
nombres = ["Memoria RAM DDR", "Portátil Dell", "Monitor HP", "Torre Macintosh", "Rato LG"]
valores = [80, 65, 48, 31, 18]

# Lienzo
dibujo = Drawing(400, 200)   # ancho, alto

# Gráfico
grafico = VerticalBarChart()
grafico.x = 70          # posición X dentro del lienzo
grafico.y = 45          # posición Y dentro del lienzo
grafico.height = 170    # alto del gráfico
grafico.width = 170     # ancho del gráfico

# IMPORTANTE: data debe ser lista de listas
grafico.data = [valores]

# Eje de valores (Y)
grafico.valueAxis.valueMin  = 0
grafico.valueAxis.valueMax  = 90
grafico.valueAxis.valueStep = 16

# Eje de categorías (X) — etiquetas
grafico.categoryAxis.categoryNames = nombres
grafico.categoryAxis.labels.boxAnchor = 'ne'
grafico.categoryAxis.labels.dx    = -15   # desplazamiento horizontal
grafico.categoryAxis.labels.dy    = -15   # desplazamiento vertical
grafico.categoryAxis.labels.angle = 30    # rotación en grados

# Apariencia
grafico.strokeColor   = colors.black
grafico.groupSpacing  = 10
grafico.barSpacing    = 2

dibujo.add(grafico)
guion.append(dibujo)
```

---

## 5. GRÁFICO DE TARTA / SECTORES (Pie)

```python
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

# Datos
nombres    = ["Cliente A", "Cliente B", "Cliente C", "Cliente D", "Cliente E"]
valores    = [1200.50, 980.00, 750.25, 640.10, 500.00]

ancho, alto = 400, 350
dibujo = Drawing(ancho, alto)

tarta = Pie()
tarta.x      = ancho/2 - 100   # centrado horizontal
tarta.y      = alto/2 - 50     # centrado vertical
tarta.width  = 200
tarta.height = 200
tarta.data   = valores
tarta.labels = nombres
tarta.slices.strokeWidth = 0.5
tarta.sideLabels = 1           # etiquetas a los lados

# Colores por sector
colores_lista = [colors.blue, colors.darkgreen, colors.pink, colors.red, colors.peru]
for i, color in enumerate(colores_lista):
    tarta.slices[i].fillColor = color

dibujo.add(tarta)
guion.append(dibujo)
```

---

## 6. CONSULTA SQLITE

### Patrón básico
```python
import sqlite3

def obtener_datos(path_bd, limite=5):
    conn   = sqlite3.connect(path_bd)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT columna1, columna2
        FROM tabla
        WHERE condicion
        LIMIT ?
    """, (limite,))
    resultados = cursor.fetchall()
    conn.close()
    return resultados
```

### Consulta productos más vendidos (examen)
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

### Consulta clientes por facturación (examen Jorge)
```python
cursor.execute("""
    SELECT c.nome,
           COUNT(DISTINCT f.id_factura) AS num_facturas,
           SUM(lf.cantidade * lf.prezo_unitario * (1 - lf.desconto/100) * (1 + p.iva/100)) AS facturacion_total
    FROM clientes c
        JOIN facturas f      ON c.id_cliente  = f.id_cliente
        JOIN linhas_factura lf ON f.id_factura = lf.id_factura
        JOIN produtos p      ON lf.id_produto  = p.id_produto
    GROUP BY c.id_cliente, c.nome
    ORDER BY facturacion_total DESC
    LIMIT ?
""", (limite,))
```

---

## 7. TEXTO DE ANÁLISIS (patrón)

```python
# Calcular totales
total_unidades   = sum([d[1] for d in datos])
total_facturacion = sum([d[2] for d in datos])

texto = (
    "O producto más vendido é %s con %i unidades. "
    "No total, os %i productos más vendidos representan %i unidades vendidas "
    "e unha facturación de %0.2f €."
    % (datos[0][0], datos[0][1], len(datos), total_unidades, total_facturacion)
)

p_analisis = Paragraph(texto, estiloTexto)
guion.append(p_analisis)
```

---

## 8. ESQUELETO COMPLETO DE INFORME (tarea3 / examen tipo)

```python
import sqlite3
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

def obtener_datos(limite=5):
    conn = sqlite3.connect("bdTendaOrdeadoresBig.bd")
    cursor = conn.cursor()
    cursor.execute("SELECT ... LIMIT ?", (limite,))
    res = cursor.fetchall()
    conn.close()
    return res

def crear_pdf(limite=5):
    datos = obtener_datos(limite)

    # --- Estilos ---
    hoja = getSampleStyleSheet()
    p_titulo    = Paragraph("Título del informe",      hoja["Title"])
    p_subgraf   = Paragraph("Subtítulo del gráfico",   hoja["Heading2"])
    p_subtabla  = Paragraph("Subtítulo de la tabla",   hoja["Heading2"])

    # --- Gráfico ---
    nombres = [d[0] for d in datos]
    valores = [d[1] for d in datos]
    dibujo = Drawing(300, 150)
    grafico = VerticalBarChart()
    grafico.x, grafico.y = 50, 50
    grafico.data = [valores]
    grafico.categoryAxis.categoryNames = nombres
    grafico.valueAxis.valueMin  = 0
    grafico.valueAxis.valueMax  = max(valores) + 10
    grafico.valueAxis.valueStep = 10
    grafico.categoryAxis.labels.angle = 30
    grafico.categoryAxis.labels.dy    = -15
    grafico.strokeColor = colors.black
    grafico.groupSpacing = 10
    grafico.barSpacing   = 2
    dibujo.add(grafico)

    # --- Tabla ---
    tabla_datos = [['Pos.', 'Producto', 'Uds.', 'Facturación']]
    for i, d in enumerate(datos):
        tabla_datos.append([i+1, d[0], d[1], '%0.2f€' % (d[2],)])
    estilo = [
        ('BACKGROUND', (0,0), (-1,0), colors.brown),
        ('TEXTCOLOR',  (0,0), (-1,0), colors.white),
        ('GRID',       (0,0), (-1,-1), 1, colors.black),
        ('ALIGN',      (0,0), (-1,-1), 'CENTER'),
        ('ALIGN',      (1,0), (1,-1),  'LEFT'),
    ]
    for i in range(2, len(tabla_datos), 2):
        estilo.append(('BACKGROUND', (0,i), (-1,i), colors.lightgrey))
    tabla = Table(tabla_datos, colWidths=[40, 180, 80, 90])
    tabla.setStyle(estilo)

    # --- Texto análisis ---
    texto = ("El producto más vendido es %s con %i uds. "
             "Los %i productos representan %i uds. y %0.2f€ de facturación."
             % (datos[0][0], datos[0][1], len(datos),
                sum(d[1] for d in datos), sum(d[2] for d in datos)))
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

## 9. COLORES ÚTILES

| Variable                | Color visual      |
|-------------------------|-------------------|
| `colors.white`          | Blanco            |
| `colors.black`          | Negro             |
| `colors.brown`          | Marrón            |
| `colors.darkblue`       | Azul oscuro       |
| `colors.blue`           | Azul              |
| `colors.green`          | Verde             |
| `colors.darkgreen`      | Verde oscuro      |
| `colors.lightgreen`     | Verde claro       |
| `colors.lightgrey`      | Gris claro        |
| `colors.red`            | Rojo              |
| `colors.pink`           | Rosa              |
| `colors.peru`           | Marrón claro      |

---

## 10. ERRORES COMUNES A EVITAR

| Error                                      | Solución                                              |
|--------------------------------------------|-------------------------------------------------------|
| `grafico.data = valores`                   | Debe ser `grafico.data = [valores]` (lista de listas) |
| Usar `self` en función fuera de clase      | Eliminar `self` del parámetro                         |
| Coordenadas tabla invertidas `(fila, col)` | Siempre es `(col, fila)` en ReportLab                 |
| `conn` sin `conn.close()`                  | Siempre cerrar la conexión                            |
| `valueMax` menor que el valor máximo real  | Ajustar `valueMax` a los datos reales                 |
| Olvidar `if __name__ == "__main__"`        | Añadir al final para ejecución directa                |

---

## 11. IMPORTS DE REFERENCIA RÁPIDA

```python
import sqlite3

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer

from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.piecharts import Pie
```