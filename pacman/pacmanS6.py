#Point
#pacman.point
#ændring af flyt
#Ændring af bane
#Tegn af point
#Ændring af tegn bane
#print point
import pygame

bredde = 500
højde = 500

skærm = pygame.display.set_mode((bredde, højde))

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

blokBredde = bredde//len(bane[0])
blokHøjde  = højde//len(bane)

ur = pygame.time.Clock()
fps = 7

#Farver: R    G    B
sort = (  0,   0,  0)
hvid = (255, 255, 255)
blå  = (  0,   0, 255)
gul  = (255, 238,   0)

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

	def tegn(self):
		#Vi finder det rigtige x- og y-koordinat
		self.x = self.blok*blokBredde
		self.y = self.række*blokHøjde
		#Vi tegner pacman, han er en gul cirkel
		pygame.draw.circle(skærm, gul, (self.x+self.r, self.y+self.r), self.r)

	def flyt(self):
		#Vi tjekker om den blok vi vil flytte pacman hen på er en væg, hvis ikke flytter vi ham
		if bane[self.række+self.yf][self.blok+self.xf] != 0:
			self.række += self.yf
			self.blok += self.xf
		#Vi tjekker om den blok vi er i (efter vi har flyttet os) er et point, hvis ja
		#pointne
		if bane[self.række][self.blok] == 2:
			bane[self.række][self.blok] = 1
			self.point += 10


pacman = Pacman(4, 4)

def tegn():
	skærm.fill(sort)
	tegnBane(bane)
	pacman.tegn()
	pygame.display.flip()

def opdater():
	pacman.flyt()

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

kør = True

while kør:
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
		