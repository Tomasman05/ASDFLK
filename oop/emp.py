class Employee:
	def __init__(self):
		self.name = ""
		self.role = ""
	def working (self, work):
		print (work)
		
	def getData(self):
		print (self.name, self.role)

engineer = Employee()
engineer.name = "Béla"
engineer.role = "Kisfőnök" 
engineer.getData()
engineer.working("Tervez")

worker = Employee()
worker.name = "Gyula"
worker.role = "Melós"
worker.getData()
worker.working ("Kapál")
