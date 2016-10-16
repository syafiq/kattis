import sys

# main program
if __name__ == '__main__':
	for line in sys.stdin:
		vals = [int(a) for a in line.split()]
		a = vals[0]
		b = vals[1]
		c = vals[2]
		if a+b == c :
			print "{}+{}={}".format(a,b,c)
		elif a-b == c :
			print "{}-{}={}".format(a,b,c)
		elif a*b == c :
			print "{}*{}={}".format(a,b,c)
		elif a/b == c :
			print "{}/{}={}".format(a,b,c)
		elif b+c == a :
			print "{}={}+{}".format(a,b,c)
		elif b-c == a :
			print "{}={}-{}".format(a,b,c)
		elif b*c == a :
			print "{}={}*{}".format(a,b,c)
		elif b/c == a :
			print "{}={}/{}".format(a,b,c)
		