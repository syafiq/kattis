import sys
import math

for line in sys.stdin:
	if line == "0\n":
		break
	n = int(line)
	out = 0
	for i in range (1, n+1):
		out = out + math.log(i)
	print 2.71828182**(out-(n+0.5)*math.log(n)+n-0.918938533)