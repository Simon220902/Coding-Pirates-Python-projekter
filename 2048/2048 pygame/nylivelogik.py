import random

bræt = [[0,8,2,2],
		[4,0,4,2],
		[16,0,0,16],
		[0,8,8,0]]


#1
#Roter for at kunne genbruge bevægTilVenstre

#2
#Lav de andre bevæg... funktioner og test dem

#3
#Lav en funktion, der tilføjer enten en to'er eller fire'r til brættet



#som vi tænkte på sidst var det jo muligt at lave bevægOp osv. ved bare at rotere rundt og så bruge bevægTilVenstre og så rotere tilbage igen
#For at vi kan lave det skal vi lave en roter funktion (hvor vi kun laver roter til venstre, hvor roter til højre bare er at kalde roter venstre tre gange)
#ROTER
def roterVenstre(bræt):
	#Det nye bræt
	nytBræt = []
	for i in range(4):
		kolTilRække = []
		for j in range(4):
			#Vi tager den kolonne yderst til højre og sætter som første række
			#og så den næst yderste kolonne til højre og sætter den som anden osv.
			kolTilRække.append(bræt[j][3-i])
		#Vi tilføjer rækken der før var en kolonne til brættet
		nytBræt.append(kolTilRække)
	return nytBræt

def roterHøjre(bræt):
	#At rotere tre gange til venstre er det samme som at rotere en gang til højre
	return roterVenstre(roterVenstre(roterVenstre(bræt)))


#DEM LAVER VI NU.
def bevægOp(bræt):
	bræt = roterVenstre(bræt)
	bræt = bevægTilVenstre(bræt)
	bræt = roterHøjre(bræt)
	return bræt

def bevægNed(bræt):
	bræt = roterHøjre(bræt)
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

#DENNE LAVEDE VI SIDSTE GANG
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

#3
def tilføjTilfældig():
	#vi finder først alle de index, hvor at værdien er lig nul
	#og tilføjer dem til nedenstående liste som en tuple (rækkeI, blokI)
	index_nul = []
	for rækkeI in range(len(bræt)):
		for blokI in range(len(bræt[0])):
			if bræt[rækkeI][blokI] == 0:
				index_nul.append((rækkeI, blokI))

	#!!!!!!!!Husk at impotere random.!!!!!!!!!!!!!!

	#Hvis brættet ikke er fyldt helt ud kan vi tilføje enten en toer eller fire
	if len(index_nul) > 0:
		#Vi vælger en tilfældig placering
		valgt_index = random.choice(index_nul)
		#Hvor vi så sætter den tilfældigt enten til 2 eller 4
		bræt[valgt_index[0]][valgt_index[1]] = random.choice([2,4])



print("BRÆT FØR")
for række in bræt:
	print(række)

print("BRÆT EFTER")
#HER PRØVER VI HVER AF DEM
#Husk at ændre brættet så vi tester det undervejs.
bræt = bevægTilHøjre(bræt)
tilføjTilfældig()
for række in bræt:
	print(række)