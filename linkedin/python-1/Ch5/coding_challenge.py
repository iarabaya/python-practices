import calendar
def count_days(year, month, whichday):
  cal = calendar.monthcalendar(year, month)
  days = 0
  for week in cal:
    if week[whichday]:
      days += 1
  return days

print(count_days(2025,12,0))
print(count_days(2030,1,5))
print(count_days(2027,7,5))
