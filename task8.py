def time_converter(time):
    time = int(time)
    hour = int(time / 60)
    minutes = time % 60 
    if time < 60 and minutes == 1:
        print(minutes, "minute")
    elif time < 60:
        print(minutes, "minutes")
    elif hour == 1 and minutes == 1:
        print(hour, "hour,", minutes, "minute")
    elif hour > 1 and minutes == 1:
        print(hour, "hours,", minutes, "minute")
    elif hour == 1:
        print(hour, "hour,", minutes, "minutes")
    else:
        print(hour, "hours,", minutes, "minutes")
