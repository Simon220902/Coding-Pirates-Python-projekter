class Hund:
	def __init__(self, navn, race, alder, vægt, farve):
		self.navn = navn
		self.race = race
		self.alder = alder
		self.vægt = vægt
		self.farve = farve
	
	def alderTilHundeår(self):
	    return self.alder * 7

	def fortælOmDigSelv(self):
		print(self.navn, "er en", self.race, "og er", self.alder, "år gammel hvilket er:", self.alderTilHundeår(), "i hunderår.")
		print("Den vejer", self.vægt, "kg og den er", self.farve)

	def gø(self):
		print("VOV!!")

molly = Hund("Molly", "golden retriever", 8, 28, "lys gylden")
molly.fortælOmDigSelv()

for i in range(5):
	molly.gø()

leonardsHund = Hund("Tinka", "dansk-svensk gårdhund", 3.5, 8, "sort hvid")
leonardsHund.fortælOmDigSelv()