from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

guion= []

cab = ['', 'Luns', 'Martes', 'Mércores', 'Xoves', 'Venres', 'Sábado', 'Domingo']
actM = ['Mañán', 'Cole', 'Correr', '-', '-', '-', 'Estudar', 'Traballar ']
actT = ['Tarde', 'Xogar', 'Xantar', 'Durmir', '-', 'Camiñar', 'Ler', 'Cociñar']
actN = ['Noite', 'Cea', 'Televisión', 'Ler', '-', '-', 'Durmir', 'Durmir']
taboa = Table ([[cab, actM, actT, actN]])

taboa.setStyle([('TEXTCOLOR',(1,-4),(7,-4),colors.red),
                ('TEXTCOLOR',(0,0),(0,3),colors.blue)
                ('BOX',(0,0),(-1,-1),1, colors.chocolate),
                ('INNERGRID',(1,1),(-1,-1),0.25, colors.lightgrey)])

guion.append(taboa)



doc = SimpleDocTemplate("taboasPlatypus.pdf", pagesize=A4, showBoundary=0)

doc.build(guion)
