from reportlab.platypus import (Paragraph, Image, SimpleDocTemplate, Spacer, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen.canvas import Color

# ==============================================================================
# CONFIGURACIÓN INICIAL
# ==============================================================================

# Obtenemos la hoja de estilos de muestra que proporciona ReportLab.
# Esto nos da estilos predefinidos como 'Normal', 'BodyText', 'Heading1', etc.
hojaEstilo = getSampleStyleSheet()

def crear_tabla_1_candidatos_basica():
    """
    Crea la tabla del ejemplo 1: Una tabla con imágenes y párrafos anidados.
    Demuestra cómo insertar elementos Flowable (párrafos, imágenes) dentro de una celda.
    """
    print("Generando Tabla 1...")

    # Cargamos una imagen pequeña (20x20 píxeles).
    # Asegúrate de que 'check.png' exista en el mismo directorio.
    imagen = Image("check.png", 20, 20)

    # Obtenemos un estilo de texto básico y lo personalizamos.
    estiloCuerpoTexto = hojaEstilo["BodyText"]
    # Cambiamos el color del texto a un verde oscuro.
    # Color(R, G, B, Alpha). Si usas valores > 1, asegúrate de la escala.
    # Aquí se usa Color(0, 150, 0, 1) que ReportLab interpreta.
    estiloCuerpoTexto.textColor = Color(0, 150, 0, 1)

    # Creamos un párrafo con el texto "Optare" y el estilo verde.
    parrafo = Paragraph("Optare", estiloCuerpoTexto)

    # Definimos los datos de la tabla.
    # Cada sub-lista es una fila.
    # Nota importante: La celda [3][0] contiene una LISTA [parrafo, imagen].
    # Esto le dice a ReportLab que coloque ambos elementos en esa misma celda.
    datos = [
        ["Empresas", "Candidato 1", "Candidato 2", "Especificaciones"],
        ["Ayco", "Marcos", "Ruben", "Desarrollo web con PHP"],
        ["Iterat", "Borja", "Juan", "Reconocimiento de imagenes con OpenCV"],
        [[parrafo, imagen], "Lidier", "Lucas", "Aplicaciones para las Telco"]
    ]

    # Definimos el estilo visual de la tabla.
    # Formato: (COMANDO, (col_inicio, fila_inicio), (col_fin, fila_fin), VALOR)
    # (-1, -1) representa la última columna/fila.
    estilo = [
        # Texto azul para toda la primera columna (Empresas).
        ("TEXTCOLOR", (0, 0), (0, -1), colors.blue),
        # Texto violeta para la cabecera (fila 0), desde la columna 1 hasta la 3.
        ("TEXTCOLOR", (1, 0), (3, 0), colors.blueviolet),
        # Texto gris para el cuerpo de datos (desde fila 1, columna 1 hasta el final).
        ("TEXTCOLOR", (1, 1), (-1, -1), colors.grey),
        # Un borde exterior (BOX) gris rodeando los datos (excluyendo primera col y fila).
        ("BOX", (1, 1), (-1, -1), 1.25, colors.grey),
        # Rejilla interna (INNERGRID) gris clara para separar las celdas de datos.
        ("INNERGRID", (1, 1), (-1, -1), 1.25, colors.lightgrey),
        # Alineación vertical centrada para todas las celdas.
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE")
    ]

    # Creamos el objeto Table pasando los datos.
    tabla = Table(data=datos)
    # Aplicamos la lista de estilos definida arriba.
    tabla.setStyle(estilo)

    return tabla

def crear_tabla_2_temperaturas():
    """
    Crea la tabla del ejemplo 2: Tabla de temperaturas con formato condicional.
    Demuestra cómo iterar sobre los datos y aplicar estilos celda por celda
    basándose en el valor numérico (colores de fondo según temperatura).
    """
    print("Generando Tabla 2...")

    # Matriz de datos:
    # Fila 0: Meses.
    # Fila 1: Máximas.
    # Fila 2: Mínimas.
    temperaturas = [
        ['', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        ["Máximas", 15, 16, 20, 25, 27, 31, 35, 38, 30, 25, 20, 18],
        ["Minimas", -3, -4, -1, 4, 6, 9, 12, 15, 16, 10, 2, -2]
    ]

    # Estilo base estático.
    estilo = [
        # Color gris para la cabecera de meses.
        ('TEXTCOLOR', (0, 0), (-1, 12), colors.grey),
        # Color gris para la primera columna (etiquetas).
        ('TEXTCOLOR', (0, 1), (0, -1), colors.grey),
        # Caja bordeando los datos numéricos.
        ('BOX', (1, 1), (-1, -1), 1.50, colors.grey),
        # Rejilla interna blanca.
        ('INNERGRID', (1, 1), (-1, -1), 0.5, colors.white)
    ]

    # Lógica de formato condicional:
    # Recorremos la matriz 'temperaturas' usando enumerate para tener índices (i, j).
    for i, fila in enumerate(temperaturas):
        for j, temperatura in enumerate(fila):
            # Solo procesamos si el valor es un número (int), ignoramos los textos.
            if type(temperatura) == int:
                # Establecemos el color de texto a negro por defecto para los números.
                estilo.append(('TEXTCOLOR', (j, i), (j, i), colors.black))
                
                # Dependiendo del rango de temperatura, añadimos un comando BACKGROUND para esa celda específica.
                if temperatura > 30:
                    estilo.append(('BACKGROUND', (j, i), (j, i), colors.red)) # Muy calor
                elif 20 < temperatura <= 30:
                    estilo.append(('BACKGROUND', (j, i), (j, i), colors.orange)) # Calor
                elif 10 < temperatura <= 20:
                    estilo.append(('BACKGROUND', (j, i), (j, i), colors.lightpink)) # Templado
                elif 0 < temperatura <= 10:
                    estilo.append(('BACKGROUND', (j, i), (j, i), colors.lightblue)) # Frío
                else:
                    # Bajo cero o 0.
                    estilo.append(('TEXTCOLOR', (j, i), (j, i), colors.blue)) # Texto azul
                    estilo.append(('BACKGROUND', (j, i), (j, i), colors.lightgrey)) # Fondo gris

    tabla = Table(data=temperaturas)
    tabla.setStyle(estilo)
    
    return tabla

def crear_tabla_3_candidatos_compleja():
    """
    Crea la tabla del ejemplo 3: Similar a la 1 pero con más anidamiento.
    Muestra cómo poner múltiples párrafos en una celda o mezclar párrafo e imagen
    con diferentes estilos.
    """
    print("Generando Tabla 3...")

    # Imagen más grande (50x50).
    imagen = Image("check.png", 50, 50)

    # Estilos de texto.
    estiloCuerpoTexto = hojaEstilo["BodyText"]
    estiloTitulo1 = hojaEstilo["Heading1"] # Usamos un estilo de encabezado para variar.

    # Modificamos el color del cuerpo de texto a un rojo oscuro.
    estiloCuerpoTexto.textColor = Color(150, 0, 0, 1)

    # Creamos párrafos.
    parrafo1 = Paragraph("Optare", estiloCuerpoTexto)
    parrafo2 = Paragraph("PSA", estiloTitulo1)

    # Datos complejos:
    # Fila 2, Col 0: Lista con DOS párrafos [parrafo1, parrafo2]. Se apilarán verticalmente.
    # Fila 3, Col 0: Lista con Párrafo e Imagen [parrafo1, imagen].
    datos = [
        ["Empresas", "Candidato 1", "Candidato 2", "Especificaciones"],
        ["Ayco", "Marcos", "Ruben", "Desarrollo web con PHP"],
        [[parrafo1, parrafo2], "Borja", "Juan", "Reconocimiento de imagenes con OpenCV"],
        [[parrafo1, imagen], "Lidier", "Lucas", "Aplicaciones para las Telco"]
    ]

    estilo = [
        # Verde para la primera columna.
        ("TEXTCOLOR", (0, 0), (0, -1), colors.green),
        # Violeta para la primera fila (cabecera), desde columna 1.
        ("TEXTCOLOR", (1, 0), (-1, 0), colors.blueviolet),
        # Gris para el resto.
        ("TEXTCOLOR", (1, 1), (-1, -1), colors.grey),
        ("BOX", (1, 1), (-1, -1), 1.25, colors.grey),
        ("INNERGRID", (1, 1), (-1, -1), 1.25, colors.lightgrey),
        # Alineación vertical al medio (MIDDLE).
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE")
    ]

    tabla = Table(data=datos)
    tabla.setStyle(estilo)

    return tabla

# ==============================================================================
# EJECUCIÓN PRINCIPAL
# ==============================================================================

if __name__ == "__main__":
    # Lista que contendrá todos los elementos (tablas, espacios, textos) del PDF final.
    elementosDoc = []

    # Añadimos un título al documento.
    estiloTitulo = hojaEstilo["Title"]
    elementosDoc.append(Paragraph("Informe Combinado de Tablas", estiloTitulo))
    elementosDoc.append(Spacer(1, 20)) # Espacio vertical de 20 puntos.

    # --- TABLA 1 ---
    elementosDoc.append(Paragraph("Ejemplo 1: Tabla Básica con Imagen", hojaEstilo["Heading2"]))
    elementosDoc.append(Spacer(1, 10))
    tabla1 = crear_tabla_1_candidatos_basica()
    elementosDoc.append(tabla1)
    elementosDoc.append(Spacer(1, 30))

    # --- TABLA 2 ---
    elementosDoc.append(Paragraph("Ejemplo 2: Temperaturas (Formato Condicional)", hojaEstilo["Heading2"]))
    elementosDoc.append(Spacer(1, 10))
    tabla2 = crear_tabla_2_temperaturas()
    elementosDoc.append(tabla2)
    elementosDoc.append(Spacer(1, 30))

    # --- TABLA 3 ---
    elementosDoc.append(Paragraph("Ejemplo 3: Tabla Compleja (Anidamiento)", hojaEstilo["Heading2"]))
    elementosDoc.append(Spacer(1, 10))
    tabla3 = crear_tabla_3_candidatos_compleja()
    elementosDoc.append(tabla3)

    # Generamos el archivo PDF final.
    nombre_archivo = "ejemplo_Tablas_Combinadas_Comentado.pdf"
    documento = SimpleDocTemplate(nombre_archivo, pagesize=A4)
    
    print(f"Guardando PDF en: {nombre_archivo}")
    documento.build(elementosDoc)
    print("¡Proceso terminado con éxito!")
