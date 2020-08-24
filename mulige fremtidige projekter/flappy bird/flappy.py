import pygame
import random

bredde = 350
højde = 500

skærm = pygame.display.set_mode((bredde, højde))
ur = pygame.time.Clock()
fps = 10
dt = 0
død = False

#Farver: R    G    B
sort = (  0,   0,  0)
hvid = (255, 255, 255)

class Fugl:
	def __init__(self):
		self.x = bredde//4
		self.y = højde//2
		self.r = 15
		self.v = 0
		self.a = 0.06
		self.hopper = False
	
	def hop(self):
		self.hopper = True
		self.v = -0.6
 
	def opdater(self):
		if self.y <= højde - self.v*dt - self.a:
			self.v += self.a
			self.y += self.v*dt 

	def tegn(self):
		pygame.draw.circle(skærm, hvid, (self.x, int(self.y)), self.r)

class Rør:
	def __init__(self, x, sidste_rørs_y):
		self.x = x
		self.y = sidste_rørs_y + random.randint(-20,20)
		self.b = 30
		#Højden på det halve hul
		self.h = 80
	
	def opdater(self):
		self.x -= 1
	
	def tegn(self):
		#Øverste rør
		pygame.draw.rect(skærm, hvid, (self.x, self.y-self.h-højde, self.b, højde))
		#Nederste rør
		pygame.draw.rect(skærm, hvid, (self.x, self.y+self.h, self.b, højde))

fugl = Fugl()
rør = [Rør(bredde//2, højde//2), Rør(bredde, højde//2), Rør(bredde+bredde//2, højde//2)]

def opdater():
	fugl.opdater()
	rørOpdater()

def tegn():
	skærm.fill(sort)
	fugl.tegn()
	for r in rør:
		r.tegn()
	pygame.display.flip()

def rørOpdater():
	global død
	for rørI in range(len(rør)):
		r = rør[rørI]
		r.opdater()

		if fugl.x+fugl.r > r.x and fugl.x-fugl.r < r.x+r.b and not(fugl.y+fugl.r < r.y+r.h and fugl.y-fugl.r > r.y-r.h):
			død = True
		if r.x + r.b < 0:
			rør.append(Rør(bredde+bredde//2, r.y))
			del rør[rørI]

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
		if rør[0].x > fugl.x-fugl.r:
			if rør[0].y < fugl.y-fugl.r:
				fugl.hop()
		else:
			if rør[1].y < fugl.y-fugl.r:
				fugl.hop()
