import sys
import operator

adrian = 'ABC'
bruno = 'BABC'
goran = 'CCAABB'

input = sys.stdin.read()
vals = input.split("\n")
leng = int(vals[0])
answ = vals[1]
while len(adrian) < leng:
	adrian += adrian
while len(bruno) < leng:
	bruno += bruno
while len(goran) < leng:
	goran += goran

adrian = list(adrian)
bruno = list(bruno)
goran = list(goran)
answ = list(answ)

x = 0
out_adrian = 0
out_bruno = 0
out_goran = 0
for a in answ :
	if a == adrian[x] :
		out_adrian = out_adrian+1
	if a == bruno[x] :
		out_bruno = out_bruno+1
	if a == goran[x] :
		out_goran = out_goran+1
	x = x+1
	
li = {'Adrian':out_adrian, 'Bruno':out_bruno, 'Goran':out_goran}
y = max(li, key=li.get)
print li[y]
outkey = []
for key, value in li.iteritems() :
    if value == li[y] :
		outkey.append(key)

outkey = sorted(outkey)
for t in outkey:
	print t