import pygame
import random

bredde = 500
højde = 500

skærm = pygame.display.set_mode((bredde, højde))
pygame.font.init()
font = pygame.font.SysFont(None, 30)
#Farver: R    G    B
sort = (  0,   0,  0)+
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
	shiftLeft(board)

	# merge cells
	for i in range(4):
		for j in range(3):
			if board[i][j] == board[i][j + 1] and board[i][j] != 0:
				board[i][j] *= 2
				board[i][j + 1] = 0
				j = 0

	# final shift
	shiftLeft(board)
	return board


def moveUp(board):
	"""
	Move ane merge tiles upwards.
	Parameters:
		board (list): game board
	Returns:
		board (list): updated game board
	"""
	board = rotateLeft(board)
	board = moveLeft(board)
	board = rotateRight(board)
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
	shiftRight(board)

	# merge cells
	for i in range(4):
		for j in range(3, 0, -1):
			if board[i][j] == board[i][j - 1] and board[i][j] != 0:
				board[i][j] *= 2
				board[i][j - 1] = 0
				j = 0

	# final shift
	shiftRight(board)
	return board


def moveDown(board):
	"""
	Move and merge tiles downwards.
	Parameters:
		board (list): game board
	Returns:
		board (list): updated game board
	"""
	board = rotateLeft(board)
	board = moveLeft(board)
	shiftRight(board)
	board = rotateRight(board)
	return board


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
		board[i].extend([0] * (4 - count))


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
		board[i].extend(nums)


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

kør = True
while kør:
	tegn()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			kør = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				bræt = moveUp(bræt)
				chooseRandom()
			elif event.key == pygame.K_DOWN:
				bræt = moveDown(bræt)
				chooseRandom()
			elif event.key == pygame.K_RIGHT:
				bræt = moveRight(bræt)
				chooseRandom()
			elif event.key == pygame.K_LEFT:
				bræt = moveLeft(bræt)
				chooseRandom()
