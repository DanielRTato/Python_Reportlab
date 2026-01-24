from reportlab.platypus import (
    Paragraph, Image, SimpleDocTemplate, Spacer,Table,TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen.canvas import Color

hojaEstilo = getSampleStyleSheet() # Hoja de estilos (no usada para texto aquí, pero estándar).

elementosDoc = [] # Lista de elementos para el PDF.


# Matriz de datos.
# Las celdas vacías "" a menudo se usan donde se planea hacer un 'merge' (fusión),
# ya que el contenido de la celda superior-izquierda del área fusionada es el que se muestra.
datos = [
    ["Arriba\nIzquierda", "", "02", "03", "04"], # Fila 0
    ["", "", "12", "13", "14"],                 # Fila 1
    ["20", "21", "22", "Abajo\nDerecha", ""],     # Fila 2
    ["30", "31", "32", "", ""]
]

# Definición de estilos.
estilo = [
    # Dibujamos una rejilla (GRID) en toda la tabla ((0,0) a (-1,-1)) de color gris y grosor 1.
    ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    
    # ---
    # Fondo lavanda para el área que vamos a fusionar (desde (0,0) hasta (1,1)).
    # Esto cubre las celdas (0,0), (0,1), (1,0) y (1,1).
    ('BACKGROUND', (0, 0), (1, 1), colors.lavender),
    # Comando SPAN: Fusiona celdas.
    # Desde la columna 0, fila 0 hasta la columna 1, fila 1.
    # El contenido que se verá es el de la celda (0,0) ("Arriba\nIzquierda").
    ('SPAN', (0, 0), (1, 1)),
    
    # ---
    # Fondo 'lavenderblush' para el área inferior derecha.
    # (-2,-2) es la penúltima columna, penúltima fila. (-1,-1) es la última columna, última fila.
    ('BACKGROUND', (-2, -2), (-1, -1), colors.lavenderblush),
    # Fusionamos desde la penúltima columna/fila hasta la última.
    ('SPAN', (-2, -2), (-1, -1))
]

# Creamos la tabla y aplicamos estilo.
tabla = Table(data=datos)
tabla.setStyle(estilo)

# Añadimos la tabla.
elementosDoc.append(tabla)

# Generamos el documento "ejemploTablasCombinadas.pdf".
documento = SimpleDocTemplate("ejemplo_TablasCombinada.pdf", pagesize=A4)
documento.build(elementosDoc)
