import math
#controll
def control():
	sideList = []
	check = False
	while ( not check ):
		sideList.clear()
		sideList.append( inData( '"A" oldal: ' ))
		sideList.append( inData( '"B" oldal: ' ))
		sideList.append( inData( '"C" oldal: ' ))
		check = checkTriangle ( sideList )
		if (not check):
			print ("Hibás adatok! ")
	choose = inData ("Kerület: [1], Terület: [2] \nválassz: ")
	
		
#Model
def inData( text ):
	
	num1 = ( float(input(text)))
	return num1
def checkTriangle ( sideList ):
	if  (sideList [0] + sideList [1] >sideList [2] and 
	sideList[1] + sideList[2]> sideList[0] and 
	sideList[0] + sideList[2]> sideList[1]):
		return True
	else:
		return False
def calcPher (sideList):
	resultPher = sideList [0] + sideList[1] + sideList[2]
	return resultPher
def calcArea (sideList):
	s = sideList [0] + sideList [1] + sideList [2] /2
	restResult = s*(s-sideList [0])*(s-sideList [1])*(s-sideList [2])
	area = math.sqrt (restResult)
	return area
def checkChoose(choose):
	while ( not ok ):
		if (choose == 1):
			resultPher = calcPher( sideList )
			print ("A háromszög kerülete: {}cm".format (resultPher))
			return True
		elif (choose == 2):
			resultArea = calcArea(sideList)
			print ("A háromszög területe: {} cm2".format (resultArea))
			return True
		else: 
			print ("Hibás adat!")
			choose = inData ("Kerület: [1], Terület: [2] \nválassz:")
			return False
#View
control ()
