import math
class Volume :
	def __init__(self):
		pass
	def getVolume(self, radius):
		result1 = 4*math.pow(radius,3)*math.pi
		result2 = result1/3
		return result2

