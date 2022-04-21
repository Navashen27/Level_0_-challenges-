# A function to convert any number into hours and minutes.

def time_conv(time):
    hours = time // 60
    minutes = time % 60
    if hours == 1 and minutes == 1:
        print (f"{hours}) hour, {minutes} minute")
    elif hours == 1 and minutes >= 0:
        print (f"{hours}) hour, {minutes} minutes")
    elif hours >=0 and minutes ==1:
        print (f"{hours}) hour, {minutes} minute")
    else:
        print (f"{hours}) hour, {minutes} minute")

time_conv(100)
