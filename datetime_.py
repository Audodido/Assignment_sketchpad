#https://pymotw.com/3/datetime/
#https://www.youtube.com/watch?v=eirjjyP2qcQ


import datetime
# import pytz

# d = datetime.datetime.today()
#d_now = datetime.datetime.now(tz=pytz.utc)
# d_now2 = datetime.datetime.now()
# d_utcnow = datetime.datetime.utcnow()

# print(d)
#print(d_now)
# print(d_now2)
# print(d_utcnow)


tdelta = datetime.timedelta(days=100)
today = datetime.datetime.now()
soon = today + tdelta
soonday = soon.strftime("%A")
soonmon = soon.strftime("%B")
soondate = soon.strftime("%d") + "th"
soonyr = soon.strftime("%Y")

print("Today + " + str(tdelta.days) + "days " + " = " + soonday + ", " + soonmon + " " + soondate + " " + soonyr)