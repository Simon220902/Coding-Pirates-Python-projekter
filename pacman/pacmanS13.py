#Næste spøgelse Clyde
#Bruger pacmans koordinater, indtil den er 8 indenfor pacman (vi sætter den til 4), hvor den derefter bruger nederste venster hjørne.
#Endnu en instans af spøgelses klassen

import pygame
import math

bredde = 500
højde = 500

skærm = pygame.display.set_mode((bredde, højde))

bane = [
	[0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0],
	[0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0],
	[0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
	[0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 2, 0],
	[0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 0],
	[0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 0, 0],
	[0, 2, 0, 0, 2, 0, 2, 2, 2, 2, 2, 0, 2, 0, 0, 0, 0],
	[2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2],
	[0, 0, 0, 0, 2, 0, 2, 2, 2, 2, 2, 0, 2, 0, 0, 2, 0],
	[0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 2, 0],
	[0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0],
	[0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0],
	[0, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0],
	[0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0],
	[0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 0],
	[0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0],
	[0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
	[0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

blokBredde = bredde//len(bane[0])
blokHøjde  = højde//len(bane)

ur = pygame.time.Clock()
fps = 7

#Farver: R    G    B
sort = (  0,   0,  0)
hvid = (255, 255, 255)
blå  = (  0,   0, 255)
gul  = (255, 238,   0)
rød = (255, 0, 0)
pink = (252,134,170)
lysblå = (27, 177, 230)
orange = (249, 126, 22)

def dist(blok1, række1, blok2, række2):
	#pythagoras til forskellen på de to punkter.
	return math.sqrt((blok1-blok2)**2 + (række1-række2)**2)

class Pacman:
	def __init__(self, række, blok):
		#Pacmans position på banen
		self.række = række
		self.blok = blok
		#Pacmans retning
		self.xf = 0
		self.yf = 0
		#Variabler til at tegne pacman
		self.x = self.blok*blokBredde
		self.y = self.række*blokHøjde
		self.r = blokHøjde//2
		#Point
		self.point = 0
		#Ilive
		self.ilive = True

	def tegn(self):
		#Vi finder det rigtige x- og y-koordinat
		self.x = self.blok*blokBredde
		self.y = self.række*blokHøjde
		#Vi tegner pacman, han er en gul cirkel
		pygame.draw.circle(skærm, gul, (self.x+self.r, self.y+self.r), self.r)

	def flyt(self):
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

		#Vi tjekker om den blok vi er i (efter vi har flyttet os) er et point, hvis ja
		#pointne
		if bane[self.række][self.blok] == 2:
			bane[self.række][self.blok] = 1
			self.point += 10

class Spøgelse:
	def __init__(self, række, blok, farve):
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
	
	def flyt(self, målRække, målBlok):
		#Få målet som argument og sæt det ind i klassens
		self.rækkeMål = målRække
		self.blokMål = målBlok

		#Generér de mulige positioner
		#Her sørger vi for at de mulige positioner ikke er den man lige kommer fra og ikke er en væg
		muligeRetninger = []
		# op, venstre, ned, højre.
		for ret in [(0,-1), (-1,0), (0,1), (1,0)]:
			#Hvis den ikke ryger ud:
			#Sørger for at spøgelset ikke går ud fra banen		Sørger for at vi ikke kan gå ind i væggen	Sørger for at den ikke går tilbage
			if (self.række+ret[1] > 0) and (self.række+ret[1] < len(bane)-1) and (self.blok+ret[0] > 0) and (self.blok+ret[0] < len(bane[0])):
				#Er den retningen en væg?
				væg = (bane[self.række+ret[1]][self.blok+ret[0]] != 0)
				#Er det den tidligere position
				tidligere = ((self.blok+ret[0], self.række+ret[1]) != (self.blok-self.xf,self.række-self.yf))
				if væg and tidligere:
					muligeRetninger.append(ret)

		#Find distancen til målet (lav dist fuktion)
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

	def tegn(self):
		#Vi finder det rigtige x- og y-koordinat
		self.x = self.blok*blokBredde
		self.y = self.række*blokHøjde
		#Vi tegner spøgelset
		pygame.draw.circle(skærm, self.farve, (self.x+self.r, self.y+self.r), self.r)
		#Vi tegner spøgelsets mål
		pygame.draw.rect(skærm, self.farve, (self.blokMål*blokBredde+blokBredde//3, self.rækkeMål*blokHøjde+blokHøjde//3, blokBredde//3, blokHøjde//3))
pacman = Pacman(4, 4)

blinky = Spøgelse(1, 1, rød)
pinky =  Spøgelse(3, 8, pink)
inky = Spøgelse(8, 3, lysblå)
clyde = Spøgelse(8, 5, orange)

spøgelser = [blinky, pinky, inky, clyde]

bevægSpøgelse = 0

def tegn():
	skærm.fill(sort)
	tegnBane(bane)
	pacman.tegn()
	tegnSpøgelser()
	pygame.display.flip()

def opdater():
	global bevægSpøgelse
	spøgelseKollision()
	pacman.flyt()
	if bevægSpøgelse > 3:
		bevægSpøgelser()
		bevægSpøgelse = 0
	else:
		bevægSpøgelse += 1

def tegnBane(bane):
	for rækkeI in range(len(bane)):
		for blokI in range(len(bane[rækkeI])):
			if bane[rækkeI][blokI] == 0:
				pygame.draw.rect(skærm, blå, (blokI*blokBredde, rækkeI*blokHøjde, blokBredde, blokHøjde))
			elif bane[rækkeI][blokI] == 1:
				pygame.draw.rect(skærm, sort, (blokI*blokBredde, rækkeI*blokHøjde, blokBredde, blokHøjde))
			elif bane[rækkeI][blokI] == 2:
				tegnBlokPoint(rækkeI, blokI)

def tegnBlokPoint(rækkeI, blokI):
	pygame.draw.rect(skærm, sort, (blokI*blokBredde, rækkeI*blokHøjde, blokBredde, blokHøjde))
	pygame.draw.circle(skærm, gul, (blokI*blokBredde+blokBredde//2, rækkeI*blokHøjde+blokHøjde//2), blokBredde//5)

def tegnSpøgelser():
	for spøgelse in spøgelser:
		spøgelse.tegn()

#Tjekker pacman har ramt spøgelset:
def spøgelseKollision():
	for spøgelse in spøgelser:
		if pacman.række == spøgelse.række and pacman.blok == spøgelse.blok:
			pacman.ilive = False

def bevægSpøgelser():
	#Blinkys mål er bare pacmans koordinater
	blinky.flyt(pacman.række, pacman.blok)
	#Pinkys mål er pacmans koordinater og 4 blokke foran
	pinky.flyt(pacman.række+4*pacman.yf, pacman.blok+4*pacman.xf)
	#Inky Bruger pacmans koordinater, men to foran, og så de samme koordinater som blinky men vendt 180 grader
	inky.flyt(pacman.række-(blinky.række-pacman.række), pacman.blok-(blinky.blok-pacman.blok))
	#Clyde Bruger pacmans koordinater, indtil den er 8 indenfor pacman (vi sætter den til 4), hvor den derefter bruger nederste venster hjørne.
	if dist(pacman.blok, pacman.række, clyde.blok, clyde.række) >= 4:
		clyde.flyt(pacman.række, pacman.blok)
	else:
		#Ellers er det nederste venstre hjørne
		clyde.flyt(len(bane)-1, 0)


kør = True

while kør and pacman.ilive:
	#Vi sørger for at vores spil aldrig kører med mere en den valgte fps
	ur.tick(fps)
	tegn()
	opdater()
	print(pacman.point)
	#Her tjekker vi keyboard input
	taster = pygame.key.get_pressed()
	
	if taster[pygame.K_DOWN]:
		#Tjek om der hvor der vil rykkes hen er en væg, hvis ikke så ændrer retningen
		if bane[pacman.række+1][pacman.blok] != 0:
			pacman.xf = 0
			pacman.yf = 1

	elif taster[pygame.K_UP]:
		if bane[pacman.række-1][pacman.blok] != 0:
			pacman.xf = 0
			pacman.yf = -1

	elif taster[pygame.K_LEFT]:
		if bane[pacman.række][pacman.blok-1] != 0:
			pacman.xf = -1
			pacman.yf = 0

	elif taster[pygame.K_RIGHT]:
		if bane[pacman.række][pacman.blok+1] != 0:
			pacman.xf = 1
			pacman.yf = 0

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			kør = False
		