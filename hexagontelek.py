import inputData
import calculator
A = inputData.getFloat("Az egész telek oldalának hossza: ")
B = inputData.getFloat("A fél telek oldalának hossza: ")
egesz = (calculator.telekhexa(A))
fel= (calculator.feltelekhexa(B))
print("Az egész telekre {0}m2 gyeptégla kell.".format(egesz))
print("Az fél telekre {0}m2 gyeptégla kell.".format(fel))

