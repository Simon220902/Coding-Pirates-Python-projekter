import pygame

højde = 500
bredde = 500

#Vi skal loade en font for at kunne tegne noget tekst
pygame.font.init()
font = pygame.font.SysFont(None, 30)

skærm = pygame.display.set_mode((bredde, højde))

def tegn():
	#Gør hele skærmen sort
	skærm.fill((0,0,0))

	tegnTekst("HVAD SÅ, ER I, ER I, ER I KLAR?")

	#Viser det vi har tegnet på skærmen
	pygame.display.flip()

def tegnTekst(tekst):
	#						(teksten,     ?, farve)
	tekstBillede = font.render(tekst, True, (255, 255, 255))
	#tekstStørrelse = tekst.get_size()

	#Blit propper et billede på skærmen på et givent koordinat
	#			(billede,     (x,        t))
	skærm.blit(tekstBillede, (100, 100))

kør = True

while kør:
	tegn()

	#Vi løber igennem alle de ting der er sket. (input)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			kør = False