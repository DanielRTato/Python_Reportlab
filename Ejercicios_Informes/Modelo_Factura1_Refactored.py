from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle, Spacer

# FACTURA 1 REFACTORIZADA (Sin PositionedTable)
# En lugar de usar una clase personalizada para posicionar la barra lateral fuera del flujo,
# usamos una "Tabla Contenedora Principal" que divide la página en dos columnas:
# Columna 1: Barra lateral decorativa.
# Columna 2: Contenido de la factura.

# 1. Configuración inicial
nombre_archivo = "Modelo_Factura1_Refactored.pdf"
# Ajustamos márgenes para aprovechar mejor el espacio con la tabla contenedora
documento = SimpleDocTemplate(nombre_archivo, pagesize=A4, rightMargin=20, leftMargin=20, topMargin=20, bottomMargin=20)

hojaEstilo = getSampleStyleSheet()
elementos_principales = []

# 2. Creación del CONTENIDO de la factura (Columna Derecha)
# ---------------------------------------------------------
contenido_factura = []

# Cabecera
estilo_cabecera = hojaEstilo["Heading1"]
estilo_cabecera.textColor = colors.darkolivegreen
estilo_cabecera.alignment = 2  # Derecha
estilo_cabecera.fontSize = 16
contenido_factura.append(Paragraph("FACTURA SIMPLIFICADA", estilo_cabecera))
contenido_factura.append(Spacer(1, 20))

# Nombre y Logo
estilo_nombre = hojaEstilo["Heading2"]
estilo_nombre.textColor = colors.darkgreen
estilo_nombre.fontSize = 16
estilo_nombre.alignment = 0  # Izquierda
p_nombre = Paragraph("Nombre de tu empresa", estilo_nombre)

estilo_logo = hojaEstilo["Heading2"]
estilo_logo.textColor = colors.darkgreen
estilo_logo.fontSize = 12
p_logo = Paragraph("Logo de la empresa", estilo_logo)

# Tabla para alinear nombre y logo en la misma fila
tabla_encabezado = Table([
    [p_nombre, "", p_logo]
], colWidths=[250, 50, 150])
tabla_encabezado.setStyle(TableStyle([
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('ALIGN', (2, 0), (2, 0), 'RIGHT'),  # Logo a la derecha
]))
contenido_factura.append(tabla_encabezado)
contenido_factura.append(Spacer(1, 20))

# Datos Dirección y Factura
datos_info = [
    ["Dirección", "", "Fecha Emisión", "DD/MMM/AAA"],
    ["Ciudad y País", "", "Número de Factura", "A0001"],
    ["CIF/NIF", "", "", ""],
    ["Teléfono", "", "", ""],
    ["Mail", "", "", ""]
]
tabla_info = Table(datos_info, colWidths=[100, 150, 100, 100])
tabla_info.setStyle(TableStyle([
    ('FONT', (0, 0), (0, -1), 'Helvetica-BoldOblique'),  # Etiquetas dirección
    ('FONT', (2, 0), (2, -1), 'Helvetica-Bold'),  # Etiquetas fecha/num
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.darkgreen),
    ('ALIGN', (2, 0), (2, 1), 'RIGHT'),  # Alinear etiquetas fecha derecha
]))
contenido_factura.append(tabla_info)
contenido_factura.append(Spacer(1, 30))

# Tabla de Productos
datos_productos = [
    ["Descripción", "Importe", "Cantidad", "Total"],
    ["Producto 1", "3,2", "5", "16,00"],
    ["Producto 2", "2,1", "3", "6,30"],
    ["Producto 3", "2,9", "76", "220,40"],
    ["Producto 4", "5", "23", "115,00"],
    ["Producto 5", "4,95", "3", "14,85"],
    ["Producto 6", "6", "2", "12,00"]
]
tabla_productos = Table(datos_productos, colWidths=[190, 90, 80, 90])
tabla_productos.setStyle(TableStyle([
    # Cabecera
    ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
    # Cuerpo
    ('BACKGROUND', (0, 1), (-1, -1), colors.lightgreen),
    ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
    ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
    ('GRID', (0, 0), (-1, -1), 1, colors.white),
]))
contenido_factura.append(tabla_productos)
contenido_factura.append(Spacer(1, 10))

# Totales
datos_totales = [
    ["", "", "TOTAL", "385 €"]
]
tabla_totales = Table(datos_totales, colWidths=[190, 90, 80, 90])
tabla_totales.setStyle(TableStyle([
    ('FONT', (2, 0), (3, 0), 'Helvetica-Bold'),
    ('BACKGROUND', (2, 0), (3, 0), colors.darkgreen),
    ('TEXTCOLOR', (2, 0), (3, 0), colors.white),
    ('ALIGN', (2, 0), (3, 0), 'CENTER'),
    ('VALIGN', (2, 0), (3, 0), 'MIDDLE'),
    ('GRID', (2, 0), (3, 0), 1, colors.white),
    ('FONTSIZE', (2, 0), (3, 0), 12)
]))
contenido_factura.append(tabla_totales)
contenido_factura.append(Spacer(1, 30))

# Línea y Pie
linea = Table([[""]], colWidths=[450], rowHeights=[1])
linea.setStyle(TableStyle([
    ('LINEBELOW', (0, 0), (-1, -1), 1, colors.black)
]))
contenido_factura.append(linea)
contenido_factura.append(Spacer(1, 20))

estilo_pie = hojaEstilo["BodyText"]
estilo_pie.textColor = colors.darkgreen
estilo_pie.alignment = 1  # Centro
estilo_pie.fontName = "Helvetica-Bold"
contenido_factura.append(Paragraph("GRACIAS POR SU CONFIANZA", estilo_pie))

# 3. Creación de la BARRA LATERAL (Columna Izquierda)
# ---------------------------------------------------
# Simulamos la barra visual usando una celda alta con colores o una tabla anidada.
# Para mayor control, usamos una tabla anidada dentro de la columna izquierda.
# Altura aproximada del contenido para calcular la barra: ~600 puntos.
tabla_barra = Table([
    [""],  # Verde oscuro
    [""],  # Verde claro
    [""],  # Blanco
    [""]  # Verde claro
], colWidths=[20], rowHeights=[50, 400, 5, 100])

tabla_barra.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, 0), colors.darkgreen),
    ('BACKGROUND', (0, 1), (0, 1), colors.lightgreen),
    ('BACKGROUND', (0, 2), (0, 2), colors.white),
    ('BACKGROUND', (0, 3), (0, 3), colors.lightgreen),
    ('LEFTPADDING', (0, 0), (-1, -1), 0),
    ('RIGHTPADDING', (0, 0), (-1, -1), 0),
]))

# 4. TABLA MAESTRA (Layout Principal)
# -----------------------------------
# Estructura: [ [Barra Lateral, Contenido Factura] ]
# Nota: El contenido de la factura es una LISTA de flowables.
# Para meter una lista de flowables en una celda de Table, ReportLab lo acepta directamente.

datos_maestros = [
    [tabla_barra, contenido_factura]
]

tabla_maestra = Table(datos_maestros, colWidths=[30, 480])
tabla_maestra.setStyle(TableStyle([
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),  # Alinear todo arriba
    ('LEFTPADDING', (0, 0), (-1, -1), 0),
    ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ('TOPPADDING', (0, 0), (-1, -1), 0),
]))

elementos_principales.append(tabla_maestra)

# Construir PDF
documento.build(elementos_principales)
print("¡PDF generado correctamente!")
