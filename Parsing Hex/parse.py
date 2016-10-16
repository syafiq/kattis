import sys

def is_hex(input):
	if input == "a" or input == "b" or input == "c" or input == "d" or input == "e" or input == "f" or input == "1" or input == "2" or input == "3" or input == "4" or input == "5" or input == "6" or input == "7" or input == "8" or input == "9" or input == "A" or input == "B" or input == "C" or input == "D" or input == "E" or input == "F" or input == "0":
		return True

# main program
if __name__ == '__main__':
	for line in sys.stdin:
		a = list(line)
		la = len(a)
		tempjalan = []
		output = []
		for jalan in range(0, la):
			tempjalan.append(a[jalan])
			if tempjalan[jalan-1] == "0" and (tempjalan[jalan] == "x" or tempjalan[jalan] == "X") :
				output.append(a[jalan-1])
				output.append(a[jalan])
				for jalan2 in range(jalan+1, la):
					if is_hex(a[jalan2]) :
						output.append(a[jalan2])
					else :
						break
				str = ''.join(output)
				strdec = int(str, 16)
				print str, strdec
				output = []
			continue