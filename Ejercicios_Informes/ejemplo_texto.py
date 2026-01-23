from reportlab.pdfgen import canvas

# Lista de cadenas que conformarán nuestras primeras líneas de texto.
frase = ["Estas es una bonita frase,", "para tener distintas partes",
         "a las que incluir en nuestro", "texto de ejemplo."]

# Creamos el objeto Canvas.
obxCanvas = canvas.Canvas("ejemplo_Texto.pdf")

# Creamos un "objeto de texto" (text object).
# El objeto de texto nos permite formatear un bloque de texto de manera eficiente 
# (fuentes, saltos de línea, colores) antes de "pintarlo" en el canvas.
objTexto = obxCanvas.beginText()

# Establecemos la posición inicial del cursor de texto en (100, 500).
objTexto.setTextOrigin(100, 500)

# Establecemos la fuente y el tamaño (Courier, 16 puntos).
objTexto.setFont("Courier", 16)

# Iteramos sobre la lista 'frase' y añadimos cada cadena como una línea separada.
# textLine() añade el texto y mueve el cursor a la siguiente línea automáticamente.
for liña in frase:
    objTexto.textLine(liña)

# Cambiamos el color de relleno a gris (0.5 es gris medio, 0=negro, 1=blanco).
objTexto.setFillGray(0.5)

# Definimos un bloque de texto multilínea (string con saltos de línea integrados).
parragrafo = '''
Este es un texto multiliña para poner el ejemplo.
En el escribimos varias frases en un parragrafo
para que despues dentro del documento o drawText de canvas.
'''

# Usamos textLines() (con 's' al final) para procesar un string que contiene saltos de línea (\n).
objTexto.textLines(parragrafo)

# Finalmente, dibujamos todo el objeto de texto acumulado en el canvas.
obxCanvas.drawText(objTexto)

# Cerramos la página y guardamos.
obxCanvas.showPage()
obxCanvas.save()
