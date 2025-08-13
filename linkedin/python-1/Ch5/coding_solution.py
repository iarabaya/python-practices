import calendar
def count_days(theyear, themonth, whichday):
  daycount = 0
  weekslist = calendar.monthcalendar(theyear, themonth)
  # monthcalendar returns an array of week lists, like this:
  # [
  #   [0,0,1,1,1,1,1],
  #   [1,1,1,1,1,1,1],
  #   [1,1,1,1,1,1,1],
  #   [1,1,1,1,1,1,1],
  #   [1,1,1,0,0,0,0],
  # ]
  for week in weekslist:
    if week[whichday] != 0:
      daycount += 1
  return daycount

print(count_days(2025,12,0))
print(count_days(2030,1,5))
print(count_days(2027,7,5))