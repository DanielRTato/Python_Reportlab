from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle, Spacer, Flowable, Image

# FACTURA 2 EN PDF

hojaEstilo = getSampleStyleSheet()
elementosDoc = []

# --- CABECERA E IMAGEN ---
cabecera_estilo = hojaEstilo["Heading1"]
cabecera_estilo.alignment = 0 # Alineación Izquierda
cabecera_estilo.fontSize = 16

cabecera = Paragraph("FACTURA Proforma", cabecera_estilo)

# Cargamos la imagen "imgLogo.png".
# Es importante que esta imagen exista en el directorio de trabajo, si no, dará error.
imagen = Image("imgLogo.png")

# Creamos una tabla para alinear el título y la imagen lado a lado.
tabla_cabecera = Table([
    [cabecera, imagen]
], colWidths=[200, 250])

tabla_cabecera.setStyle([
    ('VALIGN',(0,0),(0,0),'MIDDLE'), # Alineamos verticalmente al centro.
])


# --- SECCIÓN DE CLIENTE Y FECHA (TABLA 1) ---
datos_tabla1 = [
    ["FACTURAR A:", "", "Nº FACTURA:"],
    # Usamos \n para saltos de línea dentro de la celda.
    ["Cliente\nDomicilio\nCódigo postal/ciudad\n(NIF)", "", "Fecha\n\nNº de pedido\n\nFecha de vencimiento\n\nCondiciones de pago"]
]

tabla1 = Table(datos_tabla1, colWidths=[150, 150])

tabla1.setStyle([
    # Fondo gris claro para toda la tabla.
    ('BACKGROUND',(0,0),(-1,-1),colors.lightgrey),
    # Tamaño de fuente para la celda de "Nº FACTURA:".
    ('FONTSIZE',(2,0),(2,0),12),
    # Alineación vertical media para la segunda fila.
    ('VALIGN',(0,1),(0,1),'MIDDLE')
])


# --- TABLA DE DETALLES (TABLA 2) ---
datos_tabla2 = [
    ["Pos.", "Concepto/Descripción", "Cantidad", "Unidad", "Precio\nunitario", "Importe"],
    ["1", "", "", "", "", ""],
    ["2", "", "", "", "", ""],
    ["", "", "", "", "", ""]
]

# Definimos anchos de columna específicos.
tabla2 = Table(datos_tabla2, colWidths=[45, 145, 60, 50, 90, 60])

tabla2.setStyle([
    # Cabecera (primera fila) con fondo gris y texto centrado.
    ('BACKGROUND',(0,0),(-1,0),colors.grey),
    ('ALIGN',(0,0),(-1,0),'CENTER'),
    ('VALIGN',(0,0),(-1,0),'TOP'),
    # Rejilla negra para toda la tabla.
    ('GRID',(0,0),(-1,-1),1,colors.black)
])


# --- TABLA DE TOTALES Y PAGO (TABLA 3) - TABLAS ANIDADAS ---

## SubTabla 1: Método de pago (Izquierda)
datos_subtabla1 = [
    ["Método de pago:"]
]
subtabla1 = Table(datos_subtabla1, colWidths=[220], rowHeights=[50])
subtabla1.setStyle([
    ('FONTSIZE',(0,0),(-1,-1),8),
    ('GRID',(0,0),(-1,-1),1,colors.black),
    ('ALIGN',(0,0),(-1,-1),'LEFT'),
    ('VALIGN',(0,0),(-1,-1),'TOP'),
])

## Subtabla 2: Cálculos de importes (Derecha)
datos_subtabla2 = [
    ["Importe neto", ""],
    ["+ IVA de    %", ""],
    ["- IRPFF de    %", ""],
    ["IMPORTE BRUTO", ""]
]
subtabla2 = Table(datos_subtabla2, colWidths=[80, 40])
subtabla2.setStyle([
    ('FONTSIZE',(0,0),(-1,-1),8),
    # Negrita para "IMPORTE BRUTO".
    ('FONT',(0,3),(0,3),'Helvetica-Bold'),
    ('GRID',(0,0),(-1,-1),1,colors.black),
    ('ALIGN',(0,0),(-1,-1),'LEFT'),
    # Fondo gris para la fila de importe bruto.
    ('BACKGROUND',(0,3),(-1,3),colors.grey)
])

## Tabla 3: Contenedora principal
# Insertamos las subtablas (objetos Table) directamente dentro de las celdas de tabla3.
# Esto permite layouts complejos.
datos_tabla3 = [
    [subtabla1, "", subtabla2]
]

tabla3 = Table(datos_tabla3, colWidths=[220, 110, 130])

tabla3.setStyle([
    # Alineamos todo arriba para que las subtablas empiecen al mismo nivel.
    ('VALIGN',(0,0),(-1,-1),'TOP')
])


# --- PIE DE PÁGINA ---
pie_estilo = hojaEstilo["BodyText"]
pie_estilo.alignment = 0
pie_estilo.fontSize = 10

pie1 = Paragraph("Gracias por su confianza.", pie_estilo)
pie2 = Paragraph("Atentamente,", pie_estilo)


# --- CONSTRUCCIÓN DEL DOCUMENTO ---
elementosDoc.append(tabla_cabecera)
elementosDoc.append(Spacer(0, 10))
elementosDoc.append(tabla1)
elementosDoc.append(Spacer(0, 30))
elementosDoc.append(tabla2)
elementosDoc.append(Spacer(0, 60))
elementosDoc.append(tabla3)
elementosDoc.append(Spacer(0, 10))
elementosDoc.append(pie1)
elementosDoc.append(Spacer(0, 20))
elementosDoc.append(pie2)

# Generación del PDF.
doc = SimpleDocTemplate("Modelo_Factura2.pdf", pagesize=A4)
doc.build(elementosDoc)
