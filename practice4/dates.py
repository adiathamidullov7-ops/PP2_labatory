from datetime import datetime, timedelta


current_date = datetime.now()


new_date = current_date - timedelta(days=5)

print("Current date:", current_date.strftime("%Y-%m-%d"))
print("Date after subtracting 5 days:", new_date.strftime("%Y-%m-%d"))



from datetime import datetime, timedelta
today = datetime.now().date()
yesteray = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday", yesteray)
print("Today", today)
print("Tomorrow", tomorrow)

from datetime import datetime
now = datetime.now()
print("Datetime now", now)

no_microsecond = now.replace(microsecond=0)
print("Without microsecond", no_microsecond)






from datetime import datetime


date1_str = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date2_str = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")

date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")


delta = date2 - date1


print("Difference in seconds:", int(delta.total_seconds()))