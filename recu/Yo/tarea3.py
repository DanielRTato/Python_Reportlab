from examen.obter_produtos_mais_vendidos import obter_productos_mais_vendidos
from reportlab.graphics.charts.legends import LineLegend, Legend
from reportlab.graphics.shapes import Drawing
from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.graphics.charts.barcharts import VerticalBarChart

hojaEstilo = getSampleStyleSheet()
estiloTitulo = hojaEstilo["Title"]
estiloSubtitulo = hojaEstilo["Heading2"]
estilobody = hojaEstilo["BodyText"]


p_titulo = Paragraph("El título del informe", estiloTitulo)
p_subgrafico = Paragraph("Esto es el subtitulo del Gráfico de barras",estiloSubtitulo)
p_subtabala = Paragraph("Esto es el subtitulo de la Tabla", estiloSubtitulo)
p_informe = Paragraph('''
O priduti máis vendido é Memoria RAM DDR con 81 unidades. No total, os 5 produtos máis vendidos representan
255 ubnidades vendidas e unha facturación de 10974.83€.
''', estilobody
)



elementosDoc = []

dibujo = Drawing(600, 150)

grafico_barras = VerticalBarChart()

nombres = [["Memoria RAM DDR", "Portátil Dell", "Monitor Hp 24 pulgadas", "Torre de Macitosh", "Rato LG" ] ,
            [80, 65, 48, 31, 18 ]]


hojaEstilo = getSampleStyleSheet()
estiloCuerpoTexto = hojaEstilo["BodyText"]

dibujo1 = Drawing(300, 150)

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

dibujo1.add(grafico_barras)
elementosDoc.append(p_titulo)
elementosDoc.append(p_subgrafico)
elementosDoc.append(dibujo1)

hojaEstilo = getSampleStyleSheet()


elementosDoc.append(Spacer(1, 60))



datos = [
    ["Posición", "Produto", "unidades Vendidas", "Facturación"],
    ["1", "Memoria RAM DDR", "81", "324.08€"],
    ["2", "Portátil DELL", "71", "3648.39€"],
    ["3", "Monitor HP 24 polgadas", "51", "429.39€"],
    ["4", "Torre Macintosh", "27", "3239.76€"],
    ["5", "Rato LG", "25", "632.67€"],
]

estilo = [
    ("TEXTCOLOR", (0, 0), (3, 0), colors.white),
    ('BACKGROUND', (0, 0), (3, 0), colors.brown),
    ('BACKGROUND', (0, 2), (3, 2), colors.lightgrey),
    ('BACKGROUND', (0, 4), (3, 4), colors.lightgrey),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('ALIGN', (1, 0), (1, -1), 'LEFT'),

]
tabla = Table(datos, colWidths=[60, 200, 100, 90])

tabla.setStyle(estilo)
elementosDoc.append(p_subtabala)

elementosDoc.append(tabla)
elementosDoc.append(Spacer(1, 60))

elementosDoc.append(p_informe)

# Generamos el PDF.
documento = SimpleDocTemplate("examen_tarea3.pdf", pagesize=A4)
documento.build(elementosDoc)
