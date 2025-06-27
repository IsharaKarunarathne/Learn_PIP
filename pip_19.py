import datetime

now = datetime.datetime.now()

formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"formatted time and date: {formatted_date_time}")

formatted_date = now.strftime("%A, %B %d, %Y")
print(f"formatted date: {formatted_date}")

formatted_TIME = now.strftime("%I:%M %p")
print(f"formatted time: {formatted_TIME}")