import sys

vals = sys.stdin.read()
inx = [a for a in vals.split("\n")]
satu = []
dua = []
for b in range (1,int(inx[0])*2+1,2):
	output = []
	satu = list(inx[b])
	dua = list(inx[b+1])
	for c in range (0,len(inx[b])):
		if satu[c] == dua[c]:
			output.append(".")
		else :
			output.append("*")
	print inx[b]
	print inx[b+1]
	print "".join(output)
	print "\n"