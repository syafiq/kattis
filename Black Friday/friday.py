import sys

input = sys.stdin.read()
vals = input.split('\n')
a = []
b = vals[1].split(' ')
for x in range (0,int(vals[0])):
	c = b.pop(x)
	if not c in b :
		a.append(int(c))
	b.insert(x, c)
if not a :
	print "none"
else :
	print int(b.index(str(max(a))))+1