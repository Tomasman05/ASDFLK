also = [1,0,0,1]
felso = [224,256,256,255]
while (True):
	ipv4 = input("Add meg az Ip-t:  ")
	reszek = ipv4.split(".")
	a=int(reszek[0])
	if (len(reszek)!=4):
		continue
	try:
		hiba = False
		for i in range(0,4):
			if (not int(reszek[i]) in range (also[i],felso[i])):
				hiba = True	
		if (not hiba):
			break
	except:
		continue
if (reszek[0] in range (1,128)):
	type0=("A")
	mask = ("255.0.0.0 vagy /8")
elif(reszek[0] in range (128,192)):
	type1 = ("B")
	mask = ("255.255.0.0 vagy /16")
else :
	print ("'C' osztályú ip-cím. Maszk: 255.255.255.0 vagy /24")
print  ("'{}' osztályú ip-cím. Maszk: {} ".format (type0,mask))
