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
jord = {'x':0, 'y':højde-19}

#Jord billedet og jord variablen der indeholder værdierne knyttet til jorden
dino_billede = pygame.image.load("dino.png")
dino = {'x':120, 'y':højde - 95 - 10}

def tegn():
    #Tegn hvid baggrund
    skærm.fill((255,255,255))
    #Tegn dinoen
    skærm.blit(dino_billede, (dino['x'], dino['y']))
    #Tegn jorden
    skærm.blit(jord_billede, (jord['x'], jord['y']))
    #Vis det der er tegnet på skærmen
    pygame.display.flip()

#Spil loop
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
    #Tegn spillet
    tegn()