from reportlab.platypus import Paragraph, Image, Spacer, SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A5
from reportlab.lib import colors, styles
from reportlab.platypus import KeepTogether

guion = []
hoja = getSampleStyleSheet()

sp = Spacer(20,20) #Crea un espacio en blanco de 20×20 puntos para separar elementos verticalmente.

cabecera = hoja["Heading1"]
cabecera.fontSize=13
cabecera.alignment=0
cabecera.textColor = colors.black
titulo=Paragraph("FACTURA Proforma", cabecera)

"""
Tabla 1
"""
l1 = ['FACTURAR A:', 'Nº FACTURA']
l2 = ['Cliente', 'Fecha']
l3 = ['Domicilio', 'Nº del pedido']
l4 = ['Código postal/ciudad','Fecha de vencimiento']
l5 = ['(NIF)', 'Condiciones de pago']


tab1 = Table([l1, l2, l3, l4, l5], hAlign='CENTER') #Crea la tabla 1 con las filas definidas y la alinea horizontalmente al centro.
tab1.setStyle([
    ('INNERGRID', (0, 0), (1,4), 0.5, colors.lightgrey), #Dibuja líneas internas de la tabla (todas las celdas de 0,0 a 1,4) con grosor 0.5 y color gris claro
    ('RIGHTPADDING', (0, 0), (0,4), 35), #Añade relleno a la derecha de la columna 0 (izquierda) en todas las filas: 35 puntos.
    ('LEFTPADDING', (1, 0), (1,4), 35),
    ('BACKGROUND', (0,0), (1,4), colors.lightgrey),
    ('FONTSIZE', (1,0), (1,0), 12),
])

"""
Tabla 2
"""
t1 = ['Pos.\n', 'Concepto/Descripción\n', 'Cantidad\n', 'Unidad\n', 'Precio\nunitario', 'Importe\n'] #Cabecera de la tabla 2: 6 columnas, con saltos de línea en algunas celdas para ajustar el texto.
t2 = ['1', '', '', '', '', '']
t3 = ['2', '', '', '', '', '']
blanc = ['', '', '', '', '', '']

tab2 = Table([t1, t2, t3, blanc],  hAlign='CENTER')
tab2.setStyle([
    ('FONTSIZE', (0,0), (5,3), 8),
    ("BOX", (0,0), (5,3), 0.5, colors.black),
    ('RIGHTPADDING', (0, 0), (5,3), 6),
    ('LEFTPADDING', (1, 0), (5,3), 6),
    ('INNERGRID', (0, 0), (5,3), 0.5, colors.black), #Líneas internas de la tabla (rejilla completa).
    ('BACKGROUND', (0, 0), (5,0), colors.lightgrey),
])

"""
Tabla 3
"""
m1 = ['Método de pago:', '']
b = ['','']
tab3 = Table([m1, b])
tab3.setStyle([
    ('BOX', (0, 0), (1, 1), 0.5, colors.black),
    ('FONTSIZE', (0, 0), (0, 0), 8),
    ('RIGHTPADDING', (0, 0), (0, 1), 50),
    ('BOTTOMPADDING', (0, 0), (1, 1), 10),
])

"""
Tabla 4
"""
k1 = ['Importe neto', '']
k2 = ['+ IVA de ||| %', '']
k3 = ['- IRPF de ||| %', '']
k5 = ['IMPORTE BRUTO', '']

tab4 = Table([k1, k2, k3, k5], hAlign='LEFT')
tab4.setStyle([
    ('INNERGRID', (0,0), (1,3), 0.5, colors.black),
    ('LINEABOVE',(0,3), (1,3), 1.5, colors.black),
    ('BOX', (0, 0), (1, 3), 0.5, colors.black),
    ('BACKGROUND', (0, 3), (1, 3), colors.lightgrey),
    ('RIGHTPADDING', (1, 3), (1, 3), 20),
])

'''
Crea una tabla que en la primera fila tiene tab3 y tab4 como celdas (dos columnas), y en la segunda fila la lista b (dos celdas vacías).
Es decir, una tabla “contenedora” que coloca tab3 y tab4 en la misma fila.
'''

tablaa = Table([[tab3, tab4], b])
tablaa.setStyle([
    ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ('VALIGN', (0,0), (0,0), 'TOP'),
])

guion.append(titulo)
guion.append(sp)
guion.append(tab1)
guion.append(sp)
guion.append(tab2)
guion.append(sp)
guion.append(sp)
guion.append(tablaa)


doc = SimpleDocTemplate("Factura22.pdf", pagesize=A5, showBoundary=0)
doc.build (guion)