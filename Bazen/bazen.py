import sys
import math

input = sys.stdin.readline()
vals = input.split(' ')
vals[1] = vals[1].rstrip("\n")
vals = map(int, vals)
x = vals[0]
y = vals[1]
if x == 0 :
	if y < 125 :
		x_2 = float(15625)/((250-float(y))/2)
		y_2 = 250-x_2
	elif y > 125 :
		x_2 = float(15625)/(float(y)/2)
		y_2 = 0
	else :
		x_2 = 250
		y_2 = 0
elif y == 0 :
	if x < 125 :
		y_2 = float(15625)/((250-float(x))/2)
		x_2 = 250-y_2
	elif x > 125 :
		y_2 = float(15625)/(float(x)/2)
		x_2 = 0
	else :
		x_2 = 0
		y_2 = 250
elif x != 0 and y != 0 :
	if x > 125 :
		y_2 = float(250)-float(15625)*float(2)/float(x)
		x_2 = 0
	elif y > 125 :
		x_2 = float(250)-float(15625)*float(2)/float(y)
		y_2 = 0
	else :
		x_2 = 0
		y_2 = 0
xx = "{0:.2f}".format(round(x_2,2))
yy = "{0:.2f}".format(round(y_2,2))

print xx, yy