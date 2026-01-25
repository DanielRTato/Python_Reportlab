from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle, Spacer, Image

from Ejercicios_Informes.ejemplo_Tabla1 import documento

hojaEstilo = getSampleStyleSheet()  # Obtenemos la hoja de estilos de muestra.

elementosDoc = []  # Lista para los elementos del documento.

imagen = Image("check.png", 20, 20)  # Cargamos una imagen pequeña (20x20).
estiloTitulo = hojaEstilo["Heading1"]
estiloTitulo2 = hojaEstilo["Heading2"]

parrafo1 = Paragraph("Factura Simplificada", estiloTitulo)
parrafo2 = Paragraph("Nombre de la Empresa", estiloTitulo2)

datos1 = [
    [" ", " ", " ", " ", parrafo1],
    [parrafo2, " ", " ", " ", imagen],
    ["Dirección ", " ", " ", " ", " "],
    ["Ciudad y País ", " ", " ", " ", ""],
    ["CIF/NIF ", " ", " ", "Fecha Emisión ", "DD/MM/AAAA"],
    ["Teléfono ", " ", " ", "Número de Factura ", "A001"],
    ["Mail ", " ", " ", " ", ""]
]

estilo1 = [
    ("TEXTCOLOR", (4, 0), (4, 0), colors.olive)
]

tabla1 = Table(data=datos1)
tabla1.setStyle(estilo1)

datos2 = [
    ["Descripción", "Importe", "Cantidad", "Total"],
    ["Producto 1", "10.00 €", "2", "20.00 €"],
    ["Producto 2 ", "15.00 €", "1", "15.00 €"],
    ["Producto 3 ", "5.00 €", "5", "25.00 €"],
    ["Producto 4 ", "213", "2.45", "60.00 €"],
    ["Producto 5 ", "12", "11", "12.60 €"],
    ["Producto 6 ", "09,45", "12312", "72.60 €"]
]

estilo2 = [
    ("INNERGRID", (0, 0), (-1, -1), 0, colors.white),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONT", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("BACKGROUND", (0, 0), (-1, 0), colors.darkgreen),
    ("BACKGROUND", (0, 1), (-1, -1), colors.lightgreen),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('GRID', (0, 0), (-1, -1), 1, colors.white),
    ('ALIGN', (3, 1), (-1, -1), 'RIGHT'),

]

tabla2 = Table(data=datos2, colWidths=[200, 100, 100, 100, 100, 100])
tabla2.setStyle(estilo2)

elementosDoc.append(tabla1)
elementosDoc.append(Spacer(0, 30))
elementosDoc.append(tabla2)

documento = SimpleDocTemplate("exemplo_Factura1.pdf", pagesize=A4)
documento.build(elementosDoc)
