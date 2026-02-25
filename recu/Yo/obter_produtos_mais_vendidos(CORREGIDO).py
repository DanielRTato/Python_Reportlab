import sqlite3
from tokenize import cookie_re

from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate
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
    grafico.x = 100
    grafico.y = 15
    grafico.height = 170
    grafico.width = 170
    grafico.data = [precios]
    grafico.categoryAxis.categoryNames = nombres

    d3.add(grafico)

    gion = []
    gion.append(d3)
    doc = SimpleDocTemplate("Examen_Grupo1.pdf", pagesize=A4)
    doc.build(gion)





if __name__ == "__main__":
    crearPDF(5)