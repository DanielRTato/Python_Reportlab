from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.rl_settings import showBoundary

guion = []

follaEstilo = getSampleStyleSheet()

cabeceira = follaEstilo["Heading4"]

cabeceira.pageBreakBefore = 0
cabeceira.backColor = colors.lightcyan

paragrafo = Paragraph("CABECEIRADO DO DOCUMENTO", cabeceira)
guion.append(paragrafo)

texto = "Texto incuildo no documento, e que forma o intido" * 100

corpoTexto = follaEstilo["BodyText"]
corpoTexto.fontSize = 12
paragrafo2 = Paragraph(texto, corpoTexto)
guion.append(paragrafo2)

guion.append (Spacer(0,30))

imaxe = Image("imgGrande.jpg", 400, 500)
guion.append(imaxe)

doc = SimpleDocTemplate("exemploPlatypus.pdf", pagesize=A4, showBoundary=1)


doc.build(guion)
