from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4

d =Drawing(400, 200)

datos = [(13.3, 8, 14.3, 20, 22.1, 38.4, 12.5, 19.3, 27.2, 23.9, 17.6, 25.4)]
lendaDatos = ['11/23', '12/23', '01/24', '02/24', '03/24', '04/24', '05/11', '06/24', '07/25', '08/24', '09/21', '10/219', '11/18']

graficoBarras = VerticalBarChart()
graficoBarras.x = 50
graficoBarras.y = 50
graficoBarras.height = 125
graficoBarras.width = 300
graficoBarras.data = datos
graficoBarras.valueAxis.valueMin = 0 # Min value of 0
graficoBarras.valueAxis.valueMax = 70 # Max value of 70
graficoBarras.valueAxis.valueStep = 10 # Step of 10 units
graficoBarras.categoryAxis.labels.boxAnchor = 'ne' # North East
graficoBarras.categoryAxis.labels.dx = 8 # Shift labels right by 8,
graficoBarras.categoryAxis.labels.dy = -2 # Shift labels down by 2
graficoBarras.categoryAxis.labels.angle = 0 # Rotate labels by 30 degrees
graficoBarras.categoryAxis.categoryNames = lendaDatos
graficoBarras.groupSpacing = 10

d.add(graficoBarras)

doc = SimpleDocTemplate("exemploGrafos.pdf", pagesize=A4)

doc.build([d])

