from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

guion = []

imaxe = Image("equis23x23.jpg", 23, 23)

tit = ['Horario', '', '', '', '', '', '', '']
cab = ['', 'Luns', 'Martes', 'Mércores', 'Xoves', 'Venres', 'Sábado', 'Domingo']
actM = ['Mañán', 'Cole', 'Correr', '-', [imaxe,], '-', 'Estudar', 'Traballar ']
actT = ['Tarde', 'Xogar', 'Xantar', 'Durmir', '-', 'Camiñar', 'Ler', 'Cociñar']
actN = ['Noite', 'Cea', 'Televisión', 'Ler', '-', '-', 'Durmir', 'Durmir']
taboa = Table([tit, cab, actM, actT, actN])

taboa.setStyle([('TEXTCOLOR', (1, -4), (7, -4), colors.red),
                ('TEXTCOLOR', (0, 0), (0, -1), colors.blue),
                ('BOX', (0, 0), (-1, -1), 1, colors.chocolate),
                ('INNERGRID', (1, 1), (-1, -1), 0.25, colors.lightgrey),
                ('LINEABOVE', (1, 1), (-1,1 ), 2, colors.green),
                ('LINEBELOW', (0,0), (-1,0), 2, colors.green),
                ('SPAN', (0,0), (-1,0)),
                ('ALIGN', (0,0), (-1,0), 'CENTER'),
                ('BACKGROUND', (0,0), (-1,0), colors.lightblue)
                ])

guion.append(taboa)

doc = SimpleDocTemplate("taboasPlatypus.pdf", pagesize=A4, showBoundary=0)

doc.build(guion)
