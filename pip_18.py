import datetime


now = datetime.datetime.now()
print(f"\ncurrent datetime: {now}")

today = datetime.date.today()
print(f"\ncurrent date: {today}")


currenttime = now.time()
print(f"\ncurrent time: {currenttime}\n")



print(f"year:{now.year}")
print(f"month:{now.month}")
print(f"day:{now.day}")
print(f"hour:{now.hour}")
print(f"minute:{now.minute}")
print(f"second:{now.second}")
print(f"microsec:{now.microsecond}")
print(f"weekday (Monday = 1, sunday =7): {now.weekday()+1}")



mydate = datetime.date(2024, 4, 3)
print(f"\nmydate:{mydate}")

mytime = datetime.time(14, 2, 30, 56)
print(f"\nmytime:{mytime}")

mydatetime = datetime.datetime(2025, 5, 28, 4, 34, 34, 123)
print(f"\nmydatetime:{mydatetime}\n")