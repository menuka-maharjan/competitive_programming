#calender module
import calendar
mdy=input().split()
m=int(mdy[0])
d=int(mdy[1])
y=int(mdy[2])
print(list(calendar.day_name)[calendar.weekday(y, m, d)].upper())
