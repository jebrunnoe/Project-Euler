#PROBLEM:
#  19
#
#NAME:
#  "Counting Sundays"
#
#LINK:
#  https://projecteuler.net/problem=19

import datetime
import time
start_time = time.time()

count = 0
day = datetime.date(1901, 1, 1)

while day != datetime.date(2000, 12, 31):
   if day.weekday() == 6 and day.day == 1: 
      count += 1 
   day = day + datetime.timedelta(1)

print count
print "Runtime: %.5fs " % (time.time() - start_time)
