import os


def generador_examen_pro():
    print("--- GENERADOR REPORTLAB PRO ---")
    archivo_salida = input("Nombre del archivo .py a crear: ")

    # Asegurar que el archivo tenga extensión .py
    if not archivo_salida.endswith(".py"):
        archivo_salida += ".py"

    # 1. GESTIÓN DE COLORES
    print("\n--- CONFIGURACIÓN DE COLORES ---")
    print("Elige la variante de color:")
    print("  1) Normal")
    print("  2) Claro (Light)")
    print("  3) Oscuro (Dark)")

    # Validar selección de variante
    while True:
        variante = input("Selecciona la variante (1-3): ")
        if variante in ['1', '2', '3']:
            break
        else:
            print("[ERROR] Error: Debes introducir 1, 2 o 3. Intenta de nuevo.")

    print("\nOpciones de colores:")
    print("  A) Azul          F) Naranja        K) Turquesa      P) Personalizado")
    print("  B) Rojo          G) Rosa           L) Púrpura")
    print("  C) Verde         H) Amarillo       M) Marrón")
    print("  D) Negro         I) Cian           N) Gris")
    print("  E) Blanco        J) Magenta        O) Lima")

    # Validar selección de color
    while True:
        opc_color = input("Elige una opción (A-P): ").upper()
        if opc_color in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']:
            break
        else:
            print("[ERROR] Error: Debes introducir una opción de A a P. Intenta de nuevo.")

    # Definir colores en tres variantes
    colores_normal = {
        'A': "colors.blue",
        'B': "colors.red",
        'C': "colors.green",
        'D': "colors.black",
        'E': "colors.white",
        'F': "colors.orange",
        'G': "colors.pink",
        'H': "colors.yellow",
        'I': "colors.cyan",
        'J': "colors.magenta",
        'K': "colors.lightblue",
        'L': "colors.purple",
        'M': "colors.brown",
        'N': "colors.grey",
        'O': "colors.lime",
    }

    colores_claro = {
        'A': "colors.lightblue",
        'B': "colors.lightcoral",
        'C': "colors.lightgreen",
        'D': "colors.lightgrey",
        'E': "colors.white",
        'F': "colors.lightyellow",
        'G': "colors.lightpink",
        'H': "colors.lightyellow",
        'I': "colors.lightcyan",
        'J': "colors.lightgrey",  # Corregido: lightmagenta no existe
        'K': "colors.lightblue",
        'L': "colors.lightgrey",
        'M': "colors.lightgoldenrodyellow",
        'N': "colors.lightgrey",
        'O': "colors.lightgreen",
    }

    colores_oscuro = {
        'A': "colors.darkblue",
        'B': "colors.darkred",
        'C': "colors.darkgreen",
        'D': "colors.black",
        'E': "colors.darkgrey",
        'F': "colors.darkorange",
        'G': "colors.darkred",
        'H': "colors.olive",
        'I': "colors.darkcyan",
        'J': "colors.purple",  # Corregido: darkviolet no existe
        'K': "colors.teal",
        'L': "colors.purple",  # Corregido: darkviolet no existe
        'M': "colors.brown",
        'N': "colors.darkgrey",
        'O': "colors.darkgreen",
    }

    # Seleccionar la variante
    if variante == '1':
        colores_seleccionados = colores_normal
    elif variante == '2':
        colores_seleccionados = colores_claro
    elif variante == '3':
        colores_seleccionados = colores_oscuro
    else:
        print("Variante no válida. Usando normal.")
        colores_seleccionados = colores_normal

    if opc_color in colores_seleccionados:
        color_hex = colores_seleccionados[opc_color]
    elif opc_color == 'P':
        print("Introduce valores RGB (0-255):")

        # Validar R
        while True:
            try:
                r = int(input("R: "))
                if 0 <= r <= 255:
                    break
                else:
                    print("[ERROR] Error: El valor debe estar entre 0 y 255. Intenta de nuevo.")
            except ValueError:
                print("[ERROR] Error: Debes introducir un número entero. Intenta de nuevo.")

        # Validar G
        while True:
            try:
                g = int(input("G: "))
                if 0 <= g <= 255:
                    break
                else:
                    print("[ERROR] Error: El valor debe estar entre 0 y 255. Intenta de nuevo.")
            except ValueError:
                print("[ERROR] Error: Debes introducir un número entero. Intenta de nuevo.")

        # Validar B
        while True:
            try:
                b = int(input("B: "))
                if 0 <= b <= 255:
                    break
                else:
                    print("[ERROR] Error: El valor debe estar entre 0 y 255. Intenta de nuevo.")
            except ValueError:
                print("[ERROR] Error: Debes introducir un número entero. Intenta de nuevo.")

        color_hex = f"colors.Color({r / 255:.2f}, {g / 255:.2f}, {b / 255:.2f})"
    else:
        print("Opción no válida. Usando azul normal por defecto.")
        color_hex = "colors.blue"

    # 2. CONFIGURACIÓN DE LA TABLA (DATOS)
    while True:
        try:
            rows = int(input("\n¿Cuántas filas tiene tu tabla?: "))
            if 1 <= rows <= 20:
                break
            else:
                print("[ERROR] Error: Debes introducir entre 1 y 20 filas.")
        except ValueError:
            print("[ERROR] Error: Debes introducir un número entero. Intenta de nuevo.")

    while True:
        try:
            cols = int(input("¿Cuántas columnas tiene tu tabla?: "))
            if 1 <= cols <= 20:
                break
            else:
                print("[ERROR] Error: Debes introducir entre 1 y 20 columnas.")
        except ValueError:
            print("[ERROR] Error: Debes introducir un número entero. Intenta de nuevo.")

    tabla_datos = []
    imagenes_insertar = {}  # Diccionario para almacenar imágenes: {(fila, col): (ruta, ancho, alto)}

    # Pedir contenido de todas las celdas
    print("\n--- CONTENIDO DE LA TABLA ---")
    for r in range(rows):
        fila = []
        for c in range(cols):
            val = input(f"Texto para celda [{r}][{c}]: ")
            fila.append(val)
        tabla_datos.append(fila)

    # Preguntar al final si desea agregar imágenes
    print("\n--- INSERCIÓN DE IMÁGENES ---")

    while True:
        agregar_imagen = input("¿Deseas insertar una imagen? (s/n): ").lower()
        if agregar_imagen in ['s', 'n']:
            break
        else:
            print("[ERROR] Error: Debes responder 's' o 'n'. Intenta de nuevo.")

    while agregar_imagen == 's':
        print(f"\nLa tabla tiene {rows} filas (0-{rows - 1}) y {cols} columnas (0-{cols - 1})")

        # Validar fila de la imagen
        while True:
            try:
                fila_img = int(input("¿En qué fila deseas insertar la imagen? "))
                if 0 <= fila_img < rows:
                    break
                else:
                    print(f"[ERROR] Error: La fila debe estar entre 0 y {rows - 1}. Intenta de nuevo.")
            except ValueError:
                print("[ERROR] Error: Debes introducir un número entero. Intenta de nuevo.")

        # Validar columna de la imagen
        while True:
            try:
                col_img = int(input("¿En qué columna deseas insertar la imagen? "))
                if 0 <= col_img < cols:
                    break
                else:
                    print(f"[ERROR] Error: La columna debe estar entre 0 y {cols - 1}. Intenta de nuevo.")
            except ValueError:
                print("[ERROR] Error: Debes introducir un número entero. Intenta de nuevo.")

        ruta_imagen = input("Ruta de la imagen: ").strip()

        # Validar existencia de la imagen
        if not os.path.exists(ruta_imagen):
            print(f"[ERROR] Error: La imagen '{ruta_imagen}' no existe.")
            print(f"   Ruta absoluta esperada: {os.path.abspath(ruta_imagen)}")
            continue

        # Validar que sea archivo
        if not os.path.isfile(ruta_imagen):
            print(f"[ERROR] Error: '{ruta_imagen}' no es un archivo válido.")
            continue

        # Validar formato
        extensiones_validas = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
        if not ruta_imagen.lower().endswith(extensiones_validas):
            print(f"[ERROR] Error: Formato no soportado. Usa: {extensiones_validas}")
            continue

        # Validar ancho
        while True:
            try:
                ancho = int(input("Ancho de la imagen (en píxeles): "))
                if ancho > 0:
                    break
                else:
                    print("[ERROR] Error: El ancho debe ser mayor a 0. Intenta de nuevo.")
            except ValueError:
                print("[ERROR] Error: Debes introducir un número entero. Intenta de nuevo.")

        # Validar alto
        while True:
            try:
                alto = int(input("Alto de la imagen (en píxeles): "))
                if alto > 0:
                    break
                else:
                    print("[ERROR] Error: El alto debe ser mayor a 0. Intenta de nuevo.")
            except ValueError:
                print("[ERROR] Error: Debes introducir un número entero. Intenta de nuevo.")

        # Guardar datos de la imagen
        imagenes_insertar[(fila_img, col_img)] = (ruta_imagen, ancho, alto)
        tabla_datos[fila_img][col_img] = f"IMAGE_{fila_img}_{col_img}"  # Reemplazar contenido con placeholder

        print(f"[OK] Imagen validada: {os.path.basename(ruta_imagen)}")
        print(f"[OK] Imagen añadida en celda [{fila_img}][{col_img}]")

        # Preguntar si desea agregar más imágenes
        while True:
            agregar_otra = input("\n¿Deseas agregar otra imagen? (s/n): ").lower()
            if agregar_otra in ['s', 'n']:
                agregar_imagen = agregar_otra
                break
            else:
                print("[ERROR] Error: Debes responder 's' o 'n'. Intenta de nuevo.")

    # 3. BUCLE DE ESTILOS DINÁMICOS (SPAN, BACKGROUND, ALIGN, FONT, TEXTCOLOR, VALIGN)
    estilos_adicionales = []

    print("\n--- CONFIGURACIÓN DE ESTILOS DE TABLA ---")
    while True:
        print("\n¿Qué quieres añadir?")
        print("  1. Agrupar (SPAN)")
        print("  2. Color Fondo (BACKGROUND)")
        print("  3. Fuente/Tamaño (FONT)")
        print("  4. Alineación Horizontal (ALIGN)")
        print("  5. Color de Texto (TEXTCOLOR)")
        print("  6. Alineación Vertical (VALIGN)")
        print("  7. Terminar")

        # Validar opción de estilo
        while True:
            opc = input("Selecciona: ")
            if opc in ['1', '2', '3', '4', '5', '6', '7']:
                break
            else:
                print("[ERROR] Error: Debes introducir un número del 1 al 7. Intenta de nuevo.")

        if opc == '7':
            break

        # Validar rango de celdas
        while True:
            try:
                start = input("Celda inicio (fila,col): ")
                # Verificar formato
                if ',' in start and len(start.split(',')) == 2:
                    s_values = start.split(',')
                    int(s_values[0].strip())
                    int(s_values[1].strip())
                    break
                else:
                    print("[ERROR] Error: Formato incorrecto. Usa: fila,col (ej: 0,0). Intenta de nuevo.")
            except ValueError:
                print("[ERROR] Error: Los valores deben ser números enteros. Intenta de nuevo.")

        while True:
            try:
                end = input("Celda fin (fila,col): ")
                # Verificar formato
                if ',' in end and len(end.split(',')) == 2:
                    e_values = end.split(',')
                    int(e_values[0].strip())
                    int(e_values[1].strip())
                    break
                else:
                    print("[ERROR] Error: Formato incorrecto. Usa: fila,col (ej: 0,0). Intenta de nuevo.")
            except ValueError:
                print("[ERROR] Error: Los valores deben ser números enteros. Intenta de nuevo.")

        if opc == '1':  # SPAN
            estilos_adicionales.append(f"('SPAN', ({start}), ({end}))")
        elif opc == '2':  # BACKGROUND
            bg = input("Color (ej: colors.yellow o A,B,C): ")
            estilos_adicionales.append(f"('BACKGROUND', ({start}), ({end}), {bg})")
        elif opc == '3':  # FONT
            FUENTES_VALIDAS = [
                'Helvetica', 'Helvetica-Bold', 'Helvetica-Oblique', 'Helvetica-BoldOblique',
                'Times-Roman', 'Times-Bold', 'Times-Italic', 'Times-BoldItalic',
                'Courier', 'Courier-Bold', 'Courier-Oblique', 'Courier-BoldOblique'
            ]
            print(f"Fuentes disponibles: {', '.join(FUENTES_VALIDAS)}")
            while True:
                fn = input("Nombre fuente: ").strip()
                if fn in FUENTES_VALIDAS:
                    break
                else:
                    print(f"[ERROR] Error: Fuente no válida. Usa una de: {FUENTES_VALIDAS}")

            # Validar tamaño de fuente
            while True:
                try:
                    sz = int(input("Tamaño: "))
                    if sz > 0:
                        break
                    else:
                        print("[ERROR] Error: El tamaño debe ser mayor a 0. Intenta de nuevo.")
                except ValueError:
                    print("[ERROR] Error: Debes introducir un número entero. Intenta de nuevo.")

            estilos_adicionales.append(f"('FONT', ({start}), ({end}), '{fn}', {sz})")
        elif opc == '4':  # ALIGN
            print("Opciones válidas: LEFT, CENTER, RIGHT")
            while True:
                al = input("Alineación: ").upper()
                if al in ['LEFT', 'CENTER', 'RIGHT']:
                    break
                else:
                    print("[ERROR] Error: Debes introducir LEFT, CENTER o RIGHT. Intenta de nuevo.")
            estilos_adicionales.append(f"('ALIGN', ({start}), ({end}), '{al}')")
        elif opc == '5':  # TEXTCOLOR
            print("Opciones: colors.black, colors.white, colors.red, colors.blue, colors.green, etc.")
            print("O introduce valores RGB (0-255): ej: 255,0,0")
            color_texto = input("Color del texto: ")
            if ',' in color_texto and not color_texto.startswith('colors.'):
                # Validar RGB
                try:
                    rgb_values = color_texto.split(',')
                    if len(rgb_values) != 3:
                        raise ValueError
                    r, g, b = map(int, rgb_values)
                    if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
                        raise ValueError
                    color_texto = f"colors.Color({r / 255:.2f}, {g / 255:.2f}, {b / 255:.2f})"
                except ValueError:
                    print("[ERROR] Error: Formato RGB inválido. Usa: 255,0,0. Usando negro por defecto.")
                    color_texto = "colors.black"
            estilos_adicionales.append(f"('TEXTCOLOR', ({start}), ({end}), {color_texto})")
        elif opc == '6':  # VALIGN
            print("Opciones válidas: TOP, MIDDLE, BOTTOM")
            while True:
                valign = input("Alineación vertical: ").upper()
                if valign in ['TOP', 'MIDDLE', 'BOTTOM']:
                    break
                else:
                    print("[ERROR] Error: Debes introducir TOP, MIDDLE o BOTTOM. Intenta de nuevo.")
            estilos_adicionales.append(f"('VALIGN', ({start}), ({end}), '{valign}')")

    # 4. AUTOMATIZACIÓN DE GRÁFICOS (BONUS)
    print("\n--- CONFIGURACIÓN DE GRÁFICOS (OPCIONAL) ---")

    # Validar respuesta sobre agregar gráfico
    while True:
        agregar_grafico = input("¿Deseas añadir un gráfico? (s/n): ").lower()
        if agregar_grafico in ['s', 'n']:
            break
        else:
            print("[ERROR] Error: Debes responder 's' o 'n'. Intenta de nuevo.")

    # 4.5 NOMBRE DEL ARCHIVO PDF
    print("\n--- CONFIGURACIÓN DEL ARCHIVO PDF ---")
    nombre_pdf = input("¿Cómo deseas llamar al archivo PDF? (sin .pdf): ").strip()
    if not nombre_pdf:
        nombre_pdf = "examen_final"
    if not nombre_pdf.endswith(".pdf"):
        nombre_pdf += ".pdf"

    # 4.6 ANCHO DE COLUMNAS
    print("\n--- CONFIGURACIÓN DE COLUMNAS ---")
    print("¿Ancho de columnas?")
    print("  1. Automático (igual para todas: 80 píxeles)")
    print("  2. Personalizado (diferente por columna)")

    while True:
        opc_ancho = input("Selecciona: ")
        if opc_ancho in ['1', '2']:
            break
        else:
            print("[ERROR] Error: Debes introducir 1 o 2. Intenta de nuevo.")

    col_widths = None
    if opc_ancho == '1':
        col_widths = 80
    else:
        col_widths = []
        for c in range(cols):
            while True:
                try:
                    ancho = int(input(f"Ancho columna {c}: "))
                    if ancho > 0:
                        col_widths.append(ancho)
                        break
                    else:
                        print("[ERROR] Error: Debe ser un número positivo.")
                except ValueError:
                    print("[ERROR] Error: Debes introducir un número. Intenta de nuevo.")

    codigo_grafico = ""
    importaciones_grafico = ""

    if agregar_grafico == 's':
        print("\nTipos de gráficos disponibles:")
        print("  1. Barras (VerticalBarChart)")
        print("  2. Pastel (Pie Chart)")
        print("  3. Líneas (LineChart)")

        # Validar selección de tipo de gráfico
        while True:
            tipo_grafico = input("Selecciona el tipo (1-3): ")
            if tipo_grafico in ['1', '2', '3']:
                break
            else:
                print("[ERROR] Error: Debes introducir 1, 2 o 3. Intenta de nuevo.")

        if tipo_grafico == '1':  # GRÁFICO DE BARRAS
            importaciones_grafico = """from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.lib.units import inch"""

            print("\nDatos para gráfico de barras:")

            # Validar datos de series
            while True:
                try:
                    datos_str = input(
                        "Introduce los datos (series separadas por |, valores por comas). Ej: 10,20,30|15,25,35: ")
                    series = [tuple(map(float, s.strip().split(','))) for s in datos_str.split('|')]
                    if len(series) > 0 and all(len(s) > 0 for s in series):
                        break
                    else:
                        print("[ERROR] Error: Debes introducir al menos una serie con valores. Intenta de nuevo.")
                except ValueError:
                    print("[ERROR] Error: Formato incorrecto. Los valores deben ser números. Intenta de nuevo.")

            categorias = input("Nombres de categorías (separados por comas). Ej: Ene,Feb,Mar: ").split(',')
            categorias = [c.strip() for c in categorias]

            # ✅ MEJORA CRÍTICA 2: Validar coincidencia de datos
            num_valores_por_serie = len(series[0]) if series else 0
            num_categorias = len(categorias)

            if num_valores_por_serie != num_categorias:
                print(f"\n[⚠️  ADVERTENCIA] Mismatch detectado:")
                print(f"  - Series tienen {num_valores_por_serie} valores cada una")
                print(f"  - Se introdujeron {num_categorias} categorías")
                print(f"\nOpciones de corrección:")
                print(f"  1) Ajustar categorías (usar solo las primeras {num_valores_por_serie})")
                print(f"  2) Ajustar series (mantener solo primeros {num_categorias} valores)")
                print("  3) Cancelar")

                opcion_ajuste = input("\nSelecciona opción (1-3): ")
                if opcion_ajuste == '1':
                    categorias = categorias[:num_valores_por_serie]
                    print(f"[OK] Categorías ajustadas a: {categorias}")
                elif opcion_ajuste == '2':
                    series = [s[:num_categorias] for s in series]
                    print(f"[OK] Series ajustadas a {num_categorias} valores cada una")
                else:
                    print("[CANCELADO] Generación de gráfico de barras cancelada.")
                    agregar_grafico = 'n'
                    codigo_grafico = ""
                    importaciones_grafico = ""

            # Validar valor mínimo
            while True:
                try:
                    valor_min = float(input("Valor mínimo del eje Y (ej: 0): "))
                    break
                except ValueError:
                    print("[ERROR] Error: Debes introducir un número. Intenta de nuevo.")

            # Validar valor máximo
            while True:
                try:
                    valor_max = float(input("Valor máximo del eje Y (ej: 50): "))
                    if valor_max > valor_min:
                        break
                    else:
                        print("[ERROR] Error: El valor máximo debe ser mayor al mínimo. Intenta de nuevo.")
                except ValueError:
                    print("[ERROR] Error: Debes introducir un número. Intenta de nuevo.")

            # Validar paso
            while True:
                try:
                    valor_step = float(input("Paso entre valores en eje Y (ej: 10): "))
                    if valor_step > 0:
                        break
                    else:
                        print("[ERROR] Error: El paso debe ser mayor a 0. Intenta de nuevo.")
                except ValueError:
                    print("❌ Error: Debes introducir un número. Intenta de nuevo.")

            codigo_grafico = f"""
    # Gráfico de Barras
    drawing_grafico = Drawing(400, 250)
    bc = VerticalBarChart()
    bc.x = 50
    bc.y = 50
    bc.height = 150
    bc.width = 300
    bc.data = {series}
    bc.strokeColor = colors.black
    bc.valueAxis.valueMin = {valor_min}
    bc.valueAxis.valueMax = {valor_max}
    bc.valueAxis.valueStep = {valor_step}
    bc.categoryAxis.categoryNames = {categorias}
    bc.categoryAxis.labels.angle = 30
    bc.groupSpacing = 10
    bc.barSpacing = 2
    drawing_grafico.add(bc)
    story.append(drawing_grafico)
    story.append(Spacer(0, 0.3 * inch))
"""

        elif tipo_grafico == '2':  # GRÁFICO DE PASTEL
            importaciones_grafico = """from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.legends import Legend
from reportlab.lib.units import inch"""

            print("\nDatos para gráfico de pastel:")

            # Validar datos numéricos
            while True:
                try:
                    datos_str = input("Introduce los valores (separados por comas). Ej: 10,20,30,40: ")
                    datos_pastel = [float(x.strip()) for x in datos_str.split(',')]
                    if len(datos_pastel) > 0 and all(v > 0 for v in datos_pastel):
                        break
                    else:
                        print("[ERROR] Error: Debes introducir valores positivos. Intenta de nuevo.")
                except ValueError:
                    print("[ERROR] Error: Formato incorrecto. Los valores deben ser números. Intenta de nuevo.")

            etiquetas_str = input("Introduce las etiquetas (separadas por comas): ")
            etiquetas_pastel = [e.strip() for e in etiquetas_str.split(',')]

            # Validar cantidad de etiquetas
            if len(etiquetas_pastel) != len(datos_pastel):
                print(f"[Advertencia]: Tienes {len(datos_pastel)} valores pero {len(etiquetas_pastel)} etiquetas.")
                print("Se usarán las etiquetas disponibles.")

            # Validar índice de sector a resaltar
            resaltar = input("¿Deseas resaltar algún sector? (índice o pulsa Enter para saltarlo): ")
            codigo_resalte = ""
            if resaltar.strip() != "":
                try:
                    idx = int(resaltar)
                    if 0 <= idx < len(datos_pastel):
                        codigo_resalte = f"""    pc.slices[{idx}].popout = 10
    pc.slices[{idx}].strokeWidth = 2"""
                    else:
                        print(
                            f"[ERROR] Error: El índice debe estar entre 0 y {len(datos_pastel) - 1}. Se omite el resalte.")
                except ValueError:
                    print("[ERROR] Error: El índice debe ser un número entero. Se omite el resalte.")

            # ✅ MEJORA CRÍTICA 3: Personalización de colores en pastel
            colores_sectores = ""
            usar_colores = input("\n¿Personalizar colores de sectores? (s/n): ").lower().strip()

            if usar_colores == 's':
                print(
                    "\nColores disponibles: red, blue, green, yellow, orange, pink, purple, cyan, black, white, grey, brown, lime")
                colores_str = input("Introduce colores separados por comas (ej: red,blue,green): ")
                colores_lista = [c.strip().lower() for c in colores_str.split(',')]

                # Generar código para aplicar colores
                colores_sectores = "\n    # Aplicar colores personalizados\n"
                for i, color in enumerate(colores_lista[:len(datos_pastel)]):
                    colores_sectores += f"    pc.slices[{i}].fillColor = colors.{color}\n"

            codigo_grafico = f"""
    # Gráfico de Pastel
    drawing_grafico = Drawing(400, 250)
    pc = Pie()
    pc.x = 50
    pc.y = 30
    pc.width = 150
    pc.height = 150
    pc.data = {datos_pastel}
    pc.labels = {etiquetas_pastel}
    pc.slices.strokeWidth = 0.5
    pc.sideLabels = 1
{codigo_resalte}
{colores_sectores}

    # Leyenda para pastel
    legend = Legend()
    legend.x = 250
    legend.y = 30
    legend.dx = 8
    legend.dy = 8
    legend.fontSize = 8
    legend.colorNamePairs = [(pc.slices[i].fillColor, (pc.labels[i], '%0.1f' % pc.data[i])) for i in range(len(pc.data))]

    drawing_grafico.add(pc)
    drawing_grafico.add(legend)
    story.append(drawing_grafico)
    story.append(Spacer(0, 0.3 * inch))
"""

        elif tipo_grafico == '3':  # GRÁFICO DE LÍNEAS
            importaciones_grafico = """from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.lib.units import inch"""

            print("\nDatos para gráfico de líneas:")

            # Validar datos numéricos
            while True:
                try:
                    datos_str = input("Introduce los valores (separados por comas). Ej: 8,10,5,2: ")
                    datos_lineas = [float(x.strip()) for x in datos_str.split(',')]
                    if len(datos_lineas) > 0:
                        break
                    else:
                        print("[ERROR] Error: Debes introducir al menos un valor. Intenta de nuevo.")
                except ValueError:
                    print("[ERROR] Error: Formato incorrecto. Los valores deben ser números. Intenta de nuevo.")

            categorias = input("Nombres de categorías (separados por comas): ").split(',')
            categorias = [c.strip() for c in categorias]

            # Validar valor mínimo
            while True:
                try:
                    valor_min = float(input("Valor mínimo del eje X (ej: 0): "))
                    break
                except ValueError:
                    print("[ERROR] Error: Debes introducir un número. Intenta de nuevo.")

            # Validar valor máximo
            while True:
                try:
                    valor_max = float(input("Valor máximo del eje X (ej: 12): "))
                    if valor_max > valor_min:
                        break
                    else:
                        print("[ERROR] Error: El valor máximo debe ser mayor al mínimo. Intenta de nuevo.")
                except ValueError:
                    print("[ERROR] Error: Debes introducir un número. Intenta de nuevo.")

            # Validar paso
            while True:
                try:
                    valor_step = float(input("Paso entre valores (ej: 2): "))
                    if valor_step > 0:
                        break
                    else:
                        print("[ERROR] Error: El paso debe ser mayor a 0. Intenta de nuevo.")
                except ValueError:
                    print("[ERROR] Error: Debes introducir un número. Intenta de nuevo.")

            codigo_grafico = f"""
    # Gráfico de Líneas
    drawing_grafico = Drawing(400, 250)
    lc = HorizontalLineChart()
    lc.x = 30
    lc.y = 50
    lc.height = 150
    lc.width = 300
    lc.data = [{datos_lineas}]
    lc.categoryAxis.categoryNames = {categorias}
    lc.categoryAxis.labels.boxAnchor = 'n'
    lc.valueAxis.valueMin = {valor_min}
    lc.valueAxis.valueMax = {valor_max}
    lc.valueAxis.valueStep = {valor_step}
    lc.lines[0].strokeWidth = 2
    lc.lines[0].symbol = makeMarker('FilledCircle')
    drawing_grafico.add(lc)
    story.append(drawing_grafico)
    story.append(Spacer(0, 0.3 * inch))
"""

    # 5. CONSTRUCCIÓN DEL TEMPLATE
    # Se usan triples comillas para el bloque de código y f-strings para inyectar los datos

    # Construir estilos base con color inicial
    estilos_base = [
        "('GRID', (0,0), (-1,-1), 1, colors.black)",
        f"('BACKGROUND', (0,0), (-1,-1), {color_hex})"
    ]

    # Construir lista de estilos final
    if estilos_adicionales:
        estilos_str = ",\n        ".join(estilos_base + estilos_adicionales)
    else:
        estilos_str = ",\n        ".join(estilos_base)

    codigo_plantilla = f"""
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
{importaciones_grafico}

def build_pdf():
    doc = SimpleDocTemplate("{nombre_pdf}", pagesize=A4)
    story = []

    # Datos generados
    data = {tabla_datos}

    # Procesar imágenes en las celdas
    imagenes_mapa = {imagenes_insertar}
    for (fila, col), (ruta, ancho, alto) in imagenes_mapa.items():
        try:
            img = Image(ruta, width=ancho, height=alto)
            data[fila][col] = img
        except Exception as e:
            print(f"Error al cargar imagen {{ruta}}: {{e}}")
            data[fila][col] = "[Imagen no encontrada]"

    t = Table(data, colWidths={col_widths})

    # Estilos generados dinámicamente
    estilo_tabla = [
        {estilos_str}
    ]

    t.setStyle(TableStyle(estilo_tabla))
    story.append(t)
    story.append(Spacer(0, 0.3 * inch))

    # Gráficos (si se generaron)
    {codigo_grafico if codigo_grafico else "# Sin gráficos"}

    doc.build(story)
    print("PDF creado satisfactoriamente.")

if __name__ == "__main__":
    build_pdf()
"""

    with open(archivo_salida, "w", encoding="utf-8") as f:
        f.write(codigo_plantilla)

    print(f"\n¡Éxito! Ejecuta 'python {archivo_salida}' para generar el PDF.")


generador_examen_pro()