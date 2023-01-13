from worker import Worker

class FeketeBt:
	def __init__(self):
		self.workerList = []
		self.miskolcfizu = 0
		self.atlagfizu = 0
		self.miskolciak = 0
		self.gyoribonus = 0
	def fileRead(self):
		file = open("dolgozok100.txt", "r", encoding = "UTF-8")
		row = file.readline()
		while(row):
			row = file.readline()
			rowSp = row.split(":")
			if (len(rowSp)>1):
				w=Worker()
				w.name = rowSp[0]
				w.city = rowSp[1]
				w.address = rowSp[2]
				w.salary = rowSp[3]
				w.bonus = rowSp[4]
				w.born = rowSp[5]
				w.hired = rowSp[6]
				self.workerList.append(w)
		file.close()
		wAmount =len(self.workerList)
		print("Dolgozók száma: {0}".format (wAmount))
	def Miskolci(self):
		for worker in self.workerList:
			if (worker.city == "Miskolc"):
				self.miskolciak += 1
	def Miskolcfizu(self):
		for worker in self.workerList:
			if (worker.city == "Miskolc"):
				self.miskolcfizu += int(worker.salary)
				self.atlagfizu = self.miskolcfizu / self.miskolciak
		print ("Miskolci fizetések átlaga: {:10.2f} Ft".format (self.atlagfizu))
	def Gyoribonusz(self):
		for worker in self.workerList:
			if (worker.city == "Győr"):
				self.gyoribonus += int(worker.bonus)
		with open("gyoriJutalom.txt", "w", encoding = "UTF-8") as mentes:
			mentes.write("Győri dolgozók összesített jutalma: {0}".format (self.gyoribonus))
		
fb = FeketeBt()
fb.fileRead()
fb.Miskolci()
fb.Miskolcfizu()
fb.Gyoribonusz()
