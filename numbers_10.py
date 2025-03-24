# Arithmetic Progression

def ap(a, n, d):
    sum = n/2 * (2*a + (n-1) * d)
    return int(sum)

print(ap(a = 2, d = 3, n = 5))