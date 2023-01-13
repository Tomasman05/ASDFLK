'''oldal1 = float(input('"A" oldal:'))
oldal2 = float(input('"B" oldal:'))
oldal3 = float(input('"C" oldal:'))
kerulet = 0
if (oldal1 + oldal2 > oldal3 and oldal1+oldal3> oldal2 and oldal2 + oldal3 >oldal1):
	kerulet = oldal1 + oldal2 + oldal3
	print ("Az oldalak kerülete:{}".format (kerulet) + "cm")
else:
	print ("A háromszög nem szerkeszthető!")'''
		

A = float(input('"A" oldal:'))
B = float(input('"B" oldal:'))
C = float(input('"C" oldal:'))
 
if (A ** 2 + B ** 2 == C ** 2 or A**2 + C**2 == B**2 or C**2 + B**2 == A**2):
	 print ("A háromszög derékszögű!")
elif (A+B>C and B+C>A and C+A>B):
	print ("A háromszög nem derékszögű")
else :
	print ("Ez nem egy háromszög")
