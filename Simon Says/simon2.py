n = int(raw_input())

for _ in range(n) :
	inp = raw_input()
	if inp.startswith('simon says'):
		print ' '.join(inp.split()[2:])
	else :
		print 