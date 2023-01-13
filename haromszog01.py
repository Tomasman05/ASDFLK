sideA = float(input ('"A"odal: '))
sideB = float(input ('"B"odal: '))
sideC = float(input ('"C"odal: '))
ok = False
if (sideA+sideB>sideC and
	sideB+sideC>sideA and
	sideC+sideA>sideB):
	ok = True
while (not ok):
	sideA = float(input ('"A"odal: '))
	sideB = float(input ('"B"odal: '))
	sideC = float(input ('"C"odal: '))
