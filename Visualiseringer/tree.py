import pygame
import math

højde = 500
bredde = 500
size = 100

skærm = pygame.display.set_mode((bredde, højde))

vinkel = math.radians(60)

def træ(x, y, l):
	if l >= size:
		l = l * 1/2
		x1 = int(math.sin(vinkel)*l+x)
		y1 = int(y+math.cos(vinkel)*l)
		x2 = int(x+math.sin(-vinkel)*l)
		y2 = int(y+math.cos(-vinkel)*l)
		
		pygame.draw.line(skærm, (255,255,255), (x,y), (x1, y1))
		pygame.draw.line(skærm, (255,255,255), (x,y), (x2, y2))
		pygame.draw.circle(skærm, (0, 150, 0), (x1, y1), 10)
		pygame.draw.circle(skærm, (0, 150, 0), (x2, y2), 10)	
		træ(x1, y1, l)
		træ(x2, y2, l)

def tegn():
	skærm.fill((0,0,0))
	pygame.draw.line(skærm, (255,255,255), (bredde//2, 0), (bredde//2, 100), 10)
	træ(bredde//2, 100, 400)
	pygame.display.flip()

kør = True

while kør:
	tegn()
	vinkel = math.radians(pygame.mouse.get_pos()[0])
	size = pygame.mouse.get_pos()[1]//10 + 20
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			kør = False