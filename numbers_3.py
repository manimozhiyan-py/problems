#Check if a number is prime or not

import math

def prime(number):
    for i in range(2, math.ceil(math.sqrt(number))):
        if number % i == 0:
            return False
    return True

