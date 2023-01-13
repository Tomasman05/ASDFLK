class Employee:
	def __init__(self):
		self.__name = ""
		self.age = 0
	def setName (self, name):
		self.__name = name
	def getData (self):
		print (self.__name)
		print (self.age)
worker = Employee()
worker.name = "Béla"
worker.age = 20
worker.setName ("Gyula")
worker.getData()
