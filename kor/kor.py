from korkerulet import Area
from korterulet import Pher
class Kor:
	def __init__ (self):
		self.radius = 0
		self.area = 0
		self.pher = 0
	def getData(self):
		self.radius = float(input("Radius: "))
	def choose(self):
		chooseOK = True
		while(chooseOK):
			choose=int(input("Kerület [1], Terület[2]\nVálassz: "))
			if (choose == 1):
				chooseOK=False
				self.area = Area().calcArea(self.radius)
				print ("Kerület: {:10.3f}".format(self.area))
			elif (choose == 2):
				chooseOK=False
				self.pher = Pher().calcPher(self.radius)
				print ("Terület: {:10.3f}".format(self.pher))
			else:
				choose=int(input("Kerület [1], Terület[2]\nVálassz: "))
kor = Kor()
kor.getData()
kor.choose()
