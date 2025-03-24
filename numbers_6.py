# Perfect number
import math


def perfect_number(number):
    sum = 1
    for i in range(2, math.ceil(math.sqrt(number))):
        if number%i == 0:
            print(i)
            sum += i
            if i != number//i:
                sum += number // i


    return sum == number

print(perfect_number(28))