class Titkositas:
	def __init__ (self,kulcs="titok"):
		self.kulcs = bytes(kulcs,"utf-8")
	def titkosito (self,file):
		f=open(file,encoding="utf-8")
		output=open("titkositott.txt","w",encoding="utf-8")
		for sor in f():
			sor=bytes(sor,"utf-8")
			i=0
			titkosSzoveg=""
			while(True):
				titkositando=sor [i*len(self.kulcs):(i+1)*len(self.kulcs)]
				print(self.titkositando)
				print(self.kulcs)
				for j,c in enumerate(titkositando):
					c1=chr(c)
					c2=chr(self.kulcs[j])
					titkositottSzoveg+=chr(ord(c1)^ord(c2))
				i+=1
				if (i*len(self.kulcs))>len(sor):
					break
			print(titkosSzoveg,file=output)	
		f.close()
		output.close()	
	def visszafejto(self):
		print (f"{self.kulcs} szinten az XOR-ral fogok titkosítani")
		
if 	(__name__=="__main__"):
	"""print(__name__)
	print(globals())
	t=Titkositas("Alma")
	print(t)
	print(t.kulcs)
	t2=Titkositas
	print(t2)
	print(t2.kulcs)"""
	t=Titkositas()
	t.titkosito("titkositott.txt")
	t.visszafejto()
	print(t.titkosito())
	
