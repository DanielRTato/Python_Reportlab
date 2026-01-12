from reportlab.pdfgen import canvas
from reportlab.lib import colors

texto = ("Este texto e para emeplo", "da utilizacion de canvas", "para usar con texto")

obxCanvas = canvas.Canvas("textoCanvas.pdf")

obxTexto = obxCanvas.beginText()
obxTexto.setTextOrigin(100, 500)
obxTexto.setFont("Courier", 16)

for linha in texto:
	obxTexto.textLine(linha)

obxTexto.setFillGray(0.5)
textoLongo = """Outro texto csdfsd
sdfsdfsdfsdf werwe werewf
sdfsdfsdf dsfs
dsfdsf"""
obxTexto.textLine(textoLongo)

obxTexto.setTextOrigin(20, 700)
for tipo_letra in obxCanvas.getAvailableFonts():
	obxTexto.setFont(tipo_letra, 16)
	obxTexto.textLine(tipo_letra)
	obxTexto.moveCursor(20,15)

obxCanvas.setFont("Helvetica", 16)
obxCanvas.drawText(obxTexto)

for linha in texto:
	obxTexto.textOut(linha)
	obxTexto.moveCursor(20,15)

# usar objetos Color desde reportlab.lib.colors
obxTexto.setFillColor(colors.Color(0.2, 0, 0.6))
obxTexto.setFillColor(colors.pink)

obxTexto.moveCursor(-60,15)
espazoCaracters = 0
for linha in texto:
	obxTexto.setCharSpace(espazoCaracters)
	obxTexto.textLine("Espazo %s: %s" % (espazoCaracters, linha))
	espazoCaracters += 1

obxTexto.setFillColor("Green")
obxTexto.setTextOrigin(20, 500)
obxTexto.setCharSpace(3)


obxCanvas.drawText(obxTexto)

obxCanvas.showPage()
obxCanvas.save()
