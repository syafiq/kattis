import sys
from fractions import *

input = sys.stdin.read()
vals = input.split("\n")
count = int(vals.pop(0))
vals.pop(len(vals)-1)
for a in vals :
	b = a.split(" ")
	depan = Fraction(int(b[0]),int(b[1]))
	belakang = Fraction(int(b[3]),int(b[4]))
	operator = b[2]
	if operator == "+" :
		out = depan+belakang
	elif operator == "-" :
		out = depan-belakang
	elif operator == "/" :
		out = depan/belakang
	elif operator == "*" :
		out = depan*belakang
	
	if out.denominator == 1 :
		print "{} / 1".format(out.numerator)
	else :
		print "{} / {}".format(out.numerator, out.denominator)