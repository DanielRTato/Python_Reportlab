import os

# Importamos clases necesarias de reportlab.platypus.
# Paragraph: Para bloques de texto con estilos (permite saltos de línea automáticos).
# Image: Para insertar imágenes (aunque no se usa explícitamente en el código activo, está importada).
# SimpleDocTemplate: Plantilla predefinida para documentos sencillos, maneja márgenes y flujo de página.
# Spacer: Para añadir espacio vertical vacío entre elementos.
from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer

# Importamos getSampleStyleSheet para obtener una hoja de estilos predefinida.
from reportlab.lib.styles import getSampleStyleSheet

# Importamos tamaños de página estándar (A4).
from reportlab.lib.pagesizes import A4

# Importamos definiciones de colores.
from reportlab.lib import colors

# Obtenemos la hoja de estilos de muestra.
# Esto nos devuelve un objeto tipo diccionario con estilos como 'Normal', 'Heading1', 'BodyText', etc.
hojaEstilo = getSampleStyleSheet()

# Lista vacía que parece no usarse en este script, quizás sobrante de otro ejemplo.
guion = []

# Lista donde almacenaremos los elementos "flowables" (flotantes) del documento.
# Platypus coloca estos elementos uno tras otro en el documento, creando nuevas páginas según sea necesario.
elementosDoc = []

# Obtenemos el estilo "Heading4" (Encabezado nivel 4) de la hoja de estilos.
cabecera = hojaEstilo["Heading4"]

# Modificamos algunas propiedades del estilo "Heading4".
# pageBreakBefore = 0: No fuerza un salto de página antes de este elemento.
cabecera.pageBreakBefore = 0
# keepWithNext = 0: No obliga a que este elemento se mantenga en la misma página que el siguiente.
cabecera.keepWithNext = 0
# backColor = colors.dimgrey: Establece un color de fondo gris oscuro para el texto con este estilo.
cabecera.backColor = colors.dimgrey

# Creamos un objeto Paragraph con el texto "Cabecera del documento" y el estilo modificado.
paragrafo = Paragraph("Cabecera del documento", cabecera)

# Añadimos el párrafo a nuestra lista de elementos del documento.
elementosDoc.append(paragrafo)

# Añadimos un Spacer (espaciador) de 0 puntos de ancho y 5 puntos de alto.
# Esto crea una separación vertical.
elementosDoc.append(Spacer(0,5))

# Creamos una cadena de texto larga repitiendo una frase 100 veces.
# Esto servirá para demostrar cómo Platypus maneja el texto que excede una línea o página.
contenidoDocumento = "Este es el contenido del documento, el cual va a ocupar múltiples lineas. "*100

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
documento = SimpleDocTemplate("ejemploDocPlatypus.pdf", pagesize = A4)

# Llamamos al método build() pasando la lista de elementos (flowables).
# Este método procesa la lista y genera el PDF, calculando posiciones y saltos de página automáticamente.
documento.build(elementosDoc)
