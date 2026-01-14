from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

gion = []
imaxe = Image("equis23x23.jpg", 50 , 50)

co1 = [' ', ' ', '' , '', 'FACTURA SIMPLIFICADA']
co2 = ['Nombre de tu Empresa', ' ', '' , '', [imaxe]]
co3 = ['Dirección ', ' ', '' , '', '']
co4 = ['Ciudad y País', ' ', '' , '', '']
co5 = ['CIF/NIF ', ' ', '' , '', '']
co6 = ['Teléfono ', ' ', '' , 'Fecha Emisión', 'DD/MM/AAAA']
co7 = ['Mail ', ' ', '' , '', '']
co8 = ['', 'Descripción', 'Importe ', 'Cantidad' , 'Total']
co10 = [' ', ' ', '' , '', '']
co11 = [' ', ' ', '' , '', '']
co12 = [' ', ' ', '' , '', '']
co13 = [' ', ' ', '' , '', '']
co15 = [' ', ' ', '' , '', '']
co16 = [' ', ' ', '' , '', '']

taboa = Table([co1, co2, co3, co4, co5, co6, co7, co8])


gion.append(taboa)
doc = SimpleDocTemplate("FacturaSimple.pdf", pagesize=A4, showBoundary=0)
doc.build(gion)

