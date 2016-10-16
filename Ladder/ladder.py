import sys
import math

# main program
if __name__ == '__main__':
	for line in sys.stdin:	
		input = [int(a) for a in line.split()] 
		h = input[0]
		v = input[1]
		t = h/(math.sin(v*0.0174533))
		print int(math.ceil(t))