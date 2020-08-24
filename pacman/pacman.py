import pygame
#Til spøgelserne
import math
#Til spiselig mode
import random

bredde = 500
højde = 500

skærm = pygame.display.set_mode((bredde, højde))

bane = [
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
	[0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
	[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	[0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
	[0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
	[0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
	[0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
	[0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
	[0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0],
	[0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
	[0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
	[0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
	[0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
	[0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
	[0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0],
	[0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
	[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
#2. bane
bane = [
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0],
	[0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0],
	[0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
	[0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 2, 0],
	[0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 0],
	[0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 0, 0],
	[0, 2, 0, 0, 2, 0, 2, 2, 2, 2, 2, 0, 2, 0, 0, 0, 0],
	[0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0],
	[0, 0, 0, 0, 2, 0, 2, 2, 2, 2, 2, 0, 2, 0, 0, 2, 0],
	[0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 2, 0],
	[0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0],
	[0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0],
	[0, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0],
	[0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0],
	[0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 0],
	[0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0],
	[0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
#3. bane
bane = [
	[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0],
	[0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0],
	[0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
	[0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 2, 0],
	[0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 0],
	[0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 0, 0],
	[0, 2, 0, 0, 2, 0, 2, 2, 2, 2, 2, 0, 2, 0, 0, 0, 0],
	[1, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 1],
	[0, 0, 0, 0, 2, 0, 2, 2, 2, 2, 2, 0, 2, 0, 0, 2, 0],
	[0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 2, 0],
	[0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0],
	[0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0],
	[0, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0],
	[0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0],
	[0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 0],
	[0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0],
	[0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
	[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
bane = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
[0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0],
[0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 3, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0],
[0, 2, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0],
[0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
[0, 2, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0],
[0, 2, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0],
[0, 2, 2, 2, 2, 2, 3, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0],
[0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0],
[0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
[0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0],
[0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0],
[0, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 0],
[0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0],
[0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0],
[0, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 0],
[0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
[0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
[0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

ur = pygame.time.Clock()
fps = 7

#Farver: R    G    B
sort = (  0,   0,  0)
hvid = (255, 255, 255)
blå  = (  0,   0, 255)
gul  = (255, 238,   0)
rød  = (255, 0, 0)
orange=(255, 184, 82)
pink = (255, 184, 255)
grøn = (0,255,0)
lysblå = (0, 255, 255)

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
font = pygame.font.Font('data/8-bit.ttf', 30)
print(font)

pygame.mixer.init()

blokBredde = bredde//len(bane[0])
blokHøjde  = højde//len(bane)

def dist(blok1, række1, blok2, række2):
	#pythagoras til forskellen på de to punkter.
	return math.sqrt((blok1-blok2)**2 + (række1-række2)**2)


class Pacman:
	def __init__(self, række, blok):
		self.række = række
		self.blok = blok
		self.xf = 0
		self.yf = 0
		#Variabler til at tegne pacman
		self.x = self.blok*blokBredde
		self.y = self.række*blokHøjde
		self.r = blokHøjde//2
		#Pointne
		self.point = 0
		#animationer
		self.billede = pygame.image.load("data/sprites/pacman.png")
		self.billedBredde = 20
		self.billedHøjde = 20
		self.billedRække = 0
		self.billedNr = 0 #til at animere
		self.animer = 0
		#Lyd
		self.spiseLyd = pygame.mixer.Sound("data/lyde/pacman_chomp.wav")

	def flyt(self):
		"""
		Den første flyt funktion
		#Vi tjekker om den blok vi vil flytte pacman hen på er en væg, hvis ikke flytter vi ham
		if bane[self.række+self.yf][self.blok+self.xf] != 0:
			self.række += self.yf
			self.blok += self.xf
		#Pointne
		if bane[self.række][self.blok] == 2:
			self.point += 1
			bane[self.række][self.blok] = 1
		"""
		#Hvis den er indenfor banen
		if (self.række+self.yf < len(bane)-1 and self.række+self.yf > -1) and (self.blok+self.xf < len(bane[0])-1 and self.blok+self.xf > -1):
			if bane[self.række+self.yf][self.blok+self.xf] != 0:
				self.række += self.yf
				self.blok += self.xf
		
		#Er det i y-retningen vi bevæger os?
		elif self.yf != 0:
			#Går vi nedad
			#Hvis den går fra bunden til toppen af brættet
			if self.yf == 1 and bane[len(bane)-1][self.blok+self.xf] != 0:
				self.række = 0
			#Går vi opad
			#Hvis den går fra toppen til bunden af brættet
			elif self.yf == -1 and bane[0][self.blok+self.xf] != 0:
				self.række = len(bane)-1
		
		#Er det i x-retningen vi bevæger os?
		elif self.xf != 0:
			#Går vi mod højre
			#Hvis den går fra højre side til venstre side af brættet
			if self.xf == 1 and bane[self.række+self.yf][0] != 0:
				self.blok = 0
			#Går vi mod venstre
			#Hvis den går fra venstre side til højre side af brættet
			elif self.xf == -1 and bane[self.række+self.yf][len(bane[0])-1] != 0:
				self.blok = len(bane[0])-1
		
		#pointne
		if bane[self.række][self.blok] == 2:
			bane[self.række][self.blok] = 1
			self.point += 1
			#Vi sørger for at lyden ikke allerede bliver spillet
			if not pygame.mixer.get_busy():
				#Hvis ikke spiller vi den
				self.spiseLyd.play()
		elif bane[self.række][self.blok] == 3:
			global mode
			mode = 3
			bane[self.række][self.blok] = 1




	"""def tegn(self):
		#Vi finder det rigtige x- og y-koordinat
		self.x = self.blok*blokBredde
		self.y = self.række*blokHøjde
		#Vi tegner pacman, han er en gul cirkel
		pygame.draw.circle(skærm, gul, (self.x+self.r, self.y+self.r), self.r)"""

	def tegn(self):
		#Vi finder det rigtige x- og y-koordinat
		self.x = self.blok*blokBredde
		self.y = self.række*blokHøjde

		if self.xf == -1:
			self.billedRække = 0			
		elif self.xf == 1:
			self.billedRække = 1
		elif self.yf == -1:
			self.billedRække = 2
		elif self.yf == 1:
			self.billedRække = 3
		#Animer
		self.animer = not self.animer
		#venstre, højre, op, ned
		skærm.blit(self.billede, (self.x, self.y), (self.billedBredde*(self.billedNr+self.animer), self.billedHøjde*self.billedRække, self.billedBredde, self.billedHøjde))

pacman = Pacman(1, 1)

class Spøgelse:
	def __init__(self, række, blok, farve, billedStr, spredeRække, spredeBlok):
		self.række = række
		self.blok = blok
		self.xf = 1
		self.yf = 0
		#Variabler til at tegne pacman
		self.x = self.blok*blokBredde
		self.y = self.række*blokHøjde
		self.r = blokHøjde//2
		self.farve = farve
		#Mål
		self.rækkeMål = self.række
		self.blokMål = self.blok
		#Sprede mode målet
		self.spredeRække = spredeRække
		self.spredeBlok = spredeBlok
		#animationer
		self.billede = pygame.image.load(billedStr)
		self.flygtbillede = pygame.image.load("data/sprites/spøgelseFlygt.png")
		self.billedBredde = 20
		self.billedHøjde = 20
		self.billedRække = 0
		self.billedNr = 0 #til at animere
		self.animer = 0
	
	def flyt(self, pacmanRække, pacmanBlok):
		self.opdaterMål(pacmanBlok, pacmanRække)
		#Her sørger vi for at de mulige positioner ikke er den man lige kommer fra og ikke er en væg

		muligeRetninger = []
		# op, venstre, ned, højre.
		for ret in [(0,-1), (-1,0), (0,1), (1,0)]:
			#Hvis den ikke ryger ud:
			#Sørger for at spøgelset ikke går ud fra banen		Sørger for at vi ikke kan gå ind i væggen	Sørger for at den ikke går tilbage
			if (self.række+ret[1] > 0) and (self.række+ret[1] < len(bane)-1) and (self.blok+ret[0] > 0) and (self.blok+ret[0] < len(bane[0])):
				first = (bane[self.række+ret[1]][self.blok+ret[0]] != 0)
				second = ((self.blok+ret[0], self.række+ret[1]) != (self.blok-self.xf,self.række-self.yf))
				if first and second:
					muligeRetninger.append(ret)
		#Nu finder vi distancen til målet
		distancer = []
		for muligRet in muligeRetninger:
			distancer.append(dist(self.blokMål, self.rækkeMål, self.blok+muligRet[0], self.række+muligRet[1]))
		#Hvad er den mindste og hvilken er den
		valgtRet = muligeRetninger[distancer.index(min(distancer))]
		#Vi opdatere hastigheden
		self.xf = valgtRet[0]
		self.yf = valgtRet[1]
		#Der hvor vi flytter spøgelset
		self.række += self.yf
		self.blok += self.xf
	
	def flygt(self):
		muligeRetninger = []
		# op, venstre, ned, højre.
		for ret in [(0,-1), (-1,0), (0,1), (1,0)]:
			#Hvis den ikke ryger ud:
			#Sørger for at spøgelset ikke går ud fra banen		Sørger for at vi ikke kan gå ind i væggen	Sørger for at den ikke går tilbage
			if (self.række+ret[1] > 0) and (self.række+ret[1] < len(bane)-1) and (self.blok+ret[0] > 0) and (self.blok+ret[0] < len(bane[0])):
				first = (bane[self.række+ret[1]][self.blok+ret[0]] != 0)
				second = ((self.blok+ret[0], self.række+ret[1]) != (self.blok-self.xf,self.række-self.yf))
				if first and second:
					muligeRetninger.append(ret)
		#vi vælger en tilfældig retning
		valgtRet = random.choice(muligeRetninger)
		#Vi opdatere hastigheden
		self.xf = valgtRet[0]
		self.yf = valgtRet[1]
		#Der hvor vi flytter spøgelset
		self.række += self.yf
		self.blok += self.xf


	def opdaterMål(self, målBlok, målRække):
		self.rækkeMål = målRække
		self.blokMål = målBlok

	"""def tegn(self):
		#Vi finder det rigtige x- og y-koordinat
		self.x = self.blok*blokBredde
		self.y = self.række*blokHøjde
		#Vi tegner spøgelset
		pygame.draw.circle(skærm, self.farve, (self.x+self.r, self.y+self.r), self.r)
		pygame.draw.rect(skærm, self.farve, (self.blokMål*blokBredde+blokBredde//3, self.rækkeMål*blokHøjde+blokHøjde//3, blokBredde//3, blokHøjde//3))"""

	def tegn(self):
		#Vi finder det rigtige x- og y-koordinat
		self.x = self.blok*blokBredde
		self.y = self.række*blokHøjde
		if mode != 3:
			if self.xf == -1:
				self.billedNr = 4
			elif self.xf == 1:
				self.billedNr = 6
			elif self.yf == -1:
				self.billedNr = 0
			elif self.yf == 1:
				self.billedNr = 2
			
			#Animer
			self.animer = not self.animer
			
			#venstre, højre, op, ned
			skærm.blit(self.billede, (self.x, self.y), (self.billedBredde*(self.billedNr+self.animer), self.billedHøjde*self.billedRække, self.billedBredde, self.billedHøjde))
		elif mode == 3:
			self.animer = not self.animer
			
			#venstre, højre, op, ned
			skærm.blit(self.flygtbillede, (self.x, self.y), (self.billedBredde*(self.billedNr+self.animer), self.billedHøjde*self.billedRække, self.billedBredde, self.billedHøjde))


blinky = Spøgelse(1, 1, rød, "data/sprites/blinky.png", 0, len(bane[0]))
pinky = Spøgelse(1, len(bane[0])-2, pink, "data/sprites/pinky.png", 0, 0)
inky  = Spøgelse(len(bane)-2, 1, lysblå, "data/sprites/inky.png", len(bane), len(bane[0]))
clyde = Spøgelse(len(bane)-2, len(bane[0])-2, orange, "data/sprites/clyde.png", len(bane), 0)
spøgelser = [blinky, pinky, inky, clyde]
bevægSpøgelse = 0
#Jage: 1, Sprede: 2, Spiselige: 3
mode = 1

def tegn():
	skærm.fill(sort)
	tegnBane(bane)
	pacman.tegn()
	for spøgelse in spøgelser:
		spøgelse.tegn()
	tegnScore()
	pygame.display.flip()

def tegnBane(bane):
	for rækkeI in range(len(bane)):
		for blokI in range(len(bane[rækkeI])):
			if bane[rækkeI][blokI] == 0:
				pygame.draw.rect(skærm, blå, (blokI*blokBredde, rækkeI*blokHøjde, blokBredde, blokHøjde))
			elif bane[rækkeI][blokI] == 1:
				pygame.draw.rect(skærm, sort, (blokI*blokBredde, rækkeI*blokHøjde, blokBredde, blokHøjde))
			elif bane[rækkeI][blokI] == 2:
				tegnBlokPoint(rækkeI, blokI)
			elif bane[rækkeI][blokI] == 3:
				tegnBlokPowerPoint(rækkeI, blokI)

def tegnBlokPoint(rækkeI, blokI):
	pygame.draw.rect(skærm, sort, (blokI*blokBredde, rækkeI*blokHøjde, blokBredde, blokHøjde))
	pygame.draw.circle(skærm, gul, (blokI*blokBredde+blokBredde//2, rækkeI*blokHøjde+blokHøjde//2), blokBredde//5)

def tegnBlokPowerPoint(rækkeI, blokI):
	pygame.draw.rect(skærm, sort, (blokI*blokBredde, rækkeI*blokHøjde, blokBredde, blokHøjde))
	pygame.draw.circle(skærm, gul, (blokI*blokBredde+blokBredde//2, rækkeI*blokHøjde+blokHøjde//2), blokBredde//3)

def tegnScore():
	score = font.render('score: '+str(pacman.point), False, hvid)
	skærm.blit(score, (10, len(bane)*blokHøjde))

def opdater():
	global bevægSpøgelse
	pacman.flyt()
	if bevægSpøgelse > 3:
		#Hvis jagemode er igang
		if mode == 1:
			blinky.flyt(pacman.række, pacman.blok)
			#Fire foran
			pinky.flyt(pacman.række+pacman.yf*4, pacman.blok+pacman.xf*4)
			flytInky()
			flytClyde()
		elif mode == 2:
			blinky.flyt(blinky.spredeRække, blinky.spredeBlok)
			pinky.flyt(pinky.spredeRække, pinky.spredeBlok)
			inky.flyt(inky.spredeRække, inky.spredeBlok)
			clyde.flyt(clyde.spredeRække, clyde.spredeBlok)
		elif mode == 3:
			blinky.flygt()
			pinky.flygt()
			inky.flygt()
			clyde.flygt()

		bevægSpøgelse = 0
	else:
		bevægSpøgelse += 1

def flytInky():
	mål = (pacman.række+pacman.yf*2, pacman.blok+pacman.xf*2)
	blinkyVektor = (pacman.række-blinky.række, pacman.blok-blinky.blok)
	inky.flyt(mål[0]+blinkyVektor[0], mål[1]+blinkyVektor[1])

def flytClyde():
	if dist(pacman.blok, pacman.række, clyde.blok, clyde.række) > 8:
		clyde.flyt(pacman.række, pacman.blok)
	else:
		clyde.flyt(len(bane)-1,len(bane[0])-1)
#for at vi sørge at skifte mellem modesne.
passeret_tid = 0
kør = True
while kør:
	#Vi sørger for at vores spil aldrig kører med mere en den valgte fps
	passeret_tid += ur.tick(fps)
	tegn()
	opdater()
	print(mode)
	#Skal der skiftes mode?
	if passeret_tid > 7000:
		if mode == 1:
			mode = 2
			print("scatter")
		elif mode == 2:
			mode = 1
			print("chase")
		passeret_tid = 0

	#Her tjekker vi keyboard input
	taster = pygame.key.get_pressed()
	
	if taster[pygame.K_DOWN]:
		#Tjek om der hvor der vil rykkes hen er en væg, hvis ikke så ændrer retningen
		if bane[pacman.række+1][pacman.blok] != 0:
			pacman.xf = 0
			pacman.yf = 1

	if taster[pygame.K_UP]:
		if bane[pacman.række-1][pacman.blok] != 0:
			pacman.xf = 0
			pacman.yf = -1

	if taster[pygame.K_LEFT]:
		if bane[pacman.række][pacman.blok-1] != 0:
			pacman.xf = -1
			pacman.yf = 0

	if taster[pygame.K_RIGHT]:
		if bane[pacman.række][pacman.blok+1] != 0:
			pacman.xf = 1
			pacman.yf = 0
	
	#Her tjekker vi om der er blevet trykket på krydset
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			kør = False