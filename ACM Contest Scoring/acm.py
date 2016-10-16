import sys

# main program
if __name__ == '__main__':
	time = 0
	execu = 0
	id = []
	prob = []
	for line in sys.stdin:
		#print line
		if line == "-1\n":
			#print "break"
			break
		else :
			vals = [a for a in line.split(" ")]
			#print vals[2]
			if vals[2] == "right\n" :
				execu = execu + 1
				time = time + int(vals[0])
				prob.append(vals[1])
			else :
				id.append(vals[1])
	for b in range (0, len(prob)):
		for a in range (0, len(id)):
			if prob[b] == id[a]:
				time = time + 20
	print execu, time