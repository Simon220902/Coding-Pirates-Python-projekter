#inspireret af en side fundet på https://theuselessweb.com/
import pygame
import math
import random

bredde = 500
højde = 500

skærm = pygame.display.set_mode((bredde, højde))

radius = 10
pupilradius = 3

baggrund = (random.randint(0,255), random.randint(0,255), 50)

øjne = []

def længde(vektor):
	l = math.sqrt(vektor[0]**2+vektor[1]**2)
	#Fordi den noglegange er nul og så får man en div nul fejl
	if l != 0:
		return l
	else:
		return 1

def enhedsvektor(vektor):
	l = længde(vektor)
	return [vektor[0]/l, vektor[1]/l]

def tegnØje(øje):
	pygame.draw.circle(skærm, (255, 255, 255), (øje[0], øje[1]), radius)
	pygame.draw.circle(skærm, (0  ,   0,   0), (int(øje[0]+(øje[2][0]*pupilradius)), int(øje[1]+(øje[2][1]*pupilradius))), pupilradius)

def opdaterøjne(musx, musy):
	for øje in øjne:
		#Beregn den nye vektor fra centrum af cirkel til musen
		øje[2][0] = musx-øje[0]
		øje[2][1] = musy-øje[1]
		#Sæt den til at være lig enhedsvektoren
		øje[2] = enhedsvektor(øje[2])

def tegn():
	skærm.fill(baggrund)#skærm.fill((random.randint(0,255), random.randint(0,255), 50))
	for øje in øjne:
		tegnØje(øje)
	pygame.display.flip()

kør = True
while kør:
	tegn()
	musPos = pygame.mouse.get_pos()
	musx = musPos[0]
	musy = musPos[1]
	opdaterøjne(musx, musy)	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			øjne.append([musx-radius, musy, enhedsvektor([musx-radius, musy])])
			øjne.append([musx+radius, musy, enhedsvektor([musx+radius, musy])])