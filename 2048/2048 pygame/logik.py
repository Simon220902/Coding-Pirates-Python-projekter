bræt = [[0,0,0,0],
		[2,0,2,0],
		[2,4,2,0],
		[2,0,0,2]]

#BEVÆGELSE
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

def bevægOp(bræt):
	bræt = roterVenstre(bræt)
	bræt = bevægTilVenstre(bræt)
	bræt = roterHøjre(bræt)
	return bræt

def bevægNed(bræt):
	bræt = roterVenstre(bræt)
	bræt = bevægTilHøjre(bræt)
	bræt = roterHøjre(bræt)
	return bræt

#RYK
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

#ROTER
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

def roterHøjre(bræt):
	#At rotere tre gange til venstre er det samme som at rotere en gang til højre
	return roterVenstre(roterVenstre(roterVenstre(bræt)))


#KALD FUNKTIONERNE
print("BRÆT FØR:")
for i in range(len(bræt)):
	print(bræt[i])

print("BRÆT EFTER:")
bræt = bevægTilVenstre(bræt)
for i in range(len(bræt)):
	print(bræt[i])