import sys

a = 1
while 1:
	input = sys.stdin.readline()
	if input == "" :
		break
	vals = input.split(" ")
	vals = map(int, vals)
	vals.pop(0)
	print "Case {}: {} {} {}".format(a, min(vals), max(vals), max(vals)-min(vals))
	a = a+1