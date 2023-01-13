import random

number = 0
def getRandomNumber ():
	global  number
	number = random.randint(1, 51)
def checker ( num):
	if (num < number):
		return "Kisebb"
	elif (num >number):
		return "Nagyobb"
	else:
		return "Nyertél"
		
