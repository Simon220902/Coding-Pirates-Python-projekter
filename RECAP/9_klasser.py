class Pirat:
	def __init__(self, navn, alder):
		self.navn = navn
		self.alder = alder
		self.skills = []

	def tilføjSkill(self, skill):
		self.skills.append(skill)

	def præsenterSkills(self):
		print("Piraten ", self.navn, " er ", self.alder, " år gammel og er super god til:")
		for skill in self.skills:
			print(" - ", skill)

gustav = Pirat("Gustav", 15 )

gustav.tilføjSkill("Håndbold")
gustav.tilføjSkill("Python programmering")
gustav.tilføjSkill("Gode undskyldninger")

gustav.præsenterSkills()