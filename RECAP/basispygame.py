import pygame

højde = 500
bredde = 500

skærm = pygame.display.set_mode((bredde, højde))

def tegn():
	skærm.fill((0,0,0))
	#TEGN ET ELLER ANDET
	pygame.display.flip()

kør = True

while kør:
	tegn()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			kør = False