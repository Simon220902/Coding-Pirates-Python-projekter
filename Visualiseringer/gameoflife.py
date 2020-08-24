import pygame
import math
#Tryk på mellemrum for at stoppe eller køre
#Placér ved klik
#Den virker ikke helt rigtigt, men ja.
"""
Game of life's regler
Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""

#Farverne til de døde og levende
død = (255, 0, 0)
live = (0, 255, 0)

#Disse defineres til at starte med
celleB = 50
celleH = 50
cellerX = 10
cellerY = 10

#Og de nødvendige variabler (dog baseret på ovenstående!)
højde = cellerY*celleH
bredde = cellerX*celleB

skærm = pygame.display.set_mode((bredde, højde))
#det her er den første for at vi overhovedet for lavet boarded
#gitter = [[0]*cellerX]*cellerY
#det her er den anden for at vi 
#gitter = [[0,1,1,0,1]*2]*cellerY
#den her kan man lave til sidst for at prøve med forskellige mønstre, husk dog at de stærkt afhænger af cellerX og cellerY variablerne
"""gitter = [[0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,1,1,0,0,0,0],
		  [0,0,0,0,1,1,0,0,0,0],
		  [0,1,1,0,0,1,0,0,0,0],
		  [0,1,1,0,1,0,1,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0],
		  [0,0,0,1,1,0,0,0,0,0],
		  [0,0,0,1,1,1,0,0,0,0],
		  [0,0,0,1,1,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0,0]]
"""
#Den her skal man bruge når man vil gøre noget med musen
gitter = []
for i in range(cellerY):
	gitter.append([0]*cellerX)

#denne her skal på senere
def sætCelle(musx, musy):
	rækkeI = abs(int(musy//celleH))
	celleI = abs(int(musx//celleB))
	print("før: ", gitter)
	#sæt den pågældende celle til de modsatte
	gitter[rækkeI][celleI] = 1
	print("efter: ", gitter)



#den her laves efter gitteret og cellerne kan tegnes (indenda skal man lige gennemgå reglerne, hvad er der brug for af funktioner? osv.)
def naboerSum(rækkeI, celleI):
	naboer = 0
	for deltaRække in [-1, 0, 1]:
		for deltaCelle in [-1, 0, 1]:
			try:
				if deltaRække == 0 and deltaCelle == 0:
					pass
				elif (rækkeI == 0 and deltaRække == -1) or (celleI == 0 and deltaCelle == -1):
					pass
				else:
					naboer += gitter[rækkeI+deltaRække][celleI+deltaCelle]
			except Exception:
				pass
	return naboer

#Man laver denne 1til1 med reglerne.
def iLive(rækkeI, celleI):
	naboer = naboerSum(rækkeI, celleI)
	if naboer < 2 and gitter[rækkeI][celleI]:
		gitter[rækkeI][celleI] = 0
	elif (naboer == 2 or naboer == 3) and gitter[rækkeI][celleI]:
		pass
	elif naboer > 3 and gitter[rækkeI][celleI]:
		 gitter[rækkeI][celleI] = 0
	elif naboer == 3 and not gitter[rækkeI][celleI]:
		gitter[rækkeI][celleI] = 1

#Den første funktion
def tegnGitter():
	for rækkeI in range(1, cellerY):
		pygame.draw.line(skærm, (255, 255, 255), (0, rækkeI*celleH), (bredde, rækkeI*celleH))
	for celleI in range(1, cellerX):
		pygame.draw.line(skærm, (255, 255, 255), (celleI*celleB, 0), (celleI*celleB, højde))

#Den anden funktion
def tegnCeller():
	x = 0
	y = 0
	for række in gitter:
		x = 0
		for celle in række:
			if celle == 1:
				pygame.draw.rect(skærm, live, (x, y, celleB, celleH))
			else:
				pygame.draw.rect(skærm, død, (x, y, celleB, celleH))
			x += celleB
		y += celleH

#den første
def tegn():
	skærm.fill((0,0,0))
	tegnCeller()
	tegnGitter()
	pygame.display.flip()

kør = True
pause = True

while kør:
	tegn()
	#Dette sættes ind efter iLive funktionen er færdiggjort
	if not(pause):
		pygame.time.wait(200)
		for rækkeI in range(cellerY):
			for celleI in range(cellerX):
				iLive(rækkeI, celleI)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			kør = False
		#Denne skal med efter sætCelle funktionen er lavet
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mus = pygame.mouse.get_pos()
			sætCelle(mus[0], mus[1])
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				pause = not(pause)
