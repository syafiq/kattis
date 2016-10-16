import sys
import math

input = sys.stdin.read()
vals = input.split("\n")
n = int(vals[0])
for a in range (1,n+1):
	b = list(vals[a])
	sq = int(math.ceil(math.sqrt(len(b))))
	l = int(math.ceil(math.sqrt(len(b)))**2)
	star = l-len(b)
	out = []
	if star >= 1:
		ext = ['*']*star
		b.extend(ext)
	for counter in range(l-sq,l):
		for counter2 in range(counter, counter-((sq-1)*sq)-1, -sq):
			if b[counter2] != "*" :
				out.append(b[counter2])
	print "".join(out)