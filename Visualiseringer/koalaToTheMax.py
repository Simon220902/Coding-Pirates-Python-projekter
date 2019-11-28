#inspireret af https://koalastothemax.com/
import pygame
import random


billede = pygame.image.load("koala4.jpeg")

billedeRatio = billede.get_width()/billede.get_height()

bredde = 500
højde = 500

skærm = pygame.display.set_mode((bredde, højde))
skærm.fill((255, 255, 255))

billedeHelSkærm = pygame.transform.scale(billede, (bredde, højde))


def genmFarveCirkel(x, y, r):
	#For at finde farven på den cirkel vi skal tegne skal vi jo finde gennemsnitsfarven
	
	cirkelGenmFarve = pygame.transform.average_color(billedeHelSkærm, (x-r, y-r, r*2, r*2))
	return cirkelGenmFarve

#En liste der består af alle de cirkler vi har tegnet, den data der gemmes er x, y, r og farven i en tuple for hver cirkel
#muligvis skal det være en dictionary senere hen men det må vi se på til den tid.
cirkler = [(bredde//2, højde//2, bredde//2, genmFarveCirkel(bredde//2, højde//2, bredde//2))]

def tegnCirkel(cirkel):
	pygame.draw.circle(skærm, cirkel[3], (cirkel[0], cirkel[1]), cirkel[2])

def overlap(musX, musY, cirkel):
	return ((musX >= cirkel[0]-cirkel[2] and musX <= cirkel[0]+cirkel[2]) and (musY >= cirkel[1]-cirkel[2] and musY <= cirkel[1]+cirkel[2]))
 
def nyeCirkler(cirkel, cirkelI):
	halvR = int((cirkel[2]+1)/2)
	if halvR >= 1:
		nye = []
		#De fire nye cirkler
		nye.append((cirkel[0]-halvR, cirkel[1]-halvR, halvR, genmFarveCirkel(cirkel[0]-halvR, cirkel[1]-halvR, halvR)))
		nye.append((cirkel[0]-halvR, cirkel[1]+halvR, halvR, genmFarveCirkel(cirkel[0]-halvR, cirkel[1]+halvR, halvR)))
		nye.append((cirkel[0]+halvR, cirkel[1]-halvR, halvR, genmFarveCirkel(cirkel[0]+halvR, cirkel[1]-halvR, halvR)))
		nye.append((cirkel[0]+halvR, cirkel[1]+halvR, halvR, genmFarveCirkel(cirkel[0]+halvR, cirkel[1]+halvR, halvR)))
		#Vi erstatter den nuværende cirkel med de fire nye cirkler
		del cirkler[cirkelI]
		for i in range(4):
			cirkler.insert(cirkelI+i, nye[i])

def tegn():
	skærm.fill((255, 255, 255))
	for cirkel in cirkler:
		tegnCirkel(cirkel)
	#tegn noget
	pygame.display.flip()

kør = True

while kør:
	tegn()
	print(len(cirkler))
	if pygame.mouse.get_rel()[0] or pygame.mouse.get_rel()[1]:
		musPos = pygame.mouse.get_pos()
		musX = musPos[0]
		musY = musPos[1]
		for cirkelI in range(len(cirkler)):
			cirkel = cirkler[cirkelI]
			if overlap(musX, musY, cirkel):
				nyeCirkler(cirkel, cirkelI)
				break

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			kør = False