from reportlab.platypus import (Paragraph, Image, SimpleDocTemplate, Spacer,Table,TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen.canvas import Color

hojaEstilo = getSampleStyleSheet()

elementosDoc = []

# Matriz de datos de temperaturas:
# Fila 0: Encabezados de meses.
# Fila 1: Temperaturas máximas.
# Fila 2: Temperaturas mínimas.
temperaturas = [
    ['', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    ["Máximas", 15, 16, 20, 25, 27, 31, 35, 38, 30, 25, 20, 18],
    ["Minimas", -3, -4, -1, 4, 6, 9, 12, 15, 16, 10, 2, -2]
]

# Estilo base de la tabla.
estilo = [
    # Color de texto gris para la primera fila (encabezados de mes).
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.grey),
    # Color de texto gris para la primera columna (etiquetas "Máximas", "Mínimas").
    ('TEXTCOLOR', (0, 1), (0, -1), colors.grey),
    # Caja (borde) alrededor de las celdas de datos (desde fila 1, col 1 hasta el final).
    ('BOX', (1, 1), (-1, -1), 1.50, colors.grey),
    # Rejilla interna blanca para separar las celdas de datos.
    ('INNERGRID', (1, 1), (-1, -1), 0.5, colors.white)
]

# Iteramos sobre los datos para aplicar estilos condicionales según el valor de la temperatura.
# enumerate nos da el índice (i, j) y el valor (fila, temperatura).
for i, fila in enumerate(temperaturas):
    for j, temperatura in enumerate(fila):
        # Comprobamos si el valor es un entero (para saltarnos las cabeceras de texto).
        if type(temperatura) == int:
            # Por defecto, texto negro.
            estilo.append(('TEXTCOLOR', (j, i), (j, i), colors.black))
            
            # Aplicamos color de FONDO ('BACKGROUND') según rangos de temperatura.
            if temperatura > 30:
                # Rojo fuerte para calor extremo.
                # Nota: Si 'colors.fidred' da error, sustituir por 'colors.red'.
                estilo.append(('BACKGROUND', (j, i), (j, i), colors.red))
            elif 20 < temperatura <= 30: # Sintaxis pythonica para rango (temperatura > 20 y <= 30)
                # Naranja para calor moderado.
                estilo.append(('BACKGROUND', (j, i), (j, i), colors.orange))
            elif 10 < temperatura <= 20:
                # Rosa claro para templado.
                estilo.append(('BACKGROUND', (j, i), (j, i), colors.lightpink))
            elif 0 < temperatura <= 10:
                # Azul claro para frío.
                estilo.append(('BACKGROUND', (j, i), (j, i), colors.lightblue))
            else:
                # Para temperaturas <= 0 (bajo cero).
                # Texto azul.
                estilo.append(('TEXTCOLOR', (j, i), (j, i), colors.blue))
                # Fondo gris claro.
                estilo.append(('BACKGROUND', (j, i), (j, i), colors.lightgrey))

# Creamos la tabla y aplicamos el estilo acumulado.
tabla = Table(data=temperaturas)
tabla.setStyle(estilo)

# Añadimos la tabla al documento.
elementosDoc.append(tabla)

# Generamos el PDF.
documento = SimpleDocTemplate("ejemploTabla2.pdf", pagesize=A4)
documento.build(elementosDoc)
