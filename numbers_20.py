# FActors of given number

n =12

def factor(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors

print(factor(n))