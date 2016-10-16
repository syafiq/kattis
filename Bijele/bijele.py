import sys

# main program
if __name__ == '__main__':
	for line in sys.stdin:	
		input = [int(a) for a in line.split()] 
		king 	= (input[0]-1)*(-1)
		queen 	= (input[1]-1)*(-1)
		rooks 	= (input[2]-2)*(-1)
		bishops = (input[3]-2)*(-1)
		knights = (input[4]-2)*(-1)
		pawns 	= (input[5]-8)*(-1)
		
		print king, queen, rooks, bishops, knights, pawns