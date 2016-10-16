import sys

# main program
if __name__ == '__main__':
	vals = sys.stdin.read()
	num = [int(a) for a in vals.split(" ")]
	h1 = num[6]
	h2 = num[7]
	l = len(num)-2
	for x in range(0,l):
		for y in range(x+1,l):
			for z in range(y+1,l):
				tot=num[x]+num[y]+num[z]
				if tot == h1:
					a = num[x]
					b = num[y]
					c = num[z]
				elif tot == h2:
					d = num[x]
					e = num[y]
					f = num[z]

	list1 = [int(a),int(b),int(c)]
	list2 = [int(d),int(e),int(f)]

	list1x = sorted(list1, reverse=True)
	list2x = sorted(list2, reverse=True)
	
	print list1x[0], list1x[1], list1x[2], list2x[0], list2x[1], list2x[2] 