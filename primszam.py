import math
while (True):
	try:
		szam = int(input("Kérek egy számot: "))
		break
	except:
		pass
print(type(szam))
van = False
for oszto in range(2, int(math.sqrt(szam)+1)):
	if (szam%oszto ==0):
		print ("Nem prím")
		van = True
		break
	if (not van):
		print ("Prím")

"""for szam in range(1, 1000000001):
	van = False
	for oszto in range(2, int(math.sqrt(szam)+1)):
		if (szam%oszto ==0):
			van = True
			break
		if (not van):
			print (szam)"""
 
