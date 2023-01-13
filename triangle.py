import inputData
import checker
import calculator
import kör

def getData():
	sideList =[]
	for i in range(0, 3):
		sideList.append(inputData.getFloat ("{}.oldal: ".format (i+1)))
	return sideList

def control ():
		sideList=[]
		choose = inputData.getInt("Kerület [1], Terület N [2], Terület H [3], Kör T [4], Kör K [5]\nVálassz: ")
		chooseOK = True
		while(chooseOK):
				if (choose == 1):
					sideList= getData()
					while (not checker.checkTriangle(sideList)):
						print ("Nem háromszög")
						sideList= getData()
					
					chooseOK= False
					pher = calculator.calcPher (sideList)
					print ("A háromszög kerülete: {}cm".format (pher))
				elif (choose == 2):
					base = inputData.getFloat("Alap: ")
					height = inputData.getFloat("Magasság: ")
					
					while(not checker.checkZero(base, height)):
						print ("Adat nem lehet '0'")
						base = inputData.getFloat("Alap: ")
						height = inputData.getFloat("Magasság: ")
					chooseOK= False	
					area = calculator.calcAreaNormal(base, height)
					print ("A háromszög területe: {}cm2".format (area))
				elif (choose == 3):
					sideList= getData()
					while (not checker.checkTriangle(sideList)):
						print ("Nem háromszög")
						sideList= getData()
					chooseOK= False
					area = calculator.calcAreaHeron(sideList)
					print ("A háromszög területe: {}cm2".format (area))
				elif (choose == 4):
					radius= inputData.getFloat("Sugár: ")
					while (not checker.checkZero(radius)):
						print ("Az adat nem lehet 0")
						radius= inputData.getFloat("Sugár: ")
					chooseOK = False
					pher = kör.calcPher(radius)
					print ("A kör területe: {0}cm2".format (pher))
				elif (choose == 5):
					radius= inputData.getFloat("Sugár: ")
					while (not checker.checkZero(radius)):
						print ("Az adat nem lehet 0")
						radius= inputData.getFloat("Sugár: ")
					chooseOK = False
					area = kör.calcArea(radius)
					print ("A kör kerülete: {0}cm".format (area))
				else:
					choose = inputData.getInt("Kerület [1], Terület N [2], Terület H [3], Kör T[4], Kör K[5] \nVálassz: ")
			
	
				
control()
