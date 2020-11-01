import pygame
import random
import copy

højde = 500
bredde = 500

skærm = pygame.display.set_mode((bredde, højde))

pygame.font.init()
font = pygame.font.SysFont(None, 30)

bræt = [[0, 2, 4, 8],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0]]

def tegn():
	#Gør hele skærmen sort
	skærm.fill((0,0,0))
	#Tegn bræt
	tegnBræt()
	#Viser det vi har tegnet på skærmen
	pygame.display.flip()

klodsBredde = bredde // 4
klodsHøjde = højde//4

def tegnBræt():
	for rækkeI in range(4):
		for klodsI in range(4):
			tegnKlods(rækkeI, klodsI)

afstand = 5
farver = {0:(205, 192, 180), 2:(238, 228, 218), 4:(237, 224, 200), 8:(242, 177, 121), 16:(245, 149, 99), 32:(246, 124, 95), 64:(245, 94, 59), 128:(236, 207, 7), 256:(237, 204, 97), 512:(237, 200, 80), 1024:(240, 196, 60), 2048:(236, 196, 2)}

def tegnKlods(rækkeI, klodsI):
	x = klodsBredde * klodsI + afstand
	y = klodsHøjde * rækkeI + afstand
	b = klodsBredde - 2*afstand
	h = klodsHøjde - 2*afstand
	pygame.draw.rect(skærm, farver[bræt[rækkeI][klodsI]], (x, y, b, h))
	#Vi vil ikke skrive noget i klodsen, hvis den er tom (altså nul)
	if bræt[rækkeI][klodsI] != 0:
		tekst = font.render(str(bræt[rækkeI][klodsI]), True, (255, 255, 255))
		tekstStørrelse = tekst.get_size()
		tekstX = x + b//2 - tekstStørrelse[0]//2
		tekstY = y + h//2 - tekstStørrelse[1]//2
		skærm.blit(tekst, (tekstX, tekstY))

#INDSÆT LOGIKKEN HER
#BEVÆGELSE
def bevægTilVenstre(bræt):
	rykTilVenstre(bræt)
	#Vi prøver at samle cellerne til venstre
	for i in range(4):
		for j in range(3):
			#Hvis de er de samme og de ikke er nul
			if bræt[i][j] == bræt[i][j + 1] and bræt[i][j] != 0:
				#Så "Ryk" dem sammen ved at fordoble den længst inde til venstre
				bræt[i][j] *= 2
				#Og sæt den anden til nu
				bræt[i][j + 1] = 0
	#Nu er der muligvis kommet nogle ekstra "huller"-nuller, hvilket vi lige skal fikse
	rykTilVenstre(bræt)
	return bræt

def bevægTilHøjre(bræt):
	rykTilHøjre(bræt)
	#Vi prøver at samle cellerne til venstre
	for i in range(4):
		for j in range(3):
			#Hvis de er de samme og de ikke er nul
			if bræt[i][3-j] == bræt[i][3-j-1] and bræt[i][3-j] != 0:
				#Så "Ryk" dem sammen ved at fordoble den længst ude til højre
				bræt[i][3-j] = 2 * bræt[i][3-j]
				#Og sæt den til venstre for til nul
				bræt[i][3-j-1] = 0

	#Nu er der muligvis kommet nogle ekstra "huller"-nuller, hvilket vi lige skal fikse
	rykTilHøjre(bræt)
	return bræt

def bevægOp(bræt):
	bræt = roterVenstre(bræt)
	bræt = bevægTilVenstre(bræt)
	bræt = roterHøjre(bræt)
	return bræt

def bevægNed(bræt):
	bræt = roterVenstre(bræt)
	bræt = bevægTilHøjre(bræt)
	bræt = roterHøjre(bræt)
	return bræt

#RYK
def rykTilVenstre(bræt):
	for i in range(4):
		#Vi fjerner alle nulle 
		while 0 in bræt[i]:
			bræt[i].remove(0)
		#Vi tilføjer nuller på venstre side 
		for _ in range(4 - len(bræt[i])):
			bræt[i].append(0)

def rykTilHøjre(bræt):
	for i in range(4):
		#Vi fjerner alle nulle 
		while 0 in bræt[i]:
			bræt[i].remove(0)
		#Vi tilføjer nuller på venstre side 
		for _ in range(4 - len(bræt[i])):
			bræt[i] = [0] + bræt[i]

#ROTER
def roterVenstre(bræt):
	#Det nye bræt
	nytBræt = []
	for i in range(4):
		midBræt = []
		for j in range(4):
			#Vi tager den kolonne yderst til højre og sætter som første række
			#og så den næst yderste kolonne til højre og sætter den som anden osv.
			midBræt.append(bræt[j][3-i])
		#Vi tilføjer rækken der før var en kolonne til brættet
		nytBræt.append(midBræt)
	return nytBræt

def roterHøjre(bræt):
	#At rotere tre gange til venstre er det samme som at rotere en gang til højre
	return roterVenstre(roterVenstre(roterVenstre(bræt)))

def tilføjTilfældig():
	index_nul = []
	for rækkeI in range(len(bræt)):
		for blokI in range(len(bræt[0])):
			if bræt[rækkeI][blokI] == 0:
				index_nul.append((rækkeI, blokI))
	if len(index_nul) > 0:
		valgt_index = random.choice(index_nul)
		bræt[valgt_index[0]][valgt_index[1]] = random.choice([2,4])

def brætUbevægelig(bræt):
	brætVenstre =  copy.deepcopy(bræt)
	kanVenstre = bevægTilVenstre(brætVenstre) == bræt

	brætHøjre =  copy.deepcopy(bræt)
	kanHøjre = bevægTilHøjre(brætHøjre) == bræt

	brætOp =  copy.deepcopy(bræt)
	kanOp = bevægOp(brætOp) == bræt

	brætNed =  copy.deepcopy(bræt)
	kanNed = bevægNed(brætNed) == bræt

	return kanVenstre and kanHøjre and kanOp and kanNed

kør = True

while kør:
	if brætUbevægelig(bræt):
		print("NU KAN DU IKKE BEVÆGE DIG MERE")
	
	tegn()
	#Vi løber igennem alle de ting der er sket. (input)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			kør = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				bræt = bevægTilVenstre(bræt)
				tilføjTilfældig()
			elif event.key == pygame.K_RIGHT:
				bræt = bevægTilHøjre(bræt)
				tilføjTilfældig()
			elif event.key == pygame.K_UP:
				bræt = bevægOp(bræt)
				tilføjTilfældig()
			elif event.key == pygame.K_DOWN:
				bræt = bevægNed(bræt)
				tilføjTilfældig()