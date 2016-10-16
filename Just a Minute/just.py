import sys

input = sys.stdin.read()
vals = input.split("\n")
count = int(vals[0])
min = []
sec = []
for a in range(1,count+1) :
	inp = vals[a].split(" ")
	min.append(int(inp[0]))
	sec.append(int(inp[1]))

out = float(sum(sec))/(float(sum(min))*60)
if out <= 1.0 :
	print "measurement error"
else :
	print out