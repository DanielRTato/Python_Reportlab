from reportlab.pdfgen import canvas # Importa a biblioteca para gerar PDFs

folla = canvas.Canvas("primeiroDocumento.pdf") # Cria um novo documento PDF chamado "primeiroDocumento.pdf"

folla.drawString(0,0, "Posición incicio (0,0)") # Diseña un string no documento na posicion (0,0)
folla.drawString(50, 100 , "Posición (50,100)") # Diseña un string no documento na posicion (50,100)
folla.drawString(150, 200 , "Posición (150,200)") # Diseña un string no documento na posicion (150,200)

folla.drawImage("equis23x23.jpg", 500, 500, width=50, height=50) # Engade unha imaxe no documento na posicion (700,700) cun tamaño de 50x50
folla.drawImage("tic16x16.jpg", 100, 50, width=16, height=16) # Engade unha imaxe no documento na posicion (700,700) cun tamaño de 50x50


folla.showPage()
folla.save()