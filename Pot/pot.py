import sys
from operator import itemgetter

x = 0
for line in sys.stdin :
	a = list(line)
	if len(a) > 2:
		b = a[0:len(a)-2]
		c = "".join(b)
		d = int(c)**int(a[len(a)-2])
		x = x + d

print x