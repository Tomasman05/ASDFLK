import random
list = []
counter = 0
for i in range(0,5000):
	list.append(random.randint (1,101))
for i in range(0,len(list)):
	if (list[i] < 50):
		counter = counter +1

print("Ennyi 50 alatti szám van: {}".format(counter))
		
	
