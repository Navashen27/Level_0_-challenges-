def convert_number_into_time (x):
    
    hour = int(x/60)
    minutes =x%60

    if hour <=1 and minutes <1 :
        return " %d hour, %02d minute" % (hour,minutes)
    elif hour <=1:
        return " %d hour, %02d minutes" % (hour,minutes)
    else:
        return "%d hours, %02d minutes" % (hour,minutes)
    
    

first_any_number =71
second_any_number =133
third_any_number =60
 
print (convert_number_into_time(first_any_number))
print (convert_number_into_time(second_any_number))
print (convert_number_into_time(third_any_number))
