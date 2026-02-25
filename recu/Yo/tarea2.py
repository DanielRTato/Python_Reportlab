from reportlab.lib.colors import white
from reportlab.platypus import (Paragraph, Image, SimpleDocTemplate, Spacer, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen.canvas import Color

hojaEstilo = getSampleStyleSheet()
elementosDoc = []

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

elementosDoc.append(tabla)

# Generamos el PDF.
documento = SimpleDocTemplate("examen_tarea2.pdf", pagesize=A4)
documento.build(elementosDoc)
