import sys

while 1 :
	input = sys.stdin.readline()
	if input == "":
		break
	vals = input.split(" ")
	vals[len(vals)-1] = vals[len(vals)-1].rstrip("\n")
	nam = []
	num = []
	for a in vals :
		if a.isalpha() :	
			nam.append(a)
		else :
			num.append(a)
	num = map(float, num)
	avg = sum(num)/len(num)
	name = " ".join(nam)
	print "{} {}".format(avg, name)