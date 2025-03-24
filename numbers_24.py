#GCD

def GCD(a, b):
    while b:
        a, b = b, a%b
    return a

print(GCD(36, 60))


