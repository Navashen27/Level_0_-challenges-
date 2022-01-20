# Python Program to Convert seconds
# into hours, minutes and seconds
  
def convertor(minutes):
    print(minutes // 60)
    print(minutes % 60)
    
minutes = int(input())
convertor(minutes)

