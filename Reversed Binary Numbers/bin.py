import sys

vals = sys.stdin.read()
c = list(bin(int(vals)))
d = []
for a in range (len(c)-1,1,-1):
	d.append(c[a])
e = "".join(d)
print int(e,2)