# Importamos las clases necesarias de Platypus para crear el documento PDF.
# Table y TableStyle son las clave para crear tablas formateadas.
from reportlab.platypus import (Paragraph, Image, SimpleDocTemplate, Spacer,Table,TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen.canvas import Color

# Obtenemos la hoja de estilos de muestra.
hojaEstilo = getSampleStyleSheet()

# Lista para los elementos del documento.
elementosDoc = []

# Cargamos una imagen pequeña (20x20).
imagen = Image("check.png", 20, 20)

# Obtenemos el estilo de cuerpo de texto.
estiloCuerpoTexto = hojaEstilo["BodyText"]
# Cambiamos el color del texto a verde (usando valores RGB, ojo con la escala, aquí 150 > 1 se toma como full).
estiloCuerpoTexto.textColor = Color(0, 150, 0, 1)

# Creamos un párrafo con el estilo modificado.
parrafo = Paragraph("Optare", estiloCuerpoTexto)

# Definimos los datos de la tabla.
# La última fila contiene una lista [parrafo, imagen] en la primera celda, mostrando cómo anidar elementos.
datos = [
    ["Empresas", "Candidato 1", "Candidato 2", "Especificaciones"],
    ["Ayco", "Marcos", "Ruben", "Desarrollo web con PHP"],
    ["Iterat", "Borja", "Juan", "Reconocimiento de imagenes con OpenCV"],
    [[parrafo, imagen], "Lidier", "Lucas", "Aplicaciones para las Telco"]
]

# Definimos el estilo de la tabla.
estilo = [
    # Texto azul para la primera columna.
    ("TEXTCOLOR", (0, 0), (0, -1), colors.blue),
    # Texto violeta para la primera fila (cabecera), excluyendo la primera celda (ya coloreada antes o solapada).
    # El orden de los comandos importa si se solapan.
    ("TEXTCOLOR", (1, 0), (-1, 0), colors.blueviolet),
    # Texto gris para el cuerpo de datos.
    ("TEXTCOLOR", (1, 1), (-1, -1), colors.grey),
    # Caja (borde externo) alrededor del cuerpo de datos.
    ("BOX", (1, 1), (-1, -1), 1.25, colors.grey),
    # Rejilla interna para el cuerpo de datos.
    ("INNERGRID", (1, 1), (-1, -1), 1.25, colors.lightgrey),
    # Alineación vertical centrada. (Corrigiendo "VALING" a "VALIGN").
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE")
]

# Creamos la tabla y aplicamos el estilo.
tabla = Table(data=datos)
tabla.setStyle(estilo)

# Añadimos la tabla al documento.
elementosDoc.append(tabla)

# Generamos el PDF.
documento = SimpleDocTemplate("ejemploTabla1.pdf", pagesize=A4)
documento.build(elementosDoc)
