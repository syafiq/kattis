import sys

# main program
if __name__ == '__main__':
	move = sys.stdin.read(50)
	list(move)
	pos = 1
	for x in move:
		if x == "A" and pos == 1:
			pos += 1
		elif x == "A" and pos == 2:
			pos -= 1
		elif x == "B" and pos == 2:
			pos += 1
		elif x == "B" and pos == 3:
			pos -= 1
		elif x == "C" and pos == 3:
			pos -= 2
		elif x == "C" and pos == 1:
			pos += 2
		else:
			pos = pos
			
	print pos