from reportlab.graphics.charts.legends import LineLegend, Legend
from reportlab.graphics.shapes import Drawing
from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.graphics.charts.barcharts import VerticalBarChart

hojaEstilo = getSampleStyleSheet()
estiloCuerpoTexto = hojaEstilo["BodyText"]
elementosDoc = []

dibujo = Drawing(600, 300)

grafico_barras = VerticalBarChart()

nombres = [["Memoria RAM DDR", "Portátil Dell", "Monitor Hp 24 pulgadas", "Torre de Macitosh", "Rato LG" ] ,
            [80, 65, 48, 31, 18 ]]


hojaEstilo = getSampleStyleSheet()
estiloCuerpoTexto = hojaEstilo["BodyText"]
elementosDoc = []

dibujo = Drawing(600, 300)

grafico_barras = VerticalBarChart()

grafico_barras.x = 50
grafico_barras.y = 50
grafico_barras.data = nombres[1:]
grafico_barras.strokeColor = colors.black
grafico_barras.valueAxis.valueMin = 0
grafico_barras.valueAxis.valueMax = 90
grafico_barras.valueAxis.valueStep = 16

grafico_barras.categoryAxis.labels.boxAnchor = 'ne'
grafico_barras.categoryAxis.labels.dx = -15
grafico_barras.categoryAxis.labels.dy = -15         # Desplazamiento vertical de etiquetas
grafico_barras.categoryAxis.labels.angle = 30       # Rotación de etiquetas en grados
grafico_barras.categoryAxis.categoryNames = nombres[0]

grafico_barras.groupSpacing = 10
grafico_barras.barSpacing = 2

dibujo.add(grafico_barras)
elementosDoc.append(dibujo)
documento = SimpleDocTemplate("examen_tarea1.pdf", pagesize = A4)
documento.build(elementosDoc)


