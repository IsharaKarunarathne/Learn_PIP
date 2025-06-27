import datetime

now = datetime.datetime.now()

#+7days
future_date = now + datetime.timedelta(days=7)
print(f"7 days from now: {future_date}")


#-3 hours
past_time = now - datetime.timedelta(hours=3)
print(f"3 hours before now: {past_time}")


#calculate difference
date1= datetime.datetime(2024, 4, 3)
date2= datetime.datetime(2024, 11, 5)

differnce = date2 - date1

print(f"differnce between dates:{differnce}")
print(f"differnce in days:{differnce.days}")

