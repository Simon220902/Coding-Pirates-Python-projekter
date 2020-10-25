import pygame

højde = 500
bredde = 500

skærm = pygame.display.set_mode((bredde, højde))

bræt = [[0, 0, 0, 0],
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

def tegnKlods(rækkeI, klodsI):
  x = klodsI*klodsBredde
  y = rækkeI*klodsHøjde
  pygame.draw.rect(skærm, (255, 0, 0), (x, y, klodsBredde, klodsHøjde))


kør = True

while kør:
tegn()

#Vi løber igennem alle de ting der er sket. (input)
for event in pygame.event.get():
if event.type == pygame.QUIT:
kør = False