import sys
import pygame
bredde = 800
højde = 500
baneBredde = 500
baneHøjde = 500

skærm = pygame.display.set_mode((bredde, højde))

rækker = int(sys.argv[1])
blokke = int(sys.argv[2])

blokBredde = baneBredde//blokke
blokHøjde = baneHøjde//rækker
valgte = 0
bane = []
for rækkeI in range(rækker):
	bane.append([])
	for blokI in range(rækker):
		bane[rækkeI].append(0)


pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('Arial', 30)

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

def tegn():
	skærm.fill(hvid)
	tegnBane(bane)
	tegnBlokVælger()
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
	#Tegn linjer
	for rækkeI in range(len(bane)):
		pygame.draw.line(skærm, hvid, (0, rækkeI*blokHøjde), (baneBredde, rækkeI*blokHøjde))
	for blokI in range(len(bane[0])):
		pygame.draw.line(skærm, hvid, (blokI*blokBredde, 0), (blokI*blokBredde, baneHøjde))

def tegnBlokVælger():
	info = myfont.render('0: væg, 1: sti, 2: point, p: print', False, (0, 0, 0))
	valgteBlok = myfont.render('Valgte blok', False, (0, 0, 0))
	skærm.blit(info, (baneBredde, 10))
	skærm.blit(valgteBlok, (baneBredde, 30))
	#y:50
	if valgte == 0:
		pygame.draw.rect(skærm, blå, (baneBredde+10, 50, blokBredde, blokHøjde))	
	elif valgte == 1:
		pygame.draw.rect(skærm, sort, (baneBredde+10, 50, blokBredde, blokHøjde))
	elif valgte == 2:
		pygame.draw.rect(skærm, sort, (baneBredde+10, 50, blokBredde, blokHøjde))
		pygame.draw.circle(skærm, gul, (baneBredde+10+blokBredde//2, 50+blokHøjde//2), blokBredde//5)


def tegnBlokPoint(rækkeI, blokI):
	pygame.draw.rect(skærm, sort, (blokI*blokBredde, rækkeI*blokHøjde, blokBredde, blokHøjde))
	pygame.draw.circle(skærm, gul, (blokI*blokBredde+blokBredde//2, rækkeI*blokHøjde+blokHøjde//2), blokBredde//5)

def printBane():
	baneString = str(bane).replace("], ", "],\n")
	print(baneString)

mus = False

kør = True

while kør:
	tegn()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			kør = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_0:
				valgte = 0
			elif event.key == pygame.K_1:
				valgte = 1
			elif event.key == pygame.K_2:
				valgte = 2
			elif event.key == pygame.K_p:
				printBane()
		elif event.type == pygame.MOUSEBUTTONUP:
			mus = False
		elif event.type == pygame.MOUSEBUTTONDOWN or mus:
			mus = True
			mouse_pos = pygame.mouse.get_pos()
			x = mouse_pos[0]
			y = mouse_pos[1]
			rækkeI = y//blokHøjde
			blokI =  x//blokBredde
			if rækkeI < len(bane) and blokI < len(bane[0]):
				bane[rækkeI][blokI] = valgte

			