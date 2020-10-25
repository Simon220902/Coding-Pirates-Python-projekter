import pygame

højde = 500
bredde = 500

skærm = pygame.display.set_mode((bredde, højde))

firkantX = 100
firkantY = 100
firkantB = 200
firkantH = 100


målX = 400
målY = 400
målB = 100
målH = 100

vundet = False

rød = (255,0,0)
blå = (0,0,255)


pygame.font.init()
font = pygame.font.SysFont(None, 30)

def opdater():
	global vundet

	if firkantX >= målX and firkantY >= målY:
		vundet = True
	else:
		vundet = False

def tegn():
	skærm.fill((0,0,0))
	#TEGN ET ELLER ANDET
	pygame.draw.rect(skærm, (255, 255, 0), (målX, målY, målB, målH))	
	
	pygame.draw.rect(skærm, (255, 0, 0), (firkantX, firkantY, firkantB, firkantH))

	tegnTekst("Bevæg den røde firkant ned i den gule", 0, 0, rød)

	if vundet:
		#pygame.draw.rect(skærm, (0, 255, 0), (10, 10, 480, 480))
		tegnTekst("HURRA DU HAR VUNDET DU ER DA BARE FOR SEJ, SEJE DIG", 0, højde//2, blå)


	pygame.display.flip()

def tegnTekst(tekst, x, y, farve):
	tekstBillede = font.render(tekst, True, farve)
	skærm.blit(tekstBillede, (x, y))


kør = True

while kør:
	opdater()
	tegn()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			kør = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				firkantY = firkantY - 10
			elif event.key == pygame.K_s:
				firkantY = firkantY + 10
			elif event.key == pygame.K_a:
				firkantX = firkantX - 10
			elif event.key == pygame.K_d:
				firkantX = firkantX + 10