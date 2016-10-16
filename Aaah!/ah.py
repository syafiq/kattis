import sys

input = sys.stdin.read()
vals = input.split("\n")
if len(vals[0])>len(vals[1]):
	print "go"
else :
	print "no"