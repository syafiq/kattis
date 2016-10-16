import sys

# main program
if __name__ == '__main__':
	lista = []
	for line in sys.stdin:	
		input = int(line)
		a = input%42
		if not a in lista:
			lista.append(a)
	
	l = len(lista)
	print l