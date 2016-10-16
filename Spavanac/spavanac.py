import sys
import datetime

vals = sys.stdin.read()
a = vals.split(' ')
t = datetime.datetime(2011,1,1,int(a[0]), int(a[1]))
c = t-datetime.timedelta(minutes=45)
print c.hour, c.minute