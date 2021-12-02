from datetime import datetime, time, timedelta

#print(date.today())

dt = datetime(2013, 8, 21, 2, 30, 45)

#print(dt.hour)
#print(dt.minute)
#print(dt.second)
#print(dt.strftime("%m-%d-%Y %H:%M:%S"))

add_dt = dt + timedelta(days = 5)
print(add_dt.strftime("%m-%d-%Y %H:%M:%S"))
