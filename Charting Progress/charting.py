import sys

input = sys.stdin.read()
vals = input.split("\n")
x = 0
for a in vals :
	b = sorted(a)
	if x > 0:
		for d in range(0,x):
			b.insert(0,".")
			del b[-1]
	print "".join(b[::-1])
	if b == []:
		x = 0
	c = b.count("*")
	x = x+c