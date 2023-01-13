import inputData
import calculator
sideA = inputData.getFloat("'A' oldal: ")
sideB = inputData.getFloat("'B' oldal: ")
spherV = calculator.calcSzferoidV(sideA, sideB)
print("A lencseszferoid térfogata: {:.3f} cm3".format (spherV))
