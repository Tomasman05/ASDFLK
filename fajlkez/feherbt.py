from worker import Worker

class FeherBt:
	def __init__ (self):
		self.workerList = []
		
	def readFile(self):
		file = open("dolgozok100.txt", "r", encoding = "UTF-8")
		row = file.readline()
		
		while (row):
			row = file.readline()
			rowSp = row.split(":")
			
			if (len(rowSp) > 1): 
				w=Worker ()
				w.name = rowSp[0]
				w.city = rowSp[1]
				w.adsress = rowSp[2]
				w.salary = rowSp[3]
				w.bonus = rowSp[4]
				w.born = rowSp[5]
				w.hire = rowSp[6]
				self.workerList.append(w)
		file.close()
		print(len(self.workerList))
	def countHatvan (self):
		for worker in self.workerList:
			if (worker.city == "Hatvan"):
				counter +=1
				print (worker.name)
			print("Hatvani dolgozók: {}".format (counter))
		
		
fb = FeherBt()
fb.readFile()
fb.countHatvan()
