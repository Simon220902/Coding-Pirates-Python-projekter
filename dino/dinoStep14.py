import pygame
import random
#Start pygame op
pygame.init()

#Højde og bredde af vores skærm
højde = 300
bredde = 800

#Lav skærmen med højde og bredde
skærm = pygame.display.set_mode((bredde, højde))

#Spil variablen indeholder alle de værdier der er knyttet til spillets kørsel
spil = {'kør':True, 'score':0, 'high score':0, 'fart':1}

#Jord billedet og jord variablen der indeholder værdierne knyttet til jorden
jord_billede = pygame.image.load("ground.png")
jord = {'x1':0, 'x2':1203 - 0, 'y':højde-19, 'bredde':1203}

#Dino billedet og dino variablen der indeholder værdierne knyttet til dinoen
dino_billede = pygame.image.load("dinoer.png")
dino = {'x':120, 'y':højde - 95 - 10, 'bredde':440//5, 'højde':95, 'billed_nr':2, 'hopper':False, 'v':8, 'm':2, 'y_min': højde - 95 - 10, 'hop lyd':pygame.mixer.Sound("hop.wav"), 'levende':True}

#Kaktus billedet og kaktus variablen der indeholder værdierne knyttet til kaktussen
kaktus_billede = pygame.image.load("kaktus.png")
kaktus = {'x':bredde, 'y':højde-70-10, 'bredde':34, 'højde':70, 'billed_nr':random.randint(0, 5), 'hoppet over':False}

#Fugle billedet og fugle variablen der indeholder værdierne knyttet til fuglen
fugl_billede = pygame.image.load("fugl.png")
fugl = {'x':bredde, 'y':højde-81-10, 'bredde':94, 'højde':81, 'billed_nr':0, 'hoppet over':False}


def dino_ramt(x, y, b, h):
	if dino['x']+dino['bredde'] > x and dino['x'] < x+b and dino['y']+dino['højde'] > y and dino['y'] < y+h:
		dino['levende'] = False

def jord_opdater():
	#Ryk x1
	jord['x1'] -= 20*spil['fart']
	#Sørg for at x2 forbliver lige ved slutningen af billede 1
	jord['x2'] = jord['bredde'] + jord['x1']
	#Er x1 større end eller lig med bredden af jorden?
	#Grunden til vi ganger med -1 er fordi x1 vil være negativ og vi dermed laver det om til et positivt tal
	if jord['x1'] * -1 >= jord['bredde']:
		#Hvis ja, sæt x1 lig med 0
		jord['x1'] = 0

def dino_opdater():
	#Har dinoen ramt kaktussen
	dino_ramt(kaktus['x'], kaktus['y'], kaktus['bredde'], kaktus['højde'])
	#Har dinoen ramt fuglen
	dino_ramt(fugl['x'], fugl['y'], fugl['bredde'], fugl['højde'])
	#Hopper dinoen
	if dino['hopper']:
		dino_hopper()
	#Skift dinoens animation
	if dino['billed_nr'] >= 3.5:
		dino['billed_nr'] = 2
	else:
		dino['billed_nr'] += 0.4

def kaktus_opdater():
	#Flyt kaktussen
	kaktus['x'] -= 20*spil['fart']
	#Hvis kaktussen ryger ud for skærmen, smid den tilbage og vælg et tilfældigt billede
	if kaktus['x'] <= 0:
		kaktus['x'] = bredde + random.randint(0, 200)
		kaktus['billed_nr'] = random.randint(0, 5)
		kaktus['hoppet over'] = False
	#Hvis spilleren er på høre side af kaktussen og han ikke allerede har hoppet over den så
	if dino['x'] > kaktus['x']+kaktus['bredde'] and not kaktus['hoppet over']:
		#Læg 1 til spillerens score
		spil['score'] += 1
		#Gør sådan at kaktussen er blevet hoppet over
		kaktus['hoppet over'] = True	

def fugl_opdater():
	#Flyt kaktussen
	fugl['x'] -= 20*spil['fart']
	#Skift fuglens billede
	if fugl['billed_nr'] >= 1.5:
		fugl['billed_nr'] = 0
	else:
		fugl['billed_nr'] += 0.4
	#Hvis kaktussen ryger ud for skærmen, smid den tilbage og vælg et tilfældigt billede
	if fugl['x'] <= 0:
		fugl['x'] = bredde + random.randint(0, 200)
		fugl['billed_nr'] = 0
		fugl['hoppet over'] = False
	#Hvis spilleren er på høre side af kaktussen og han ikke allerede har hoppet over den så
	if dino['x'] > fugl['x']+fugl['bredde'] and not fugl['hoppet over']:
		#Læg 1 til spillerens score
		spil['score'] += 1
		#Gør sådan at kaktussen er blevet hoppet over
		fugl['hoppet over'] = True

def dino_hopper():
	#Vi tjekker om v er større end nul, hvis det er tilfældet vil vi gerne gøre y-værdien mindre (bevægelse op ad)
	if dino['v'] > 0:
		F = ((dino['m'] * (dino['v']*dino['v']))/2)
	#hvis v er mindre end nul, vil vi gøre y-værdien større (bevægelse nedad), ved at gøre F negativ
	else:
		F = -((dino['m'] * (dino['v']*dino['v']))/2)
	#Vi rykker dinoen op eller ned med vores før udregnede F
	dino['y'] -= F
	#Vi sænker dinoens hastighed
	dino['v'] -= 1
	#Til sidst tjekker vi om dinoen har nået jorden igen
	if dino['y'] >= dino['y_min']:
		dino['y'] = dino['y_min']
		dino['hopper'] = False
		dino['v'] = 8

def visScore():
	font = pygame.font.SysFont("Arial", 20)
	#Rendér scoren, ved først at lave det til en streng
	score_tekst = font.render('High Score: '+str(spil['high score'])+' '+'Score: '+str(spil['score']), True, (0,0,0))
	#Prop de teksten på skærmen, get_rect() funktionen giver en liste med fire tal tilbage, [x, y, bredde, højde], vi minusser med breden så teksten kommer til at stå yderst til venstre
	skærm.blit(score_tekst, (bredde - score_tekst.get_rect()[2], 5))

def gameOver():
	font = pygame.font.SysFont("Arial", 50)
	#Renderer teksten "Game Over!"
	tekst = font.render("Game Over", True, (0,0,0))
	#Prop de teksten på skærmen
	skærm.blit(tekst, (bredde/2 - tekst.get_rect()[2]/2, højde/2 - tekst.get_rect()[3]/2 ))
	pygame.display.flip()
	
def tegn():
	#Tegn hvid baggrund
	skærm.fill((255,255,255))
	#Tegn dinoen
	skærm.blit(dino_billede, (dino['x'], dino['y']), (dino['bredde']*int(dino['billed_nr']), 0, dino['bredde'], dino['højde']))
	#Tegn jorden, først den ene så den anden
	skærm.blit(jord_billede, (jord['x1'], jord['y']))
	skærm.blit(jord_billede, (jord['x2'], jord['y']))
	#Tegn kaktussen
	skærm.blit(kaktus_billede, (kaktus['x'], kaktus['y']), (kaktus['bredde']*kaktus['billed_nr'], 0, kaktus['bredde'], kaktus['højde']))
	#Tegn fuglen
	skærm.blit(fugl_billede, (fugl['x'], fugl['y']), (fugl['bredde']*int(fugl['billed_nr']), 0, fugl['bredde'], fugl['højde']))
	#Tegn scoren
	visScore()
	#Vis det der er tegnet på skærmen
	pygame.display.flip()
	#Vent 30 milisekunder
	pygame.time.delay(30)

while spil['kør']:
	gameOver()
	#For hver begivenhed(tastatur tryk eller lignende) 
	for event in pygame.event.get():
		#Er der blevet trykket på 'X' i højre hjørne?
		if event.type == pygame.QUIT:
			#Hvis ja, stop spillet
			spil['kør'] = False
		#Er der trykket en tast ned?
		if event.type == pygame.KEYDOWN:
			#Hvis ja, er denne tast escape-tasten?
			if event.key == pygame.K_ESCAPE:
				#Hvis ja, stop spillet
				spil['kør'] = False
			#Hvis hvilken som helst anden tast trykkes ned, så genstart spillet og sæt kaktussen tilbage
			else:
				dino['levende'] = True
				kaktus = {'x':bredde, 'y':højde-70-10, 'bredde':34, 'højde':70, 'billed_nr':random.randint(0, 5), 'hoppet over':False}
				fugl = {'x':bredde, 'y':højde-81-10, 'bredde':94, 'højde':81, 'billed_nr':0, 'hoppet over':False}
				spil['fart'] = 1
	
	while dino['levende']:
		#For hver begivenhed(tastatur tryk eller lignende) 
		for event in pygame.event.get():
				#Er der blevet trykket på 'X' i højre hjørne?
				if event.type == pygame.QUIT:
					#Hvis ja, stop spillet
					spil['kør'] = False
				#Er der trykket en tast ned?
				if event.type == pygame.KEYDOWN:
					#Hvis ja, er denne tast escape-tasten?
					if event.key == pygame.K_ESCAPE:
						#Hvis ja, stop spillet
						spil['kør'] = False
					#Hvis pil op bliver trykket ned skal dinoen hoppe
					elif event.key == pygame.K_UP:
						dino['hopper'] = True
						dino['hop lyd'].play()
		#Opdater farten
		spil['fart'] += 0.001 
		#Opdater jordens position
		jord_opdater()
		#Opdater dinoen position
		dino_opdater()
		#Opdater kaktussen
		kaktus_opdater()
		#Opdater fuglen
		fugl_opdater()
		#Tegn spillet
		tegn()

	if spil['score'] > spil['high score']:
		spil['high score'] = spil['score']
		spil['score'] = 0
