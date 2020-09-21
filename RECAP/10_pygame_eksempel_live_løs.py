#Mål
#Firkant(TJEK)
#Firkant kan bevæge sig(TJEK)
#Tekst
#Firkant bevæger sig et sted hen og så tekst!

import pygame

højde = 500
bredde = 500

#Vi skal loade en font for at kunne tegne noget tekst
pygame.font.init()
font = pygame.font.SysFont(None, 30)


skærm = pygame.display.set_mode((bredde, højde))

firkantX = 50
firkantY = 50
firkantB = 100
firkantH = 50

feltX = 400
feltY = 400
feltB = 100
feltH = 100

def tegn():
	#Gør hele skærmen sort
	skærm.fill((0,0,0))

	#Vi tegner teksten
	tegnTekst("Flyt firkanten ind i det gule felt", 10, 10)

	#Hvis firkanten er lidt inde giver vi en besked
	if firkantX+firkantB >= feltX and firkantY+firkantH >= feltY and (firkantX < feltX or firkantY < feltY):
		tegnTekst("KOM SÅ DU ER DER NÆSTEN", 10, 50)
	#Hvis firkanten er helt inde giver vi en anden besked
	elif firkantX+firkantB >= feltX and firkantY+firkantH >= feltY and firkantX >= feltX and firkantY >= feltY:
		tegnTekst("WUUHUU DU GJORDE DET", 10, 50)


	#Vi tegner firkanten
	pygame.draw.rect(skærm, (255, 0, 0), (firkantX, firkantY, firkantB, firkantH))

	#Vi tegner felt
	pygame.draw.rect(skærm, (255, 255, 0), (feltX, feltY, feltB, feltH))
	


	#Viser det vi har tegnet på skærmen
	pygame.display.flip()

def tegnTekst(tekst, x, y):
	#						(teksten,     ?, farve)
	tekstBillede = font.render(tekst, True, (255, 255, 255))
	#tekstStørrelse = tekst.get_size()

	#Blit propper et billede på skærmen på et givent koordinat
	#			(billede,     (x,        t))
	skærm.blit(tekstBillede, (x, y))

kør = True

while kør:
	tegn()

	#Vi løber igennem alle de ting der er sket. (input)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			kør = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				firkantY -= 10
			elif event.key == pygame.K_s:
				firkantY += 10
			elif event.key == pygame.K_a:
				firkantX -= 10
			elif event.key == pygame.K_d:
				firkantX += 10