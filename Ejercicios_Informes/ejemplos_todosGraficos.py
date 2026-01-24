import os
from reportlab.graphics.shapes import Drawing, String
from reportlab.platypus import SimpleDocTemplate, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
import importlib

# Carga dinámica y segura de clases de reportlab
def try_import(module_name, class_name):
    try:
        mod = importlib.import_module(module_name)
        return getattr(mod, class_name)
    except Exception:
        return None

# Intentamos resolver las clases desde los módulos más comunes. Si no están, quedan en None y se usa fallback.
VerticalBarChart = try_import('reportlab.graphics.charts.barcharts', 'VerticalBarChart')
HorizontalBarChart = try_import('reportlab.graphics.charts.barcharts', 'HorizontalBarChart')

HorizontalLineChart = try_import('reportlab.graphics.charts.linecharts', 'HorizontalLineChart')
VerticalLineChart = try_import('reportlab.graphics.charts.linecharts', 'VerticalLineChart')

LinePlot = try_import('reportlab.graphics.charts.lineplots', 'LinePlot')

# ScatterPlot está en lineplots en esta versión
ScatterPlot = try_import('reportlab.graphics.charts.lineplots', 'ScatterPlot')

# Pie / Doughnut
Pie = try_import('reportlab.graphics.charts.piecharts', 'Pie')
Pie3d = try_import('reportlab.graphics.charts.piecharts', 'Pie3d')
# Doughnut tiene su propio módulo
Doughnut = try_import('reportlab.graphics.charts.doughnut', 'Doughnut')

# Spider se llama SpiderChart
Spider = try_import('reportlab.graphics.charts.spider', 'SpiderChart')
# Candlestick no parece estar disponible en la instalación estándar, dejamos None
Candlestick = try_import('reportlab.graphics.charts.candlestick', 'Candlestick')

# Datos reutilizables de ejemplo
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 30]
multi_series = [[10, 20, 15, 30], [12, 18, 22, 28]]
scatter_points = [(1, 10), (2, 20), (3, 15), (4, 30)]
pie_values = [30, 20, 25, 25]
spider_values = [4, 3, 5, 2]
candles = [
    # (x, open, high, low, close)
    (1, 10, 14, 8, 12),
    (2, 12, 18, 11, 17),
    (3, 17, 20, 15, 16),
]

# Lista de flowables/drawings para el documento
elements = []

# Helper para añadir una sección con título y dibujo
def add_section(title, make_chart_fn, width=450, height=200):
    d = Drawing(width, height)
    # Título en la parte superior
    d.add(String(5, height - 15, title, fontSize=12))
    try:
        make_chart_fn(d, width, height)
    except Exception as e:
        # Si algo falla al crear el gráfico, añadimos una nota en el dibujo
        d.add(String(10, height/2, f"Omitido: error creando gráfico - {e}", fontSize=9, fillColor=colors.red))
    elements.append(d)
    elements.append(Spacer(1, 12))

# Implementaciones concretas (si la clase no existe, el make_chart_fn lanzará o hará el fallback)

# Vertical Bar Chart
def make_vertical_bar(d, w, h):
    if not VerticalBarChart:
        raise ImportError('VerticalBarChart no disponible')
    gb = VerticalBarChart()
    gb.x = 50
    gb.y = 30
    gb.width = 300
    gb.height = 120
    gb.data = multi_series
    gb.categoryAxis.categoryNames = categories
    gb.valueAxis.valueMin = 0
    gb.valueAxis.valueMax = max(max(s) for s in multi_series) + 5
    gb.valueAxis.valueStep = 5
    gb.groupSpacing = 10
    gb.barSpacing = 2
    gb.strokeColor = colors.black
    d.add(gb)

# Horizontal Bar Chart
def make_horizontal_bar(d, w, h):
    if not HorizontalBarChart:
        raise ImportError('HorizontalBarChart no disponible')
    hb = HorizontalBarChart()
    hb.x = 100
    hb.y = 10
    hb.width = 300
    hb.height = 120
    hb.data = multi_series
    hb.categoryAxis.categoryNames = categories
    hb.valueAxis.valueMin = 0
    hb.valueAxis.valueMax = max(max(s) for s in multi_series) + 5
    d.add(hb)

# Horizontal Line Chart
def make_horizontal_line(d, w, h):
    if not HorizontalLineChart:
        raise ImportError('HorizontalLineChart no disponible')
    gl = HorizontalLineChart()
    gl.x = 50
    gl.y = 30
    gl.width = 300
    gl.height = 120
    gl.data = multi_series
    gl.categoryNames = categories
    gl.categoryAxis.categoryNames = categories
    gl.valueAxis.valueMin = 0
    gl.valueAxis.valueMax = max(max(s) for s in multi_series) + 5
    gl.valueAxis.valueStep = 5
    # Personalizaciones simples si existen
    try:
        gl.lines[0].strokeWidth = 1
        gl.lines[1].strokeWidth = 1
    except Exception:
        pass
    d.add(gl)

# Vertical Line Chart
def make_vertical_line(d, w, h):
    if not VerticalLineChart:
        raise ImportError('VerticalLineChart no disponible')
    vl = VerticalLineChart()
    vl.x = 50
    vl.y = 30
    vl.width = 300
    vl.height = 120
    vl.data = multi_series
    vl.categoryAxis.categoryNames = categories
    vl.valueAxis.valueMin = 0
    vl.valueAxis.valueMax = max(max(s) for s in multi_series) + 5
    d.add(vl)

# LinePlot (puede comportarse distinto según versión)
def make_lineplot(d, w, h):
    if not LinePlot:
        raise ImportError('LinePlot no disponible')
    lp = LinePlot()
    lp.x = 50
    lp.y = 30
    lp.width = 300
    lp.height = 120
    # LinePlot suele aceptar series de pares (x,y) o listas; aquí generamos pares sencillos
    series = [(i+1, v) for i, v in enumerate(values)]
    lp.data = [series]
    # Ajuste de ejes si existen
    try:
        lp.xValueAxis.valueMin = 0
        lp.xValueAxis.valueMax = len(values) + 1
        lp.yValueAxis.valueMin = 0
        lp.yValueAxis.valueMax = max(values) + 5
    except Exception:
        pass
    d.add(lp)

# ScatterPlot
def make_scatter(d, w, h):
    if not ScatterPlot:
        raise ImportError('ScatterPlot no disponible')
    sp = ScatterPlot()
    sp.x = 50
    sp.y = 30
    sp.width = 300
    sp.height = 120
    # ScatterPlot puede recibir data en diferentes formatos; intentamos usar la forma básica
    try:
        sp.data = [scatter_points]
    except Exception:
        # convertir a listas separadas
        sp.data = [list(zip(*scatter_points))]
    d.add(sp)

# Pie charts
def make_pie(d, w, h):
    if not Pie:
        raise ImportError('Pie no disponible')
    p = Pie()
    p.x = 100
    p.y = 20
    p.width = 120
    p.height = 120
    p.data = pie_values
    p.labels = [str(x) for x in pie_values]
    d.add(p)

def make_pie3d(d, w, h):
    if not Pie3d:
        raise ImportError('Pie3d no disponible')
    p = Pie3d()
    p.x = 90
    p.y = 10
    p.data = pie_values
    p.labels = ["P1", "P2", "P3", "P4"]
    d.add(p)

def make_doughnut(d, w, h):
    if not Doughnut:
        raise ImportError('Doughnut no disponible')
    dough = Doughnut()
    dough.x = 90
    dough.y = 10
    dough.width = 120
    dough.height = 120
    dough.data = pie_values
    dough.labels = ["D1", "D2", "D3", "D4"]
    d.add(dough)

# Spider chart
def make_spider(d, w, h):
    if not Spider:
        raise ImportError('Spider no disponible')
    sp = Spider()
    sp.x = 200
    sp.y = 80
    sp.width = 120
    sp.height = 120
    # Spider espera una lista de listas o similar; probamos con datos sencillos
    try:
        sp.data = [spider_values]
        sp.labels = categories[:len(spider_values)]
    except Exception:
        raise
    d.add(sp)

# Candlestick
def make_candlestick(d, w, h):
    if not Candlestick:
        raise ImportError('Candlestick no disponible')
    cs = Candlestick()
    cs.x = 50
    cs.y = 30
    cs.width = 300
    cs.height = 120
    cs.data = candles
    d.add(cs)

# Construimos secciones para cada tipo
add_section('VerticalBarChart', make_vertical_bar)
add_section('HorizontalBarChart', make_horizontal_bar)
add_section('HorizontalLineChart', make_horizontal_line)
add_section('VerticalLineChart', make_vertical_line)
add_section('LinePlot', make_lineplot)
add_section('ScatterPlot', make_scatter)
add_section('Pie', make_pie)
add_section('Pie3d', make_pie3d)
add_section('Doughnut', make_doughnut)
add_section('Spider', make_spider)
add_section('Candlestick', make_candlestick)

# Generamos el PDF en la misma carpeta que el script
output_name = os.path.join(os.path.dirname(__file__), 'ejemplos_todosGraficos.pdf')

doc = SimpleDocTemplate(output_name, pagesize=A4)
print('Generando', output_name)
doc.build(elements)
print('PDF generado con', len(elements), 'elementos (incluyendo spacers)')
