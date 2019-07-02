import sys
import pygame
from pygame.locals import *

pygame.init()

FPS = 60.0
FPSClock = pygame.time.Clock()

WIDTH, HEIGHT = 300, 300
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

#muligvis en dict
xboard = [0, WIDTH/3, WIDTH/3*2, WIDTH]
yboard = [0, HEIGHT/3, HEIGHT/3*2, HEIGHT]

BLACK = [  0,   0,   0]
WHITE = [255, 255, 255]
BLUE  = [  0,   0, 255]

def drawBoard():
	#vertikale linjer
	pygame.draw.line(SCREEN, WHITE, (xboard[1], yboard[0]), (xboard[1], yboard[3]))
	pygame.draw.line(SCREEN, WHITE, (xboard[2], yboard[0]), (xboard[2], yboard[3]))
	#horisontale linjer
	pygame.draw.line(SCREEN, WHITE, (xboard[0], yboard[1]), (xboard[3], yboard[1]))
	pygame.draw.line(SCREEN, WHITE, (xboard[0], yboard[2]), (xboard[3], yboard[2]))

def drawPieces(board):
	for row in range(len(board)):
		for col in range(len(board[row])):
			piece = board[row][col]
			#hvis der ikke er nogen brik i feltet står der None, derfor tester vi om der står none først fordi hvis der gør det så kører den bare videre i loopet
			if piece is None:
				pass
			#hvis piece er true er det det samme som kryds
			elif piece:
				#her tegner vi krydset ved først at tegne en streg fra øverste venstre hjørne til nederste højre hjørne
				pygame.draw.line(SCREEN, WHITE, (xboard[col], yboard[row]), (xboard[col + 1], yboard[row + 1]), 10)
				#her tegnes den anden streg af krydset fra nederste venstre hjørne til øverste højre hjørne
				pygame.draw.line(SCREEN, WHITE, (xboard[col], yboard[row+1]), (xboard[col + 1], yboard[row]), 10)
				#pygame.draw.rect(SCREEN, WHITE, [xboard[col], yboard[row], xboard[1], yboard[1]])
			#ellers er brikken False som er bolle 
			else:
				#tegn en crikel (bolle) da man skal tegne en cirkel fra dens midte bliver vi nødt til at finde midten af det felt den er i hendholdsvis for x-koordinatet og y-koordinatet
				pygame.draw.circle(SCREEN, WHITE, [int(xboard[col]+((xboard[col+1]-xboard[col])/2)), int(yboard[row]+((yboard[row+1]-yboard[row])/2))], 50)
				pygame.draw.circle(SCREEN, BLACK, [int(xboard[col]+((xboard[col+1]-xboard[col])/2)), int(yboard[row]+((yboard[row+1]-yboard[row])/2))], 35)
				#pygame.draw.rect(SCREEN, BLUE, [xboard[col], yboard[row], xboard[1], yboard[1]]) #dette tegner en blå firkand 

def draw(board):
	SCREEN.fill((0, 0, 0)) # Fill the screen with black.
	# Redraw screen here.
	drawBoard()
	drawPieces(board)
	# Flip the display so that the things we drew actually show up.
	pygame.display.flip()

def winScreen(winner):
	if winner == "Tie":
		titleText = "Det blev uafgjort"
	elif winner: #Hvis winner er True (kryds)
		titleText = "Kryds vandt"
	else: #Ellers er winner False (bolle)
		titleText = "Bolle vandt!"
	titleFont = pygame.font.Font('freesansbold.ttf', 30)
	titleWon = titleFont.render(titleText, True, BLUE)
	titleRect = titleWon.get_rect()
	titleRect.center = (WIDTH/2, HEIGHT/2)
	SCREEN.fill(BLACK)
	SCREEN.blit(titleWon, titleRect)
	pygame.display.flip()
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					terminate()
				else:
					return #start nyt spil 

#turn er enten True eller False for enten kryds eller bolle
def validClick(coord, board):
	for row in range(3):
		if coord[1] > yboard[row] and coord[1] < yboard[row+1]:
			for col in range(3):
				if coord[0] > xboard[col] and coord[0] < xboard[col+1]:
					if board[row][col] == None:
						#Man bliver nødt til at returnere en 
						return (True, row, col)
					else:
						return (False, None, None)

#de forskellige check funktioner virker
def checkBoard(board):
	if checkCross(board) != None:
		return checkCross(board)
	elif checkVertical(board) != None:
		return checkVertical(board)
	elif checkHorizontal(board) != None:
		return checkHorizontal(board)
	elif checkTie(board):
		return "Tie"
	else:
		return None

def checkCross(board):
	if board[0][0] == board[1][1] == board[2][2] and board[0][0] != None:
		return board[0][0]
	elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != None:
		return board[0][2]

def checkVertical(board):
	for col in range(3):
		if board[0][col] == board[1][col] == board[2][col] and board[0][col] != None:
			return board[0][col]

def checkHorizontal(board):
	for row in range(3):
		if board[row][0] == board[row][1] == board[row][2] and board[row][0] != None:
			return board[row][0]

def checkTie(board):
	for row in range(3):
		for col in range(3):
			if board[col][row] == None:
				return False
	return True

def terminate():
	pygame.quit() #Luk pygame
	sys.exit() #Luk "systemet"

if __name__ == '__main__':
	while True:
		TURN = True
		BOARD = [[None, None, None],
		 		 [None, None, None],
		 		 [None, None, None]]
		dt = 1/FPS
		while checkBoard(BOARD) == None: #Loop indtil enten kryds eller bolle har vundet eller det står uafgjort
			for event in pygame.event.get():
				if event.type == QUIT:
					terminate()
				elif event.type == MOUSEBUTTONDOWN:
					#Vi checker om der hvor musen har klikket er et sted der ikke allerede er en brik
					validIn = validClick(pygame.mouse.get_pos(), BOARD)
					if validIn[0]:
						BOARD[validIn[1]][validIn[2]] = TURN
						TURN = not TURN
			draw(BOARD)
			dt = FPSClock.tick(FPS)
		winScreen(checkBoard(BOARD))