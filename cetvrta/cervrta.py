import sys

# main program
if __name__ == '__main__':
	xlist = []
	ylist = []
	for line in sys.stdin:	
		vals = [int(a) for a in line.split()] 
		xlist.append(vals[0])
		ylist.append(vals[1])
		
	if xlist[0] == xlist[1]:
		outx = xlist[2]
	elif (xlist[1] == xlist[2]):
		outx = xlist[0]
	else:
		outx = xlist[1]
		
	if ylist[0] == ylist[1]:
		outy = ylist[2]
	elif (ylist[1] == ylist[2]):
		outy = ylist[0]
	else:
		outy = ylist[1]

	print outx, outy
