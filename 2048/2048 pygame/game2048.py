import pygame
import random

bredde = 500
højde = 500

skærm = pygame.display.set_mode((bredde, højde))
pygame.font.init()
font = pygame.font.SysFont(None, 30)
#Farver: R    G    B
sort = (  0,   0,  0)
hvid = (255, 255, 255)

blokBredde = bredde//4

blokHøjde = højde//4

bræt = [[0,0,0,0],
		[2,0,2,0],
		[2,4,2,0],
		[2,0,0,2]]

farver = {0:(205, 192, 180), 2:(238, 228, 218), 4:(237, 224, 200), 8:(242, 177, 121), 16:(245, 149, 99), 32:(246, 124, 95), 64:(245, 94, 59), 128:(236, 207, 7), 256:(237, 204, 97), 512:(237, 200, 80), 1024:(240, 196, 60), 2048:(236, 196, 2)}

"""Stjålen logik"""
#Så hvordan virker det?
"""

"""


def moveLeft(board):
	"""
	Move and merge tiles to the left.
	Parameters:
		board (list): game board
	Returns:
		board (list): updated game board
	"""
	# initial shift
	#shiftLeft(board)
	rykTilVenstre(board)
	# merge cells
	for i in range(4):
		for j in range(3):

			if board[i][j] == board[i][j + 1] and board[i][j] != 0:
				board[i][j] *= 2
				board[i][j + 1] = 0
				j = 0

	# final shift
	#shiftLeft(board)
	rykTilVenstre(board)
	return board

def bevægTilVenstre(bræt):
	rykTilVenstre(bræt)
	#Vi prøver at samle cellerne til venstre
	for i in range(4):
		for j in range(3):
			#Hvis de er de samme og de ikke er nul
			if bræt[i][j] == bræt[i][j + 1] and bræt[i][j] != 0:
				#Så "Ryk" dem sammen ved at fordoble den længst inde til venstre
				bræt[i][j] *= 2
				#Og sæt den anden til nu
				bræt[i][j + 1] = 0
	#Nu er der muligvis kommet nogle ekstra "huller"-nuller, hvilket vi lige skal fikse
	rykTilVenstre(bræt)
	return bræt


def bevægOp(bræt):
	bræt = roterVenstre(bræt)
	bræt = bevægTilVenstre(bræt)
	bræt = roterHøjre(bræt)
	return bræt


def moveUp(board):
	"""
	Move ane merge tiles upwards.
	Parameters:
		board (list): game board
	Returns:
		board (list): updated game board
	"""
	board = roterVenstre(board)
	board = moveLeft(board)
	board = roterHøjre(board)
	return board


def moveRight(board):
	"""
	Move and merge tiles to the right.
	Parameters:
		board (list): game board
	Returns:
		board (list): updated game board
	"""
	# initial shift
	rykTilHøjre(board)

	# merge cells
	for i in range(4):
		for j in range(3, 0, -1):
			if board[i][j] == board[i][j - 1] and board[i][j] != 0:
				board[i][j] *= 2
				board[i][j - 1] = 0
				j = 0

	# final shift
	rykTilHøjre(board)
	return board

def bevægTilHøjre(bræt):
	rykTilHøjre(bræt)
	#Vi prøver at samle cellerne til venstre
	for i in range(4):
		for j in range(3):
			#Hvis de er de samme og de ikke er nul
			if bræt[i][3-j] == bræt[i][3-j-1] and bræt[i][3-j] != 0:
				#Så "Ryk" dem sammen ved at fordoble den længst ude til højre
				bræt[i][3-j] = 2 * bræt[i][3-j]
				#Og sæt den til venstre for til nul
				bræt[i][3-j-1] = 0

	#Nu er der muligvis kommet nogle ekstra "huller"-nuller, hvilket vi lige skal fikse
	rykTilHøjre(bræt)
	return bræt

def moveDown(board):
	"""
	Move and merge tiles downwards.
	Parameters:
		board (list): game board
	Returns:
		board (list): updated game board
	"""
	board = roterVenstre(board)
	board = moveRight(board)
	board = roterHøjre(board)
	return board

def bevægNed(bræt):
	bræt = roterVenstre(bræt)
	bræt = bevægTilHøjre(bræt)
	bræt = roterHøjre(bræt)
	return bræt


def shiftLeft(board):
	"""
	Perform tile shift to the left.
	Parameters:
		board (list): game board
	"""
	# remove 0's in between numbers
	for i in range(4):
		nums, count = [], 0
		for j in range(4):
			if board[i][j] != 0:
				nums.append(board[i][j])
				count += 1
		board[i] = nums
		for x in range(4 - count):
			board[i].append(0)

def rykTilVenstre(bræt):
	for i in range(4):
		#Vi fjerner alle nulle 
		while 0 in bræt[i]:
			bræt[i].remove(0)
		#Vi tilføjer nuller på venstre side 
		for _ in range(4 - len(bræt[i])):
			bræt[i].append(0)

def rykTilHøjre(bræt):
	for i in range(4):
		#Vi fjerner alle nulle 
		while 0 in bræt[i]:
			bræt[i].remove(0)
		#Vi tilføjer nuller på venstre side 
		for _ in range(4 - len(bræt[i])):
			bræt[i] = [0] + bræt[i]

def shiftRight(board):
	"""
	Perform tile shift to the right.
	Parameters:
		board (list): game board
	"""
	# remove 0's in between numbers
	for i in range(4):
		nums, count = [], 0
		for j in range(4):
			if board[i][j] != 0:
				nums.append(board[i][j])
				count += 1
		board[i] = [0] * (4 - count)
		for x in range(4 - count):
			board[i] = [0] + board[i]




def rotateLeft(board):
	"""
	90 degree counter-clockwise rotation.
	Parameters:
		board (list): game board
	Returns:
		b (list): new game board after rotation
	"""
	b = [[board[j][i] for j in range(4)] for i in range(3, -1, -1)]
	return b

def roterVenstre(bræt):
	#Det nye bræt
	nytBræt = []
	for i in range(4):
		midBræt = []
		for j in range(4):
			#Vi tager den kolonne yderst til højre og sætter som første række
			#og så den næst yderste kolonne til højre og sætter den som anden osv.
			midBræt.append(bræt[j][3-i])
		#Vi tilføjer rækken der før var en kolonne til brættet
		nytBræt.append(midBræt)
	return nytBræt

def rotateRight(board):
	"""
	270 degree counter-clockwise rotation.
	Parameters:
		board (list): game board
	Returns:
		(list): new game board after rotation
	"""
	b = rotateLeft(board)
	b = rotateLeft(b)
	return rotateLeft(b)

def roterHøjre(bræt):
	#At rotere tre gange til venstre er det samme som at rotere en gang til højre
	return roterVenstre(roterVenstre(roterVenstre(bræt)))

"""Slut på stjålen logik"""





def op():
	for minusI in range(-3, 0):
		for blokI in range(len(bræt[0])):
			if bræt[-minusI][blokI] != 0:
				if bræt[-(1+minusI)][blokI] == 0:
					bræt[-(1+minusI)][blokI] = bræt[-minusI][blokI]
					bræt[-minusI][blokI] = 0

				elif bræt[-(1+minusI)][blokI] == bræt[-minusI][blokI]:
					bræt[-(1+minusI)][blokI] += bræt[-minusI][blokI]
					bræt[-minusI][blokI] = 0

def ned():
	for rækkeI in range(0,3):
		for blokI in range(len(bræt[0])):
			if bræt[rækkeI][blokI] != 0:
				if bræt[rækkeI+1][blokI] == 0:
					bræt[rækkeI+1][blokI] = bræt[rækkeI][blokI]
					bræt[rækkeI][blokI] = 0
					#Okay så den vi forlader afhænigt af retning skal vi flytte den tidligere med osv.
				elif bræt[rækkeI+1][blokI] == bræt[rækkeI][blokI]:
					bræt[rækkeI+1][blokI] += bræt[rækkeI][blokI]
					bræt[rækkeI][blokI] = 0

def højre():
	for blokI in range(0,3):
		for rækkeI in range(0,4):
			if bræt[rækkeI][blokI] != 0:
				if bræt[rækkeI][blokI+1] == 0:
					bræt[rækkeI][blokI+1] = bræt[rækkeI][blokI]
					bræt[rækkeI][blokI] = 0
				elif bræt[rækkeI][blokI+1] == bræt[rækkeI][blokI]:
					bræt[rækkeI][blokI+1] += bræt[rækkeI][blokI]
					bræt[rækkeI][blokI] = 0

def venstre():
	for minusI in range(-3, 0):
		for rækkeI in range(0,4):
			if bræt[rækkeI][-minusI] != 0:
				if bræt[rækkeI][-(1+minusI)] == 0:
					bræt[rækkeI][-(1+minusI)] = bræt[rækkeI][-minusI]
					bræt[rækkeI][-minusI] = 0
				elif bræt[rækkeI][-(1+minusI)] == bræt[rækkeI][-minusI]:
					bræt[rækkeI][-(1+minusI)] += bræt[rækkeI][-minusI]
					bræt[rækkeI][-minusI] = 0

def chooseRandom():
	#vi finder først alle de index, hvor at værdien er lig nul
	index_nul = []
	for rækkeI in range(len(bræt)):
		for blokI in range(len(bræt[0])):
			if bræt[rækkeI][blokI] == 0:
				index_nul.append((rækkeI, blokI))
	if len(index_nul) > 0:
		valgt_index = random.choice(index_nul)
		bræt[valgt_index[0]][valgt_index[1]] = random.choice([2,4])


def tegn():
	skærm.fill((186, 173, 155))
	for rækkeI in range(len(bræt)):
		for blokI in range(len(bræt[0])):
			pygame.draw.rect(skærm, farver[bræt[rækkeI][blokI]], (blokI*blokBredde+5, rækkeI*blokHøjde+5, blokBredde-10, blokHøjde-10))
			if bræt[rækkeI][blokI] != 0:
				tekst = font.render(str(bræt[rækkeI][blokI]), True, hvid)
				tekstStørrelse = tekst.get_size()
				tekstX = blokI*blokBredde+(blokBredde//2-tekstStørrelse[0]//2)
				tekstY = rækkeI*blokHøjde+(blokHøjde//2-tekstStørrelse[1]//2)
				skærm.blit(tekst, (tekstX, tekstY))
	pygame.display.flip()

kør = True
while kør:
	tegn()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			kør = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				#bræt = moveUp(bræt)
				bræt = bevægOp(bræt)
				chooseRandom()
			elif event.key == pygame.K_DOWN:
				#bræt = moveDown(bræt)
				bræt = bevægNed(bræt)
				chooseRandom()
			elif event.key == pygame.K_RIGHT:
				#bræt = moveRight(bræt)
				bræt = bevægTilHøjre(bræt)
				chooseRandom()
			elif event.key == pygame.K_LEFT:
				#bræt = moveLeft(bræt)
				bræt = bevægTilVenstre(bræt)
				chooseRandom()