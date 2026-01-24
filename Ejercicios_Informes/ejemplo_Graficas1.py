import os
from reportlab.graphics.charts.legends import LineLegend, Legend
from reportlab.graphics.shapes import Drawing
from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.graphics.charts.piecharts import Pie, Pie3d

hojaEstilo = getSampleStyleSheet() # Obtenemos la hoja de estilos.

estiloCuerpoTexto = hojaEstilo["BodyText"] # Obtenemos el estilo de cuerpo de texto (aunque no se usa mucho aquí).

elementosDoc = [] # Lista para los elementos "flowables" del documento.

# Datos de temperaturas: [Meses, Temperaturas Máximas, Temperaturas Mínimas].
temperaturas = [
    ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","Julio","Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
    [15, 16, 20, 25, 27, 31, 35, 38, 30, 25, 20, 18], # Máximas
    [-3, -4, -1, 4, 6, 9, 12, 15, 16, 10, 2, -2]     # Mínimas
]

## --- GRÁFICO DE BARRAS VERTICALES ---

# Definimos un área de dibujo de 400x200 puntos.
dibujo = Drawing(450,200)

# Creamos el objeto gráfico de barras verticales.
grafico_barras = VerticalBarChart() #HorizontalBarChart()

# Posición del gráfico dentro del área de dibujo (Drawing).
grafico_barras.x = 50
grafico_barras.y = 50
# Dimensiones del gráfico (el área donde se pintan las barras).
grafico_barras.height = 125
grafico_barras.width = 300

# Asignamos los datos numéricos (excluyendo la primera lista que son las etiquetas de meses).
grafico_barras.data = temperaturas[1:]

# Color del borde de las barras.
grafico_barras.strokeColor = colors.black

# Configuración del eje de valores (Y).
grafico_barras.valueAxis.valueMin = -5  # Valor mínimo
grafico_barras.valueAxis.valueMax = 40  # Valor máximo
grafico_barras.valueAxis.valueStep = 5  # Paso entre marcas

# Configuración del eje de categorías (X).
grafico_barras.categoryAxis.labels.boxAnchor = 'ne' # Anclaje de las etiquetas (ne = north east)
grafico_barras.categoryAxis.labels.dx = 8           # Desplazamiento horizontal de etiquetas
grafico_barras.categoryAxis.labels.dy = -15         # Desplazamiento vertical de etiquetas
grafico_barras.categoryAxis.labels.angle = 30       # Rotación de etiquetas en grados
grafico_barras.categoryAxis.categoryNames = temperaturas[0] # Asignamos los nombres de los meses

# Espaciado entre grupos de barras y entre barras individuales.
grafico_barras.groupSpacing = 10
grafico_barras.barSpacing = 2

# Añadimos el gráfico al dibujo.
dibujo.add(grafico_barras)

# Añadimos el dibujo al documento PDF.
elementosDoc.append(dibujo)
elementosDoc.append(Spacer(50, 50))


## --- GRÁFICO DE LÍNEAS HORIZONTAL ---

# Nueva área de dibujo.
dibujo = Drawing(400,200)

# Creamos el gráfico de líneas.
gl = HorizontalLineChart()
gl.x = 50
gl.y = 50
gl.height = 125
gl.width = 300

# Asignamos datos y etiquetas de categorías.
gl.data = temperaturas[1:]
gl.categoryNames = temperaturas[0]

# Configuración de etiquetas del eje X.
gl.categoryAxis.labels.boxAnchor = 'ne'
gl.categoryAxis.labels.angle = 30
gl.categoryAxis.labels.dx = 10
gl.categoryAxis.labels.dy = -20
gl.categoryAxis.categoryNames = temperaturas[0]

# Configuración del eje Y.
gl.valueAxis.valueMin = 0
gl.valueAxis.valueMax = 40
gl.valueAxis.valueStep = 10

# Personalización de las líneas.
# Línea 0 (Máximas): grosor 1, con marcadores circulares rellenos.
gl.lines[0].strokeWidth = 1
gl.lines[0].symbol = makeMarker('FilledCircle')
# Línea 1 (Mínimas): grosor 5, sin marcadores especiales.
gl.lines[1].strokeWidth = 5

# Añadimos el gráfico de líneas al dibujo.
dibujo.add(gl)

# Creación de la leyenda para el gráfico de líneas.
leyenda = LineLegend()
leyenda.fontSize = 8
leyenda.fontName = "Helvetica"
leyenda.alignment = "right"
leyenda.x = 0
leyenda.y = -15
leyenda.columnMaximum = 2 # Máximo número de columnas en la leyenda

# Definimos las series manualmente para la leyenda.
series = ["Máximas", "Minimas"]
# Creamos pares de (Color, Nombre) para la leyenda, tomando el color de las líneas del gráfico.
leyenda.colorNamePairs = [(gl.lines[i].strokeColor, series[i]) for i in range(len(gl.data))]

# Añadimos la leyenda al dibujo.
dibujo.add(leyenda)

# Añadimos el dibujo al documento.
elementosDoc.append(dibujo)
elementosDoc.append(Spacer(50, 35))


## --- GRÁFICO DE TARTA (PIE CHART) 3D ---

# Nueva área de dibujo más pequeña.
dibujo = Drawing(300,200)

# Creamos el gráfico de tarta 3D.
tarta = Pie3d()
tarta.x = 65
tarta.y = 15
tarta.data = [10, 5, 20, 25, 40] # Datos porcentuales o absolutos
tarta.labels = ['Edge', 'Brave', 'Firefox', 'Safari', 'Chrome'] # Etiquetas

# Personalización de los sectores (slices).
tarta.slices.strokeWidth = 0.5
# Resaltamos el sector 3 (Safari) separándolo del centro ("popout").
tarta.slices[3].popout = 10
tarta.slices[3].strokeWidth = 2
tarta.slices[3].strokeDashArray = [2,2] # Borde discontinuo
tarta.slices[3].labelRadius = 2 # Radio para la etiqueta
tarta.slices[3].fontColor = colors.blue

# Etiquetas laterales activadas.
tarta.sideLabels = 1

# Añadimos la tarta al dibujo.
dibujo.add(tarta)

# Creamos una leyenda compleja para la tarta.
leyenda = Legend()
leyenda.x = 300
leyenda.y = 5
leyenda.dx = 10
leyenda.dy = 10
leyenda.fontName = "Helvetica"
leyenda.fontSize = 7
leyenda.boxAnchor = 'n'
leyenda.columnMaximum = 15
leyenda.strokeWidth = 0.5
leyenda.strokeColor = colors.grey
leyenda.deltax = 75 # Separación horizontal entre elementos
leyenda.deltay = 10 # Separación vertical
leyenda.autoXPadding = 5
leyenda.yGap = 1
leyenda.dxTextSpace = 3
leyenda.alignment = "right"
# Líneas divisorias en la leyenda (combinación de bits flags).
leyenda.dividerLines = 1|2|4 
leyenda.dividerOffsY = 4.5
leyenda.subCols.rpad = 30

# Asignamos colores personalizados a los sectores y construimos la leyenda.
paresColorLeyenda = list()
colores = [colors.red, colors.green, colors.blue, colors.yellow, colors.pink]
for i, color in enumerate(colores):
    tarta.slices[i].fillColor = color # Cambiamos color del sector
    paresColorLeyenda.append((color, tarta.labels[i])) # Añadimos a la leyenda

leyenda.colorNamePairs = paresColorLeyenda

# Añadimos leyenda al dibujo.
dibujo.add(leyenda)

# Añadimos el dibujo final al documento.
elementosDoc.append(dibujo)

# Construimos el PDF final.
documento = SimpleDocTemplate("ejemplo_Graficas1.pdf", pagesize = A4)
documento.build(elementosDoc)
