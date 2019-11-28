import pygame
import random

højde = 500
bredde = 600

skærm = pygame.display.set_mode((bredde, højde))

dvdBillede = pygame.image.load("dvd.png")
dvdX = random.randint(0, bredde)
dvdY = random.randint(0, højde)
dvdB = 32
dvdH = 32
dvdSX = 5
dvdSY = 5
dvdFarve = (0,0,0)

def tegn():
	skærm.fill((255, 255, 255))
	skærm.blit(dvdBillede, (dvdX, dvdY))
	pygame.display.flip()

def skiftFarve():
	global dvdFarve
	pixels = pygame.PixelArray(dvdBillede)
	nyFarve = (random.randint(0, 255), random.randint(0, 255), random.randint(0,255))
	pixels.replace(dvdFarve, nyFarve)
	dvdFarve = nyFarve
	del pixels

kør = True

while kør:
	tegn()
	dvdX += dvdSX
	dvdY += dvdSY

	if (dvdX + dvdB >= bredde or dvdX <= 0):
		dvdSX = -dvdSX
		skiftFarve()
	if (dvdY + dvdH >= højde or dvdY <= 0):
		dvdSY = - dvdSY
		skiftFarve()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			kør = False
