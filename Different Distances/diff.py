import sys
from decimal import Decimal

for line in sys.stdin :
	if line == '0\n':
		break
	vals = line.split(' ')
	x1 = float(vals[0])
	y1 = float(vals[1])
	x2 = float(vals[2])
	y2 = float(vals[3])
	p = float(vals[4])
	print ((abs(x1-x2))**p+(abs(y1-y2))**p)**(1/p)