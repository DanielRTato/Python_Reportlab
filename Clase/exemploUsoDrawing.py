from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from  reportlab.lib.pagesizes import A4

from exemploUsoCanvas import folla

guion = []

imaxe = Image(0, 0, 300, 300, "imgGrande.jpg")

debuxo = Drawing(300, 12)
debuxo.add(imaxe)
guion.append(debuxo)

imaxe
debuxo2 = Drawing()
debuxo2.add(imaxe)
debuxo2.translate(350, 250) # mover o debuxo2
guion.append(debuxo2)

debuxo3 = Drawing()
debuxo3.add(imaxe)
debuxo3.rotate(45) # xirar o debuxo3
debuxo3.translate(400, 200) # mover o debuxo3
guion.append(debuxo3)

debuxo4 = Drawing()
debuxo4.add(imaxe)
debuxo4.scale(0.5, 0.5) # reducir o debuxo4
debuxo4.translate(595.2755905511812, 841.8897637795277) # mover o debuxo4
guion.append(debuxo4)

imaxe
folla = Drawing (A4[0], A4[1])
print(A4) # (595.2755905511812, 841.8897637795277)

for elemento in guion:
    folla.add(elemento)

renderPDF.drawToFile(folla, "exemploConDrawing.pdf")