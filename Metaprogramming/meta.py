import sys
import re

dict = {}
while 1:
	input = sys.stdin.readline()
	if input == "":
		break
	else :
		input = input.rstrip("\n")
	vals = input.split(" ")
	if vals[0] == "define":
		name = " ".join(vals[2:len(vals)])
		value = int(vals[1])
		dict[name] = value
	elif vals[0] == "eval" :
		vals.pop(0)
		for x in vals :
			if x=="<" or x==">" or x=="=":
				operator = x
		inp = " ".join(vals)
		inp2 = re.split('<|>|=', inp)
		inp2[0] = inp2[0].rstrip(" ")
		inp2[1] = inp2[1].lstrip(" ")

		if (operator == "<" and inp2[1] in dict.keys() and inp2[0] in dict.keys()):
			s = str(dict[inp2[0]]<dict[inp2[1]])
			print s.lower()
		elif (operator == ">" and inp2[1] in dict.keys() and inp2[0] in dict.keys()):
			s = str(dict[inp2[0]] > dict[inp2[1]])
			print s.lower()
		elif (operator == "=" and inp2[1] in dict.keys() and inp2[0] in dict.keys()):
			s = str(dict[inp2[0]] == dict[inp2[1]])
			print s.lower()
		else :
			print "undefined"