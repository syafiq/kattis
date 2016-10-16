import sys

while 1:
	input = sys.stdin.readline()
	if input == "0\n":
		break
	vals = input.split(" ")
	count = int(vals[0])
	vals[1] = vals[1].rstrip("\n")
	a = list(vals[1])
	out = []
	for x in a :
		if x == "_":
			num = 91+count
		elif x == ".":
			num = 92+count
		else :
			num = ord(x)+count
		if num > 92 :
			num = 64 + (count-(92-num+count))
#		print num
		if num == 91 :
			out.append("_")
		elif num == 92 :
			out.append(".")
		else :
			out.append(chr(num))
	print "".join(out[::-1])