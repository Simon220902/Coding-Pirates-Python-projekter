# pylint: disable=C0103,C0301,R0903,R0912,R0913,R0915,W0703
# Coding Pirates Hørsholm, Space Invaders
# based on https://github.com/jatinmandav/Gaming-in-Python/blob/master/Space_Invaders/space%20invaders.py
import sys
import time
import pygame
from random import randint
# -------------- Initialization ------------
pygame.init()

width = 700
height = 500

display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")

ship_width = 40
ship_height = 30

# -------------- Colours -----------------
background = (74, 35, 90)
white = (244, 246, 247)
yellow = (241, 196, 15)
orange = (186, 74, 0)
green = (35, 155, 86)
white1 = (253, 254, 254)
dark_gray = (23, 32, 42)

# -------------- Space-Ship Class --------------
class SpaceShip:
    def __init__(self, x, y, w, h, colour):
        self.x = x              # self.x er positionen på x aksen
        self.y = y              # self.y er positionen på y aksen
        self.w = w              # self.w er hvor bredt dit rumskib skal være
        self.h = h              # self.h er højden på dit rumskib
        self.colour = colour    # ja sjovt nok farven....

    def draw(self):
        pygame.draw.rect(display, self.colour, (self.x, self.y, self.h, self.w))
        #Firkant:
        #pygame.draw.rect(display, farve, (x_koordinat, y_koordinat, højde, bredde))
        #Trekant(eller flere kanter):
        #pygame.draw.polygon(display, farve, ((x_koordinat1, y_koordinat1), (x_koordinat2, y_koordinat2), (x_koordinat3, y_koordinat3)))
        #Det polygon(...) funktionen gør er den tegner en streg mellem alle de punkter der er givet til sidst, der kan godt være flere end 3 punkter
        #Cirkel:
        #pygame.draw.circle(display, farve, (x_koordinat, y_koordinat), radius)
        #Ellipse/oval:(En cirkel der ikke er helt rund)
        #pygame.draw.ellipse(display, farve, (x_koordinat, y_koordinat, højde, bredde))
        #Oval tegnes således den går igennem de fire hjørner i firkanten angivet til sidst

# ----------------- Bullet Class -------------
class Bullet:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.d = 10
        self.speed = speed

    def draw(self):
        pygame.draw.ellipse(display, orange, (self.x, self.y, self.d, self.d))

    def move(self):
        self.y += self.speed

    def hit(self, x, y, d):
        if x < self.x < x + d:
            if y + d > self.y > y:
                return True

# ------------------ Alien Class ---------------
class Alien:
    def __init__(self, x, y, d, speed, color):
        self.x = x
        self.y = y
        self.d = d
        self.x_dir = 1
        self.speed = speed
        self.color = color

    def draw(self):
        pygame.draw.ellipse(display, self.color, (self.x, self.y, self.d, self.d))
        pygame.draw.ellipse(display, dark_gray, (self.x + 10, self.y + self.d/3, 8, 8), 2)
        pygame.draw.ellipse(display, dark_gray, (self.x + self.d - 20, self.y + self.d/3, 8, 8), 2)
        pygame.draw.rect(display, dark_gray, (self.x, self.y+self.d-20, self.d, 7))

    def move(self):
        self.x += self.x_dir*self.speed

    def shift_down(self):
        self.y += self.d

class Boss(Alien):
    def __init__(self, x, y, d, speed, color, lives):
        Alien.__init__(self, x, y, d, speed, color)
        self.lives = lives
        self.color_change = 255//lives
        self.bossFont = pygame.font.SysFont("Calibri", 50)

    def WasHit(self):
        #Fjern et liv fra bossen
        self.lives -= 1
        #Gør bossen mere rød
        if self.color[1] > 0 and self.color[0] < 255:
            self.color = [self.color[0]+self.color_change, self.color[1]-self.color_change, 0]

    def ShowLives(self):
        #Render tallet
        bossLivesText = self.bossFont.render("Bossen har " + str(self.lives) + " liv tilbage", True, white)
        #Prop bossens liv på skærmen
        display.blit(bossLivesText, (0,0))

# ------------------- Saved ------------------
#Denne er funktionen der kaldes, hvis du redder verdenen fra en alien invasion
def saved():
    #Loader fonten Wide Latin i to størrelser
    font = pygame.font.SysFont("Wide Latin", 22)
    font_large = pygame.font.SysFont("Wide Latin", 43)
    #Renderer teksten "YAAAAA!!!" og "Du fik dem alle sammen!" i den store font og normale font
    text2 = font_large.render("YAAAAAAAAA!!!!!!", True, white1)
    text = font.render("Du fik dem alle sammen!", True, white1)
    #Prop de to stykker tekst på skærmen
    display.blit(text2, (60, height/2))
    display.blit(text, (45, height/2 + 100))
    pygame.display.update()
    #Vent 3 sek
    time.sleep(3)

# -------------------- Death ----------------
#Denne funktion kaldes når der tabes med en årsags streng
def GameOver(cause):
    #Loader fonten Chiller i to størrelser
    font = pygame.font.SysFont("Chiller", 50)
    font_large = pygame.font.SysFont("Chiller", 100)
    #Renderer teksten "Game Over!" og cause i den store font og normale font
    text2 = font_large.render("Game Over!", True, white1)
    text = font.render(cause, True, white1)
    #Prop de to styrkker tekst på skærmen
    display.blit(text2, (180, height/2-50))
    display.blit(text, (45, height/2 + 100))

# --------------------- The Game ------------------
def game():
    invasion = False
    #Her initieres vores rumskib
    ship = SpaceShip(width/2-ship_width/2, height-ship_height - 10, ship_width, ship_height, white)

    #Rumskibets skud
    bullets = []
    #Bossens skud
    boss_bullets = []
    #Den værdi vores rumskib skal flytte sig med
    x_move = 0

    #Herunder laver vi vores aliens
    aliens = []
    num_aliens = 7
    alienSize = 50
    for i in range(num_aliens):
        newAlien = Alien((i+1)*alienSize + i*20, alienSize+20, alienSize, 3, green)
        aliens.append(newAlien)

    #Herunder laver vi vores boss alien
    bossAlien = Boss(alienSize/2+1, alienSize+20, alienSize, 2, [0, 255, 0], 5)

    #Dette er vores gameloop, der hvor alt der sker i spillet checkes...
    while not invasion:
        #Herunder checker vi om der er blevet trykket på nogle taster eller om programmet er blevet lukket.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Hvis der er trykket ned på en tast
            if event.type == pygame.KEYDOWN:
                #Q tasten
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

                #-> tasten
                if event.key == pygame.K_RIGHT:
                    x_move = 5

                #<- tasten
                if event.key == pygame.K_LEFT:
                    x_move = -5

                #Mellemrums tasten
                if event.key == pygame.K_SPACE:
                    i = Bullet(ship.x + ship_width/2 - 5, ship.y, -5)
                    bullets.append(i)
            #Hvis der bliver løftet en tast
            if event.type == pygame.KEYUP:
                #Hvis tasten der bliver løftet for ikke er mellemrumstasten stopper rumskibet
                if event.key != pygame.K_SPACE:
                    x_move = 0

        #Baggrundsfarven tegnes på skærmen
        display.fill(background)

        for bullet in bullets:
            bullet.draw()
            bullet.move()
            #Her checkes der om et af rumskibets skud har ramt boss alien. hvis ja skal bossen dræbes
            if bullet.hit(bossAlien.x, bossAlien.y, bossAlien.d):
                bullets.remove(bullet)
                bossAlien.WasHit()

        for alien in aliens:
            #Om nogle af aliensne har ramt en af siderne
            if alien.x + alienSize >= width or alien.x <= 0:
                #Hvis ja, skifter alle aliens retning og række
                for alien_ in aliens:
                    alien_.x_dir *= -1
                    alien_.shift_down()
            #Flyt og tegn aliensne
            alien.draw()
            alien.move()
            #Her checkes om et af rumskibets skud har ramt nogle af aliensne
            for bullet in bullets:
                if bullet.hit(alien.x, alien.y, alien.d):
                    bullets.remove(bullet)
                    aliens.remove(alien)
                    num_aliens -= 1

        #Her checkes om bossen skal tegnes osv.
        if num_aliens <= 3 and bossAlien.lives > 0:
            bossAlien.draw()
            bossAlien.move()
            bossAlien.ShowLives()
            #1/20 chance for at bossalien skydder et skud
            if randint(1,20)==1:
                boss_bullets.append(Bullet(bossAlien.x + alienSize /2 - 5, bossAlien.y, 5))

            #Flyt og tegn alle bossens skud
            for boss_bullet in boss_bullets:
                boss_bullet.draw()
                boss_bullet.move()

            #Om boss alien skal skifte retning
            if bossAlien.x >= width or bossAlien.x <= 0 or randint(1,120) == 1:
                bossAlien.x_dir *= -1

        #Hvis alle aliens og boss er dræbt.
        if num_aliens == 0 and bossAlien.lives <= 0:
            saved()
            invasion = True

        #Hvis aliensne invaderede
        if num_aliens >= 1 and aliens[0].y + alienSize > height:
            GameOver("ÅRRHH nej aliens fik dig!")
            pygame.display.update()
            time.sleep(3)
            invasion = True

        #Hvis en af bossens skud ramte dig
        for boss_bullet in boss_bullets:
            if boss_bullet.hit(ship.x, ship.y, ship.w):
                boss_bullets.remove(boss_bullet)
                GameOver("Bossen ramte dig!")
                pygame.display.update()
                time.sleep(3)
                invasion = True

        #Her flyttes rumskibet
        ship.x += x_move

        #Her sørges der for at rumskibet ikke ryger ud over kanten
        if ship.x < 0 or ship.x + ship_width > width:
            ship.x -= x_move

        ship.draw()

        pygame.display.update()
        clock.tick(60)

# ----------------- Calling the Game Function ---------------------
game()