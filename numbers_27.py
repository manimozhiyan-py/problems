#abudant number

n = 18

def abudant(number):
    sum =0
    for i in range(1,number // 2 +1 ):
        if n%i == 0:
            sum += i

    return sum > number

print(abudant(n))