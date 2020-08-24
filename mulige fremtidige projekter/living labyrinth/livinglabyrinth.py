import pygame

pygame.init()

height = 500
width = 500

screen = pygame.display.set_mode((width, height))

board = [[None, None, None, None],
		 [None, None, None, None],
		 [None, None, None, None],
		 [None, None, None, None]]

border = 100
boardWidth = height - 2*border
boardHeight = width - 2*border
pieceWidth = boardWidth // len(board[0])
pieceHeight = boardHeight // len(board)

class Arrow:
	def __init__(self, rowOrCol, direction, value):
		#True indicates it is a row arrow, false that it is a column arrow
		self.rowOrCol =  rowOrCol
		#True indicates either down/right and False indicates up/left
		self.direction = direction
		self.value = value
		#The surf is an arrow pointing right
		self.surf = pygame.Surface((border, pieceHeight), pygame.SRCALPHA)
		pygame.draw.polygon(self.surf, (0,255,0), ((border-pieceHeight, 0),(border-pieceHeight, pieceHeight),(border, pieceHeight//2)))
		pygame.draw.line(self.surf, (0, 255, 0), (0,pieceHeight//2), (border-pieceHeight, pieceHeight//2), pieceHeight//4)
		#The rect collider, to check whether the mouse has clicked
		#ROW
		if self.rowOrCol:
			#RIGHT
			if self.direction:
				self.button = pygame.Rect(0,self.value*pieceHeight+border, border, pieceHeight)
			#LEFT
			else:
				self.button = pygame.Rect(border+boardWidth, self.value*pieceHeight+border, border, pieceHeight)
		#COL
		else:
			#DOWN
			if self.direction:
				self.button = pygame.Rect(self.value*pieceWidth+border, 0, pieceWidth, border)
			#UP
			else:
				self.button = pygame.Rect(self.value*pieceWidth+border, border+boardHeight, pieceWidth, border)

	def draw(self):
		#CHECH WHETHER IT CAN BE CLICKED DRAW THE BUTTON RECT IF IT CAN'T
		if ((self.rowOrCol and self.value == player.row) or (not self.rowOrCol and self.value == player.col)) or ((self.rowOrCol and self.value == lock.row) or (not self.rowOrCol and self.value == lock.col)) :
			pygame.draw.rect(screen, (255,0,0), self.button)
		#ROW
		if self.rowOrCol:
			#RIGHT
			if self.direction:
				screen.blit(pygame.transform.rotate(self.surf, 0), (0,self.value*pieceHeight+border))
			#LEFT
			else:
				screen.blit(pygame.transform.rotate(self.surf, 180), (border+boardWidth,self.value*pieceHeight+border))
		#COL
		else:
			#DOWN
			if self.direction:
				screen.blit(pygame.transform.rotate(self.surf, 270), (self.value*pieceWidth+border, 0))
			#UP
			else:
				screen.blit(pygame.transform.rotate(self.surf, 90), (self.value*pieceWidth+border, border+boardHeight))

class Player:
	def __init__(self, row, col):
		self.previousDirection = (-1, 0)
		self.row = row
		self.col = col

	def draw(self):
		pygame.draw.circle(screen, (255, 0, 0), (self.col*pieceWidth+border+pieceWidth//2, self.row*pieceHeight+border+pieceHeight//2), pieceWidth//4)

	def move(self):
		direction = board[self.row][self.col].entryExitDict[self.previousDirection]
		if board[self.row+direction[0]][self.col+direction[1]] != None:
			self.row += direction[0]
			self.col += direction[1]
			self.previousDirection = (-direction[0], -direction[1])

class Piece:
	def __init__(self, entryExitDict, surf):
		"""Entries are the key and corresponding exit is the value.
		For the horizontal piece it would look something like this: self.entryExitDict = {(0,-1):(0,1), (0,-1):(0,1)},
		which means the relative coordinate of the previous or next block.
		Where the "coordinates" are given as (row, column)"""

		self.entryExitDict = entryExitDict
		#We just give it a picture
		self.surf = surf

	def draw(self, x, y):
		screen.blit(self.surf, (x, y))

class Lock:
	def __init__(self,row,col):
		self.row = row
		self.col = col
	def draw(self):
		pygame.draw.line(screen, (255,0,0), (self.col*pieceWidth+border,self.row*pieceHeight+border), ((self.col+1)*pieceWidth+border,(self.row+1)*pieceHeight+border), 5)
		pygame.draw.line(screen, (255,0,0), (self.col*pieceWidth+border,(self.row+1)*pieceHeight+border), ((self.col+1)*pieceWidth+border,self.row*pieceHeight+border), 5)

class Goal:
	def __init__(self,row,col):
		self.row = row
		self.col = col
	def draw(self):
		pygame.draw.circle(screen, (255, 255, 0), (self.col*pieceWidth+border+pieceWidth//2, self.row*pieceHeight+border+pieceHeight//2), pieceWidth//5)


#HORIZONTAL
#We make the surface for the horizontal piece				To make the background transparent
horizontalStraightSurf = pygame.Surface((pieceWidth, pieceHeight), pygame.SRCALPHA)
#Top and bottom line
pygame.draw.rect(horizontalStraightSurf, (0,0,0), (0, pieceHeight//4-pieceHeight//5,pieceWidth,pieceHeight//5))
pygame.draw.rect(horizontalStraightSurf, (0,0,0), (0,pieceHeight-pieceHeight//4,pieceWidth,pieceHeight//5))

horizontalStraight = Piece({(0,-1):(0,1), (0,1):(0,-1)},horizontalStraightSurf)

#VERTICAL
#We make the surface for the horizontal piece				To make the background transparent
verticalStraightSurf = pygame.Surface((pieceWidth, pieceHeight), pygame.SRCALPHA)
#Left and right line
pygame.draw.rect(verticalStraightSurf, (0,0,0), (pieceWidth//4-pieceWidth//5, 0,pieceWidth//5,pieceHeight))
pygame.draw.rect(verticalStraightSurf, (0,0,0), (pieceWidth-pieceWidth//4,0,pieceWidth//5,pieceHeight))

verticalStraight = Piece({(-1,0):(1,0), (1,0):(-1,0)},verticalStraightSurf)

#TURN1
#We make the surface for the horizontal piece				To make the background transparent
turn1Surf = pygame.Surface((pieceWidth, pieceHeight), pygame.SRCALPHA)
#Vertical and buttom line, little top corner piece
pygame.draw.rect(turn1Surf, (0,0,0), (pieceWidth//4-pieceWidth//5,0,pieceWidth//5,pieceHeight-(pieceHeight//4-pieceHeight//5)))
pygame.draw.rect(turn1Surf, (0,0,0), (pieceWidth//4-pieceWidth//5,pieceHeight-pieceHeight//4,pieceWidth,pieceHeight//5))
#top corner
pygame.draw.rect(turn1Surf, (0,0,0), (pieceWidth-pieceWidth//4,0,pieceWidth//5,pieceHeight//4))
pygame.draw.rect(turn1Surf, (0,0,0), (pieceWidth-pieceWidth//4,(pieceHeight//4-pieceHeight//5),pieceWidth//4,pieceHeight//5))

turn1 = Piece({(-1,0):(0,1), (0,1):(-1,0)},turn1Surf)

#TURN2
#We make the surface for the horizontal piece				To make the background transparent
turn2Surf = pygame.Surface((pieceWidth, pieceHeight), pygame.SRCALPHA)
#Vertical and buttom line, little top corner piece
pygame.draw.rect(turn2Surf, (0,0,0), (pieceWidth-pieceWidth//4,0,pieceWidth//5,pieceHeight-(pieceHeight//4-pieceHeight//5)))
pygame.draw.rect(turn2Surf, (0,0,0), (0,pieceHeight-pieceHeight//4,pieceWidth-(pieceWidth//4-pieceWidth//5),pieceHeight//5))
#top corner
pygame.draw.rect(turn2Surf, (0,0,0), (0,(pieceHeight//4-pieceHeight//5),pieceWidth//4,pieceHeight//5))
pygame.draw.rect(turn2Surf, (0,0,0), ((pieceWidth//4-pieceWidth//5),0,pieceWidth//5,pieceHeight//4))

turn2 = Piece({(0,-1):(-1,0), (-1,0):(0,-1)},turn2Surf)

#TURN3
#We make the surface for the horizontal piece				To make the background transparent
turn3Surf = pygame.Surface((pieceWidth, pieceHeight), pygame.SRCALPHA)
#Vertical and buttom line, little top corner piece
pygame.draw.rect(turn3Surf, (0,0,0), (pieceWidth-pieceWidth//4,(pieceHeight//4-pieceHeight//5),pieceWidth//5,pieceHeight-(pieceHeight//4-pieceHeight//5)))#-(pieceHeight//4-pieceHeight//5)))
pygame.draw.rect(turn3Surf, (0,0,0), (0,(pieceHeight//4-pieceHeight//5),pieceWidth-(pieceWidth//4-pieceWidth//5),pieceHeight//5))
#top corner
pygame.draw.rect(turn3Surf, (0,0,0), (0,pieceHeight-pieceHeight//4,pieceWidth//4,pieceHeight//5))
pygame.draw.rect(turn3Surf, (0,0,0), ((pieceWidth//4-pieceWidth//5),pieceHeight-pieceHeight//4,pieceWidth//5,pieceHeight//4))

turn3 = Piece({(1,0):(0,-1), (0,-1):(1,0)},turn3Surf)

#TURN4
#We make the surface for the horizontal piece				To make the background transparent
turn4Surf = pygame.Surface((pieceWidth, pieceHeight), pygame.SRCALPHA)
#Vertical and buttom line, little top corner piece
pygame.draw.rect(turn4Surf, (0,0,0), ((pieceWidth//4-pieceWidth//5),(pieceHeight//4-pieceHeight//5),pieceWidth//5,pieceHeight-(pieceHeight//4-pieceHeight//5)))
pygame.draw.rect(turn4Surf, (0,0,0), ((pieceWidth//4-pieceWidth//5),(pieceHeight//4-pieceHeight//5),pieceWidth-(pieceWidth//4-pieceWidth//5),pieceHeight//5))
#top corner
pygame.draw.rect(turn4Surf, (0,0,0), (pieceWidth-pieceWidth//4,pieceHeight-pieceHeight//4,pieceWidth//4,pieceHeight//5))
pygame.draw.rect(turn4Surf, (0,0,0), (pieceWidth-pieceWidth//4,pieceHeight-pieceHeight//4,pieceWidth//5,pieceHeight//4))

turn4 = Piece({(1,0):(0,1), (0,1):(1,0)},turn4Surf)

#ClosedLeft
#We make the surface for the horizontal piece				To make the background transparent
closedLeftSurf = pygame.Surface((pieceWidth, pieceHeight), pygame.SRCALPHA)
#Vertical and buttom line, little top corner piece
pygame.draw.rect(closedLeftSurf, (0,0,0), ((pieceWidth//4-pieceWidth//5),(pieceHeight//4-pieceHeight//5),pieceWidth,pieceHeight//5))
pygame.draw.rect(closedLeftSurf, (0,0,0), ((pieceWidth//4-pieceWidth//5),pieceHeight-pieceHeight//4,pieceWidth,pieceHeight//5))
pygame.draw.rect(closedLeftSurf, (0,255,0), ((pieceWidth//4-pieceWidth//5),(pieceHeight//4-pieceHeight//5),pieceWidth//5,pieceHeight-2*(pieceHeight//4-pieceHeight//5)))

closedLeft = Piece({(0,1):(0,1)},closedLeftSurf)

#ClosedRight
#We make the surface for the horizontal piece				To make the background transparent
closedRightSurf = pygame.Surface((pieceWidth, pieceHeight), pygame.SRCALPHA)
#Vertical and buttom line, little top corner piece
pygame.draw.rect(closedRightSurf, (0,0,0), (0,(pieceHeight//4-pieceHeight//5),pieceWidth-(pieceWidth//4-pieceWidth//5),pieceHeight//5))
pygame.draw.rect(closedRightSurf, (0,0,0), (0,pieceHeight-pieceHeight//4,pieceWidth-(pieceWidth//4-pieceWidth//5),pieceHeight//5))
pygame.draw.rect(closedRightSurf, (0,255,0), (pieceWidth-pieceWidth//4,(pieceHeight//4-pieceHeight//5),pieceWidth//5,pieceHeight-2*(pieceHeight//4-pieceHeight//5)))

closedRight = Piece({(0,-1):(0,-1)},closedRightSurf)

#ClosedUp
#We make the surface for the horizontal piece				To make the background transparent
closedUpSurf = pygame.Surface((pieceWidth, pieceHeight), pygame.SRCALPHA)
#Vertical and buttom line, little top corner piece
pygame.draw.rect(closedUpSurf, (0,0,0), ((pieceWidth//4-pieceWidth//5),(pieceHeight//4-pieceHeight//5),pieceWidth//5,pieceHeight-(pieceHeight//4-pieceHeight//5)))
pygame.draw.rect(closedUpSurf, (0,0,0), (pieceWidth-pieceWidth//4,(pieceHeight//4-pieceHeight//5),pieceWidth//5,pieceHeight-(pieceHeight//4-pieceHeight//5)))
pygame.draw.rect(closedUpSurf, (0,255,0), ((pieceWidth//4-pieceWidth//5),(pieceHeight//4-pieceHeight//5),pieceWidth-2*(pieceWidth//4-pieceWidth//5),pieceHeight//5))

closedUp = Piece({(1,0):(1,0)},closedUpSurf)

#ClosedDown
#We make the surface for the horizontal piece				To make the background transparent
closedDownSurf = pygame.Surface((pieceWidth, pieceHeight), pygame.SRCALPHA)
#Vertical and buttom line, little top corner piece
pygame.draw.rect(closedDownSurf, (0,0,0), ((pieceWidth//4-pieceWidth//5),0,pieceWidth//5,pieceHeight-(pieceHeight//4-pieceHeight//5)))
pygame.draw.rect(closedDownSurf, (0,0,0), (pieceWidth-pieceWidth//4,0,pieceWidth//5,pieceHeight-(pieceHeight//4-pieceHeight//5)))
pygame.draw.rect(closedDownSurf, (0,255,0), ((pieceWidth//4-pieceWidth//5),pieceHeight-pieceHeight//4,pieceWidth-2*(pieceWidth//4-pieceWidth//5),pieceHeight//5))

closedDown = Piece({(-1,0):(-1,0)},closedDownSurf)
#horizontalStright, verticalStraight, turn1, turn2, turn3, turn4, closedLeft, closedRight, closedUp, closedDown
"""board[2][2] = horizontalStraight
board[1][1] = verticalStraight
board[2][1] = turn1
board[2][3] = turn2
board[1][3] = verticalStraight
board[0][3] = turn3
board[0][2] = horizontalStraight
board[1][0] = turn4

board[0][0] = closedLeft
board[0][1] = closedRight
board[2][0] = closedUp
board[3][0] = closedDown
"""
board = [[None, None, closedUp, None], [None, turn3, verticalStraight, None], [closedLeft, horizontalStraight, turn2, None], [None, None, closedDown, None]]

player = Player(1,2)

lock = Lock(2,0)
goal = Goal(3,1)
arrows = []

for value in range(4):
	for rowOrCol in range(2):
		for direction in range(2):
			arrows.append(Arrow(rowOrCol, direction, value))

def drawBoard():
	for rowI in range(len(board)):
		for pieceI in range(len(board[rowI])):
			piece = board[rowI][pieceI]
			if piece != None:
				piece.draw(pieceWidth*pieceI+border, pieceHeight*rowI+border)
	
def drawArrows():
	for arrow in arrows:
		arrow.draw()

def clickedArrow(mouseX, mouseY):
	for arrow in arrows:
		if arrow.button.collidepoint(mouseX,mouseY):
			#row
			if arrow.rowOrCol and player.row != arrow.value and lock.row != arrow.value:
				shiftRow(arrow.value, arrow.direction)
			#col
			elif not arrow.rowOrCol and player.col != arrow.value and lock.col != arrow.value:
				shiftCol(arrow.value, arrow.direction)

def shiftRow(row, direction):
	#RIGHT
	if direction:
		board[row] = [board[row][len(board[row])-1]] + board[row][:len(board[row])-1]
	else:
		board[row] = board[row][1:] + [board[row][0]]

def shiftCol(col, direction):
	#Down
	if direction:
		#I maybe need to add a special case for the first one.
		previousPiece = board[0][col]
		board[0][col] = board[-1][col]
		for rowI in range(len(board)-1):
			nextPiece = board[rowI+1][col]
			board[rowI+1][col] = previousPiece
			previousPiece = nextPiece
	#Up
	else:
		previousPiece = board[-1][col]
		board[-1][col] = board[0][col]
		for rowI in range(1,len(board)):
			nextPiece = board[-rowI-1][col]
			board[-rowI-1][col] = previousPiece
			previousPiece = nextPiece

def draw():
	screen.fill((255,255,255))
	#pygame.draw.rect(screen, (0,0,255), (border, border, boardWidth, boardHeight))
	drawBoard()
	player.draw()
	lock.draw()
	goal.draw()
	drawArrows()
	pygame.display.flip()

if __name__ == "__main__":
	running = True

	while running:
		if player.row == goal.row and player.col == goal.col:
			print("DU HAR VUNDET")
		#For hver begivenhed(tastatur tryk eller ligende) 
		for event in pygame.event.get():
				#Er der blevet trykket på 'X' i højre hjørne?
				if event.type == pygame.QUIT:
					#Hvis ja, stop spillet
					running = False
				#Er der trykket en tast ned?
				if event.type == pygame.KEYDOWN:
					#Hvis ja, er denne tast escape-tasten?
					if event.key == pygame.K_ESCAPE:
						#Hvis ja, stop spillet
						running = False
					elif event.key == pygame.K_m:
						player.move()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					mousePos = pygame.mouse.get_pos()
					clickedArrow(mousePos[0], mousePos[1])
		#Tegn spillet
		draw()
