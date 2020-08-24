import pygame
import random

bredde = 350
højde = 500

skærm = pygame.display.set_mode((bredde, højde))
ur = pygame.time.Clock()
fps = 10
dt = 0

point = 0

pygame.font.init() #Vi starter font modulet
#Vores font, der ligner den i pacman
font = pygame.font.Font('/Users/simon/Desktop/mulige fremtidige projekter/flappy bird/04B_19__.ttf', 40)

død = False

#Farver: R    G    B
sort = (  0,   0,  0)
hvid = (255, 255, 255)

baggrund_x = 0
baggrunds_billede = pygame.image.load("/Users/simon/Desktop/mulige fremtidige projekter/flappy bird/baggrund.png")
baggrunds_billede = pygame.transform.scale(baggrunds_billede, (bredde, højde))

class Fugl:
	def __init__(self):
		self.x = bredde//4
		self.y = højde//2
		self.r = 15
		self.v = 0
		self.a = 0.06
		self.hopper = False
		self.billede = pygame.image.load("/Users/simon/Desktop/mulige fremtidige projekter/flappy bird/midt.png")
		self.bredde = self.billede.get_width()
		self.højde = self.billede.get_height()

	def hop(self):
		self.hopper = True
		self.v = -0.3

	def opdater(self):
		if self.y <= højde - self.v*dt - self.a:
			self.v += self.a
			self.y += self.v*dt 

	def tegn(self):
		if self.v < 0:
			roteret_billede = pygame.transform.rotate(self.billede, 20)
		elif self.v == 0:
			roteret_billede = self.billede
		else:
			roteret_billede = pygame.transform.rotate(self.billede, -20)
		#pygame.draw.circle(skærm, hvid, (self.x, int(self.y)), self.r)
		skærm.blit(roteret_billede, (self.x-self.bredde//2, int(self.y)-self.højde//2))


class Rør:
	def __init__(self, x, sidste_rørs_y):
		self.x = x
		self.y = sidste_rørs_y + random.randint(-100,100)
		#Højden på det halve hul
		self.h = 80
		self.billede = pygame.image.load("/Users/simon/Desktop/mulige fremtidige projekter/flappy bird/rør.png")
		self.billede_h = self.billede.get_height()
		self.billede_w = self.billede.get_width()
		self.b = self.billede_w
		self.point_givet = False

	def opdater(self):
		self.x -= 1
	
	def tegn(self):
		#Øverste rør
		skærm.blit(pygame.transform.rotate(self.billede, 180), (self.x, self.y-self.h-self.billede_h))
		#pygame.draw.rect(skærm, hvid, (self.x, self.y+self.h, self.b, højde))
		#Nederste rør
		skærm.blit(self.billede, (self.x, self.y+self.h))
		#pygame.draw.rect(skærm, hvid, (self.x, self.y-self.h-højde, self.b, højde))

fugl = Fugl()
rør = [Rør(bredde//2, højde//2), Rør(bredde, højde//2), Rør(bredde+bredde//2, højde//2)]

def opdater():
	fugl.opdater()
	rørOpdater()
	baggrundOpdater()

def tegn():
	skærm.fill(sort)
	baggrundTegn()
	fugl.tegn()
	for r in rør:
		r.tegn()
	scoreTegn()
	pygame.display.flip()

def baggrundTegn():
	skærm.blit(baggrunds_billede, (baggrund_x, 0))
	skærm.blit(baggrunds_billede, (bredde+baggrund_x, 0))

def scoreTegn():
	score = font.render(str(point), False, (255, 255, 255))
	skærm.blit(score, (bredde//2-(score.get_width()//2), højde//8-(score.get_height()//2)))

def baggrundOpdater():
	global baggrund_x
	if baggrund_x < -bredde:
		baggrund_x = 0
	else:
		baggrund_x -= 1

def rørOpdater():
	global død, point
	for rørI in range(len(rør)):
		r = rør[rørI]
		r.opdater()
		if fugl.x+fugl.r > r.x and fugl.x-fugl.r < r.x+r.b and not(fugl.y+fugl.r < r.y+r.h and fugl.y-fugl.r > r.y-r.h):
			død = True
		if r.x + r.b < 0:
			rør.append(Rør(bredde+bredde//2, r.y))
			del rør[rørI]
		if fugl.x-fugl.r > r.x + r.b and not r.point_givet:
			point += 1
			r.point_givet = True

kør = True
#variabel ai vi tænder/slukker for den ved at trykke på a
ai = True
while kør and not død:
	dt = ur.tick()
	opdater()
	tegn()
	for event in pygame.event.get():
		kørt = True
		if event.type == pygame.QUIT:
			kør = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				ai = not ai
			if event.key == pygame.K_SPACE and not ai:
				fugl.hop()

	#AI
	if ai:
		if rør[0].x + rør[0].b > fugl.x-fugl.r:
			if rør[0].y < fugl.y-fugl.r:
				fugl.hop()
		else:
			if rør[1].y < fugl.y-fugl.r:
				fugl.hop()
