# GP

def gp(a, r, n):
    if r != 1:
        sum = (a*(1-r**n))/(1-r)
        return sum

print(gp(5, 2, 5))