#hello
start_h = 0
start_m = 0
timee = ""

duration_h = 0
duration_m = 0
count = 0


def add_mn():
  global start_h, start_m, timee, duration_h, duration_m
  if (start_m+duration_m) >= 60:

      start_m = (start_m+duration_m)-60
      start_h += 1

  else:
      start_m += duration_m


def add_h():
  global start_h, count, duration_h, timee
  i = 0
  start_h += duration_h
  if start_h > 24:
      while i == 0:
         start_h -= 24
         count += 1
         if start_h < 24:
           i = 1

  if start_h >= 12:

    if timee == "AM":
      timee = "PM"
    else:
      timee = "AM"
      count += 1
    start_h -= 12
    if start_h == 0:
      start_h = 12


def add_time(start, duration, day=None):
  global start_h, start_m, timee, duration_h, duration_m, count
  start = start.split()
  timee = start[1]
  start = start[0].split(":")
  start_h = int(start[0])
  start_m = int(start[1])
  duration = duration.split(":")
  duration_h = int(duration[0])
  duration_m = int(duration[1])
  add_mn()
  add_h()
  startt_m = f"0{start_m}" if len(str(start_m)) == 1 else f"{start_m}"
  count = 0
  if day is None:
    if count == 0:
      return f"{start_h}:{startt_m} {timee}"
    elif count == 1:
      return f"{start_h}:{startt_m} {timee} (next day)"
    if count > 1:
      return f"{start_h}:{startt_m} {timee} " + f"({count} days later)"
  else:
    days_week = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
        "Sunday"
    ]
    start_index = days_week.index(day.capitalize()) + count
    i = 0
    for _ in range(start_index):
      i += 1
      if i > 6:
        i = 0
    day = days_week[i]
    if count == 0:
      return f"{start_h}:{startt_m} {timee}, {day.capitalize()}"
    elif count == 1:
      return f"{start_h}:{startt_m} {timee}, {day.capitalize()} (next day)"
    else:
      return f"{start_h}:{startt_m} {timee}, {day.capitalize()} " + f"({count} days later)"

 


print(add_time("8:16 PM", "24:00", "tuesday"))
