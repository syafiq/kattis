import sys

input = sys.stdin.read()
vals = input.split('\n')
x = 0
while 1:
	if vals[x] == '-1':
		break
	count = int(vals[x])
	uplim = x+count
	t = 0
	tot = 0
	for a in range (x+1,uplim+1):
		st = vals[a].split(' ')
		s = int(st[0])*(int(st[1])-int(t))
		t = st[1]
		tot = tot+s
	print "{} miles".format(tot)
	x = x+count+1