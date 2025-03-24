from numbers_24 import GCD

def LCM(a,b):
    lcm = (a * b)/(GCD(a, b))
    return lcm

print(LCM(9, 27))