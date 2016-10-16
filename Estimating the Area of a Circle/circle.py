import sys
import math
while 1 :
	input = sys.stdin.readline()
	if input == "0 0 0\n":
		break
	vals = input.split(" ")
	vals = map(float, vals)
	print math.pi*vals[0]*vals[0], (vals[2]/vals[1])*((2*vals[0])*(2*vals[0]))