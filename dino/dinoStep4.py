import pygame
#Start pygame op
pygame.init()

#Højde og bredde af vores skærm
højde = 300
bredde = 800

#Lav skærmen med højde og bredde
skærm = pygame.display.set_mode((bredde, højde))

#Spil variablen indeholder alle de værdier der er knyttet til spillets kørsel
spil = {'kør':True}

#Jord billedet og jord variablen der indeholder værdierne knyttet til jorden
jord_billede = pygame.image.load("ground.png")
jord = {'x1':0, 'x2':1203 - 0, 'y':højde-19, 'bredde':1203}

#Dino billedet og dino variablen der indeholder værdierne knyttet til jorden
dino_billede = pygame.image.load("dinoer.png")
dino = {'x':120, 'y':højde - 95 - 10, 'bredde':440//5, 'højde':95, 'billed_nr':2}

def jord_opdater():
    #Ryk x1
    jord['x1'] -= 20
    #Sørg for at x2 forbliver lige ved slutningen af billede 1
    jord['x2'] = jord['bredde'] + jord['x1']
    #Er x1 større end eller lig med bredden af jorden?
    #Grunden til vi ganger med -1 er fordi x1 vil være negativ og vi dermed laver det om til et positivt tal
    if jord['x1'] * -1 >= jord['bredde']:
        #Hvis ja, sæt x1 lig med 0
        jord['x1'] = 0

def dino_opdater():
	if dino['billed_nr'] >= 3.5:
		dino['billed_nr'] = 2
	else:
		dino['billed_nr'] += 0.4

def tegn_dino():
	skærm.blit(dino_billede, (dino['x'], dino['y']), (dino['bredde']*int(dino['billed_nr']), 0, dino['bredde'], dino['højde']))

def tegn():
    #Tegn hvid baggrund
    skærm.fill((255,255,255))
    #Tegn dinoen
    skærm.blit(dino_billede, (dino['x'], dino['y']), (dino['bredde']*int(dino['billed_nr']), 0, dino['bredde'], dino['højde']))
    #Tegn jorden, først den ene så den anden
    skærm.blit(jord_billede, (jord['x1'], jord['y']))
    skærm.blit(jord_billede, (jord['x2'], jord['y']))
    #Vis det der er tegnet på skærmen
    pygame.display.flip()
    #Vent 30 milisekunder
    pygame.time.delay(30)

while spil['kør']:
    #For hver begivenhed(tastatur tryk eller ligende) 
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
    #Opdater jordens position
    jord_opdater()
    #Opdater dinoen position
    dino_opdater()
    #Tegn spillet
    tegn()