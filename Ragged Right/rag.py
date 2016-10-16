import sys

count = []
x = 0
while 1:
	input = sys.stdin.readline()
	if input == "":
		break
	input = input.rstrip("\n")
	count.append(len(input))
	continue
	
max = max(count)
#print count
for a in range (0, len(count)-1) :
	x = x+(count[a]-max)**2
#	print x
print x