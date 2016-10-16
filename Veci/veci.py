import sys
from itertools import permutations

input = sys.stdin.readline()
input = input.rstrip('\n')
perms = [''.join(p) for p in permutations(input)]
perms.remove(input)
perms = map(int, perms)
p2 = []
for a in perms :
	if a > int(input) :
		p2.append(a)
if p2 :
	print min(p2)
else :
	print "0"