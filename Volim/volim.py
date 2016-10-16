import sys

input = sys.stdin.read()
vals = input.split('\n')
init = int(vals[0])
ques = int(vals[1])
ttot = 0
for a in range (2, ques+2):
	inp = vals[a].split(' ')
	time = int(inp[0])
	ttot = ttot+time
	if ttot >= 210 :
		break
	if inp[1] == 'T':
		if init < 8 :
			init = init + 1
		else :
			init = 1
print init