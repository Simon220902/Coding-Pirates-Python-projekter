import pygame

højde = 500
bredde = 500

skærm = pygame.display.set_mode((højde, bredde))

sort = (0, 0, 0)
hvid = (255, 255, 255)
blå = (0, 0, 255)
rød = (255, 0, 0)

def fraktal(x, y, bredde, højde, loft):
    pygame.draw.line(skærm, sort, (x+0.25*bredde, y+højde//2), (x+0.75*bredde, y+højde//2),3)
    pygame.draw.line(skærm, rød, (x+0.25*bredde, y+(højde*0.5)//2), (x+0.25*bredde, y+(højde*1.5)//2), 3)
    pygame.draw.line(skærm, blå, (x+0.75*bredde, y+(højde*0.5)//2), (x+0.75*bredde, y+(højde*1.5)//2), 3)
    if loft > 0:
        loft -= 1
        #Venstre øverst
        fraktal(x, y, bredde//2, højde//2, loft)
        #Venstre nederst
        fraktal(x, y+højde//2, bredde//2, højde//2, loft)
        #Højre øverst
        fraktal(x+bredde//2, y, bredde//2, højde//2, loft)
        #Højre nederst
        fraktal(x+bredde//2, y+højde//2, bredde//2, højde//2, loft)

skærm.fill(hvid)
fraktal(0,0,bredde,højde,3)
pygame.display.flip()


kør = True 
while kør:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kør = False
