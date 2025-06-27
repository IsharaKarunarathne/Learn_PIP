import datetime

sri_lanka_offset = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
now_srilanka = datetime.datetime.now(sri_lanka_offset)
print(f"current datetime in SL:{now_srilanka}")