import pygame

højde = 500
bredde = 500

skærm = pygame.display.set_mode((bredde, højde))

def tegn():
	#Gør hele skærmen sort
	skærm.fill((0,0,0))

	#Firkant:			(skærm, farve,	 (x,   y,   b,   h))
	pygame.draw.rect(skærm, (255, 0, 0), (100, 100, 200, 100))

	#Cirkel:		   (skærm, farve,		(x,     y),  r)
	pygame.draw.circle(skærm, (0, 255, 0), (200, 200), 10)

	#Cirkel:		   (skærm, farve,	 (x1,   y1), (x2,        y2), linjeBredde)
	pygame.draw.line(skærm, (0, 0, 255), (200, 200), (bredde, højde), 5)

	#Viser det vi har tegnet på skærmen
	pygame.display.flip()

kør = True

while kør:
	tegn()

	#Vi løber igennem alle de ting der er sket. (input)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			kør = False