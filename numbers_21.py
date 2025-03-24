#prime factors
import math


def prime_factors(n):
    factors = []

    while n%2 ==0:
        factors.append(2)
        n //= 2

    for i in range(3, math.ceil(math.sqrt(n))+1,2):
        while n % i ==0 :
            print(i)
            factors.append(i)
            n //= i

    if n >1:
        factors.append(n)

    return factors

print(prime_factors(36))