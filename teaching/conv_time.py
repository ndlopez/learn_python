#!/bin/env/python3.8
# Print the difference between two times
time1, min1 = map(int,input("Enter hour and minutes (HH MM):").split())
time2, min2 = map(int,input("Enter hour and minutes:").split())

a = time1 + min1/60.0
b = time2 + min2/60.0

print(time2,":",min2,"-",time1,":",min1)
if min2 - min1 < 0:
	d = int((b-a)/1)
	if d == 0:
		c = (b-a)*60.0
	else:
		c = (b-a)*d*60.0
	print("dif",d,":",int(c/1))
else:
	print("dif",time2-time1,":",min2-min1)
