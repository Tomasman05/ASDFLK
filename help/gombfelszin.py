import math
class Surface :
	def __init__(self):
		pass
	def getSurface (self, radius):
		result = 4*math.pow(radius,2)*math.pi
		return result
