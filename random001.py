import random
list = []

for i in range(0,500):
	number = random.randint (1, 500)
	list.append (number)
print ("A lista mérete: {}".format(len(list)))
print (list)
