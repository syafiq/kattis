import sys

input = sys.stdin.read()
vals = input.split("\n\n")
y = 1
for x in vals :
	if x == "":
		break
	abcd = x.split("\n")
	ab = abcd[0].split(" ")
	cd = abcd[1].split(" ")
	a = int(ab[0])
	b = int(ab[1])
	c = int(cd[0])
	d = int(cd[1])
	det = 1/(a*d-b*c)
	a_inv = det*d
	b_inv = det*(-b)
	c_inv = det*(-c)
	d_inv = det*a
	print "Case {}:".format(y)
	print a_inv, b_inv
	print c_inv, d_inv
	y=y+1