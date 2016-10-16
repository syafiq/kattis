import sys

vals = sys.stdin.read()
input = [a for a in vals.split('\n')]
li = []
for b in range (0,5):
	c = input[b].split(' ')
	t = int(c[0])+int(c[1])+int(c[2])+int(c[3])
	li.append(t)

max_list = max(li)
max_index = li.index(max_list)+1

print max_index, max_list