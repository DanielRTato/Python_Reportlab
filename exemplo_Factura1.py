from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle, Spacer, Image

hojaEstilo = getSampleStyleSheet()  # Obtenemos la hoja de estilos de muestra.

elementosDoc = []  # Lista para los elementos del documento.

imagen = Image("check.png", 20, 20)  # Cargamos una imagen pequeña (20x20).
estiloTitulo = hojaEstilo["H2"]
