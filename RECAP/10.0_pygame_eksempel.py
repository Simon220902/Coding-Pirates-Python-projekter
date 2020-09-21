import pygame

højde = 500
bredde = 500

skærm = pygame.display.set_mode((bredde, højde))

def tegn():
	#Gør hele skærmen sort
	skærm.fill((0,0,0))

	#Viser det vi har tegnet på skærmen
	pygame.display.flip()

kør = True

while kør:
	tegn()

	#Vi løber igennem alle de ting der er sket. (input)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			kør = False