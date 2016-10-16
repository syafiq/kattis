import sys

input = sys.stdin.read()
vals = input.split("\n")
count = int(vals.pop(0))
vals.pop(len(vals)-1)
out = sorted(vals)
if out == vals :
	print "INCREASING"
elif out[::-1] == vals :
	print "DECREASING"
else :
	print "NEITHER"