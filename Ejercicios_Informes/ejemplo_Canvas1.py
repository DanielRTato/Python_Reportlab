from reportlab.pdfgen import canvas

# Creamos un objeto Canvas.
# Este objeto representa el documento PDF que vamos a generar.
hoja = canvas.Canvas("ejemplo_Canvas1.pdf")

# Utilizamos el método drawString para dibujar una cadena de texto en el PDF.
# 1. Coordenada X (horizontal).
# 2. Coordenada Y (vertical).
# 3. El texto a escribir.
# Nota: En ReportLab, el origen de coordenadas (0,0) está por defecto en la esquina INFERIOR IZQUIERDA de la página.
hoja.drawString(0, 0, "Posicion Origen (X,Y) = (0,0)")

# Dibujamos otro texto en la posición X=50, Y=100 (50 puntos a la derecha, 100 puntos hacia arriba desde el origen).
hoja.drawString(50, 100, "Posicion (X,Y) = (50,100)")

# Dibujamos otro texto en la posición X=150, Y=20.
hoja.drawString(150, 20, "Posicion (X,Y) = (150,20)")

# Utilizamos el método drawImage para insertar una imagen en el PDF.
# 1. Ruta de la imagen
# 2. Coordenada X de la esquina inferior izquierda de la imagen.
# 3. Coordenada Y de la esquina inferior izquierda de la imagen.
# 4. (Opcional) Ancho de la imagen (width).
# 5. (Opcional) Alto de la imagen (height).
# Aquí estamos insertando "check.png" en (250, 300) con un tamaño de 512x512 puntos.
hoja.drawImage("check.png", 250, 300, 512, 512)

# El método showPage() indica que hemos terminado de dibujar en la página actual.
# Si quisiéramos añadir más contenido en una segunda página, seguiríamos dibujando después de esta llamada.
hoja.showPage()

hoja.drawImage("check.png", 250, 300, 512, 512)

# El método save() finaliza el documento y guarda el archivo en el disco.
# Es fundamental llamar a este método para que se genere el PDF.
hoja.save()
