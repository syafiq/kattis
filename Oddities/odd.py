import sys

vals = sys.stdin.read()
inx = [a for a in vals.split("\n")]
for b in range (1,int(inx[0])+1):
	if int(inx[b])%2 == 0:
		print "{} is even".format(inx[b])
	else :
		print "{} is odd".format(inx[b])