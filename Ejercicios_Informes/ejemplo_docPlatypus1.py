import os
from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet # Importamos getSampleStyleSheet para obtener una hoja de estilos predefinida.
from reportlab.lib.pagesizes import A4 # Importamos tamaños de página estándar (A4).
from reportlab.lib import colors # Importamos definiciones de colores.
from reportlab.rl_settings import showBoundary

# Obtenemos la hoja de estilos de muestra.
# Esto nos devuelve un objeto tipo diccionario con estilos como 'Normal', 'Heading1', 'BodyText', etc.
hojaEstilo = getSampleStyleSheet()

# Lista donde almacenaremos los elementos "flowables" (flotantes) del documento.
# Platypus coloca estos elementos uno tras otro en el documento, creando nuevas páginas según sea necesario.
elementosDoc = []

cabecera = hojaEstilo["Heading3"] # Obtenemos el estilo "Heading4" (Encabezado nivel 3) de la hoja de estilos.

# Modificamos algunas propiedades del estilo "Heading4".
# pageBreakBefore = 0: No fuerza un salto de página antes de este elemento.
cabecera.pageBreakBefore = 0
# keepWithNext = 0: No obliga a que este elemento se mantenga en la misma página que el siguiente.
cabecera.keepWithNext = 0
# backColor = colors.dimgrey: Establece un color de fondo lightcyan para el texto con este estilo.
cabecera.backColor = colors.lightcyan

paragrafo = Paragraph("Cabecera del documento", cabecera) # Creamos un objeto Paragraph con el texto "Cabecera del documento" y el estilo modificado.

elementosDoc.append(paragrafo) # Añadimos el párrafo a nuestra lista de elementos del documento.

# Añadimos un Spacer (espaciador) de 0 puntos de ancho y 5 puntos de alto.
# Esto crea una separación vertical.
elementosDoc.append(Spacer(0,5))

# Creamos una cadena de texto larga repitiendo una frase 100 veces.
# Esto servirá para demostrar cómo Platypus maneja el texto que excede una línea o página.
contenidoDocumento = "Este es el contenido del documento, el cual va a ocupar múltiples lineas. " *100

# Obtenemos el estilo "BodyText" (texto del cuerpo) de la hoja de estilos.
estiloCuerpoTexto = hojaEstilo["BodyText"]

# Creamos un Paragraph con el texto largo y el estilo de cuerpo.
# Paragraph se encargará automáticamente del ajuste de línea (word wrap).
paragrafo = Paragraph(contenidoDocumento, estiloCuerpoTexto)

# Añadimos el párrafo largo a la lista de elementos.
elementosDoc.append(paragrafo)

# Añadimos otro espaciador, esta vez de 20 puntos de alto.
elementosDoc.append(Spacer(0,20))

# Creamos el objeto SimpleDocTemplate.
# Argumentos:
# 1. Nombre del archivo PDF de salida.
# 2. pagesize=A4: Tamaño de la página.
documento = SimpleDocTemplate("ejemplo_docPlatypus.pdf", pagesize = A4, showBoundary=1)

# Llamamos al método build() pasando la lista de elementos (flowables).
# Este método procesa la lista y genera el PDF, calculando posiciones y saltos de página automáticamente.
documento.build(elementosDoc)
