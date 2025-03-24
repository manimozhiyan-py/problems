# maximum and minimum digits

n = 50982

def max_min(n):
    maxx = 0
    minn = n
    while n:
        temp = n % 10
        maxx, minn = max(maxx, temp), min(minn, temp)
        n = n // 10

    return maxx, minn

print(max_min(n))