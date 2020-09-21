import pygame

højde = 500
bredde = 500

skærm = pygame.display.set_mode((bredde, højde))

def tegn():
	#Gør hele skærmen sort
	skærm.fill((0,0,0))

	#Viser det vi har tegnet på skærmen
	pygame.display.flip()

kør = True

while kør:
	tegn()

	#Vi løber igennem alle de ting der er sket. (input)
	for event in pygame.event.get():
		#Her håndtere vi de forskellige begivenheder/events
		if event.type == pygame.QUIT:
			kør = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				print("W")
			elif event.key == pygame.K_a:
				print("A")
			elif event.key == pygame.K_s:
				print("S")
			elif event.key == pygame.K_d:
				print("D")
			