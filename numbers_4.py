#prime within a range

import math

def prime(number):
    for i in range(2, math.ceil(math.sqrt(number))):
        if number%i == 0:
            return False
    return True


def number_flow(start, end):
        prime_numbers = [i for i in range (start, end +1) if prime(i) ]
        return prime_numbers


print(number_flow(10, 20))


