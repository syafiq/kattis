import sys

# main program
if __name__ == '__main__':
	for line in sys.stdin:
		vals = [int(a) for a in line.split()]
		lv = len(vals)
		for x in range(0,lv):
			sum = vals[x]
			all = 0
			for y in range(0,lv):
				all += vals[y]
			last = all-sum
			if last == sum:
				break
		print sum