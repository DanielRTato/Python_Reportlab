# Importamos Image y Drawing del módulo de gráficos vectoriales de ReportLab.
# Image: Representa una imagen bitmap dentro de un gráfico vectorial.
# Drawing: El lienzo o contenedor donde se colocan los elementos gráficos.
from reportlab.graphics.shapes import Image, Drawing
# Importamos renderPDF para generar el archivo PDF final a partir del dibujo.
from reportlab.graphics import renderPDF
# Importamos el tamaño de página A4.
from reportlab.lib.pagesizes import A4

# Lista para almacenar los diferentes dibujos que crearemos (aunque en este script se combinan al final).
imagenes = []

# Creamos un objeto Image.
# Argumentos: x, y, ancho, alto, ruta_archivo.
# (0,0,100,100) -> Posición (0,0), tamaño 100x100 puntos.
imagen = Image(0, 0, 100, 100, "check.png")

# --- PRIMER DIBUJO ---
# Creamos un Drawing sin especificar tamaño inicial (se ajustará o usará valores por defecto).
dibujo = Drawing()
# Añadimos la imagen al dibujo.
dibujo.add(imagen)

# Aplicamos una traslación (desplazamiento) de (0,0). Esto no cambia nada visualmente aquí.
dibujo.translate(0, 0)
# Añadimos este dibujo a nuestra lista.
imagenes.append(dibujo)

# --- SEGUNDO DIBUJO ---
# Creamos otro Drawing.
dibujo = Drawing()
# Añadimos la MISMA imagen base.
dibujo.add(imagen)
# Rotamos todo el sistema de coordenadas del dibujo 45 grados en sentido antihorario.
dibujo.rotate(45)
# Escalamos el sistema de coordenadas: 3x en el eje X y 2x en el eje Y.
dibujo.scale(3, 2)
# Trasladamos el dibujo a la posición (100, 50).
# Nota: El orden de las transformaciones (translate, rotate, scale) es importante y afecta el resultado final.
dibujo.translate(100, 50) 
# Añadimos el segundo dibujo modificado a la lista.
imagenes.append(dibujo)

# --- DIBUJO FINAL COMBINADO ---
# Creamos un Drawing final con el tamaño de una página A4.
# A4 es una tupla (ancho, alto), por lo que accedemos por índice.
dibujo = Drawing(A4[0], A4[1])

# Iteramos sobre los dibujos creados anteriormente y los añadimos al dibujo final.
# Al añadir un dibujo dentro de otro, se comportan como grupos de elementos.
for aux in imagenes:
   dibujo.add(aux)

# Generamos el archivo PDF "ejemploImagen.pdf" que contiene el dibujo final.
renderPDF.drawToFile(dibujo, "ejemploImagen.pdf")
