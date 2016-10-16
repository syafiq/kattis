import sys

x = 1
while 1 :
	input = sys.stdin.readline()
	if input == "END\n":
		break
	input = input.rstrip("\n")
	vals = list(input)
	black = []
	for a,val in enumerate(vals) :
		if val == "*":
			black.append(a)
	flag = 0
	if len(black) == 1 or len(black) == 2:
		flag = 1
	else :
		diff = black[1] - black[0]
		for b in range (2, len(black)) :
			flag2 = 0
			if black[b]-black[b-1] == diff:
				flag2 = 1
				continue
			else :
				print "{} NOT EVEN".format(x)
				break
			continue
	if flag == 1 or flag2 ==1 :
		print "{} EVEN".format(x)
	x = x + 1