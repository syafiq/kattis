import sys

# main program
if __name__ == '__main__':
	b = []
	for line in sys.stdin:
		a = list(line)
#		print a
		b.append(a[0])
		for x in range (1,len(a)):
			if a[x] != a[x-1] :
				b.append(a[x])
				
	print "".join(b)