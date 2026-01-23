from reportlab.pdfgen import canvas

frase = "Esta es una bonita frase para ver los distintos tipos de letra." # Definimos una frase de muestra.

hoja = canvas.Canvas("tiposLetra.pdf") # Creamos el objeto Canvas.

obxTexto = hoja.beginText() # Creamos un objeto de texto (Text Object).

obxTexto.setTextOrigin(20, 700) # Posición inicial del texto (X=20, Y=700).

# Establecemos el color de relleno del texto a verde.
# Se puede usar el nombre del color en string o RGB.
obxTexto.setFillColor("green")
# obxTexto.setFillColorRGB(0, 1, 0) # Equivalente a "green"

# Variable para controlar el espaciado entre caracteres (CharSpace).
espacioCaracteres = 0

# Iteramos sobre todas las fuentes disponibles en el sistema de ReportLab.
# aux.getAvailableFonts() devuelve una lista de nombres de fuentes estándar (Courier, Helvetica, Times-Roman, etc.)
for tipoLetra in hoja.getAvailableFonts():
    # Establecemos el espaciado entre caracteres. 
    # En cada iteración aumentamos este valor, haciendo que las letras se separen más.
    obxTexto.setCharSpace(espacioCaracteres)
    
    # Establecemos la fuente actual y tamaño 12.
    obxTexto.setFont(tipoLetra, 12)
    
    # Escribimos una línea: Nombre de la fuente + la frase de muestra.
    obxTexto.textLine(tipoLetra + ": " + frase)
    
    # Movemos el cursor explícitamente (X=20 hacia la derecha, Y=15 hacia abajo).
    # Nota: textLine() ya hace un salto de línea, esto añade un desplazamiento extra o ajusta sangría.
    # En realidad moveCursor(dx, dy) mueve RELATIVO a la posición actual.
    # Aquí parece que se quiere forzar un espaciado vertical extra o sangría.
    obxTexto.moveCursor(20, 15)
    
    # Incrementamos el espaciado para la siguiente línea.
    espacioCaracteres += 1

# --- SEGUNDA PARTE: ESPACIADO ENTRE PALABRAS ---

# Cambiamos el color a un gris oscuro (0.3).
obxTexto.setFillGray(0.3)
# Volvemos a una fuente estándar (Helvetica) tamaño 15.
obxTexto.setFont("Helvetica", 15)
# Reseteamos el espaciado de caracteres a 0.
obxTexto.setCharSpace(0)
# Movemos el cursor a una nueva posición absoluta (20, 200).
obxTexto.setTextOrigin(20, 200)

# Iteramos 10 veces para probar diferentes espaciados entre palabras.
for i in range(10):
    # Establecemos el espaciado entre palabras (WordSpace).
    # Las palabras se separarán más en cada línea.
    obxTexto.setWordSpace(i)
    
    # Escribimos la frase.
    obxTexto.textLine(frase)

# Dibujamos el objeto de texto en el canvas.
hoja.drawText(obxTexto)

# Guardamos el PDF.
hoja.save()
