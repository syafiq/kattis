import sys

vals = sys.stdin.read()
a = vals.split('\n')
a1 = a[1].split(' ')
b = 0
for c in range (0, len(a1)):
	x = int(a1[c])
	if x < 0:
		b= b+1
		
print b