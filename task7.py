def celcius_to_fahrenheit(x):
    fahrenheit =(x*9)/5+32
    return fahrenheit

in_celcius = 32

print (int(celcius_to_fahrenheit(in_celcius)))


def fahrenheit_to_celcius(y):
    celcius=(y-32)*5/9
    return celcius

b = 89.6
print (int(fahrenheit_to_celcius(b)))
