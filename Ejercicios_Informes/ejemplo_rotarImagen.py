from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

imagenes = [] # Lista para almacenar los diferentes dibujos que crearemos (aunque en este script se combinan al final).

# Creamos un objeto Image.
# Argumentos: x, y, ancho, alto, ruta_archivo.
imagen = Image(0, 0, 100, 100, "check.png") # (0,0,100,100) -> Posición (0,0), tamaño 100x100 puntos.

# --- PRIMER DIBUJO ---
dibujo = Drawing() # Creamos un Drawing sin especificar tamaño inicial (se ajustará o usará valores por defecto).
dibujo.add(imagen) # Añadimos la imagen al dibujo.

dibujo.translate(0, 0) # Aplicamos una traslación (desplazamiento) de (0,0). Esto no cambia nada visualmente aquí.
imagenes.append(dibujo) # Añadimos este dibujo a nuestra lista.

# --- SEGUNDO DIBUJO ---
dibujo = Drawing() # Creamos otro Drawing.
dibujo.add(imagen) # Añadimos la MISMA imagen base.
dibujo.rotate(45) # Rotamos todo el sistema de coordenadas del dibujo 45 grados en sentido antihorario.
dibujo.scale(3, 2) # Escalamos el sistema de coordenadas: 3x en el eje X y 2x en el eje Y.
# Trasladamos el dibujo a la posición (100, 50).
# Nota: El orden de las transformaciones (translate, rotate, scale) es importante y afecta el resultado final.
dibujo.translate(100, 50)
imagenes.append(dibujo) # Añadimos el segundo dibujo modificado a la lista.

# --- DIBUJO FINAL COMBINADO ---
# Creamos un Drawing final con el tamaño de una página A4.
# A4 es una tupla (ancho, alto), por lo que accedemos por índice.
dibujo = Drawing(A4[0], A4[1])

# Iteramos sobre los dibujos creados anteriormente y los añadimos al dibujo final.
# Al añadir un dibujo dentro de otro, se comportan como grupos de elementos.
for aux in imagenes:
   dibujo.add(aux)

# Generamos el archivo PDF "ejemploImagen.pdf" que contiene el dibujo final.
renderPDF.drawToFile(dibujo, "ejemplo_rotarImagen.pdf")
