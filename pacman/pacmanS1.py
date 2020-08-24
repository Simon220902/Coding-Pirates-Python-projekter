import pygame

bredde = 500
højde = 500

skærm = pygame.display.set_mode((bredde, højde))

kør = True

while kør:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			kør = False
