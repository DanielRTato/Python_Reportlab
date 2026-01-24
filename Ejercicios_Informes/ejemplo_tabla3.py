from reportlab.platypus import (Paragraph, Image, SimpleDocTemplate, Spacer,Table,TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen.canvas import Color

hojaEstilo = getSampleStyleSheet() # Obtenemos estilos predefinidos.

elementosDoc = [] # Lista de elementos del documento.

# Cargamos una imagen "check.png" con tamaño 50x50.
# Esta imagen se usará dentro de una celda de la tabla.
imagen = Image("check.png", 50, 50)

# Obtenemos estilos de texto y modificamos uno.
estiloCuerpoTexto = hojaEstilo["BodyText"]
estiloCuerpoTexto2 = hojaEstilo["Heading1"]

# Modificamos el color del texto de BodyText a un rojo oscuro personalizado.
# Color(R, G, B, alpha) -> En ReportLab los colores suelen definirse con floats de 0.0 a 1.0.
# Color(150, 0, 0, 1) probablemente se interprete como rojo saturado (valores > 1 se toman como 1).
# Para un RGB específico se usaría: Color(150/255.0, 0, 0, 1).
estiloCuerpoTexto.textColor = Color(150, 0, 0, 1)

# Creamos párrafos para insertar en la tabla.
parrafo = Paragraph("Optare", estiloCuerpoTexto)
parrafo2 = Paragraph("PSA", estiloCuerpoTexto2)

# Definimos los datos de la tabla.
# Observa que las celdas pueden contener cadenas simples O listas de objetos Flowable (Párrafos, Imágenes).
# Fila 0: Encabezados (cadenas).
# Fila 1: Datos simples.
# Fila 2: La primera celda es una LISTA con dos párrafos [parrafo, parrafo2].
# Fila 3: La primera celda es una LISTA con un párrafo y una imagen [parrafo, imagen].
datos = [
    ["Empresas", "Candidato 1", "Candidato 2", "Especificaciones"],
    ["Ayco", "Marcos", "Ruben", "Desarrollo web con PHP"],
    [[parrafo, parrafo2], "Borja", "Juan", "Reconocimiento de imagenes con OpenCV"],
    [[parrafo, imagen], "Lidier", "Lucas", "Aplicaciones para las Telco"]
]

# Definimos el estilo de la tabla mediante una lista de tuplas (Comando, Inicio, Fin, Argumentos...).
# Coordenadas: (Columna, Fila). Indices negativos cuentan desde el final (-1 es el último).
estilo = [
    # Color de texto verde para la primera columna ((0,0) a (0,-1)).
    ("TEXTCOLOR", (0, 0), (0, -1), colors.green),
    # Color de texto violeta para la primera fila (excluyendo la celda 0,0) -> ((1,0) a (-1,0)).
    ("TEXTCOLOR", (1, 0), (-1, 0), colors.blueviolet),
    # Color de texto gris para el resto de celdas de datos ((1,1) a (-1,-1)).
    ("TEXTCOLOR", (1, 1), (-1, -1), colors.grey),
    # Caja exterior (borde) gris para la zona de datos (desde (1,1) al final).
    ("BOX", (1, 1), (-1, -1), 1.25, colors.grey),
    # Rejilla interna gris claro para la zona de datos.
    ("INNERGRID", (1, 1), (-1, -1), 1.25, colors.lightgrey),
    # Alineación vertical al medio para toda la tabla. 
    # (Corregido de "VALING" a "VALIGN").
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE")
]

# Creamos la tabla con los datos.
tabla = Table(data=datos)
# Aplicamos el estilo.
tabla.setStyle(estilo)

# Añadimos la tabla al documento.
elementosDoc.append(tabla)

# Generamos el PDF.
documento = SimpleDocTemplate("ejemplo_tabla3.pdf", pagesize=A4)
documento.build(elementosDoc)
