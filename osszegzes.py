import random
list = []
summarize = 0 
for i in range(0,10):
	list.append (random.randint(1, 101))
print (len(list))
print (list)
for i in range(0,len(list)-1):
	summarize = summarize + list[ i ]
print ("A lista számainak összege: {}".format (summarize))
