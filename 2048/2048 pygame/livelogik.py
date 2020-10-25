bræt = [[0,0,2,2],
		[4,0,4,2],
		[16,0,0,16],
		[0,8,8,0]]


def bevægOp(bræt):
	pass

def bevægNed(bræt):
	pass

def bevægTilHøjre(bræt):
	pass

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

print("BRÆT FØR")
for række in bræt:
	print(række)

print("BRÆT EFTER")
bræt = bevægTilVenstre(bræt)
for række in bræt:
	print(række)