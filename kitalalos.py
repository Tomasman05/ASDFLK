import ellenorzo

def tipp ():
	
	ellenorzo.getRandomNumber()
	response = ""
	counter = 0
	while (response != "Nyertél" and counter !=3):
		number = int(input("Szám: "))
		response = ellenorzo.checker(number)
		print (response)
		counter +=1
	if (counter == 3 and response != "Nyertél"):
		print ("Vesztettél")
	else:
		print ("Nyertél")
tipp()
