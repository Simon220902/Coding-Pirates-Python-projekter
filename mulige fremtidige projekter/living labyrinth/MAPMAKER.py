import pygame
import livinglabyrinth as l

bredde = 800
højde = 500
baneBredde = 300
baneHøjde = 300

skærm = pygame.display.set_mode((bredde, højde))

rækker = 4
blokke = 4

blokBredde = baneBredde//blokke
blokHøjde = baneHøjde//rækker
valgte = 0
bane = []
for rækkeI in range(rækker):
	bane.append([])
	for blokI in range(rækker):
		bane[rækkeI].append(0)

pygame.font.init()
font = pygame.font.SysFont('Arial', 30)

#Farver: R    G    B
sort = (  0,   0,  0)
hvid = (255, 255, 255)
blå  = (  0,   0, 255)
gul  = (255, 238,   0)
rød  = (255, 0, 0)
orange=(255, 184, 82)
pink = (255, 184, 255)
grøn = (0,255,0)
lysblå = (0, 255, 255)

def tegn():
	skærm.fill(hvid)
	tegnBane()
	tegnBlokVælger()
	pygame.display.flip()


"""
def drawBoard():
	for rowI in range(len(board)):
		for pieceI in range(len(board[rowI])):
			piece = board[rowI][pieceI]
			if piece != None:
				piece.draw(pieceWidth*pieceI+border, pieceHeight*rowI+border)
		#Tegn linjer
	for rækkeI in range(len(bane)):
		pygame.draw.line(skærm, hvid, (0, rækkeI*blokHøjde), (baneBredde, rækkeI*blokHøjde))
	for blokI in range(len(bane[0])):
		pygame.draw.line(skærm, hvid, (blokI*blokBredde, 0), (blokI*blokBredde, baneHøjde))
"""
def tegnBane():
	for rowI in range(len(bane)):
		for colI in range(len(bane[rowI])):
			skærm.blit(blokke[bane[rowI][colI]], (colI*l.pieceWidth, rowI*l.pieceHeight))
	#Tegn linjer
	for rækkeI in range(len(bane)):
		pygame.draw.line(skærm, sort, (0, rækkeI*blokHøjde), (baneBredde, rækkeI*blokHøjde))
	for blokI in range(len(bane[0])):
		pygame.draw.line(skærm, sort, (blokI*blokBredde, 0), (blokI*blokBredde, baneHøjde))


blokke = {0:pygame.Surface((l.pieceWidth, l.pieceHeight)), 1:l.horizontalStraightSurf, 2:l.verticalStraightSurf, 3:l.turn1Surf, 4:l.turn2Surf, 5:l.turn3Surf, 6:l.turn4Surf, 7:l.closedLeftSurf, 8:l.closedRightSurf, 9:l.closedUpSurf, 10:l.closedDownSurf}
#VI GØR DEN TOMME HVID
blokke[0].fill(hvid)
def tegnBlokVælger():
	info = []
	info.append(font.render('0: BLANK, 1: horizontalStraight', False, (0, 0, 0)))
	info.append(font.render('2: verticalStraight, 3: turn1', False, (0, 0, 0)))
	info.append(font.render('4: turn2, 5: turn3, 6: turn4', False, (0, 0, 0)))
	info.append(font.render('7: closedLeft, 8: closedRight', False, (0, 0, 0)))
	info.append(font.render('9: closedUp, +: closedDown', False, (0, 0, 0)))
	info.append(font.render('p: print, Valgte blok:', False, (0, 0, 0)))
	for infoI in range(len(info)):
		skærm.blit(info[infoI], (baneBredde, infoI*info[infoI].get_height()+10))
	skærm.blit(blokke[valgte], (baneBredde+10, len(info)*info[0].get_height()+2*10))

blokkeString = {0:'None', 1:'horizontalStraight', 2:'verticalStraight', 3:'turn1', 4:'turn2', 5:'turn3', 6:'turn4', 7:'closedLeft', 8:'closedRight', 9:'closedUp', 10:'closedDown'}
def printBane():
	baneString = str(bane)
	for key in blokke.keys():
		baneString = baneString.replace(" " + str(key)+",", " "+blokkeString[key]+",")
		baneString = baneString.replace("[" + str(key)+",", "["+blokkeString[key]+",")
		baneString = baneString.replace(" " + str(key)+"]", " "+blokkeString[key]+"]")
	print(str(bane))
	print(baneString)

mus = False

kør = True

while kør:
	tegn()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			kør = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_0:
				valgte = 0
			elif event.key == pygame.K_1:
				valgte = 1
			elif event.key == pygame.K_2:
				valgte = 2
			elif event.key == pygame.K_3:
				valgte = 3
			elif event.key == pygame.K_4:
				valgte = 4
			elif event.key == pygame.K_5:
				valgte = 5
			elif event.key == pygame.K_6:
				valgte = 6
			elif event.key == pygame.K_7:
				valgte = 7
			elif event.key == pygame.K_8:
				valgte = 8
			elif event.key == pygame.K_9:
				valgte = 9
			elif event.key == pygame.K_PLUS:
				valgte = 10
			elif event.key == pygame.K_p:
				printBane()
		elif event.type == pygame.MOUSEBUTTONUP:
			mus = False
		elif event.type == pygame.MOUSEBUTTONDOWN or mus:
			mus = True
			mouse_pos = pygame.mouse.get_pos()
			x = mouse_pos[0]
			y = mouse_pos[1]
			rækkeI = y//blokHøjde
			blokI =  x//blokBredde
			if rækkeI < len(bane) and blokI < len(bane[0]):
				bane[rækkeI][blokI] = valgte

			