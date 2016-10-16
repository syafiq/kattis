import sys

t9 = {}
t9['a'] = '2'
t9['b'] = '22'
t9['c'] = '222'
t9['d'] = '3'
t9['e'] = '33'
t9['f'] = '333'
t9['g'] = '4'
t9['h'] = '44'
t9['i'] = '444'
t9['j'] = '5'
t9['k'] = '55'
t9['l'] = '555'
t9['m'] = '6'
t9['n'] = '66'
t9['o'] = '666'
t9['p'] = '7'
t9['q'] = '77'
t9['r'] = '777'
t9['s'] = '7777'
t9['t'] = '8'
t9['u'] = '88'
t9['v'] = '888'
t9['w'] = '9'
t9['x'] = '99'
t9['y'] = '999'
t9['z'] = '9999'
t9[' '] = '0'

x = 0
for line in sys.stdin:
	out = []
	line = line.rstrip("\n")
	if not line.isdigit():
		inp = list(line)
		for a in inp :
			if out == []:
				out.append(t9[a])
			else :
				if out[-1][0] == t9[a][0]:
					out.append(" ")
					out.append(t9[a])
				else :
					out.append(t9[a])
	show = "".join(out)
	if out :
		print "Case #{}: {}".format(x, show)
	x=x+1