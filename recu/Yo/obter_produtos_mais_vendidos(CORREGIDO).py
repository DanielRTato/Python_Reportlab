import sqlite3

from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, Spacer, Paragraph
from reportlab.graphics.charts.barcharts import VerticalBarChart



def obter_productos_mais_vendidos(self, limite = 5):
    conn = sqlite3.connect("bdTendaOrdeadoresBig.bd")
    cursor = conn.cursor()

    cursor.execute("""
        select
         p.nome, 
         SUM(if.cantidade) as total_vendido,
        SUM(if.cantidade * if.prezo_unitario * (1 - if.desconto/100)) as facturacion
    from linhas_factura if
        join produtos p on if.id_produto = p.id_produto
    group by p.id_produto, p.nome
    order by total_vendido desc
    limit ?
    """, (limite,))

    resultados = cursor.fetchall()
    conn.close()

    return resultados

def crearPDF(limite = 5):
    datos = obter_productos_mais_vendidos(limite)
    print(datos)

    nombres = []
    precios = []

    for dato in datos:
        nombres.append(dato[0])
        precios.append(dato[1])

    print (nombres)
    print(precios)

    # ------------------------------Grafico----------------------------------
    d3 = Drawing(400,200)
    grafico = VerticalBarChart()
    grafico.x = 70
    grafico.y = 45
    grafico.height = 170
    grafico.width = 170
    grafico.data = [precios]
    grafico.categoryAxis.categoryNames = nombres
    grafico.strokeColor = colors.black
    grafico.valueAxis.valueMin = 0
    grafico.valueAxis.valueMax = 90
    grafico.valueAxis.valueStep = 16
    grafico.categoryAxis.labels.boxAnchor = 'ne'
   # grafico.categoryAxis.labels.dx = -15
    grafico.categoryAxis.labels.dy = -15  # Desplazamiento vertical de etiquetas
    grafico.categoryAxis.labels.angle = 30  # Rotación de etiquetas en grados


    grafico.groupSpacing = 10
    grafico.barSpacing = 2

    d3.add(grafico)

    # ------------------------------Tabla----------------------------------

    fila0 = ['Posición','Producto','Unidades Vendidas', 'Facturación']
    tabla = [fila0]

    for i, dato in enumerate(datos):
        fila = [i+1, dato[0], dato[1], '%0.2f€' % (dato[2],)]
        tabla.append(fila)

    estilo = [
        ("TEXTCOLOR", (0, 0), (3, 0), colors.white),
        ('BACKGROUND', (0, 0), (3, 0), colors.brown),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),

    ]

    for i in range(2,len(datos),2):
        estilo.append(('BACKGROUND', (0,i), (-1, i), colors.lightgrey))

    tab = Table(tabla)
    tab.setStyle(estilo)


    #------------------------------Texto----------------------------------

    hojaEstilo = getSampleStyleSheet()

    texto = ("O producto más vendito e %s con %i unidades. No total, os %i productos más vendidos representa %i unidades vendidas e unha fcturación de %0.2f €." % (datos[0][0], datos[0][1], len(datos), sum(precios), sum([dato[2] for dato in datos])))

    estiloTitulo = hojaEstilo["Title"]
    estiloSubtitulo = hojaEstilo["Heading2"]
    estiloboddy = hojaEstilo["BodyText"]

    p_titulo = Paragraph("El título del informe", estiloTitulo)
    p_subtitulo = Paragraph("Esto es el subtítulo del Gráfico de barras", estiloSubtitulo)
    p_subtabla = Paragraph("Esto es el subtítulo de la tabla", estiloSubtitulo)
    p_informe = Paragraph(texto, estiloboddy)



    gion = []
    gion.append(p_titulo)
    gion.append(Spacer(0,20))
    gion.append(p_subtabla)
    gion.append(tab)
    gion.append(Spacer(0,40))
    gion.append(p_subtitulo)
    gion.append(d3)
    gion.append(Spacer(0,40))
    gion.append(p_informe)
    doc = SimpleDocTemplate("Examen_Grupo1.pdf", pagesize=A4)
    doc.build(gion)





if __name__ == "__main__":
    crearPDF(5)