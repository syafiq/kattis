import sys
import math

input = sys.stdin.read()
vals = input.split("\n")
count = int(vals[0])
for a in range (1, count+1):
	out = []
	x = len(vals[a])
	y = list(vals[a])
	sq = int(math.sqrt(x))
	for b in range(sq-1,-1,-1):
		for c in range(b,x,sq):
			out.append(y[c])
	print "".join(out)