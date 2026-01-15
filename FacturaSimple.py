from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

gion = []
imaxe = Image("equis23x23.jpg", 50, 50)

co1 = [' ', ' ', '', '', 'FACTURA SIMPLIFICADA']
co2 = ['Nombre de tu Empresa', ' ', '', '', [imaxe]]
co3 = ['Dirección ', ' ', '', '', '']
co4 = ['Ciudad y País', ' ', '', '', '']
co5 = ['CIF/NIF ', ' ', '', 'Fecha Emisión', 'DD/MM/AAAA']
co6 = ['Teléfono ', ' ', '', 'Número de Factura', 'A0001']
co7 = ['Mail ', ' ', '', '', '']
co8 = ['', 'Descripción', 'Importe ', 'Cantidad', 'Total']
co10 = [' ', 'Producto 1 ', '3,2', '5', '16,00']
co11 = [' ', 'Producto 2 ', '2,1', '3', '6,30']
co12 = [' ', 'Producto 3 ', '2,9', '76', '220,40']
co13 = [' ', 'Producto 4 ', '5', '23', '115,00']
co15 = [' ', 'Producto 5 ', '4,95', '3', '14,85']
co16 = [' ', 'Producto 6 ', '6', '2', '12,00']

taboa = Table([co1, co2, co3, co4, co5, co6, co7, co8, co10, co11, co12, co13, co15, co16],
              colWidths=[0, 150, 80, 80, 80])

taboa.setStyle([('TEXTCOLOR', (0, 0), (7, 7), colors.green),
                ('BOX', (0, 0), (-1, -1), 0, colors.black),
                ('INNERGRID', (0, 0), (-1, -1), 0, colors.lightgrey),
                ('BACKGROUND', (0, 7), (7, 7), colors.darkgreen),
                ('ALIGN', (0, 7), (7, 13), 'CENTER'),
                ('ALIGN', (5, 3), (5, 3), 'CENTER'),
                ])

gion.append(taboa)
doc = SimpleDocTemplate("FacturaSimple.pdf", pagesize=A4, showBoundary=0)
doc.build(gion)
