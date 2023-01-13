import math
def calcPher (sideList):
	pher = sideList [0] + sideList[1] + sideList[2]
	return pher
	
def calcAreaNormal (base, height):
	area = base * height  / 2
	return area
		
def calcAreaHeron (sideList):
	s = (sideList [0] + sideList [1] + sideList [2]) /2
	area = sqrt(s*(s-sideList [0])*(s-sideList [1])*(s-sideList [2]))
	return area
def calcSzferoidV (sideA, sideB):
	part1 =(4*math.pi) / 3
	part2 = (math.pow(sideA, 2))*sideB
	V = part1*part2
	return V

def masodfokuplus (A, B, C):
	part1=(math.pow(B,2) - (4*A*C))
	Bminus =(B-(B*2))
	plus = ((Bminus + part1) /(2*A))
	return plus
def masodfokuminus (A, B, C):
	part1=(math.pow(B,2) - (4*A*C))
	Bminus =(B-(B*2))
	minus = ((Bminus - part1) /(2*A))
	return minus
	
def telekhexa (A):
	part1 = ((3/2)*math.pow(A,2))
	T=(part1*math.sqrt(3))
	return T
def feltelekhexa (B):
	part1 = ((3/2)*math.pow(B,2))
	T=((part1*math.sqrt(3))/2)
	return T
