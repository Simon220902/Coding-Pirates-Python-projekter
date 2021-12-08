import random

bræt = [[0,0,8,8],
		[8,0,0,8],
		[16,0,0,16],
		[0,0,0,0]]
#Roteret til venstre
def roterVenstre(bræt):
	nytBræt = []
	for i in range(4):
		nyRække = []
		for j in range(4):
			nyRække.append(bræt[j][3-i])
		nytBræt.append(nyRække)
	return nytBræt
	


def bevægOp(bræt):
	bræt = roterVenstre(bræt)
	bræt = bevægTilVenstre(bræt)
	bræt = roterVenstre(bræt)
	bræt = roterVenstre(bræt)
	bræt = roterVenstre(bræt)
	return bræt

def bevægNed(bræt):
	bræt = roterVenstre(bræt)
	bræt = roterVenstre(bræt)
	bræt = roterVenstre(bræt)
	bræt = bevægTilVenstre(bræt)
	bræt = roterVenstre(bræt)
	return bræt


def bevægTilHøjre(bræt):
	bræt = roterVenstre(bræt)
	bræt = roterVenstre(bræt)
	bræt = bevægTilVenstre(bræt)
	bræt = roterVenstre(bræt)
	bræt = roterVenstre(bræt)
	return bræt

def bevægTilVenstre(bræt):
	bræt = rykTilVenstre(bræt)
	#saml til venstre
	#For hver række samler vi tallene i rækken hvis de to tal er det samme.
	for i in range(0, 4):
		for j in range(0, 3):
			if bræt[i][j] == bræt[i][j+1] and bræt[i][j] != 0:
				bræt[i][j] = bræt[i][j] * 2
				bræt[i][j+1] = 0
	
	bræt = rykTilVenstre(bræt)
	return bræt


def rykTilVenstre(bræt):
	#For hver af rækkerne i brættet
	for række in bræt:
		#imens der er nuller i rækken
		while 0 in række:
			#Slet nuller
			række.remove(0)

		#udfyld resten af rækken med nuller
		for i in range(4-len(række)):
			række.append(0)
	return bræt


# på en tom plads (så altså der hvor der er nuller)
# tilføj enten en 2'er eller en 4'er
def tilføjTilfældig(bræt):
	indexer = []
	for rækkeI in range(4):
		for kolI in range(4):
			if bræt[rækkeI][kolI] == 0:
				#  0       1
				#(rækkeI, kolI)
				indexer.append((rækkeI, kolI))
	
	# tilføj enten en 2'er eller en 4'er på en tilfældig tom plads
	index = random.choice(indexer) #tilfældig tom pladsz
	bræt[index[0]][index[1]] = random.choice([2, 4])
	return bræt



print("BRÆT FØR")
for række in bræt:
	print(række)

print("BRÆT EFTER")
bræt = tilføjTilfældig(bræt)
for række in bræt:
	print(række)