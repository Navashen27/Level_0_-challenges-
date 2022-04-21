def maximum_num(*numbers):
    
    biggest = numbers[0]

    for num in numbers:

        if num > biggest:

            biggest = num

    return biggest

print(maximum_num(10, 1, 105))
