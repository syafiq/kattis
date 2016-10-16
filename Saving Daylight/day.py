import sys
import datetime

for line in sys.stdin:
	a = line.split(' ')
	rise = a[3].split(':')
	set  = a[4].split(':')
	t2 = datetime.datetime(2011,1,1,int(set[0]),int(set[1]))
	td = t2-datetime.timedelta(hours = int(rise[0]), minutes= int(rise[1]))
	print "{} {} {} {} hours {} minutes".format(a[0], a[1], a[2], td.hour, td.minute)