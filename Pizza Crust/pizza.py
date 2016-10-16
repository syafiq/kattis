import sys

input = sys.stdin.read()
vals = input.split(" ")
a = float(vals[0])
b = float(vals[1])
diff = a-b
out = ((diff**2)/(a**2))*100
kel = "%.6f" % out
print kel