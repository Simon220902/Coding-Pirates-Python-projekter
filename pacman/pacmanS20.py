#Spøgelse animation
#Hver af spøgelserne har et forskelligt billede så vi vil have at der gives en sti som argument til init funktionen.
#Vi laver om på størrelsen så det passer på vores størrelse spilleplade
#Vi sletter farven
#Vi laver om på tegn-funktionen
#Vi giver spøgelset deres respektive sti som argument.

#Vi kigger på spøgelsernes billeder til at starte med, hvordan er de opbygget?
#Vi ser der kun er en række. Dermed kan vi ikke bare bruge rækkerne som ved pacmans billede.
#Vi vælger derfor istedet at forskyde hvor langt henne så vi laver en variabel billede nr.
#Afhængigt af hvilken retning spøgelset vender skal det have et forskelligt billedNr til at forskydes med
#For at sørge for at det har den rigtige forskydning opdaterer vi hvilken retning de skal tegnes i i tegn funktionen
#For at skifte mellem de to billeder der er til hver retning laver vi en variabel animer, der skifter mellem 0 og 1
#Vi bruger disse to når vi tegner den

import pygame
import math
import random

bredde = 500
højde = 500

skærm = pygame.display.set_mode((bredde, højde))

pygame.font.init() #Vi starter font modulet
#Vores font, der ligner den i pacman
font = pygame.font.Font('data/8-bit.ttf', 30)

bane = [
	[0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0],
	[0, 3, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 0, 3, 0],
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
	[0, 3, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 3, 0],
	[0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0],
	[0, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 0],
	[0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0],
	[0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
	[0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

blokBredde = bredde//len(bane[0])
blokHøjde  = højde//len(bane)

ur = pygame.time.Clock()
fps = 5

#Farver: R    G    B
sort = (  0,   0,  0)
hvid = (255, 255, 255)
blå  = (  0,   0, 255)
gul  = (255, 238,   0)
rød = (255, 0, 0)
pink = (252,134,170)
lysblå = (27,177,230)
orange = (249,126,22)

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
		#Pacman's billede og relaterede variabler
		self.billede = pygame.image.load("data/sprites/pacman.png")
		#Vi resizer det så at pacman fylder en hel blok, (vi ganger med antal af pacman henad og nedad)
		self.billede = pygame.transform.scale(self.billede, (blokBredde*2,blokHøjde*4))
		self.billedBredde = blokBredde
		self.billedHøjde = blokHøjde
		#Variabler til at animere
		self.animer = 0
		self.billedRække = 0

	def tegn(self):
		#Vi finder det rigtige x- og y-koordinat
		self.x = self.blok*blokBredde
		self.y = self.række*blokHøjde
		#Animer
		#Da vi kun har to billeder af pacman pr. række skal vi bare skifte mellem 0 og 1
		self.animer = not self.animer
		#Hvilken retning
		#Venstre
		if self.xf == -1:
			self.billedRække = 0
		#Højre		
		elif self.xf == 1:
			self.billedRække = 1
		#Op
		elif self.yf == -1:
			self.billedRække = 2
		#Ned
		elif self.yf == 1:
			self.billedRække = 3
		#Vi tegner pacman, hvor vi forskyder x-koordinatet afhængigt af hvilket billede vi er på. Vi tegner ham fra den tilsvarende række der passer på hans retning.
		skærm.blit(self.billede, (self.x, self.y), (self.billedBredde*self.animer, self.billedHøjde*self.billedRække, self.billedBredde, self.billedHøjde))

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
		elif bane[self.række][self.blok] == 3:
			bane[self.række][self.blok] = 1
			global mode, dt
			mode = 3
			dt = 0

class Spøgelse:
	def __init__(self, række, blok, billedSti):
		self.række = række
		self.blok = blok
		self.xf = 1
		self.yf = 0
		#Variabler til at tegne pacman
		self.x = self.blok*blokBredde
		self.y = self.række*blokHøjde
		self.r = blokHøjde//2
		#Mål
		self.rækkeMål = self.række
		self.blokMål = self.blok
		#Spøgelsets billede
		self.billede = pygame.image.load(billedSti)
		self.billede = pygame.transform.scale(self.billede, (blokBredde*8, blokHøjde))
		self.billedBredde = blokBredde
		self.billedHøjde = blokHøjde
		self.billedNr = 0
		self.animer = 0

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

	def tegn(self):
		#Vi finder det rigtige x- og y-koordinat
		self.x = self.blok*blokBredde
		self.y = self.række*blokHøjde
		#Vi forskyder billedet afhængigt af bevægelsesretningen
		if self.xf == -1:
			self.billedNr = 4
		elif self.xf == 1:
			self.billedNr = 6
		elif self.yf == -1:
			self.billedNr = 0
		elif self.yf == 1:
			self.billedNr = 2
		#Vi skifter animer mellem 1 og 0
		self.animer = not self.animer
		#Vi tegner spøgelset
		skærm.blit(self.billede, (self.x, self.y), (self.billedBredde*(self.billedNr+self.animer), 0, self.billedBredde, self.billedHøjde))

	def tegnFlygt(self):
		#Vi finder det rigtige x- og y-koordinat
		self.x = self.blok*blokBredde
		self.y = self.række*blokHøjde
		#Vi tegner spøgelset
		pygame.draw.circle(skærm, blå, (self.x+self.r, self.y+self.r), self.r)

pacman = Pacman(4, 4)

blinky = Spøgelse(1, 1, "data/sprites/blinky.png")
pinky =  Spøgelse(3, 8, "data/sprites/pinky.png")
inky = Spøgelse(8, 3, "data/sprites/inky.png")
clyde = Spøgelse(8, 5, "data/sprites/clyde.png")

spøgelser = [blinky, pinky, inky, clyde]
spisteSpøgelser = []
bevægSpøgelse = 0

mode = 1

dt = 0 #Står for deltatid en variabel, der gemmer hvor lang tid der er gået siden sidste mode skifte. Hvor vi sætter den til nul efter vi skifter mode.

def tegn():
	skærm.fill(sort)
	tegnBane(bane)
	pacman.tegn()
	tegnSpøgelser()
	tegnSpisteSpøgelser()
	tegnScore()
	pygame.display.flip()

def opdater():
	global bevægSpøgelse
	if mode != 3:
		spøgelseKollision()
	else:
		spøgelseSpis()
	pacman.flyt()
	if bevægSpøgelse > 3:
		bevægSpøgelser()
		bevægSpøgelse = 0
	else:
		bevægSpøgelse += 1
	skiftMode()
	håndterSpisteSpøgelser()

def tegnScore():
	score = font.render('score: '+str(pacman.point), False, hvid)
	skærm.blit(score, (10, (len(bane)-1)*blokHøjde))

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
				tegnPowerBlokPoint(rækkeI, blokI)

def tegnBlokPoint(rækkeI, blokI):
	pygame.draw.rect(skærm, sort, (blokI*blokBredde, rækkeI*blokHøjde, blokBredde, blokHøjde))
	pygame.draw.circle(skærm, gul, (blokI*blokBredde+blokBredde//2, rækkeI*blokHøjde+blokHøjde//2), blokBredde//5)

def tegnPowerBlokPoint(rækkeI, blokI):
	pygame.draw.rect(skærm, sort, (blokI*blokBredde, rækkeI*blokHøjde, blokBredde, blokHøjde))
	pygame.draw.circle(skærm, gul, (blokI*blokBredde+blokBredde//2, rækkeI*blokHøjde+blokHøjde//2), blokBredde//3)

def tegnSpøgelser():
	if mode != 3:
		for spøgelse in spøgelser:
			spøgelse.tegn()
	else:
		for spøgelse in spøgelser:
			spøgelse.tegnFlygt()

#Tjekker pacman har ramt spøgelset:
def spøgelseKollision():
	for spøgelse in spøgelser:
		if pacman.række == spøgelse.række and pacman.blok == spøgelse.blok:
			pacman.ilive = False

#Tjekker pacman har ramt spøgelset: og giv ham point (hvis han er i modde 3)
def spøgelseSpis():
	for spøgelseI in range(len(spøgelser)):
		spøgelse = spøgelser[spøgelseI]
		#Hvis spøgelset rør pacman giver vi pacman point og propper spøgelset i spistespøgelser listen.
		if pacman.række == spøgelse.række and pacman.blok == spøgelse.blok:
			pacman.point += 100
			spisteSpøgelser.append(spøgelser[spøgelseI])
			del spøgelser[spøgelseI]
			#Vi kan kun spise et spøgelse af gangen(ellers får vi problemer med indeksene)
			break


#Vi laver 3 bevægelses funktioner så vores bevægSpøgelser kun spørger om hvilken mode den er i
def bevægSpøgelser():
	if mode == 1:
		bevægSpøgelserFang()
	elif mode == 2:
		bevægSpøgelserSpred()
	elif mode == 3:
		for spøgelse in spøgelser:
			spøgelse.flygt()

def bevægSpøgelserFang():
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

def bevægSpøgelserSpred():
	blinky.flyt(0, len(bane[0]))
	pinky.flyt(0, 0)
	inky.flyt(len(bane), len(bane[0]))
	clyde.flyt(len(bane), 0)

def skiftMode():
	global mode, dt
	if dt > 7000:
		if mode == 1:
			mode = 2
		elif mode == 2:
			mode = 1
		elif mode == 3:
			mode = 1
		dt = 0

def håndterSpisteSpøgelser():
	#Så vi ved hvor mange vi har slettet
	genoplivneSpøgelser = 0
	#Vi flytter dem til række 7 blok 8, når de når den blok 
	for spøgelseI in range(len(spisteSpøgelser)):
		spøgelse = spisteSpøgelser[spøgelseI-genoplivneSpøgelser]
		#Hvis den er nået tilbage skal vi live den op
		if spøgelse.række == 7 and spøgelse.blok == 8:
			#Vi sætter spøgelset i den levende spøgelse liste
			spøgelser.append(spøgelse)
			del spisteSpøgelser[spøgelseI-genoplivneSpøgelser]
			genoplivneSpøgelser += 1
		else:
			spøgelse.flyt(7, 8)
	
def tegnSpisteSpøgelser():
	for spøgelse in spisteSpøgelser:
		blokMidteX = spøgelse.blok*blokBredde + blokBredde//2
		blokMidteY = spøgelse.række*blokHøjde + blokHøjde//2
		#Vi tegner spøgelset som to øjne.
		#Venstre øje
		pygame.draw.circle(skærm, hvid, (blokMidteX-blokBredde//4, blokMidteY-blokHøjde//4), blokBredde//5)
		pygame.draw.circle(skærm, sort, (blokMidteX-blokBredde//4, blokMidteY-blokHøjde//4 ), blokBredde//8)
		#Højre øje
		pygame.draw.circle(skærm, hvid, (blokMidteX+blokBredde//4, blokMidteY-blokHøjde//4 ), blokBredde//5)
		pygame.draw.circle(skærm, sort, (blokMidteX+blokBredde//4, blokMidteY-blokHøjde//4 ), blokBredde//8)
	
kør = True

while kør and pacman.ilive:
	#Vi sørger for at vores spil aldrig kører med mere en den valgte fps
	dt += ur.tick(fps)
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