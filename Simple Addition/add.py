import sys

# main program
if __name__ == '__main__':
	vals = sys.stdin.read()
	inx = [a for a in vals.split("\n")]
	print int(inx[0])+int(inx[1])