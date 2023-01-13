def checkTriangle (sideList):
	if (sideList[0] + sideList[1]>sideList[2] and
		 sideList[1] + sideList[2]>sideList[0] and
		 sideList[0] + sideList[2]>sideList[1] ):
		return True
	else :
		return False
def checkZero(data01, data02 = 1):
	if (data01 == 0 or data02 == 0):
		return False
	else:
		return True
		
