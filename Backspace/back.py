import sys

input = sys.stdin.readline()
input = input.rstrip("\n")
out = []
proc = list(input)
dele = 0

for x in range (len(proc)-1, -1, -1):
	if proc[x] == "<":
		dele = dele+1
	else :
		if dele > 0 :
			dele = dele-1
		else :
			out.append(proc[x])
print "".join(out[::-1])