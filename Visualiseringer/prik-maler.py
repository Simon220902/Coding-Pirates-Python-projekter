import pygame
import random

billede = pygame.image.load("monetFlot.jpeg")

bredde = 800
højde = int(bredde*(billede.get_height()/billede.get_width()))

skærm = pygame.display.set_mode((bredde, højde))

billedeHelSkærm = pygame.transform.scale(billede, (bredde, højde))

radius = 20

def tegn():
	#skærm.blit(billedeHelSkærm, (0, 0))
	x = random.randint(0, bredde-1)
	y = random.randint(0, højde-1)
	farve = billedeHelSkærm.get_at((x, y))
	pygame.draw.circle(skærm, farve, (x, y), radius)
	pygame.display.flip()


kør = True

while kør:
	tegn()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			kør = False
