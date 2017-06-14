import datetime
count = 0
day = datetime.date(1901, 1, 1)
while day != datetime.date(2000, 12, 31):
    if day.weekday() == 6 and day.day == 1: count += 1 
    day = day + datetime.timedelta(1)
print count
