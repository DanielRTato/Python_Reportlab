from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.charts.piecharts import Pie, Pie3d
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.rl_settings import strikeWidth

#Tamaño del grafico
d = Drawing(400,200)

#etiqueta de titulo
titulo = Label()

#asignamos la posición de la etiqueta
titulo.setOrigin(200,180)

#añadimos el texto
titulo.setText("Porcentaje contratados/aprobados")

#añadimos el titulo al documento
d.add(titulo)

#etiqueta del lateral del grafico
etiquetaLateral = Label()

etiquetaLateral.setOrigin(10,100)

#en teoría coloca el texto en 90 grados
etiquetaLateral.angle = 90

#
etiquetaLateral.setText("Porcentaje")

d.add(etiquetaLateral)

#------------PARAMETROS DEL GRAFICO (falta documentar)---------------

datos = [(13.3,8,14.3,25,33.3,37.5,21.1,28.6,45.5,38.1,54.6,36.0,42.3), (67,69,68,81,92,90,87,82,77,79,59,69,61)]
lendaDatos = ['11/12','12/13','13/14','14/15','15/16','16/17','17/18','18/19','19/20','20/21','21/22','22/23','23/24','24/25']

#tipo de grafico, en este caso barras verticales
graficoBarras = VerticalBarChart()

graficoBarras.x = 50
graficoBarras.y = 50
graficoBarras.height = 125
graficoBarras.width = 300
graficoBarras.data = datos
graficoBarras.valueAxis.valueMin = 0
graficoBarras.valueAxis.valueMax = 100
graficoBarras.valueAxis.valueStep = 10
graficoBarras.categoryAxis.labels.boxAnchor = 'ne'
graficoBarras.categoryAxis.labels.dx = 8
graficoBarras.categoryAxis.labels.dy = -10
graficoBarras.categoryAxis.labels.angle = 30
graficoBarras.categoryAxis.categoryNames = lendaDatos
#espace los graficos
graficoBarras.groupSpacing = 10
#se espacea entre las barras
graficoBarras.barSpacing = 3

d.add(graficoBarras)

#-------NUEVO GRAFICO-------

d2 = Drawing(400,200)

#Se va a realizar un gráfico de lineas
graficoLineas = HorizontalLineChart()

#Le tenemos que dar coordenadas
graficoLineas.x = 30
graficoLineas.y = 50

#le damos tamaño
graficoLineas.height = 125
graficoLineas.width = 300

#le añadimos los datos
graficoLineas.data = datos

#le pasamos la etiqueta de los datos de la linea horizontal
graficoLineas.categoryAxis.categoryNames = lendaDatos

#la dirección del anaclaje, en este caso Norte = n
graficoLineas.categoryAxis.labels.boxAnchor = "n"

#Valores minimos y maximos
graficoLineas.valueAxis.valueMin = 0
graficoLineas.valueAxis.valueMax = 100

#saltos entre valores
graficoLineas.valueAxis.valueStep = 20

#stroke es el grosor de la linea
graficoLineas.lines[0].strokeWidth = 2

# le ponemos un "punto" en cada valor del dato
graficoLineas.lines[0].symbol = makeMarker('FilledCircle')

#grosor de la linea 2
graficoLineas.lines[1].strokeWidth = 1.5

#colocamos un triangulo en los puntos de cada valor
graficoLineas.lines[1].symbol = makeMarker('FilledTriangle')

d2.add(graficoLineas)

#-----------NUEVO GRAFICO----------------

d3 = Drawing(400,200)

graficoTarta = Pie()

#dimensiones dentro del dibujo d3
graficoTarta.x = 65
graficoTarta.y = 15
graficoTarta.width = 170
graficoTarta.height = 170

graficoTarta.data = [10,20,30,40,50]

graficoTarta.labels = ['Oppo','Pixel','Galaxy','Iphone','Xiaomi']

#son las "porciones" de la tarta, el ancho de la linea
graficoTarta.slices.strokeWidth = 0.5

#la porción "3" se va a destacar
graficoTarta.slices[3].popout = 10

#a la porción 3 tiene una linea de contorno especial intermitente
graficoTarta.slices[3].strokeDashArray = [5,2]

#
graficoTarta.slices[3].labelRadius = 3

#le damos color a la descripción de la porción
graficoTarta.slices[3].fontColor = colors.red

#crea una linea indicativa de sección de gráfico y su definición
graficoTarta.sideLabels = 1

#reasignaremos colores al gráfico
colores = [colors.blue, colors.red, colors.green, colors.yellow, colors.orange]

for i, color in enumerate(colores):
    graficoTarta.slices[i].fillColor = color

d3.add(graficoTarta)

#--------------OBJETO LEGEND(la leyenda del gráfico)----------

leyenda = Legend()

#hay que pasar una lista con el nombre de los valores de los colores, primero color luego la leyenda
#primero el color de relleno
#segundo se metería los nombres de moviles y el porcentaje que tiene el nombre en la tarta
leyenda.colorNamePairs = [(graficoTarta.slices[i].fillColor,
                           (graficoTarta.labels[i][0:20],'%0.2f' % graficoTarta.data[i] ))
                            for i in range (len(graficoTarta.data))]

#coordenadas de la leyenda
leyenda.x = 370
leyenda.y = 5

#fuente de la leyenda
leyenda.fontName = 'Helvetica'

#tamaño de la letra en la leyenda
leyenda.fontSize = 7

#posición a donde esta anclada la leyenda
leyenda.boxAnchor = 'n'

#delimita el máximo de columnas
leyenda.columnMaximum = 3

#
leyenda.strokeWidth = 1

#
leyenda.strokeColor = colors.black

#
leyenda.deltax = 20

#separa los elementos entre sí con el deltay
leyenda.deltay = 10

#separación entre las columnas
leyenda.autoXPadding = 20

#seperación entre los valores
leyenda.yGap = 0

# espaciado del texto dentro de su celda (el espaciado es del color)
leyenda.dxTextSpace = 10

#alinea el color a la izquierda de la palabra que lo relaciona
leyenda.alignment = 'right'

# son lineas divisoras en binario (no se como usar esta monda)
leyenda.dividerLines = 7

#esto mueve a la linea divisora
leyenda.dividerOffsY = 5.5

#subCols separa las columnas dentro de la leyenda
leyenda.subCols.rpad = 15

d3.add(leyenda)

#---------------------------------------

doc = SimpleDocTemplate("ExemploGrafico.pdf", pagesize=A4)
doc.build([d, Spacer(20,20), d2, Spacer(20,20), d3])