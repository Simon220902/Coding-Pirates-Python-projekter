import pygame
import math

bredde = 18*20
højde = 300

skærm = pygame.display.set_mode((bredde, højde))


class Spiller:
	x = bredde//2
	y = højde - 20
	b = 50
	h = 10
	vx = 0
	farve = (255, 0, 0)

	def opdater(self):
		if self.x + self.vx <= bredde and self.x + self.vx + self.b >= 0:
			self.x += self.vx

	def tegn(self):
		pygame.draw.rect(skærm, self.farve, (self.x, self.y, self.b, self.h))

class Blok:
	def __init__(self, x, y, b, h, farve):
		self.x = x
		self.y = y
		self.b = b
		self.h = h
		self.farve = farve
	
	def tegn(self):
		pygame.draw.rect(skærm, self.farve, (self.x, self.y, self.b, self.h))

class Bold:
	def __init__(self):
		self.x = bredde // 2 + spiller.b//2
		self.y = højde - 30
		self.r = 5
		self.fart = 4
		self.vx = 0
		self.vy = -self.fart
	
	def opdater(self):
		#Hvis vi rammer "battet"
		if self.y-self.r >= spiller.y:
			print("ramt")
			#Hvis den er lige på så er 
			if self.x == spiller.x+spiller.b//2:
				print("midt")
				self.vx = 0
				self.vy = -self.fart
			#Hvis den er til højre for, men ikke udenfor
			elif self.x > spiller.x+spiller.b//2 and self.x <= spiller.x+spiller.b:
				print("højre")
				#Så afhængigt af hvor langt henne den er jo mere bliver den mod venstre?
				#  ca. 75 grad i rad * 
				vinkel = 1.3 * ((self.x-(spiller.x+spiller.b//2))/(spiller.b//2))
				self.vx = math.cos(vinkel)*self.fart
				self.vy = -math.sin(vinkel)*self.fart
			#Hvis den er til venstre for, men ikke udenfor
			elif self.x < spiller.x+spiller.b//2 and self.x >= spiller.x:
				print("venstre")
				vinkel = (math.pi)-1.3 * ((self.x-(spiller.x+spiller.b//2))/(spiller.b//2))
				self.vx = math.cos(vinkel)*self.fart
				self.vy = math.sin(vinkel)*self.fart

		self.x += self.vx
		self.y += self.vy
		if self.y-self.r <= 0:
			self.vy = -self.vy
		elif self.y-self.r >= højde:
			global kør
			kør = False
		if self.x-self.r <= 0 or self.x+self.r >=bredde:
			self.vx = -self.vx

	def tegn(self):
		pygame.draw.circle(skærm, (255, 0, 0), (int(self.x), int(self.y)), self.r)
		#Linjen hvor den skal til at lande
		#pygame.draw.line(skærm, (0,255,0),(self.x, self.y), (self.x+self.vx*1000,self.y+self.vy*1000),5)


spiller = Spiller()
bold = Bold()
blokke = []
#Her genererer vi blokkene
kolonner = 18
rækker = 6
kolonne_bredde = bredde//kolonner
kolonne_højde = 10
#Den øverste række er 
farver = [(200, 72, 72), (198, 108, 108), (178, 127, 127), (162, 162, 162), (72, 160, 160), (66, 72, 72)]

for række in range(rækker):
	for kolonne in range(kolonner):
		blokke.append(Blok(kolonne*kolonne_bredde, række*kolonne_højde+kolonne_højde*3, kolonne_bredde, kolonne_højde,farver[række]))


def tegn():
	skærm.fill((0,0,0))
	spiller.tegn()
	for blok in blokke:
		blok.tegn()
	bold.tegn()
	pygame.display.flip()

def opdater():
	print(bold.vx, bold.vy)
	spiller.opdater()
	bold.opdater()
	kollision_mellem_bold_og_blok()

#Returnere "ned", "op", "venstre", "højre" afhængigt af hvilken side den rammmer ellers return
def kollision_mellem_bold_og_blok():
	for blokI in range(len(blokke)):
		blok = blokke[blokI]
		# 							x											y
		if (blok.x <= bold.x+bold.r and blok.x+blok.b >= bold.x-bold.r) and (blok.y <= bold.y+bold.r and blok.y+blok.h >= bold.y-bold.r):
			#har den ramt slettes blokken og bolden sendes i omvendt y 
			#Siderne hvor vi sætter vx = -vx
			del blokke[blokI]
			bold.vy = -bold.vy
			break

kør = True

while kør:
	opdater()
	tegn()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			kør = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				spiller.vx = -5
			elif event.key == pygame.K_RIGHT:
				spiller.vx = 5
			elif event.key == pygame.K_UP:
				bold.vx *= 1.2
				bold.vy *= 1.2
			elif event.key == pygame.K_DOWN:
				bold.vx *= 0.835
				bold.vy *= 0.835
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT and spiller.vx < 0:
				spiller.vx = 0
			elif event.key == pygame.K_RIGHT and spiller.vx > 0:
				spiller.vx = 0