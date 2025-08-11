#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.now()
print("Today is", now)

# print today's date one year from now
print("In one year it will be:", now +  timedelta(days=365))

# create a timedelta that uses more than one argument
print("In two weeks and 3 days it will be:", now +  timedelta(weeks=2, days=3))

# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d")
print("One week ago it was", s)
print("---" * 10)

### How many days until April Fools' Day?
today = date.today()
today = date(today.year, 11, 10)
aFoolsDay = date(today.year, 4, 1)
if aFoolsDay < today:
  print(f"April fools' day already went by {(today - aFoolsDay).days} days ago")
  aFoolsDay = aFoolsDay.replace(year=today.year + 1)
time_to_afd = aFoolsDay - today
print(f"It's just {time_to_afd.days} days until April Fools' day")