import sys

# main program
if __name__ == '__main__':
	count = 0
	for line in sys.stdin:	
		input = line
		text = list(input)
		l = len(text)-1
		for x in range(0,l):
			if (x%3 == 0) and (text[x] != "P"):
					count += 1
			elif (x%3 == 1) and (text[x] != "E"):
					count += 1
			elif (x%3 == 2) and (text[x] != "R"):
					count += 1
					
	print count