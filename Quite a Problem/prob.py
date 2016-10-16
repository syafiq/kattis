import sys

while 1:
	input= sys.stdin.readline()
	if input=="":
		break
	input = str(input)
	if "problem" in input.lower():
		print "yes"
	else :
		print "no"