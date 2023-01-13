import inputData
import calculator
print("Másodfokú egyenlet megoldó")
A = inputData.getFloat("A:")
B = inputData.getFloat("B:")
C = inputData.getFloat("C:")
plus = calculator.masodfokuplus(A, B, C)
minus = calculator.masodfokuminus(A, B, C)
print ("X1= {1}\nX2= {0}".format (plus, minus))
 
