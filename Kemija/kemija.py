inp = raw_input();
vow = ['a', 'i', 'u', 'e', 'o']
out = ''
i = 0
while i < len(inp) :
	out += inp[i]
	if inp[i] in vow :
		i+=2
	i+=1
print out