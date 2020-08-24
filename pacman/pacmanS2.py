import pygame

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

blokBredde = bredde//len(bane[0])
blokHøjde  = højde//len(bane)

#Farver: R    G    B
sort = (  0,   0,  0)
hvid = (255, 255, 255)
blå  = (  0,   0, 255)
gul  = (255, 238,   0)

def tegn():
	skærm.fill(sort)
	tegnBane(bane)
	pygame.display.flip()

def tegnBane(bane):
	for rækkeI in range(len(bane)):
		for blokI in range(len(bane[rækkeI])):
			if bane[rækkeI][blokI] == 0:
				pygame.draw.rect(skærm, blå, (blokI*blokBredde, rækkeI*blokHøjde, blokBredde, blokHøjde))
			elif bane[rækkeI][blokI] == 1:
				pygame.draw.rect(skærm, sort, (blokI*blokBredde, rækkeI*blokHøjde, blokBredde, blokHøjde))

kør = True

while kør:

	tegn()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			kør = False